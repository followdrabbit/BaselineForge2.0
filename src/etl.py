import json
import re
import os

def clean_json_openai_response(response_content):
    """
    Cleans the response from OpenAI Assistant, removing markdown formatting and extracting valid JSON.

    Args:
        response_content (str): The raw response content from OpenAI.

    Returns:
        dict or list: Parsed JSON data.

    Raises:
        ValueError: If the extracted content is not a valid JSON.
    """
    try:
        # Remove Markdown JSON code block delimiters
        cleaned_response = re.sub(r"```json|```", "", response_content).strip()
        
        # Convert to JSON
        extracted_json = json.loads(cleaned_response)

        # Ensure it's either a dictionary or a list
        if not isinstance(extracted_json, (dict, list)):
            raise ValueError(f"Expected JSON object (dictionary or list), but got {type(extracted_json).__name__}")

        return extracted_json

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}")

def save_data(output_dir, filename, data, file_format=None):
    """
    Saves data to a file in the specified format.

    Args:
        output_dir (str): Directory where the file will be saved.
        filename (str): Name of the file (without extension or with any).
        data (dict, list, or str): Data to be saved.
        file_format (str, optional): Format to save the file (json, txt, md). If None, inferred from filename.

    Returns:
        str: Path to the saved file.

    Raises:
        ValueError: If an unsupported file format is provided.
        IOError: If the file cannot be saved.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Define a extensão correta do arquivo
    ext = os.path.splitext(filename)[-1].lower()
    inferred_format = ext.lstrip('.') if ext else None
    file_format = file_format or inferred_format

    # Se ainda não tiver extensão, adiciona a correta
    if not ext and file_format:
        filename += f".{file_format}"

    file_path = os.path.join(output_dir, filename)

    try:
        if file_format == "json":
            if not isinstance(data, (dict, list)):
                raise ValueError(f"Invalid data type for JSON: {type(data).__name__}. Expected dict or list.")
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        elif file_format in ["md", "txt"]:
            if not isinstance(data, str):
                raise ValueError(f"Invalid data type for text: {type(data).__name__}. Expected string.")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(data)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

        print(f"File saved: {file_path}")
        return file_path
    except Exception as e:
        raise IOError(f"Failed to save file '{filename}': {e}")
