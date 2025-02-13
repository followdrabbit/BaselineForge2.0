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
1️⃣ O usuário insere **nome do produto AWS** e URLs de documentação.
2️⃣ O sistema realiza **scraping** das páginas e converte para Markdown.
3️⃣ O conteúdo é enviado para a **OpenAI API** para classificação de ações IAM.
4️⃣ Os dados processados são armazenados em **arquivos JSON e Markdown**.
5️⃣ O resultado final é exibido na interface e salvo no diretório `data_source/`.

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
🔥 **Contribuições são bem-vindas!** Qualquer dúvida, entre em contato. 🚀

---

## 📌 Melhorias Pendentes (TO DO)

- [ ] Aprimorar as mensagens exibidas na tela para fornecer feedback claro e detalhado sobre o progresso das operações.
- [ ] Implementar um módulo de logging que registre eventos e erros em arquivos para auditoria e depuração.
- [ ] Adicionar uma funcionalidade para contabilizar e exibir a quantidade de tokens consumidos nas interações com a OpenAI API.
- [ ] Melhorar a robustez do módulo de execução do assistente, garantindo tratamento adequado para diferentes status de erro (exemplo: `RuntimeError: Unexpected run status: failed`).
- [ ] Criar um sistema de monitoramento de execução que registre o status de cada etapa do processo, permitindo a reexecução seletiva apenas das etapas que falharam.

