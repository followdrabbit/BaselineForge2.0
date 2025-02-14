graph TD
    %% Entrada do Usuário
    A["👤 Arquiteto de Segurança"]
    A -->|📩 Nome do serviço AWS, URLs| B["🖥️ Streamlit (Interface) (main.py)"]

    %% Coleta de Dados
    subgraph Data_Ingestion ["🟢 Coleta de Dados (scraping.py)"]
        B -->|🌍 Requisição de Página| C["🌍 Requests (fetch_page_content)"]
        C -->|📄 Conversão para Markdown| D["📑 HTML2Text (convert_to_markdown)"]
        D -->|📂 Salva Arquivos Markdown| E["📂 data_source"]
    end

    %% Processamento com OpenAI
    subgraph AI_Processing ["🟡 Processamento com OpenAI (openai_assistant.py)"]
        E -->|📄 Carrega Arquivo Markdown| F["📜 Leitura do Arquivo (main.py)"]

        %% Primeira Chamada OpenAI - Classificação IAM
        F -->|🚀 Envio para OpenAI API| G["🤖 AWSIAMCLASSIFIER"]
        G -->|📊 Classificação de Ações IAM| H["📝 Resposta da OpenAI"]
        H -->|📂 Salva JSON/Markdown| I["📂 data_source"]

        %% Segunda Chamada OpenAI - Modelagem de Ameaças
        I -->|📊 Limpeza de Dados| J["📂 clean_json_openai_response (etl.py)"]
        J -->|🚀 Envio para OpenAI API| K["🤖 AWSIAMTHREADMODELER"]
        K -->|📊 Modelagem de Ameaças| L["📂 Threat Modeling"]
        L -->|📂 Salva Resultados| I
    end
