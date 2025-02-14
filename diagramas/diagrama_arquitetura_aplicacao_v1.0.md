graph TD
    %% Entrada do Usuário
    A["👤 Arquiteto de Segurança"]
    A -->|📩 Nome do serviço AWS, URLs, PDFs| B["🖥️ FastAPI (Backend)"]

    %% Coleta de Dados
    subgraph Data Ingestion ["🟢 Coleta e Armazenamento"]
        B -->|🌍 Web Scraping| C["🎭 Playwright"]
        B -->|📄 Conversão para Markdown| D["📑 Markdownify"]
        B -->|📂 Extração de PDFs| E["📜 pdf2text"]
        C --> D
        E --> D
        D --> F["🗄️ Armazenamento de Documentos"]
    end

    %% Indexação e IA
    subgraph AI Processing ["🟡 Processamento com IA e RAG"]
        F -->|📡 Indexação| G["📦 ChromaDB"]
        G -->|🔍 Busca Inteligente| H["🧠 RAG (ChromaDB)"]
        H -->|🚀 Envio para IA| I["🤖 Ollama (Modelagem de Ameaças)"]
        I -->|📝 Gera Markdown| J["📂 Modelagem de Ameaças"]
        I -->|📜 Gera Baseline de Segurança| K["📂 Baseline de Segurança"]
    end

    %% Publicação dos Documentos
    subgraph Docs Publication ["🔵 Publicação no Hugo"]
        J -->|🌐 Adiciona ao Hugo| L["📑 Página de Modelagem"]
        K -->|🌐 Adiciona ao Hugo| M["📑 Página de Baseline"]
        B -->|📊 Gera Log de Auditoria| N["📝 Arquivo de Auditoria"]
        N -->|🌐 Adiciona ao Hugo| O["📑 Página de Auditoria"]
    end

    %% Consulta do Usuário
    subgraph User Interaction ["🔴 Acesso aos Documentos"]
        P["👀 Usuário"]
        P -->|🔎 Acessa Hugo| L
        P -->|🔎 Acessa Hugo| M
        P -->|🔎 Acessa Hugo| O
    end

    %% Infraestrutura
    subgraph Infrastructure ["⚙️ Infraestrutura"]
        Q["🖥️ Ubuntu (OS)"]
        R["🐳 Docker"]
        S["🔗 Docker Compose"]
        T["🐍 Python + FastAPI"]
        U["🗄️ SQLite (Banco de Dados)"]
        V["📦 ChromaDB (Banco Vetorial)"]
        W["📖 Hugo Docs + Tema Relearn"]
        Q --> R
        R --> S
        S --> T
        T --> U
        T --> V
        W --> P
    end

    %% Conectando Infraestrutura com Processamento
    B -->|📊 Armazena Dados| U
    G -->|📡 Armazena Embeddings| V
    W --> L
    W --> M
    W --> O
