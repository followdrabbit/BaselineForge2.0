
## Action: CloneReceiptRuleSet
### **Modelagem de Ameaças para Ação IAM: CloneReceiptRuleSet**

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                                                                            | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                  | **Recomendações de Segurança**                                                                                     |
|-------------------------|---------------|------------------------------------------------------------------------------------------|--------------------------|---------------------------------------|-----------|-----------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `CloneReceiptRuleSet`   | BUILD         | Permissão para criar um conjunto de regras de recebimento clonando um existente no SES. | Initial Access           | T1078 - Valid Accounts                | **Alto**  | **Requer Controle**   | Ação explorável para criar regras de e-mail que podem redirecionar tráfego malicioso ou interceptar comunicações. | Monitorar criação e modificação de regras no SES, restringir uso por meio de políticas IAM, implementar o princípio de menor privilégio, revisar logs regularmente no AWS CloudTrail. |

### **Notas e Contexto**
- **Avaliação de Risco**: A capacidade de clonar regras de recebimento pode ser utilizada para interceptar ou redirecionar e-mails de forma maliciosa, comprometendo assim a confidencialidade das comunicações. Isso justifica a classificação de risco alto, especialmente em setores sujeitos a regulamentações rigorosas.
- **Recomendações Específicas**:
  - **IAM Policies**: Configure as políticas de IAM para permitir apenas usuários ou funções específicas e necessárias para realizar essa ação.
  - **AWS CloudTrail**: Habilitar a auditoria de alterações nos conjuntos de regras e revisar regularmente.
  - **Monitoramento Contínuo**: Usar AWS Security Hub e AWS GuardDuty para identificar comportamentos suspeitos associados ao SES.
  - **Princípio do Menor Privilégio**: Apenas conceder as permissões mínimas necessárias para realizar operações legítimas.

Caso precise de mais informações ou análise sobre outras ações IAM, estou à disposição para ajudar!

## Action: CreateConfigurationSet
### 📊 Modelagem de Ameaças AWS com MITRE ATT&CK

| **AWS IAM Action**           | **BUILD/RUN** | **Descrição**                                                    | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                  | **Recomendações de Segurança**                                                                              |
|------------------------------|---------------|------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `CreateConfigurationSet`     | BUILD         | Permissão para criar um novo conjunto de configurações no SES.   | Defense Evasion           | T1562.001 - Impair Defenses: Unsecured Communication | **Médio**  | **Melhor Prática**     | A criação de conjuntos de configuração pode ser utilizada para alterar a forma como mensagens são enviadas, potencialmente evadindo detecções de segurança. | Restringir a criação de conjuntos de configuração a usuários confiáveis por meio de políticas IAM; monitorar eventos de criação com AWS CloudTrail. |

### 🔍 Análise Detalhada:
- **Risco**: A ação é categorizada como **BUILD** porque pode criar novos conjuntos de configuração, o que poderia potencialmente alterar fluxos de e-mail para desviar de sistemas de detecção.
- **Justificativa da Classificação**: Esta ação não compromete diretamente a confidencialidade ou integridade, mas pode impactar a detecção de anomalias, justificando assim um risco **Médio**.
- **Recomendações de Segurança**: Utilize políticas de IAM para restringir esta ação a contas ou papéis com necessidade legítima. Monitore logs do AWS CloudTrail para detectar criações não autorizadas ou suspeitas de conjuntos de configuração.

### 🛡️ Ferramentas Sugeridas:
- **AWS CloudTrail**: Para monitorar e registrar eventos de API sobre criação de conjuntos de configuração.
- **IAM Policies**: Para implementar o princípio do menor privilégio.
- **AWS Security Hub**: Para integrar e correlacionar eventos de segurança. 

Estas práticas ajudam a garantir que cada modificação nos conjuntos de configuração seja justificada e segura no contexto do ambiente AWS.

## Action: CreateConfigurationSetEventDestination
### Modelagem de Ameaças para AWS IAM Action

| **AWS IAM Action**                        | **BUILD/RUN** | **Descrição**                                                                          | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**        | **Justificativa da Classificação**                                                                                                                                         | **Recomendações de Segurança**                                                                                                               |
|-------------------------------------------|---------------|----------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateConfigurationSetEventDestination` | BUILD        | Permite a criação de um destino de evento para um conjunto de configurações.           | Initial Access            | T1078 - Valid Accounts               | **Alto**  | Requer Controle          | Essa ação pode ser explorada para configurar destinos de eventos maliciosos, possibilitando a interceptação ou redirecionamento de dados de eventos sensíveis.                                                       | Restringir quem pode criar destinos de eventos por meio de políticas IAM. Monitorar e revisar regularmente os destinos de eventos configurados. Utilizar logs do AWS CloudTrail para auditoria. |

---

### Justificativa e Mapeamento

**Tática e Técnica**:
- **Initial Access** está alinhada com a possibilidade de um invasor obter acesso inicial configurando destinos de eventos que desviam ou monitoram informações sensíveis sem autorização.

**Risco e Avaliação**:
- A ação é marcada como **Alto** risco dada a capacidade de um atacante potencialmente desviar dados críticos ou monitorar atividades.
- **Requer Controle** devido ao impacto adverso potencialmente significativo combinado com a facilidade de criação de configuração se indevidamente acessada.

**Recomendações de Segurança**:
- **Políticas IAM**: Aplicar o princípio de menor privilégio, garantindo que apenas usuários autorizados possam usar esta ação.
- **Monitoramento Contínuo**: Implementar monitoração com AWS CloudTrail e estabelecer alertas para alterações em destinos de eventos.
- **Auditoria Regular**: Revisar regularmente os destinos configurados e suas permissões para garantir conformidade e detectar anomalias rapidamente.


## Action: CreateConfigurationSetTrackingOptions
### 🛡️ Modelagem de Ameaças AWS para `CreateConfigurationSetTrackingOptions`

| **AWS IAM Action**                       | **BUILD/RUN** | **Descrição**                                                                                          | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                                                                  | **Recomendações de Segurança**                                                                                                                                         |
|------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------|-----------------------------|---------------------------------------|-----------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateConfigurationSetTrackingOptions` | BUILD         | Cria uma associação entre um conjunto de configurações e um domínio personalizado para rastreamento de eventos de abertura e clique. | Collection                    | T1114.001 - Email Collection          | Médio     | Melhor Prática         | A ação permite configurar o rastreamento de aberturas e cliques de e-mails, que pode ser monitorado para fins analíticos. Contudo, o risco de uso indevido é limitado. | Restringir a ação a usuários e funções específicas via políticas IAM, monitorar regularmente logs de eventos usando AWS CloudTrail para atividades suspeitas.                     |

### 📌 Explicações Adicionais

- **Classificação de Risco**: A ação é considerada de **risco médio** porque envolve a coleta de dados de rastreamento associados a e-mails, mas não prejudica diretamente a confidencialidade, integridade ou disponibilidade.
- **Justificativa da Classificação**: A ação, ao ser um componente de configuração de monitoramento, não é altamente explorável, mas o rastreamento de eventos deve ser gerenciado adequadamente para evitar falhas de privacidade ou vazamentos de dados.
- **Técnica (MITRE ATT&CK)**: Foi mapeada para a coleção de e-mails porque lida com o rastreamento e dados de comunicações eletrônicas.

### 🔒 Diretrizes Adicionais de Segurança
- **Princípio do Menor Privilégio**: Aplique controles de acesso estritos para garantir que apenas administradores ou usuários autorizados possam modificar configurações de rastreamento.
- **Monitoramento Contínuo**: Utilizar AWS CloudWatch e CloudTrail para monitorar mudanças nas configurações e detectar atividades incomuns.
- **Auditorias Regulares**: Realize auditorias periódicas das configurações e permissões para garantir conformidade com regulamentações, como LGPD e ISO 27001.

## Action: CreateCustomVerificationEmailTemplate
Com base na entrada fornecida, aqui está a modelagem de ameaças para a ação IAM `CreateCustomVerificationEmailTemplate`:

| **AWS IAM Action**                   | **BUILD/RUN** | **Descrição**                                                                                | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                                                  | **Recomendações de Segurança**                                                                                                                                               |
|--------------------------------------|---------------|----------------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateCustomVerificationEmailTemplate` | BUILD         | Concede permissão para criar um novo modelo de e-mail de verificação personalizado.          | Initial Access            | T1078 - Valid Accounts                | **Médio** | **Melhor Prática** | Embora a ação não comprometa diretamente o sistema, criar modelos de e-mail personalizados pode ser usado para phishing em campanhas de engenharia social.                      | Restringir a criação de modelos a usuários confiáveis por meio de políticas IAM. Monitorar e logar atividades relacionadas à criação de modelos customizados usando AWS CloudTrail. |

### Justificativas e Recomendações

1. **Mapeamento para MITRE ATT&CK**:
   - A ação permite criar modelos de e-mail que podem potencialmente ser explorados para enganar usuários através de e-mails de phishing, justificando a associação com a técnica de **Initial Access**.

2. **Classificação de Risco**:
   - **Risco Médio**: Embora a ação não cause dano imediato aos recursos AWS, ela pode ser uma porta de entrada para ataques de phishing se usada de maneira maliciosa.
   
3. **Recomendações de Segurança**:
   - Implementar **políticas de menor privilégio** para que apenas usuários autorizados possam criar modelos de e-mail.
   - Usar ferramentas de monitoramento como o **AWS CloudTrail** para auditar a criação e modificação desses modelos.
   - Educar os usuários sobre **práticas seguras de e-mail** para reduzir a eficácia de campanhas de phishing.

O uso de práticas de segurança rigorosas, juntamente com o monitoramento contínuo, garantirá que essa ação IAM não seja explorada maliciosamente.
