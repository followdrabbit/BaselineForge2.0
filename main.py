import streamlit as st
import uuid
import os
import json
from src.scraping import URLProcessor
from src.openai_assistant import OpenAIService
from src.etl import clean_json_openai_response, save_data

AWSIAMCLASSIFIER_ID = "asst_pFXy3ZjfuMSQHUXRSfHqO1C0"
AWSIAMTHREADMODELER20_ID = "asst_SygtKaMk7xSdKqcAiWkrTs5g"

def generate_unique_id():
    """Generates a unique identifier for the session."""
    return str(uuid.uuid4())[:8]

def main():
    st.title("Baseline Forge 2.0")
    
    product_name = st.text_input("AWS Product Name", "")
    product_url = st.text_input("Product Information URL", "")
    actions_url = st.text_input("IAM Actions URL", "")
    output_dir = st.text_input("Output Directory", "data_source")
    
    if st.button("Run Scraping"):
        if not product_name or not product_url or not actions_url:
            st.error("Please fill in all required fields.")
            return
        
        processor = URLProcessor()
        section_id = generate_unique_id()
        
        generated_files = []
        
        # Process product URL
        product_html = processor.fetch_page_content(product_url)
        if product_html:
            product_markdown = processor.convert_to_markdown(product_url, product_html)
            product_filename = f"{product_name}_product_info_{section_id}"
            product_file = save_data(output_dir, product_filename, product_markdown, "md")
            generated_files.append(product_file)
        
        # Process actions URL
        actions_html = processor.fetch_page_content(actions_url)
        if actions_html:
            actions_markdown = processor.convert_to_markdown(actions_url, actions_html)
            actions_filename = f"{product_name}_product_actions_{section_id}"
            actions_file = save_data(output_dir, actions_filename, actions_markdown, "md")
            generated_files.append(actions_file)
        
        if generated_files:
            st.success("Scraping completed successfully!")
            st.write("Generated files:")
            for file in generated_files:
                st.write(f"- {file}")

            # Lendo o conteúdo do arquivo antes de enviá-lo ao assistente OpenAI
            with open(generated_files[1], "r", encoding="utf-8") as file:
                file_content = file.read()

            response_content = OpenAIService.process_file_content(file_content, AWSIAMCLASSIFIER_ID)
            
            if response_content:
                st.success("AWSIAMClassifier processed the file successfully!")

                response_filename = f"{product_name}_product_actions_{section_id}_actions_classified"
                save_data(output_dir, response_filename, response_content, "md")
                
                st.write(f"Response saved in: {os.path.join(output_dir, response_filename)}")
                st.markdown(response_content)
                
                # Processamento e salvamento do JSON corrigido via módulo ETL
                try:
                    extracted_json = clean_json_openai_response(response_content)
                    response_json_filename = f"{product_name}_product_actions_{section_id}_actions_classified"
                    save_data(output_dir, response_json_filename, extracted_json, "json")
                    st.write(f"Response JSON saved in: {os.path.join(output_dir, response_json_filename)}")
                    
                    # Iterar sobre os dados de extracted_json e enviá-los ao assistente
                    output_md_path = os.path.join(output_dir, f"{product_name}_threadmodeled_results_{section_id}.md")
                    
                    for entry in extracted_json:
                        st.write(f"Processing action: {entry['action_iam']}")
                        response_data = OpenAIService.process_file_content(json.dumps(entry), AWSIAMTHREADMODELER20_ID)
                        
                        with open(output_md_path, "a", encoding="utf-8") as md_file:
                            md_file.write(f"\n## Action: {entry['action_iam']}\n")
                            md_file.write(response_data + "\n")
                    
                    st.success(f"IAM Thread Modeler processing completed. Results appended to {output_md_path}")
                    st.write(f"Results saved in: {output_md_path}")
                except ValueError as e:
                    st.error(f"Failed to parse JSON: {e}")
                    st.write("Raw response content:", response_content)
        else:
            st.warning("No files were generated.")

if __name__ == "__main__":
    main()
