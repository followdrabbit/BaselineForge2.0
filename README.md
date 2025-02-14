# 🛡️ Baseline Forge 2.0

O **Baseline Forge 2.0** é um sistema automatizado para homologação de serviços AWS, realizando modelagem de ameaças, criação de baselines de segurança e logs de auditoria. Ele utiliza **Streamlit** para interface, **Web Scraping**, e integração com a API da OpenAI para processamento automático.

## 📌 Funcionalidades
✅ Coleta de dados via **Web Scraping** (extração de HTML e conversão para Markdown)
✅ Processamento de dados usando **OpenAI API**
✅ Geração automática de **Modelagem de Ameaças** e **Baseline de Segurança**
✅ Armazenamento e exportação de dados em **JSON e Markdown**
✅ Interface interativa com **Streamlit**

---

## 📂 Estrutura do Projeto

```bash
📦 baseline-forge-2.0
├── main.py                 # Interface Streamlit
├── 📂 src                  # Código principal
│   ├── etl.py              # Processamento e limpeza de dados
│   ├── scraping.py         # Extração de dados via Web Scraping
│   ├── openai_assistant.py # Comunicação com OpenAI API
├── 📂 data_source          # Armazena arquivos gerados
├── 📂 .streamlit           # Configurações do Streamlit
│   ├── secrets.toml        # Chave de API para OpenAI
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Ignorar arquivos desnecessários no GitHub
├── README.md               # Documentação inicial do projeto
```

# Diagrama de Arquitetura da Aplicação

<img src="diagramas/diagrama_arquitetura_aplicacao.png" alt="Diagrama de Arquitetura da Aplicação" width="600">

---

## 🚀 Instalação e Setup

### 1️⃣ **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/baseline-forge-2.0.git
cd baseline-forge-2.0
```

### 2️⃣ **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Configure o Streamlit**
Crie o diretório `.streamlit` e o arquivo `secrets.toml`:
```bash
mkdir .streamlit
```
Adicione o seguinte conteúdo ao arquivo `.streamlit/secrets.toml`:
```toml
OpenAI_key = "CHAVE_API_OPENAI"
```

### 4️⃣ **Execute a interface Streamlit**
```bash
streamlit run main.py
```
O sistema estará disponível em **http://localhost:8501**.

---

## 📡 Fluxo de Execução

- 1️⃣ **O usuário insere** o **nome do serviço AWS** e as **URLs de documentação** na interface do **Streamlit** (`main.py`).  
- 2️⃣ O sistema **realiza scraping** das páginas usando `Requests` para obter o HTML e o converte para **Markdown** com `HTML2Text` (`scraping.py`).  
   - Os arquivos Markdown resultantes são **salvos no diretório `data_source/`**.  
- 3️⃣ O conteúdo do Markdown é **lido e enviado para a API da OpenAI** (`AWSIAMCLASSIFIER`) para **classificação das ações IAM** (`openai_assistant.py`).  
   - A resposta da OpenAI é retornada no formato **texto bruto**.  
   - O conteúdo classificado é **salvo em arquivos Markdown e JSON** (`etl.py`).  
- 4️⃣ O JSON resultante é processado e enviado novamente para a OpenAI, desta vez para a **modelagem de ameaças** (`AWSIAMTHREADMODELER`) (`openai_assistant.py`).  
   - A OpenAI retorna um relatório de modelagem de ameaças baseado nos dados IAM extraídos.  
   - O relatório é salvo no formato **Markdown** no diretório `data_source/`.  
- 5️⃣ **O resultado final é exibido na interface do Streamlit** e salvo no diretório `data_source/`, permitindo que o usuário acesse e utilize os arquivos gerados.  

---

## 🛠️ Tecnologias Utilizadas
- **🐍 Python** - Linguagem principal
- **📊 Streamlit** - Interface interativa
- **🌍 Requests & HTML2Text** - Web Scraping
- **🤖 OpenAI API** - Processamento de conteúdo
- **🗄️ JSON & Markdown** - Armazenamento de dados

---

## 📜 Licença

Este projeto é **open-source** e está sob a licença **MIT**.

---

## 📌 Melhorias Pendentes (TO DO)  

- [ ] Aprimorar as mensagens exibidas na tela para fornecer feedback claro e detalhado sobre o progresso das operações.  
- [ ] Implementar um módulo de logging que registre eventos e erros em arquivos para auditoria e depuração.  
- [ ] Adicionar uma funcionalidade para contabilizar e exibir a quantidade de tokens consumidos nas interações com a OpenAI API.  
- [ ] Melhorar a robustez do módulo de execução do assistente, garantindo tratamento adequado para diferentes status de erro (exemplo: `RuntimeError: Unexpected run status: failed`).  
- [ ] Criar um sistema de monitoramento de execução que registre o status de cada etapa do processo, permitindo a reexecução seletiva apenas das etapas que falharam.  
- [ ] Implementar um mecanismo de segmentação de entrada para dividir grandes quantidades de dados em partes menores e enviá-las em múltiplas requisições à OpenAI API, respeitando o limite de 256.000 caracteres.  
- [ ] Adicionar a lógica para que cada *action* identificada como *"requer controle"* seja enviada para um assistente que verificará as *conditions* possíveis e determinará se é necessário adicionar alguma *condition* ou outro mecanismo de mitigação.  

## 🐛 Bug Fix  

- [ ] Corrigir o problema ao enviar grandes quantidades de dados para a OpenAI API, garantindo que a entrada respeite o limite de 256.000 caracteres (`BadRequestError: string too long`).  
- [ ] Analisar e corrigir o problema de classificação incompleta das ações, garantindo que todas as ações sejam devidamente processadas, possivelmente dividindo a lista em partes menores para facilitar a análise do assistente.
