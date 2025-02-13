
## Action: CloneReceiptRuleSet
| **AWS IAM Action**        | **BUILD/RUN** | **Descrição**                                           | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco**  | **Classificação**   | **Justificativa da Classificação**                                                                                                                                          | **Recomendações de Segurança**                                                                                     |
|---------------------------|---------------|--------------------------------------------------------|---------------------------|---------------------------------------|------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `CloneReceiptRuleSet`     | BUILD         | Cria um conjunto de regras de recebimento clonando um existente. | Initial Access            | T1078 - Valid Accounts                | **Alto**   | **Requer Controle**  | Essa ação pode ser explorada para criar regras de e-mail que redirecionam tráfego malicioso ou interceptam comunicações. Pode ser usada por atores maliciosos para obter uma posição inicial. | Monitorar criação e modificação de regras no SES, restringir uso por meio de políticas IAM. Implementar o uso de MFA e o princípio do menor privilégio. |

## Action: CreateConfigurationSet
Com base nos dados fornecidos, vamos proceder com a análise da ação IAM dentro do contexto AWS e mapeá-la para o framework MITRE ATT&CK, considerando os riscos associados e as recomendações de segurança. Aqui está a tabela resultante da modelagem de ameaças:

| **AWS IAM Action**        | **BUILD/RUN** | **Descrição**                                     | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                   | **Recomendações de Segurança**                                                                                                                                             |
|---------------------------|--------------|--------------------------------------------------|---------------------------|--------------------------------------|-----------|------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateConfigurationSet` | BUILD        | Cria um novo conjunto de configuração.            | Defense Evasion           | T1562.001 - Impair Defenses: Disable or Modify Tools | **Médio** | **Melhor Prática**     | A ação pode ser usada para criar configurações maliciosas que desviam a detecção ou monitoramento. | Implementar revisões de configuração automatizadas usando AWS Config e permitir apenas usuários autorizados para a operação por meio de políticas IAM rígidas.                                                              |

### Justificativa e Detalhes Adicionais

1. **Tática e Técnica MITRE ATT&CK:**
   - A ação `CreateConfigurationSet` tem o potencial de ser usada para modificar configurações de segurança para evitar a detecção, embora esse não seja seu propósito principal. Portanto, está associada à tática de "Defense Evasion" e à técnica de "Impair Defenses" (Modificar Ferramentas).

2. **Classificação de Risco:**
   - **Médio**: Embora a ação possa ser usada de maneira mal-intencionada, não há impacto direto na confidencialidade, integridade ou disponibilidade automaticamente. Contudo, as implicações de configurações criadas com propósitos maliciosos representam um risco que exige atenção para mitigação e monitoramento apropriados.

3. **Recomendações de Segurança:**
   - Utilize ferramentas como **AWS Config** para auditar constantemente configurações e garantir que qualquer novo conjunto de configuração criado siga padrões de segurança predefinidos.
   - Restrinja permissões para esta ação através de políticas AWS IAM baseadas no princípio do menor privilégio, assegurando que apenas usuários ou roles necessários tenham acesso.
   - Monitore esta ação e outras alterações de configuração com o uso de **AWS CloudTrail** para assegurar visibilidade sobre quem está realizando alterações e quando.

Essas medidas ajudam a garantir que a segurança não seja comprometida através do uso inadvertido ou mal-intencionado dessa ação IAM.

## Action: CreateConfigurationSetEventDestination
### 🚀 Modelagem de Ameaças AWS com MITRE ATT&CK

Com base na ação IAM fornecida, abaixo está a modelagem de ameaças detalhada.

| **AWS IAM Action**                            | **BUILD/RUN** | **Descrição**                                                    | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                                                                     | **Recomendações de Segurança**                                                                                                                                                                  |
|-----------------------------------------------|---------------|-----------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateConfigurationSetEventDestination`      | BUILD         | Cria um destino de evento para um conjunto de configuração.     | Collection                | T1026 - Data From Information Repositories              | **Médio**  | **Melhor Prática**     | Esta ação pode ser explorada para capturar, registrar ou monitorar dados sobre eventos que ocorrem nos sistemas, potencialmente desviando informações sensíveis.          | Implementar políticas IAM para limitar quem pode criar destinos de eventos; usar AWS CloudTrail para monitorar e registrar a atividade de configuração; aplicar o princípio do menor privilégio. |

### **🔒 Notas Adicionais de Segurança:**
- **Monitoramento Contínuo:** Aproveitar o AWS CloudTrail para registros detalhados de todas as ações relacionadas à configuração de destino de eventos, detectando anomalias ou atividades não autorizadas.
- **Princípio do Menor Privilégio:** Assegurar que apenas usuários ou sistemas que realmente necessitem desta permissão a possuam, reduzindo a superfície de ataque potencial.
- **Revisão Regular de Acessos:** Verificar periodicamente quem possui essas permissões e ajustar conforme necessário, levando em consideração mudanças na equipe ou nos requisitos do projeto.

### 🌐 Contexto Regulatório:
A segurança de dados é crucial, especialmente em contextos onde é necessário conformidade com regulamentos como a LGPD e a ISO 27001. A criação de destinos de eventos pode potencialmente expor dados sensíveis, e controles devem ser implementados para garantir que apenas dados necessários sejam acessados e armazenados de maneira segura.

Ao aplicar essa tabela de modelagem de ameaças, as organizações podem melhorar sua postura de segurança e reduzir riscos associados ao uso indevido de ações IAM dentro do AWS.

## Action: CreateConfigurationSetTrackingOptions
### Modelagem de Ameaças AWS para Ação IAM: `CreateConfigurationSetTrackingOptions`

Com base nos dados fornecidos sobre a ação IAM `CreateConfigurationSetTrackingOptions`, vamos criar uma tabela de modelagem de ameaças seguindo as diretrizes do MITRE ATT&CK:

| **AWS IAM Action**                        | **BUILD/RUN** | **Descrição**                                                                                                                | **Tática (MITRE ATT&CK)**   | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                              | **Recomendações de Segurança**                                                                                                       |
|-------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------|-----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `CreateConfigurationSetTrackingOptions`   | BUILD         | Cria uma associação entre um conjunto de configuração e um domínio personalizado para rastreamento de eventos de abertura e clique. | Collection                 | T1114 - Email Collection             | **Médio** | **Melhor Prática**    | Esta ação pode ser usada para coletar informações de e-mails, como eventos de abertura e cliques, o que, se mal configurado, pode afetar a privacidade.                      | Garantir que apenas usuários autorizados possam criar ou modificar conjuntos de configuração de rastreamento. Utilizar políticas de IAM restritivas e monitorar logs. |

### Explicação Detalhada

1. **Análise da Ação IAM**:
   - **Risco**: A ação tem um risco médio, pois pode ser utilizada para redirecionar ou registrar acessos e interações de e-mail sem o devido controle, impactando a confidencialidade.
   - **Classificação**: Construção (BUILD). Como essa ação envolve a criação de configurações, ela se enquadra na categoria BUILD.

2. **Mapeamento para MITRE ATT&CK**:
   - **Tática**: `Collection`. A ação se relaciona com a coleta de informações devido ao seu potencial de monitorar aberturas e cliques em e-mails.
   - **Técnica/Subtécnica**: `T1114 - Email Collection`. Esta técnica aborda o monitoramento e coleta de dados de comunicações de e-mail.

3. **Recomendações de Segurança**:
   - **Acesso Restritivo**: Implementar políticas de IAM estritas para limitar quem pode criar ou modificar as opções de rastreamento de configuração.
   - **Monitoramento Contínuo**: Utilizar serviços como AWS CloudTrail para monitorar mudanças e acessos a estas ações. Considerar o uso de AWS Security Hub para detectar e responder a configurações suspeitas.
   - **Princípio do Menor Privilégio**: Assegurar que os usuários tenham apenas o acesso necessário para suas funções, minimizando assim a superfície de ataque.

## Action: CreateCustomVerificationEmailTemplate
### 🛡️ Modelagem de Ameaças para "CreateCustomVerificationEmailTemplate"

| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                            | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                                 | **Recomendações de Segurança**                                                                                          |
|--------------------------------------------|---------------|----------------------------------------------------------|---------------------------|---------------------------------------|-----------|-------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `CreateCustomVerificationEmailTemplate`    | BUILD         | Cria um novo modelo de email de verificação personalizada.| Collection                | T1114.002 - Email Collection         | **Médio**  | **Melhor Prática** | A criação de modelos personalizados pode ser usada para coletar informações ou realizar phishing, embora explorá-la geralmente seja mais complexa. | Monitorar a criação e alteração de templates; aplicar políticas restritivas de IAM, garantindo permissões mínimas necessárias; usar AWS CloudTrail para auditoria. |

### 📝 Justificativa Detalhada

- **Tática (Collection):** Adversários podem usar e-mails de verificação personalizados para capturar informações sensíveis ou redirecionar usuários para sites maliciosos.
- **Técnica (T1114.002 - Email Collection):** Modificação dos templates de e-mail pode ser um vetor para coletar informações de forma maliciosa.
- **Risco Médio:** Embora o impacto potencial seja significativo se explorado, criar um modelo de e-mail personalizado malicioso requer acesso IAM apropriado, tornando a exploração mais difícil se boas práticas de segurança estiverem em vigor.

### 🔐 Recomendações de Segurança

1. **Monitoramento e Auditoria:** 
   - Use **AWS CloudTrail** para registrar e monitorar a criação e alteração de modelos de e-mail, assegurando que todas as atividades sejam auditáveis.

2. **Princípio do Menor Privilégio:**
   - Restrinja as permissões necessárias para criar ou alterar modelos de e-mail usando **IAM Policies**, assegurando que apenas usuários autorizados possam realizar essas ações.

3. **Configurações de Segurança do AWS Config:**
   - Configure regras de **AWS Config** para verificar a conformidade com práticas de segurança e detectar qualquer configuração não autorizada ou suspeita.

4. **Detecção e Monitoramento Contínuo:**
   - Implemente soluções como **AWS GuardDuty** para detecções avançadas e respostas a atividades incomuns ou potencialmente maliciosas.

## Action: CreateReceiptFilter
### 📊 Tabela de Modelagem de Ameaças

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                                    | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                                                                    | **Recomendações de Segurança**                                                                                                     |
|-------------------------|--------------|------------------------------------------------|--------------------------|--------------------------------------|-----------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `CreateReceiptFilter`   | BUILD        | Cria um novo filtro de endereço IP.            | Defense Evasion          | T1562.001 - Impair Defenses: Disable or Modify Tools | **Médio** | **Melhor Prática** | A ação pode ser usada para criar filtros que bypassam medidas de segurança configuradas, facilitando a evasão de detecção de e-mails indesejados ou maliciosos. | Monitorar e auditar a criação e modificação de filtros de recebimento; restringir permissões através de políticas IAM; habilitar logs com AWS CloudTrail para rastreamento de atividades. |

---

### 🛠️ Explicações e Recomendações Detalhadas:

1. **Tática e Técnica (MITRE ATT&CK):**
   - **Defense Evasion**: Modificação ou criação de ferramentas e filtros pode permitir que atacantes ocultem atividades potencialmente maliciosas.
   - **T1562.001 - Impair Defenses**: Modificar ou desativar ferramentas de defesa para evitar detecção.

2. **Justificativa da Classificação:**
   - **Impacto**: Embora a criação de filtros não comprometa diretamente recursos críticos, a potencial para camuflar comportamento malicioso representa um risco moderado.
   - **Probabilidade de Exploração**: Existem cenários plausíveis onde essa ação pode ser utilizada para evasão de detecção, especialmente se combinada com outras técnicas de ataque.

3. **Recomendações de Segurança:**
   - **Monitoramento Contínuo**: Utilize o AWS CloudTrail para manter logs de atividades relacionadas à criação e modificação de filtros. Isso fornece visibilidade e ajuda na detecção de configurações anômalas.
   - **Restrições de Permissão**: Aplique o princípio do menor privilégio garantindo que somente usuários e serviços necessários tenham acesso à ação `CreateReceiptFilter`.
   - **Revisões Regulares de Políticas**: Implemente revisões regulares das políticas IAM para assegurar que os filtros criados sejam consistentes com as políticas de segurança e conformidade da organização.

Essas ações pretendem não apenas mitigar riscos de forma proativa, mas também alavancar práticas de segurança que maximizem a segurança geral do ambiente AWS.

## Action: CreateReceiptRule
| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `CreateReceiptRule` | BUILD | Cria uma regra de recebimento no Amazon SES. | Collection | T1114 - Email Collection | **Alto** | **Requer Controle** | A ação pode ser usada para criar regras que interceptam ou desviam e-mails de interesse do adversário. | Implementar políticas de IAM restritivas para controle de criação e modificação de regras de e-mail, ativar registro de auditoria com AWS CloudTrail para monitoramento dessas atividades. |

## Action: CreateReceiptRuleSet
| **AWS IAM Action**           | **BUILD/RUN** | **Descrição**                                        | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                                                                                                           | **Recomendações de Segurança**                                                                                                                                           |
|------------------------------|---------------|------------------------------------------------------|---------------------------|----------------------------------------|-----------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateReceiptRuleSet`       | BUILD         | Cria um conjunto de regras de recebimento vazio.     | Initial Access            | T1098 - Account Manipulation          | **Médio**  | **Melhor Prática** | Esta ação pode ser utilizada para estabelecer configurações que facilitem acesso não autorizado, embora diretamente não comprometa a integridade ou confidencialidade dos dados.          | Restringir quem pode criar conjuntos de regras através de políticas IAM, monitorar e auditar criação e modificação de regras no SES, utilizar o princípio do menor privilégio.                  |

### **Detalhes da Análise**
- **Tática (MITRE ATT&CK)**: A criação de regras pode ser mapeada para a tática de **Initial Access**, onde adversários podem configurar sistemas para criar portas de entrada para futuras explorações.
- **Técnica/Subtécnica**: **T1098 - Account Manipulation**. Adversários poderiam potencialmente usar essa funcionalidade para manipular contas ou configurações de forma a beneficiar ações maliciosas futuras.
- **Risco e Classificação**: Classificado como **Médio - Melhor Prática**, já que a ação isolada não compromete diretamente os recursos, mas possui potencial de exploração se associada a outras ações não mitidas. Ela requer melhores práticas para evitar uso indevido.
- **Recomendações de Segurança**: Aplicar políticas de menor privilégio para limitar quem pode criar e modificar conjuntos de regras. Realizar monitoramento contínuo e auditorias sobre essas ações para detecção precoce de atividades suspeitas.

## Action: CreateTemplate
Baseado na ação IAM fornecida, vamos realizar a modelagem de ameaças de acordo com as diretrizes estabelecidas:

---

### **Modelagem de Ameaças AWS para Ação IAM**

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**             | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**       | **Justificativa da Classificação**                                                                            | **Recomendações de Segurança**                                                                                                                                             |
|------------------------|--------------|--------------------------|---------------------------|--------------------------------------|-----------|-------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateTemplate`       | BUILD        | Cria um modelo de email. | Initial Access            | T1566 - Phishing                    | **Alto**  | **Requer Controle**     | A ação pode ser explorada para criar modelos de email maliciosos para campanhas de phishing.                     | Restringir a criação de modelos apenas para usuários autorizados, monitorar e registrar a criação e modificação de modelos por meio de AWS CloudTrail. Implementar políticas de segurança no uso do SES.    |

---

### **Detalhes Adicionais**
- **Tática (Initial Access)**: A criação de modelos de e-mail pode ser explorada por agentes maliciosos para lançar ataques de phishing, comprometendo o acesso inicial a sistemas e serviços.
- **Técnica (Phishing)**: Utilizando modelos maliciosos, um adversário pode simular comunicações legítimas, induzindo usuários a revelar credenciais ou executar ações não autorizadas.

---

### **Recomendações para Reforço da Segurança**
- **Políticas de Restrição IAM**: Apenas usuários com necessidade clara devem ter permissão para criar templates de e-mail.
- **Monitoramento Contínuo**: Utilize AWS CloudTrail para auditar ações relacionadas a criação e modificação de templates.
- **Educação e Conscientização**: Realizar treinamentos de segurança para sensibilizar usuários sobre os riscos de phishing.
- **Detecção de Anomalias**: Implementar sistemas de detecção para identificar atividades suspeitas, como a criação de templates fora do padrão.

Estas ações são críticas para evitar o uso indevido de modelos de email no contexto de ameaças cibernéticas, como ataques de phishing.

## Action: DeleteConfigurationSet
| **AWS IAM Action**          | **BUILD/RUN** | **Descrição**                                        | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                    | **Recomendações de Segurança**                                                                                                                                                                  |
|-----------------------------|--------------|----------------------------------------------------|----------------------------|---------------------------------------|-----------|-----------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteConfigurationSet`    | BUILD        | Exclui um conjunto de configuração existente.      | Impact | T1485 - Data Destruction                | **Crítico** | **Requer Controle** | A ação pode ser utilizada para destruir dados críticos de configuração, levando à disrupção de serviços que dependem destas configurações. | Implementar controle de acesso rigoroso e logs para exclusões, revisar permissões de IAM para assegurar que apenas usuários autorizados possam executar essa ação. Habilitar o AWS CloudTrail para monitoramento. |



## Action: DeleteConfigurationSetEventDestination
### Tabela de Modelagem de Ameaças

| **AWS IAM Action**                        | **BUILD/RUN** | **Descrição**                                   | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                              | **Recomendações de Segurança**                                                                                                                                                  |
|-------------------------------------------|---------------|-------------------------------------------------|--------------------------|--------------------------------------|-----------|----------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteConfigurationSetEventDestination`  | BUILD         | Exclui um destino de evento.                    | Impact | T1485 - Data Destruction           | **Alto**   | **Requer Controle**  | A exclusão de destinos de eventos pode resultar na perda de monitoramento e alertas críticos no Amazon SES, impactando a capacidade de detectar e reagir a incidentes de segurança. | Implementar políticas IAM restritivas que limitem quem pode executar a exclusão de configurações, utilizar AWS CloudTrail para monitorar atividades suspeitas e auditar regularmente permissões atreladas a ações sensíveis. |

---

### Detalhamento e Justificativas

- **Tática e Técnica (MITRE ATT&CK):** A ação de deletar destinos de evento no Amazon SES pode ser associada à tática de **Impacto** (IMPACT), mais precisamente à técnica de **Destruição de Dados** (T1485), já que remove aspectos críticos do monitoramento e pode prejudicar significativamente a visibilidade e o alerta de eventos dentro do sistema.
  
- **Risco e Classificação:** A ação `DeleteConfigurationSetEventDestination` está classificada como **Alto** devido ao potencial severo de comprometer a integridade da monitoração de eventos. Tal ação, se explorada maliciosamente, poderia incapacitar detecções automáticas, gerando riscos graves para a segurança.

- **Recomendações de Segurança:** Como prática de mitigação, é crucial manter privilégios mínimos em conformidade ao modelo de Zero Trust, assegurando que somente roles explicitamente autorizadas consigam realizar essa ação. Além disso, verificar frequentemente logs do AWS CloudTrail para identificar atividades atípicas e manter controles rigorosos sobre alterações nas configurações de eventos são medidas recomendadas para detectar e evitar explorações.

Essa análise ajuda a fortalecer a segurança em ambientes AWS, garantindo que ações IAM sensíveis recebam a devida atenção e controle.

## Action: DeleteConfigurationSetTrackingOptions
### 📊 Modelagem de Ameaças para Ação IAM: `DeleteConfigurationSetTrackingOptions`

| **AWS IAM Action**                          | **BUILD/RUN** | **Descrição**                                                                                                                                     | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                                                            | **Recomendações de Segurança**                                                                                                                    |
|---------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteConfigurationSetTrackingOptions`     | BUILD         | Exclui uma associação entre um conjunto de configuração e um domínio personalizado para rastreamento de eventos de abertura e clique.            | Defense Evasion           | T1562 - Impair Defenses              | **Alto**  | **Requer Controle**  | A exclusão de opções de rastreamento pode impedir a detecção de ações maliciosas, dificultando o monitoramento de eventos de segurança ou comportamento anômalo.                | Implementar alertas para alterações nas configurações de rastreamento, usar políticas de IAM para restringir quem pode excluir essas associações e auditar logs regularmente.             |

### 🔍 Análise Contextual
- **Impacto Potencial**: A exclusão sem controle dessas associações pode ser explorada para evadir mecanismos de monitoramento e dificultar a identificação de atividades suspeitas em serviços de comunicação (e.g., Amazon SES).
- **Contexto de Segurança**: Considerando que você opera em um ambiente que requer regulamentação rigorosa, como o setor financeiro, essa ação pode comprometer relatórios de conformidade e auditorias de segurança.

🔗 **Referências Úteis**:
- [MITRE ATT&CK - Impair Defenses](https://attack.mitre.org/techniques/T1562/)
- [Documentação AWS IAM](https://docs.aws.amazon.com/iam/) para melhores práticas em políticas de acesso.

### 🔒 Estratégia de Segurança
Implementar uma abordagem de **Zero Trust**, garantindo que somente identidades autorizadas tenham permissão para modificar configurações de segurança e que tais ações sejam sempre auditáveis e sujeitas a revisão de conformidade.

## Action: DeleteCustomVerificationEmailTemplate
### 📊 Modelagem de Ameaças para a Ação IAM `DeleteCustomVerificationEmailTemplate`

| **AWS IAM Action**                                | **BUILD/RUN** | **Descrição**                                                                          | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                                       | **Recomendações de Segurança**                                                                                                             |
|---------------------------------------------------|---------------|----------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteCustomVerificationEmailTemplate`          | BUILD         | Exclui um modelo de email de verificação personalizada existente.                       | Defense Evasion          | T1070.004 - Indicator Removal on Host | **Médio** | Melhor Prática     | Esta ação pode ser explorada para remover evidências de uso malicioso de modelos de e-mail, mas tem impacto limitado por si só.  | Aplicar políticas de IAM restritivas, monitorar logs de atividade via AWS CloudTrail, e implementar alertas para ações de exclusão de templates.             |

### 🔍 Detalhes da Análise

1. **Riscos Identificados**:
   - A ação de eliminar modelos de verificação de email pode ser utilizada para ocultar ou apagar evidências de tentativas de fraude ou phishing detectáveis em um ambiente AWS.
   - Pelo seu impacto ser mais voltado à ocultação de ações ao invés de alterar o estado do sistema ou dados críticos, o risco é considerado médio.

2. **Diretrizes de Mitigação**:
   - **IAM Policies**: Implemente políticas de menor privilégio para restringir quem pode executar a exclusão de modelos.
   - **AWS CloudTrail**: Habilite e configure o AWS CloudTrail para capturar eventos relacionados à modificação ou exclusão de templates de e-mail.
   - **Alertas e Monitoramento**: Configure alertas quando ações de exclusão forem detectadas, integrando ao AWS Security Hub.

### 🛡️ Estratégia de Segurança

O foco para mitigar riscos associados a esta ação deve ser o monitoramento contínuo e o uso de controles de segurança baseada em listas de controle de acesso (ACLs) apropriadas, garantindo que apenas usuários devidamente autorizados executem tais exclusões e que qualquer exclusão seja devidamente auditada.

## Action: DeleteIdentity
Aqui está a modelagem de ameaças para a ação IAM fornecida:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `DeleteIdentity` | BUILD | Exclui a identidade especificada. | Defense Evasion | T1531 - Account Access Removal | **Crítico** | **Requer Controle** | A ação pode ser utilizada para excluir identidades de usuários ou serviços, impedindo acesso legítimo e dificultando a investigação de atividades maliciosas. | Implementar monitoramento para exclusão de identidades, limitar permissões de ações de exclusão, e usar IAM Policies para controlar quem pode executar essa ação. |

### Considerações Adicionais
- **Risco Elevado:** A exclusão de identidades pode gerar grande impacto em questões de continuidade operacional e traz sérios riscos de segurança, caso explorado de maneira maliciosa.
- **Mitigação Rigorosa:** Recomenda-se a configuração de **alertas através do AWS CloudTrail para monitorar tais ações**, além do uso de **AWS IAM Access Analyzer** para garantir adesão ao princípio do menor privilégio.
- **Continuidade da Segurança:** Realizar auditorias periódicas nas permissões concedidas e revisar logs de auditoria de IAM para identificação de ações suspeitas.

Realize essas ações para garantir maior segurança no gerenciamento de identidades em seu ambiente AWS.

## Action: DeleteIdentityPolicy
### 🚨 Modelagem de Ameaças para Ação IAM: `DeleteIdentityPolicy`

A tabela abaixo resume a análise da ação IAM `DeleteIdentityPolicy` utilizando o framework MITRE ATT&CK, sua classificação de risco, justificativa e recomendações de segurança.

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação** | **Recomendações de Segurança**                      |
|----------------------|---------------|---------------|---------------------------|----------------------------------------|-----------|--------------------|------------------------------------|---------------------------------------------------|
| `DeleteIdentityPolicy` | BUILD         | Exclui a política de autorização de envio especificada para a identidade dada (um endereço de email ou um domínio). | Defense Evasion | T1070.004 - Indicator Removal on Host | **Alto**   | **Requer Controle** | A exclusão de políticas de autorização pode ser usada para evitar a detecção de atividade maliciosa ou para remover restrições de segurança, prejudicando a integridade do sistema de autorização para envio de emails. | Monitorar e auditar exclusões de políticas de envio no SES, aplicar políticas de IAM para restringir esta ação a usuários estritamente necessários, habilitar registros detalhados no AWS CloudTrail. |

### 🛡️ Detalhamento das Recomendações de Segurança

1. **Monitoramento Contínuo e Auditoria**:
   - Ativar **AWS CloudTrail** para capturar e registrar chamadas de API, especialmente as que envolvem exclusão de políticas.
   - Utilizar **AWS Config Rules** para garantir que a ação de exclusão de políticas seja realizada apenas por usuários autorizados e sob condições controladas.

2. **Aplicação de Políticas de Menor Privilégio**:
   - Restringir essa ação a usuários ou funções que realmente precisam realizar a exclusão de políticas, aplicando o conceito de menor privilégio através de políticas de IAM rigorosas.

3. **Alertas e Detecção**:
   - Configurar **AWS Security Hub** para emitir alertas quando uma política de identidade for excluída, permitindo uma resposta rápida e eficaz.

4. **Revisão Periódica de Políticas**:
   - Realizar avaliações periódicas das ações autorizadas nas políticas IAM para garantir que nenhuma permissão excessiva esteja ativada.

### 📌 Contexto Adicional

Ao considerar infraestruturas que devem estar em conformidade com regulamentações do setor financeiro, como **BACEN, LGPD, e PCI-DSS**, é essencial implementar controles rigorosos para proteção de dados sensíveis e manutenção da integridade dos processos de envio de e-mails corporativos.

## Action: DeleteReceiptFilter
### Modelagem de Ameaças para Ação IAM: `DeleteReceiptFilter`

#### Análise da Ação IAM
- **Ação IAM**: `DeleteReceiptFilter`
- **BUILD/RUN**: BUILD
- **Descrição**: Exclui o filtro de endereço IP especificado.
- **Análise de Risco**: A capacidade de excluir filtros de endereço IP pode ser usada maliciosamente para desabilitar restrições de segurança previamente configuradas. Isso poderia permitir que tráfego não autorizado alcançasse o serviço, comprometendo dados ou aumentando a superfície de ataque.

#### Mapeamento para MITRE ATT&CK

| **AWS IAM Action**   | **BUILD/RUN**  | **Descrição**                                      | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação** | **Recomendações de Segurança**                                                                                                                                 |
|----------------------|----------------|----------------------------------------------------|---------------------------|--------------------------------------|-----------|-------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteReceiptFilter`| BUILD          | Exclui o filtro de endereço IP especificado.       | Defense Evasion           | T1562.001 - Impair Defenses: Disable or Modify Tools | **Alto**  | **Requer Controle** | Ação pode apagar filtros críticos, expondo o sistema a tráfego malicioso ou impedindo mecanismos de defesa. | Monitorar e logar todas as exclusões de filtros com AWS CloudTrail. Aplicar políticas restritivas de IAM, permitindo a alteração apenas para usuários necessários, e revisar regularmente os logs. |

#### Contexto e Recomendações de Segurança
- **Princípio do Menor Privilégio**: Assegurar que apenas usuários absolutamente necessários tenham permissões para excluir filtros.
- **Monitoramento Contínuo**: Utilizar ferramentas como AWS CloudTrail para auditoria completa dessas ações.
- **Alertas de Modificação**: Configurar notificações para alterações em filtros de endereço IP.
- **Zero Trust**: Implementar controles rígidos de fluxo de tráfego baseado em IP.

#### Conclusão
A ação `DeleteReceiptFilter` representa um risco considerável, pois permite a desativação de barreiras de segurança vitais. A vigilância contínua e o controle rigoroso de permissões são essenciais para evitar exploração maliciosa.

## Action: DeleteReceiptRule
### 🛡️ Modelagem de Ameaças para Ação IAM: DeleteReceiptRule

Com base na análise da ação IAM recebida, segue a tabela de modelagem de ameaças:

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**                                           | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                       | **Recomendações de Segurança**                                                                                       |
|------------------------|---------------|---------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `DeleteReceiptRule`    | BUILD         | Exclui a regra de recebimento especificada.             | Defense Evasion           | T1562.004 - Impair Defenses: Disable or Modify Email Forwarding Rules | **Alto**   | **Requer Controle**   | Excluir regras de recebimento pode ser usado para interromper processos normais de e-mail, ocultando atividades maliciosas. | Monitorar e registrar todos os eventos de exclusão no Amazon SES usando AWS CloudTrail. Implementar políticas de IAM restritivas. |

### **🌐 Considerações Adicionais**
1. **Análise do Impacto**:
   - **Confidencialidade**: Acesso não autorizado pode excluir regras críticas, afetando a entrega segura de emails.
   - **Integridade e Disponibilidade**: A exclusão de regras pode interromper o fluxo normal de e-mails, afetando sistemas dependentes.

2. **Regulamentações**:
   - **LGPD e PCI-DSS**: Garantias que dados pessoais protegidos por essas regras não estejam comprometidos devido à modificação ou exclusão de regras de recebimento.

3. **Mitigação Detalhada**:
   - Implementar **log de auditoria** para ações DELETE no SES.
   - **Revisões regulares** de políticas de IAM para estabelecer o princípio do menor privilégio.
   - Usar **AWS Security Hub** para integrar avisos de segurança e conformidade.

Cada etapa de mitigação deve ser feita considerando o conceito de segurança **Zero Trust**, assegurando que apenas indivíduos e dispositivos autorizados possam realizar alterações críticas.

## Action: DeleteReceiptRuleSet
### Modelagem de Ameaças para Ação IAM

Abaixo está a análise detalhada e a modelagem de ameaças para a ação IAM **DeleteReceiptRuleSet** no contexto de AWS SES, utilizando o framework MITRE ATT&CK:

| **AWS IAM Action**       | **BUILD/RUN** | **Descrição**                                                                             | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                   | **Recomendações de Segurança**                                                                                                           |
|--------------------------|---------------|------------------------------------------------------------------------------------------|-------------------------|--------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteReceiptRuleSet` | BUILD         | Exclui o conjunto de regras de recebimento especificado e todas as regras de recebimento que ele contém. | Impact | T1485 - Data Destruction | **Crítico** | **Requer Controle** | Esta ação permite a exclusão de regras de recebimento, o que pode resultar na perda de configurações críticas e na interrupção de serviços de e-mail. | Implementar controle de acesso rigoroso com IAM Policies e SCPs, monitorar auditorias com AWS CloudTrail, e ativar AWS Config para verificar configurações. |

### **Análise Detalhada**
#### **1. Mapeamento para MITRE ATT&CK**
- **Tática**: Impact
- **Técnica**: T1485 - Data Destruction

#### **2. Justificativa da Classificação**
- A exclusão de conjuntos de regras de recebimento pode afetar drasticamente a funcionalidade do serviço de e-mail, resultando em perda de dados ou interrupção de serviços essenciais. Por isso, a ação é considerada crítica e requer controles e monitoramento rigorosos para prevenir abuso.

#### **3. Recomendações de Segurança**
- **Controle de Acesso**: Utilizar IAM Policies e Service Control Policies (SCPs) para restringir quem pode excluir regras de recebimento.
- **Monitoramento e Auditoria**: Ativar e analisar logs de auditoria com AWS CloudTrail para detectar alterações suspeitas nos conjuntos de regras.
- **Configurações de Segurança**: Empregar AWS Config para garantir que todas as configurações estejam alinhadas com as políticas de segurança estabelecidas.
- **Redundância e Backup**: Implementar backups regulares das configurações de regras de recebimento para permitir a recuperação rápida em caso de exclusão acidental ou maliciosa.

Estas medidas devem ser integradas em uma estratégia mais ampla de segurança para garantir que somente usuários autorizados possam executar ações destrutivas e que qualquer atividade suspeita seja rapidamente identificada e tratada.

## Action: DeleteTemplate
Com base na ação IAM fornecida para o serviço AWS, aqui está a tabela de modelagem de ameaças associada, considerando o framework MITRE ATT&CK:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `DeleteTemplate` | BUILD | Exclui um modelo de email. | Impact | T1485 - Data Destruction | **Alto** | **Requer Controle** | A exclusão de modelos de email pode causar perda de dados importantes, prejudicando operações de comunicação e comprometendo o histórico de transações ou correspondências. | Implementar permissões restritas para exclusão de modelos, usar backups regulares para recuperar dados excluídos, monitorar logs de exclusão com o AWS CloudTrail. |

### Justificativas e Recomendações

- **Tática: Impact (Destruição de Dados)**: A ação de `DeleteTemplate` se alinha com a tática de destruição de dados, onde um ator mal-intencionado pode deletar informações críticas para causar interrupções.
- **Risco Alto**: Devido ao potencial de perda de informações e impacto nas operações de comunicação, essa ação é considerada de alto risco.
- **Mitigação**: 
  - **Gerenciando Permissões**: Restringir quem pode realizar esta ação através de políticas IAM rigorosas.
  - **Backups**: Garantir que todos os modelos críticos sejam respaldados regularmente para recuperação em caso de exclusão acidental ou maliciosa.
  - **Monitoramento e Auditoria**: Usar AWS CloudTrail para registrar ações de exclusão e configurar alertas para atividades não autorizadas ou suspeitas.

Esta tabela proporciona uma visão clara sobre como a ação pode ser explorada, seu risco associado e como proteger os dados e operações relativas a modelos de email na AWS.

## Action: DeleteVerifiedEmailAddress
Para a ação IAM fornecida, "DeleteVerifiedEmailAddress", a análise de modelagem de ameaças é estruturada da seguinte forma:

| **AWS IAM Action**            | **BUILD/RUN** | **Descrição**                                                                      | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                  | **Recomendações de Segurança**                                                                                                                                     |
|-------------------------------|--------------|-----------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteVerifiedEmailAddress`  | BUILD        | Exclui o endereço de email especificado da lista de endereços verificados.         | Defense Evasion           | T1070 - Indicator Removal on Host    | **Médio** | **Melhor Prática** | Ação pode ser usada para remover evidências de comunicações autorizadas, impactando logs de auditoria e rastreamento. | Monitorar e auditar exclusões de endereços verificados; aplicar políticas de menor privilégio com base em IAM; realizar revisões periódicas de atividades de auditoria. |

### **Detalhes da Análise**

- **Tática:** `Defense Evasion` - A exclusão de endereços de e-mail verificados pode ser utilizada por um ator malicioso para remover evidências de configuração e uso legítimo, evitando a detecção de ações indevidas.
  
- **Técnica:** `Indicator Removal on Host (T1070)` - Simplificação dos rastros deixados por atividades através da remoção de endereços de e-mail verificados, o que pode afetar a capacidade de auditoria e rastreamento no ambiente.

- **Risco:** **Médio** - Ainda que possa impactar a visibilidade em auditorias e verificações, o impacto direto na segurança operacional é moderado.
  
- **Justificativa da Classificação:** Embora a ação não cause um impacto direto crítico no sistema ou nos dados, sua capacidade de remover evidências de endereços de e-mail verificados pode interromper processos de auditoria e forense.

- **Recomendações de Segurança:** Implementar práticas de auditoria e revisão para monitorar a exclusão desses endereços, restringir a permissão de exclusão para apenas usuários/roles essenciais, e assegurar que toda ação seja devidamente registrada e passível de auditoria.

## Action: DescribeActiveReceiptRuleSet
### **Tabela de Modelagem de Ameaças para Ação IAM**

| **AWS IAM Action**                   | **BUILD/RUN** | **Descrição**                                                                                           | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                                          | **Recomendações de Segurança**                                                                                                                                                    |
|--------------------------------------|---------------|----------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DescribeActiveReceiptRuleSet`       | RUN           | Retorna os metadados e regras de recebimento para o conjunto de regras de recebimento que está atualmente ativo. | Discovery                | T1590 - Gather Victim Network Information | **Médio** | **Melhor Prática**    | Esta ação permite que um invasor obtenha informações sobre regras de e-mail ativas, que podem ser usadas posteriormente para ajuste de ataques ou reconhecimento.                            | Revisar permissões de IAM para garantir que apenas usuários autorizados possam acessar esta ação. Ativar o AWS CloudTrail para auditar e monitorar o uso desta ação.                                                   |

---

### **Análise e Justificativa**
- **Tática e Técnica Mapeada**: A ação está associada à tática de reconhecimento, pois permite coletar informações específicas sobre as regras de recebimento de e-mail, o que pode ajudar um invasor a entender melhor o ambiente e planejar ataques mais direcionados.
- **Classificação de Risco**: Embora não modifique recursos ou impacte diretamente a segurança imediata, o acesso a informações sensíveis sobre a configuração da rede e comunicação pode ser explorado para ataques de phishing ou ajustamentos de engenharia social.
- **Recomendações de Segurança**: Implementar o princípio do menor privilégio, assegurando que apenas usuários com necessidade específica possam realizar consultas a regra. O monitoramento através de CloudTrail ajudará a rastrear atividades suspeitas e possibilitar respostas rápidas a possíveis indicações de comprometimento.

## Action: DescribeConfigurationSet
Com base nos dados fornecidos, vamos realizar a modelagem de ameaças para a ação IAM `DescribeConfigurationSet`:

---

### **Tabela de Modelagem de Ameaças**

| **AWS IAM Action**          | **BUILD/RUN** | **Descrição**                                                               | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                                                           | **Recomendações de Segurança**                                                                                                                                             |
|-----------------------------|---------------|-----------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DescribeConfigurationSet`  | RUN           | Retorna os detalhes do conjunto de configuração especificado.               | Reconhecimento            | T1592 - Gather Victim Host Information | **Baixo** | **Melhor Prática** | A ação apenas retorna metadados sobre a configuração, minimizando impacto direto. Possui baixo impacto na confidencialidade e integridade. | Restringir o uso dessa ação a entidades que realmente necessitam, aplicando o princípio do menor privilégio. Monitorar logs de acesso utilizando AWS CloudTrail e AWS Config. |

---

### **Considerações Gerais**
- A ação `DescribeConfigurationSet` é mais informativa e não modifica configuracões existentes, o que correlaciona com táticas de reconhecimento direcionadas à coleta de informações.
- O uso apropriado de políticas IAM restritivas pode mitigar riscos associados a consultas de metadados.
- A detecção de uso impróprio pode ser aprimorada através de monitoramento contínuo e alertas de segurança.

### **Referências**
- Consulte as [melhores práticas de IAM da AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) para garantir que os princípios de segurança sejam respeitados.
- Explore a documentação do [MITRE ATT&CK Framework](https://attack.mitre.org/) para um entendimento aprofundado das táticas e técnicas.

---

Essa análise visa proporcionar uma visão clara sobre os riscos associados e recomendações práticas para garantir um ambiente AWS mais seguro.

## Action: DescribeReceiptRule
| **AWS IAM Action**         | **BUILD/RUN** | **Descrição**                                    | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                               | **Recomendações de Segurança**                                                                                                |
|----------------------------|---------------|--------------------------------------------------|---------------------------|----------------------------------------|-----------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `DescribeReceiptRule`      | RUN           | Retorna os detalhes da regra de recebimento especificada. | Discovery                 | T1087 - Account Discovery             | **Médio** | **Melhor Prática** | A ação pode ser usada para coletar informações sobre regras que controlam o fluxo de e-mails, permitindo aos invasores obter informações valiosas para planejar ataques posteriores. | Monitorar atividades relacionadas ao SES, implementar políticas IAM restritivas limitando acesso a usuários ou grupos específicos. |

### Considerações Adicionais

- **Contexto de Monitoramento Contínuo**: Utilize o AWS CloudTrail para registrar e monitorar atividades associadas ao SES, com alertas configurados para detecções anômalas.
- **Princípio do Menor Privilégio**: Garanta que somente usuários com necessidade legítima tenham permissões para visualizar regras do SES, reforçando a segurança.
- **Revisão Regular de Logs**: Implemente revisões periódicas dos logs de auditoria para identificar acessos não autorizados ou comportamentos suspeitos.
- **Cross-Referência com Regulamentações**: Certifique-se de que o uso dessas ações esteja alinhado com as políticas de conformidade estabelecidas pelo seu setor.

Esta tabela fornece uma visão para garantir que possíveis ameaças sejam identificadas e mitigadas adequadamente em sua infraestrutura AWS, mantendo a segurança e a proteção de dados sensíveis.

## Action: DescribeReceiptRuleSet
Com base nos dados fornecidos, segue a modelagem de ameaças para a ação IAM `DescribeReceiptRuleSet`:

| **AWS IAM Action**               | **BUILD/RUN** | **Descrição**                                                  | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                                      | **Recomendações de Segurança**                                                                                       |
|----------------------------------|--------------|---------------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `DescribeReceiptRuleSet`         | RUN          | Retorna os detalhes do conjunto de regras de recebimento especificado no Amazon SES. | Collection                | T1580 - Cloud Infrastructure Discovery | **Médio** | **Melhor Prática** | Essa ação permite a um adversário obter informações sobre a configuração de recebimento de mensagens, útil para reconhecimento. | Restringir o uso dessa ação a apenas usuários ou funções que realmente necessitem. Monitorar e registrar chamadas dessa ação no CloudTrail. |

### **Notas:**
- **Tática - Collection**: Os invasores podem buscar informações que ajudem em ataques posteriores, explorando `DescribeReceiptRuleSet` para mapear a configuração de regras no serviço SES. 
- **Risco Médio**: Embora essa ação não modifique estados ou recursos, ela pode fornecer informações a serem usadas em atividades maliciosas.
- **Recomendações**:
  - **Princípio do Menor Privilégio**: Garantir que apenas usuários/serviços com necessidade específica tenham permissão para executar esta ação.
  - **Monitoramento com AWS CloudTrail**: Configurar alertas para detectar uso incomum ou não autorizado dessa ação.
  - **Revisão Regular de Políticas IAM**: Assegurar que políticas IAM estejam devidamente atualizadas e resguardem acesso legítimo.

## Action: GetAccountSendingEnabled
| **AWS IAM Action**             | **BUILD/RUN** | **Descrição**                                                         | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                 |
|--------------------------------|---------------|-----------------------------------------------------------------------|-------------------------|--------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `GetAccountSendingEnabled`     | RUN           | Retorna o status de envio de email da sua conta.                      | Discovery               | T1082 - System Information Discovery | **Médio** | **Melhor Prática** | Essa ação pode ser usada para coletar informações sobre a capacidade de envio de e-mails, o que pode informar configurações para ataques de phishing ou spam, mas não compromete diretamente o sistema. | Limitar essa ação apenas a usuários e roles que necessitam dessa informação, monitorar logs de uso e revisar permissões regularmente. |

### **Notas e Justificativas Adicionais**

- **Impacto na Confidencialidade, Integridade e Disponibilidade**: Embora não comprometa diretamente a confidencialidade ou integridade dos dados, pode informar um invasor sobre a capacidade de envio de emails, ajudando em tentativas de evasão ou engenharia social.
  
- **Probabilidade de Exploração**: O uso malicioso requer acesso prévio ao ambiente AWS e interesse específico nas capacidades da conta, tornando a exploração menos comum.
  
- **Recomendações de Mitigação**: Implementar práticas de monitoramento contínuo para detectar atividades suspeitas e aplicar o princípio do menor privilégio para restringir essa ação a usuários realmente necessários.

### **Regulamentações e Contexto**
- **ISO 27001 e PCI-DSS**: Assegurar que a auditoria de logs da AWS detalhando o uso dessa ação é atendida.
- **Zero Trust**: Garantir que somente as partes explicitamente autorizadas possam acessar essas informações.

As medidas acima ajudarão a mitigar potenciais ameaças, alinhando a segurança às melhores práticas e regulamentos do setor.

## Action: GetCustomVerificationEmailTemplate
| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                                                                            | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                                  | **Recomendações de Segurança**                                                                                                                                                                                                                                         |
|--------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetCustomVerificationEmailTemplate` | RUN           | Retorna o modelo de email de verificação personalizado para o nome do modelo especificado.               | Collection                 | T1114.002 - Email Collection         | **Médio** | **Melhor Prática**      | Essa ação pode ser utilizada para coletar modelos de email utilizados em verificações, podendo expor formatação e conteúdo sensíveis se mal utilizados.                        | Implementar políticas de menor privilégio para acesso a modelos de email de verificação e monitorar o uso dessa ação com AWS CloudTrail. Evitar compartilhar credenciais e usar MFA para proteger contas com permissão para acessar modelos de e-mail de verificação. |

## Action: GetIdentityDkimAttributes
| **AWS IAM Action**           | **BUILD/RUN** | **Descrição**                                                                  | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                | **Recomendações de Segurança**                                                                                                                                                       |
|------------------------------|---------------|-------------------------------------------------------------------------------|------------------------|--------------------------------------|-----------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetIdentityDkimAttributes`  | RUN           | Retorna o status atual da assinatura DKIM fácil para uma entidade.            | Discovery              | T1087 - Account Discovery            | **Médio** | **Melhor Prática** | A ação permite verificação de configurações DKIM, possível vetor para obter informações sobre configurações.                                                           | Implementar princípio de menor privilégio, registrar todas as chamadas desta ação usando AWS CloudTrail, revisar permissões regularmente para este tipo de consulta.                                                       |



## Action: GetIdentityMailFromDomainAttributes
### 📊 Modelagem de Ameaças AWS - Análise da Ação IAM

| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                                                                     | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                                                                         | **Recomendações de Segurança**                                                                                                                                                           |
|--------------------------------------------|---------------|---------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetIdentityMailFromDomainAttributes`      | RUN           | Retorna os atributos de correio personalizados para uma lista de identidades (endereços de email e/ou domínios). | Discovery                 | T1083 - File and Directory Discovery | **Médio**  | Melhor Prática | Esta ação pode ser explorada para descobrir informações sobre a configuração dos domínios de e-mail, mas não modifica ou compromete os dados diretamente. | Monitorar chamadas a essa ação para detectar padrões de uso indevido, restringir acesso por meio de políticas IAM, e analisar logs do AWS CloudTrail para verificar acessos não autorizados. |

### ✅ Considerações Adicionais

1. **Justificativa do Risco**:
   - A ação é classificada como **RUN** e seu potencial de exploração está relacionado ao uso indevido de informações descobertas, o que pode ajudar adversários em etapas subsequentes de outras táticas.
   
2. **Recomendações de Segurança**:
   - **Implementar o Princípio do Menor Privilégio**: Limitar acesso a esta ação apenas a usuários ou roles que realmente necessitam dessa informação para funções operacionais.
   - **Utilizar AWS CloudTrail** para monitorar e registrar acessos a esta ação, possibilitando auditorias e investigações detalhadas.
   - **Configurar alertas no AWS Security Hub** e/ou **AWS GuardDuty** para detecção de atividades anômalas relacionadas ao uso desta ação.

3. **Regulamentações e Conformidade**:
   - Garantir que o uso desta ação esteja em conformidade com diretrizes de proteção de dados, como LGPD e regulamentos internos de segurança.

Por favor, entre em contato se precisar de mais alguma análise ou detalhes adicionais.

## Action: GetIdentityNotificationAttributes
### 📊 Tabela de Modelagem de Ameaças para Ação IAM

| **AWS IAM Action**                  | **BUILD/RUN** | **Descrição**                                                                                                                  | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                                           | **Recomendações de Segurança**                                                                                     |
|-------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `GetIdentityNotificationAttributes` | RUN           | Retorna uma estrutura descrevendo atributos de notificação de identidade para uma lista de identidades verificadas (endereços de email e/ou domínios). | Discovery                | T1580 - Cloud Infrastructure Discovery | **Médio** | **Melhor Prática**   | Esta ação permite descobrir informações sobre notificações configuradas para identidades, mas não modifica ou compromete diretamente recursos. | Limitar o uso desta ação a usuários ou roles que realmente necessitem desta capacidade; monitorar logs de acesso com o AWS CloudTrail para detecção de uso indevido. |

### 📝 Análise Detalhada

1. **Análise da Ação IAM**:
   - A ação `GetIdentityNotificationAttributes` é classificada como **RUN**, pois retorna informações sobre configurações existentes, sem modificar ou criar novos recursos.
   - A ação pode ser explorada para **descoberta de configurações** em um ambiente AWS, particularmente visando a coleta de informações sobre notificações para emails e domínios.

2. **Mapeamento para MITRE ATT&CK**:
   - **Tática**: Discovery
   - **Técnica/Subtécnica**: T1580 - Cloud Infrastructure Discovery
   - Essa técnica inclui o levantamento de informações para identificar recursos de infraestrutura na nuvem e suas respectivas configurações.

3. **Classificação de Risco**:
   - Avaliado como **Médio**, pois enquanto permite descobrir configurações, a ação não afeta diretamente a confidencialidade, integridade ou disponibilidade dos recursos.

4. **Recomendações de Segurança**:
   - Aplicar o **princípio do menor privilégio**, restringindo quem pode realizar esta ação.
   - **Monitorar logs** com o AWS CloudTrail para identificar acessos suspeitos ou não autorizados à função.
   - Verificar configurações regularmente para garantir que somente identidades autorizadas têm permissão de realizar esta ação.

### 🌟 Contexto Adicional
Considerando **regulamentações do setor financeiro** e a necessidade de **controles rigorosos de IAM**, a limitação e o monitoramento são críticos para manter a segurança e conformidade.

### 🔗 Referências e Cross-Mapping
Considere consultar a [Documentação AWS IAM](https://docs.aws.amazon.com/iam/) e o [MITRE ATT&CK](https://attack.mitre.org/) para mais detalhes sobre correlacionamento e melhores práticas associadas ao uso desta ação.

## Action: GetIdentityPolicies
| **AWS IAM Action**           | **BUILD/RUN** | **Descrição**                                                                                  | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                       | **Recomendações de Segurança**                                                                                                                                                     |
|------------------------------|---------------|----------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetIdentityPolicies`        | RUN           | Retorna as políticas de autorização de envio solicitadas para a identidade especificada (um endereço de email ou um domínio). | Discovery                 | T1580 - Cloud Service Dashboard     | **Médio** | **Melhor Prática** | Essa ação permite que um adversário veja as políticas de envio associadas a uma identidade, podendo identificar políticas indevidamente configuradas. | Limitar o uso da ação a usuários que realmente precisem acessar essas informações, monitorar acessos e revisões periódicas das políticas IAM associadas a identidades no IAM. |

## Action: GetIdentityVerificationAttributes
### Modelagem de Ameaças para Ação IAM: `GetIdentityVerificationAttributes`

| **AWS IAM Action**               | **BUILD/RUN** | **Descrição**                                                                                                                                      | **Tática (MITRE ATT&CK)**  | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                                                                                                                                            | **Recomendações de Segurança**                                                                                                                                                                |
|----------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------------|-----------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetIdentityVerificationAttributes` | RUN           | Retorna o status de verificação e (para identidades de domínio) o token de verificação para uma lista de identidades.                                | Discovery                  | T1083 - File and Directory Discovery | **Médio**  | **Melhor Prática**     | Essa ação permite que um usuário obtenha detalhes sobre o status de verificação de identidades, o que poderia ser explorado para reconhecer o ambiente e planejar fases subsequentes de um ataque.                                           | Implementar políticas de IAM baseadas no princípio do menor privilégio, garantindo que apenas usuários ou serviços autorizados possam realizar esta ação. Monitorar logs de acesso ao AWS CloudTrail para atividades incomuns.                                          |

### Observações
- **Contexto e Justificativa**: A ação `GetIdentityVerificationAttributes` geralmente não compromete diretamente recursos, mas pode fornecer informações úteis a um invasor sobre a verificação de identidades, potencialmente facilitando ataques futuros.
- **Recomendações**: Além das práticas recomendadas acima, considere a implementação de **monitoramento contínuo** através de serviços como AWS CloudTrail e AWS Security Hub para identificar e responder rapidamente a acessos não autorizados ou suspeitos.

## Action: GetSendQuota
| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `GetSendQuota` | RUN | Retorna os limites de envio atuais do usuário. | Discovery | T1592 - Gather Victim Network Information | **Médio** | **Melhor Prática** | Esta ação pode ser utilizada para coletar informações sobre os limites de envio de e-mail, potencialmente indicando capacidades e permitindo preparação para exfiltração de dados. | Restringir o uso desta ação a usuários e serviços que genuinamente necessitem dela, aplicar o princípio de menor privilégio. Monitorar o uso frequente ou anômalo deste tipo de consulta. |

### **Justificativas e Recomendações Detalhadas:**

- **Tática e Técnica:** 
  - **Discovery Tactics (T1592)**: A ação `GetSendQuota` permite que um potencial invasor descubra dados sobre o ambiente e avalie a capacidade de envio de e-mails, que pode posteriormente ser explorada para atividades maliciosas.

- **Classificação de Risco:**
  - **Médio - Melhor Prática:** A ação por si só não compromete a segurança, mas proporciona informações que podem ser usadas em fases posteriores de um ataque. A facilidade de explorar essa informação é discutível, mas restringir o acesso é cauteloso.

- **Recomendações de Segurança:**
  - **Restringir o acesso:** Certifique-se de que somente usuários e aplicações que necessitam estrategicamente destas informações tenham permissão para executar esta ação.
  - **Princípio do Menor Privilégio:** Avalie e ajuste as permissões dos usuários e funções para garantir que tenham apenas o necessário.
  - **Monitoramento Ativo:** Utilize ferramentas como AWS CloudTrail para registrar e monitorar o uso da ação `GetSendQuota`, verificando anomalias ou padrão de uso incomum.

Estas medidas de mitigação visam reduzir o impacto e a chance de exploração maliciosa da capacidade de obtenção de dados de envio no AWS SES.

## Action: GetSendStatistics
Com base na análise da ação IAM fornecida, aqui está a modelagem de ameaças para a ação `GetSendStatistics`.

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**                                       | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                 | **Recomendações de Segurança**                                                     |
|------------------------|---------------|-----------------------------------------------------|---------------------------|----------------------------------------|-----------|----------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `GetSendStatistics`    | RUN           | Retorna as estatísticas de envio do usuário.        | Discovery                 | T1083 - File and Directory Discovery   | **Médio**  | **Melhor Prática**   | Ação permite obter estatísticas de envio que podem auxiliar no reconhecimento de padrões de tráfego, mas com impacto limitado. | Restringir o uso a processos automatizados, usar IAM Roles com princípio de menor privilégio. |

**Considerações Adicionais:**

- **Risco e Classificação:** A ação `GetSendStatistics` oferece informações sobre o uso do serviço que podem ser usadas em técnicas de reconhecimento. No entanto, o impacto direto é limitado, dado que a ação não modifica ou remove dados, apenas os consulta.
  
- **Tática e Técnica (MITRE ATT&CK):** A ação foi mapeada para a tática de **Discovery** e a técnica de **File and Directory Discovery (T1083)**, pois permite o levantamento de informações sobre o ambiente operacional, o que pode auxiliar adversários na compreensão e planejamento de ataques mais sofisticados.

- **Recomendações de Segurança:** Aplicar o mínimo de privilégios para essa ação e garantir que apenas usuários ou processos com necessidade explícita tenham acesso. Além disso, é importante monitorar ativamente o uso dessa ação para detectar padrões anômalos que possam indicar atividades suspeitas.

Essas informações devem ajudar a garantir que o uso da ação `GetSendStatistics` seja adequadamente controlado e monitorado, alinhando-se aos requisitos de segurança do ambiente AWS.

## Action: GetTemplate
### 📊 Modelagem de Ameaças para a Ação IAM: `GetTemplate`

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|---------------|---------------------------|---------------------------------------|-----------|-------------------|------------------------------------|---------------------------------|
| `GetTemplate` | RUN | Retorna o objeto modelo, que inclui o assunto, a parte HTML e a parte de texto para o modelo especificado. | Collection | T1114 - Email Collection | **Médio** | **Melhor Prática** | Embora essa ação forneça acesso ao conteúdo dos modelos de e-mail, o risco está mais associado à exposição acidental de informações sensíveis. | Implementar políticas de acesso restritivo, usar logs do AWS CloudTrail para monitorar acesso, e revisar regularmente permissões IAM. |

### 🛡️ Diretrizes Adicionais
- **Zero Trust**: Assegurar que somente usuários ou serviços estritamente necessários tenham acesso a esta ação.
- **Monitoramento Contínuo**: Ativação de AWS CloudTrail para auditar acessos e detecções de padrões suspeitos.
- **Criticidade para Regulamentações**: Em conformidade com LGPD, garanta que dados acessados via modelos sejam tratados conforme diretrizes de proteção de dados.

## Action: ListConfigurationSets
Para a ação IAM "ListConfigurationSets", a modelagem de ameaças deve levar em consideração os aspectos e riscos associados ao ambiente AWS. Abaixo, segue a tabela de análise conforme solicitado:

| **AWS IAM Action**        | **BUILD/RUN** | **Descrição**                                                  | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                         |
|---------------------------|--------------|--------------------------------------------------------------|---------------------------|---------------------------------------|-----------|--------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `ListConfigurationSets`   | RUN          | Lista todos os conjuntos de configuração da sua conta.       | Discovery                 | T1518 - Software Discovery            | **Médio**  | **Melhor Prática** | Embora liste informações de configuração, a ação está mais relacionada a descoberta, sem modificação direta nos recursos. | Monitoramento contínuo com AWS CloudTrail, implementar o princípio de menor privilégio para IAM Policies que utilizam essa ação. |

### Justificativa e Análise Detalhada
1. **Tática e Técnica Mapeada do MITRE ATT&CK**:
   - **Discovery (T1518 - Software Discovery)**: A ação "ListConfigurationSets" pode ser utilizada para descobrir configurações existentes dentro da conta, oferecendo visibilidade sobre como os serviços estão configurados.

2. **Classificação de Risco**:
   - **Médio (Melhor Prática)**: A ação em si não altera configurações ou dados, mas a visibilidade obtida pode ser explorada para identificar potenciais alvos ou vulnerabilidades. Portanto, é importante monitorar seu uso e garantir que apenas usuários autorizados tenham permissão para executá-la.

3. **Recomendações de Segurança**:
   - **Políticas de Menor Privilégio**: Assegurar que apenas usuários ou funções que realmente precisam listar os conjuntos de configuração tenham essa permissão.
   - **Monitoramento Contínuo com AWS CloudTrail**: Rastrear acessos e usos dessa ação para identificar padrões incomuns ou acessos não autorizados.
   - **Avaliação Regular de IAM Roles e Policies**: Certificar-se de que as permissões estão alinhadas com as responsabilidades dos usuários e são revisadas regularmente para evitar excessos.

A modelagem acima considera práticas de segurança recomendadas e a integração com o MITRE ATT&CK para fornecer um entendimento holístico do risco associado a essa ação IAM específica.

## Action: ListCustomVerificationEmailTemplates
| **AWS IAM Action**                          | **BUILD/RUN** | **Descrição**                                                                                   | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                 | **Recomendações de Segurança**                                                                                                               |
|---------------------------------------------|---------------|-----------------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `ListCustomVerificationEmailTemplates`      | RUN           | Lista todos os modelos de email de verificação personalizados existentes da sua conta.        | Collection                | T1114.002 - Email Collection         | **Médio** | **Melhor Prática**   | Listar templates de e-mail pode expor detalhes que ajudem a configurar ataques de coleta de e-mails ou phishing, mas não modifica ou exclui dados críticos. | Restringir permissões para listar modelos de e-mail a usuários que realmente precisam, monitorar listagens de templates com AWS CloudTrail. |

### 🛡️ Recomendações Adicionais
- **Uso de IAM Policies** para aplicar o **princípio do menor privilégio** em ações de Listagem.
- **Monitorar constantemente** com o **AWS CloudTrail** para detectar usos suspeitos ou não autorizados desta ação.
- **Revisar regularmente** as permissões de IAM para garantir que as contas de usuário only têm permissões necessárias.

## Action: ListIdentities
### **Modelagem de Ameaças para a Ação IAM: ListIdentities**

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                                              | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                | **Recomendações de Segurança**                                                                                           |
|----------------------|---------------|------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `ListIdentities`     | RUN           | Lista as identidades de email da sua conta.                | Discovery                 | T1087 - Account Discovery           | **Médio** | **Melhor Prática** | A ação pode ser usada para descobrir endereços de email associados a uma conta AWS, potencialmente visando phishing.    | Limitar o uso da ação a usuários e funções que realmente precisam dela. Monitorar acessos inusitados ou fora do padrão. |


### **Análise e Justificação**

- **Tática (MITRE ATT&CK): Discovery**: A ação é classificada sob a tática de descoberta porque pode ser usada para coletar informações sobre o ambiente alvo, como contas e identidades.

- **Técnica (MITRE ATT&CK): T1087 - Account Discovery**: Esta técnica refere-se à exploração de informações de descoberta de contas, utilizadas frequentemente por adversários para identificar alvos relevantes.

- **Classificação de Risco**: 
  - **Médio - Melhor Prática**: Embora o impacto direto possa ser limitado, a ação pode facilitar ataques subsequentes, como campanhas de phishing ou spear-phishing, aproveitando informações sobre contas.
  - **Justificativa**: Não apresenta um impacto direto severo, mas aumenta a superfície de ataque ao expor dados de configuração da conta.

### **Recomendações de Segurança**

- **Práticas de Gestão de Acesso**: Certifique-se de aplicar o princípio do menor privilégio, garantindo que apenas usuários e aplicações autorizadas possam executar esta ação.
- **Monitoramento e Alerta**: Utilizar ferramentas como AWS CloudTrail e AWS GuardDuty para monitoramento e detecção de padrões de uso anormais ou suspeitos.
- **Revisão de Políticas IAM**: Reavalie as permissões e políticas de IAM regularmente para assegurar que as permissões estão adequadamente restritas.

## Action: ListIdentityPolicies
Com base na entrada fornecida, aqui está a modelagem de ameaças para a ação IAM `ListIdentityPolicies`:

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                                                              | **Tática (MITRE ATT&CK)**    | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                      | **Recomendações de Segurança**                                                                                                                                                  |
|----------------------|---------------|---------------------------------------------------------------------------|------------------------------|---------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ListIdentityPolicies` | RUN           | Lista todas as políticas de envio de email para a sua conta.                | Discovery                    | T1087.002 - Cloud Account | **Médio**  | **Melhor Prática** | Essa ação pode ser usada para obter informações sobre as políticas de email existentes, o que pode auxiliar em obter insights sobre a configuração de segurança do ambiente. | Restringir quem pode listar políticas usando políticas IAM, monitoramento de auditoria com AWS CloudTrail, implementar políticas de menor privilégio e revisão regular de permissões. |

### **Análise e Justificativa**
- **Risco de Descoberta**: Embora listar políticas em si não modifique o estado do sistema, fornece informações valiosas sobre as políticas configuradas, que podem ser usadas como parte de uma fase de reconhecimento mais ampla.
- **Impacto Potencial**: Conhecer as políticas pode ajudar um agente malicioso a planejar ataques futuros, mas a ação não compromete diretamente a integridade dos recursos.
- **Mitigação Recomendada**: Assegurar que apenas indivíduos com necessidade legítima tenham permissões para listar políticas, além de realizar uma auditoria contínua para detectar acessos não autorizados.

A correlação foi feita com o MITRE ATT&CK T1087.002, que aborda o reconhecimento em contas na nuvem, reforçando a necessidade de implementar restrições e monitoramento para essa ação IAM.

## Action: ListReceiptFilters
### Modelagem de Ameaças AWS para a Ação IAM "ListReceiptFilters"

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                                               | **Recomendações de Segurança**                                                                                                                           |
|------------------------|--------------|------------------------------------------------------------------------------|-------------------------|--------------------------------------|-----------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ListReceiptFilters`   | RUN          | Lista os filtros de endereço IP associados à sua conta.                                                                        | Discovery              | T1082 - System Information Discovery | **Médio**    | **Melhor Prática**   | Apesar de listar apenas filtros, essa ação pode expor configurações de rede que são parte do processo de reconhecimento por um invasor. Identificar esses filtros pode ajudar a planejar ataques. | Implementar o princípio do menor privilégio, garantindo que apenas usuários ou funções específicas possam acessar essas informações. Monitorar e registrar acessos usando AWS CloudTrail.          |

Notas:
- **Justificativa da Classificação**: A ação não modifica recursos, mas pode expor informações importantes para reconhecimento do ambiente.
- **Recomendações de Segurança**: A ênfase está em restringir o acesso à informação para usuários que realmente necessitam e em aplicar monitoramento rigoroso para detectar acessos indevidos.

## Action: ListReceiptRuleSets
### Modelagem de Ameaças para Ação IAM na AWS

| **AWS IAM Action**       | **BUILD/RUN** | **Descrição**                                                             | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                  | **Recomendações de Segurança**                                                                                           |
|--------------------------|---------------|--------------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|----------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `ListReceiptRuleSets`    | RUN           | Lista os conjuntos de regras de recebimento que existem em sua conta.     | Discovery                 | T1087.002 - Account Discovery: Cloud Account | **Médio** | **Melhor Prática**   | Essa ação permite a enumeração dos conjuntos de regras, o que pode ser usado para reconhecimento, mas não modifica o estado dos recursos. | Restringir o uso desta ação a usuários e roles estritamente necessários, revisar logs de acesso com CloudTrail regularmente. |

### Análise Detalhada

- **Tática (MITRE ATT&CK): Discovery** - A identificação de conjuntos de regras pode fazer parte do reconhecimento de informações sobre recursos.
- **Técnica (MITRE ATT&CK): T1087.002 - Account Discovery: Cloud Account** - Esta técnica é usada para obter informações sobre contas e recursos na nuvem, podendo auxiliar em planejamento de ataques subsequentes.
  
### Estratégia de Segurança

1. **Princípio do Menor Privilégio**: Certifique-se de que somente usuários e funções que realmente necessitam dessa permissão a possuam.
2. **Monitoramento Contínuo**: Utilize o AWS CloudTrail para monitorar e alertar sobre o uso incomum ou não autorizado dessa ação.
3. **Revisão Regular de Políticas**: Faça revisões periódicas das políticas para garantir que não haja permissões excessivas atribuídas, e ajuste conforme as melhores práticas de segurança.

🔹 É importante sempre alinhar as práticas de segurança com as mudanças contínuas no ambiente e regulamentações aplicáveis.

## Action: ListTemplates
### Modelagem de Ameaças para Ação IAM: `ListTemplates`

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|---------------|--------------|--------------------------|--------------------------------------|-----------|------------------|------------------------------------|-------------------------------|
| `ListTemplates` | RUN | Lista os modelos de email presentes na sua conta. | Reconnaissance | T1592 - Gather Victim Identity Information | **Médio** | **Melhor Prática** | Esta ação pode ser explorada para coletar informações sobre os modelos de email em uso, que podem ajudar um atacante a compreender a estratégia de comunicação e explorar vulnerabilidades. | Implementar o princípio do menor privilégio, restringindo quem pode listar esses modelos. Monitorar atividades anômalas com AWS CloudTrail e configurar alertas no AWS Security Hub para acesso a informações sensíveis. |

---

**📌 Nota:** Esta análise considera que a ação `ListTemplates` pertence à categoria **RUN** e que, apesar de seu uso não modificar diretamente recursos, ela pode ser uma etapa preliminar valiosa para ataques mais elaborados.

## Action: ListVerifiedEmailAddresses
### 📊 Tabela de Modelagem de Ameaças

| **AWS IAM Action**             | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                     | **Recomendações de Segurança**                                                                                                                                           |
|--------------------------------|---------------|-------------------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|---------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ListVerifiedEmailAddresses`   | RUN           | Lista todos os endereços de email que foram verificados na sua conta.         | Discovery                 | T1087 - Account Discovery              | Médio     | Melhor Prática      | Essa ação permite listar recursos não-sensíveis anonimamente, mas fornece informações úteis para reconhecimento.          | Limitar essa ação a usuários que realmente precisam dela por meio de políticas IAM. Monitorar seu uso com AWS CloudTrail e aplicar princípio do menor privilégio.       |

### ✅ Notas Importantes
- **Análise de Ameaça:** A ação `ListVerifiedEmailAddresses` está ligada à tática de **Discovery**, uma vez que fornece visibilidade sobre quais endereços de e-mail estão associados à conta. Mesmo que a ação por si só não cause uma modificação direta na infraestrutura, pode ser explorada para reconhecimento por um atacante.
- **Classificação de Risco:** Considerada como **Médio** devido à sua capacidade de auxiliar no reconhecimento, mas não causa impacto direto sem acesso adicional.
- **Recomendações de Segurança:** Implementar o princípio do menor privilégio, garantindo que apenas usuários que necessitem dessa informação tenham acesso. Monitorar regularmente através de **AWS CloudTrail** para identificar possíveis usos anômalos.

## Action: PutConfigurationSetDeliveryOptions
| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                         | **Recomendações de Segurança**                                                                                                                                                             |
|--------------------------------------------|---------------|----------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PutConfigurationSetDeliveryOptions`       | BUILD         | Adiciona ou atualiza as opções de entrega para um conjunto de configuração.                   | Initial Access           | T1078 - Valid Accounts               | **Alto**  | **Requer Controle**  | Esta ação pode ser explorada para alterar opções de entrega e potencialmente redirecionar ou interceptar comunicações.    | Monitorar alterações em opções de entrega, aplicar princípio do menor privilégio, usar registros do CloudTrail para auditoria de alterações e configurar alertas para modificações não autorizadas.                        |



## Action: PutIdentityPolicy
Para a ação IAM `PutIdentityPolicy`, procederemos com a análise conforme o framework MITRE ATT&CK e as diretrizes estabelecidas. 

### **Modelagem de Ameaças**

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `PutIdentityPolicy` | BUILD | Adiciona ou atualiza uma política de autorização de envio para a identidade especificada (um endereço de email ou um domínio). | Credential Access | T1081 - Credentials in Files | **Alto** | **Requer Controle** | Esta ação permite a modificação de políticas que podem comprometer a autorização e controle de envio de e-mails, possibilitando ataques de phishing ou uso malicioso de recursos de e-mail. | Aplicar o princípio de menor privilégio. Monitorar a criação e modificação de políticas com AWS CloudTrail para detectar anomalias. Restringir a capacidade de modificar políticas apenas a usuários e funções confiáveis. |

### **Considerações Adicionais**
- **Impacto na Segurança**: A modificação de políticas de identidade pode permitir a interceptação ou redirecionamento de e-mails, ameaçando a confidencialidade e integridade das comunicações.
- **Detecção e Mitigação**: Uso de AWS CloudTrail para monitorar atividades associadas a essa ação é essencial para garantir que ações suspeitas ou não autorizadas sejam identificadas rapidamente.

A análise acima fornece uma visão detalhada do risco associado à ação `PutIdentityPolicy` do AWS IAM, mapeando-a a técnicas do MITRE ATT&CK e oferecendo medidas de mitigação efetivas.

## Action: ReorderReceiptRuleSet
### 📊 Modelagem de Ameaças para Ação IAM `ReorderReceiptRuleSet`

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                                                                          | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                   | **Recomendações de Segurança**                                                                                       |
|-------------------------|--------------|----------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `ReorderReceiptRuleSet` | BUILD        | Reordena as regras de recebimento dentro de um conjunto de regras de recebimento no SES. | Defense Evasion           | T1562 - Impair Defenses               | Médio     | **Melhor Prática**   | Reordenar as regras pode ser explorado para desativar ou dar prioridade inadequada a regras que filtram ou bloqueiam tráfego malicioso.                           | Implementar monitoramento rigoroso das alterações nas regras do SES com o AWS CloudTrail. Adotar o princípio do menor privilégio nas permissões de IAM. |

---

### 📝 Detalhamento e Justificativas

1. **Análise da Ação IAM:**
   - **ReorderReceiptRuleSet** permite alterar a ordem de aplicação das regras de recebimento de e-mail no Amazon SES.
   - O risco moderado está relacionado à potencial priorização inadequada de regras, podendo impactar a capacidade de filtragem de e-mails maliciosos.

2. **Mapeamento para MITRE ATT&CK:**
   - **Tática: Defense Evasion (Evasão de Defesa)**
     - **Técnica T1562 - Impair Defenses (Desabilitar Defesas)**: Refere-se a ações que modificam a configuração de sistemas de segurança para evadir a detecção ou bloquear ferramentas de resposta.

3. **Classificação de Risco:**
   - **Risco Médio**:
     - **Impacto:** Moderado, pois o reordenamento pode comprometer parcialmente a defesa contra e-mails indesejados ou maliciosos.
     - **Probabilidade:** Potencialmente explorável, embora exija acesso e intenção maliciosa.
     - **Mitigação:** Fácil de detectar e mitigar com controles adequados.

4. **Recomendações de Segurança:**
   - **Monitoramento:** Usar AWS CloudTrail para monitorar alterações nas regras e detectar reordenações suspeitas de forma contínua.
   - **Princípio do Menor Privilégio:** Limitar as permissões de IAM para garantir que apenas usuários ou serviços autorizados possam alterar a ordem das regras.
   - **Auditoria Regular:** Realizar auditorias periódicas das configurações do Amazon SES e regras de recebimento para assegurar que elas permaneçam alinhadas com as políticas de segurança organizacionais.

## Action: SendBounce
Baseando-se na entrada fornecida e aplicando o mapeamento com o framework MITRE ATT&CK, a avaliação para a ação IAM **`SendBounce`** do Amazon SES resultou na seguinte análise:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `SendBounce` | RUN | Gera e envia uma mensagem de erro para o remetente de um email recebido através do Amazon SES. | Impact | T1531 - Account Access Removal | **Médio** | **Melhor Prática** | A ação pode ser explorada para simular mensagens de falha de entrega, potencialmente levando a falhas na comunicação ou danos à reputação. É menos provável de impacto direto em confidencialidade, integridade ou disponibilidade, mas pode induzir erros operacionais. | Configurar políticas IAM para restringir o uso ao menor número de identidades necessárias, monitorar logs do SES para padrões de falhas incomuns usando AWS CloudTrail. Ativar notificações ou alarmes para padrões de falhas atípicas. |

### **Nota Adicional**
- **Contexto de Ameaça**: A utilização de `SendBounce` pode ser um vetor em ataques de engenharia social ao simular falhas de entrega com o objetivo de perturbar o fluxo normal de e-mails.
- **Mitigação Refinada**: Além do monitoramento, a integração com AWS Security Hub pode ajudar a automatizar a detecção de comportamentos anômalos neste contexto.

Essa análise proporciona uma visão clara sobre os riscos associados à ação e orientações sobre como se proteger contra ameaças potenciais.

## Action: SendBulkTemplatedEmail
### Modelagem de Ameaças para Ação IAM: `SendBulkTemplatedEmail`

| **AWS IAM Action**           | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                                            | **Recomendações de Segurança**                                                                                                                                                                                |
|------------------------------|---------------|-------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SendBulkTemplatedEmail`     | RUN           | Compõe uma mensagem de email para múltiplos destinos.                         | Exfiltration             | T1071.001 - Application Layer Protocol: Web Protocols                         | **Alto** | **Requer Controle** | A capacidade de enviar e-mails em massa pode ser explorada para exfiltração de dados, phishing ou espalhar malware. A ação pode comprometer a integridade e confidencialidade dos dados.       | Implementar monitoramento rigoroso do uso de e-mails, filtrar e bloquear e-mails suspeitos, usar políticas de IAM para limitar quem pode enviar e-mails em massa e habilitar o AWS CloudTrail para auditoria de ações de envio de e-mail. |

### Observações Adicionais
- **Contextualização**: Em um ambiente financeiro, o envio não autorizado de e-mails pode violar políticas de proteção de dados e normas de compliance. É crítico garantir que esta função seja rigorosamente controlada.
- **Mitigação Adicional**: Evitar o uso excessivo da ação por entidades externas e aplicar o princípio do menor privilégio para limitar o acesso.

## Action: SendCustomVerificationEmail
Baseado nos dados fornecidos, aqui está a modelagem de ameaças para a ação do AWS IAM `SendCustomVerificationEmail`:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `SendCustomVerificationEmail` | RUN | Adiciona um endereço de email à lista de identidades e tenta verificá-lo em sua conta. | Credential Access | T1566 - Phishing | **Médio** | **Melhor Prática** | Esta ação pode ser utilizada para enviar e-mails de phishing em uma tentativa de coletar credenciais ou informações sensíveis, embora dependa de engenharia social externa para ser efetiva. | Implementar políticas de controle de uso de identidades, monitoramento de logs de envio de e-mails, e aplicar filtros de segurança nos e-mails. |

### **Justificação da Classificação:**
A exploração desta ação requer intervenção de engenharia social ou erro humano para ser efetiva em compromissos credenciais ou informações. No entanto, o potencial para abuso em campanhas de phishing justifica a implementação de proteções.

### **Recomendações Detalhadas:**
- **Políticas IAM**: Restringir o uso da ação `SendCustomVerificationEmail` apenas a entidades confiáveis ou processos automatizados verificados.
- **Monitoramento Continuado**: Utilizar AWS CloudTrail para monitorar atividades e AWS Config para garantir conformidade contínua.
- **Mitigação Phishing**: Configuração de filtros de segurança para detectar e-mails suspeitos e implementando treinamentos de conscientização de segurança para usuários finais.
- **Menor Privilégio**: Aplicar o princípio de menor privilégio nas permissões IAM para reduzir a superfície de risco.

Este modelo de ameaças pode ajudar a proteger melhor o ambiente AWS contra usos indevidos dessas ações IAM específicas.

## Action: SendEmail
### **Modelagem de Ameaças para Ação IAM**

| **AWS IAM Action** | **BUILD/RUN** | **Descrição**                      | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                   |
|--------------------|---------------|------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `SendEmail`        | RUN           | Envia uma mensagem de email.       | Exfiltration              | T1041 - Exfiltration Over C2 Channel  | Médio     | Melhor Prática       | Ação pode ser utilizada para exfiltração de dados, mas depende de acesso prévio e cadeia de ataque. | Monitorar logs de envio de e-mails, aplicar o princípio de menor privilégio, e utilizar controles de monitoração como CloudTrail e GuardDuty. |

### **Justificativas e Contexto Adicional**

- **Tática - Exfiltration:** A ação de enviar e-mails pode ser utilizada por um atacante para exfiltrar dados sensíveis em um ambiente comprometido. Embora em si não seja suficiente para comprometer o sistema, ela é parte de uma cadeia de ataque mais ampla.
  
- **Risco Médio:** Apesar do potencial de exfiltração de dados, o risco é considerado médio devido à necessidade de comprometimento prévio e à possibilidade de detecção através de monitoramento adequado.

- **Recomendações de Segurança:** O uso do CloudTrail e do GuardDuty permite o monitoramento contínuo das atividades de envio de e-mails, ajudando a detectar comportamentos anômalos. Além disso, a aplicação do princípio de menor privilégio garante que apenas entidades autorizadas possam executar essa ação. A implementação de controle de tráfego de e-mail e inspeção de conteúdo através de integrações de segurança também pode mitigar riscos.

### **Considerações Regulatórias**

- Caso o ambiente seja regulado por normas financeiras ou de proteção de dados, como as mencionadas anteriormente, é crítico garantir que as práticas de segurança estejam em conformidade com esses regulamentos para evitar penalidades e proteger dados sensíveis.

## Action: SendRawEmail
Com base nos dados fornecidos, aqui está a modelagem de ameaças para a ação IAM `SendRawEmail`:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `SendRawEmail`     | RUN          | Envia uma mensagem de email, com cabeçalho e conteúdo especificados pelo cliente. | Exfiltration | T1041 - Exfiltration Over C2 Channel | **Alto** | **Requer Controle** | Permite envio de informações potencialmente sensíveis para fora da organização, possibilitando vazamento de dados. | Implementar políticas de IAM que restrinjam o uso da ação, monitorar ativamente o envio de e-mails suspeitos via CloudTrail e configurar alertas. |

**Notas Adicionais:**
- **Justificativa do Risco:** A ação `SendRawEmail` tem o potencial de ser explorada para o exfiltração de dados e envio de e-mails phishing, visto que o remetente pode especificar cabeçalhos e conteúdos arbitrários, o que pode ser utilizado para conduzir ataques fraudulentos ou vazamento de informações sensíveis.
- **Recomendações Adicionais:** Considere o uso de filtros de conteúdo para análise de mensagens, e estabeleça limites rigorosos para quem pode usar esse tipo de ação dentro da organização. A implementação de verificação e autenticação de e-mails enviados (como SPF, DKIM, e DMARC) também é uma prática recomendada para aumentar a segurança de e-mails.

## Action: SendTemplatedEmail
### 📝 Modelagem de Ameaças para Ação IAM

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                                         | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                     | **Recomendações de Segurança**                                                                                              |
|-------------------------|---------------|-------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `SendTemplatedEmail`    | RUN           | Compõe uma mensagem de email usando um modelo de email.| Phishing                  | T1566.002 - Spearphishing Link        | **Alto**  | **Requer Controle** | Essa ação pode ser explorada para enviar e-mails de phishing altamente personalizados, comprometendo usuários.        | Monitorar atividades de envio de e-mails, implementar filtros de conteúdo, restringir o uso de modelos através de políticas IAM. |

### Notas Adicionais
- **Risco e Justificativa**: A capacidade de enviar e-mails usando modelos pode ser explorada por atacantes para criar campanhas de phishing altamente direcionadas, utilizando informações contextuais do ambiente, aumentando as chances de sucesso do ataque.
- **Estratégia de Segurança**: É crucial ter auditoria contínua de logs de e-mail para detectar e responder rapidamente a tentativas de phishing. Configure serviços de alerta e resposta a incidentes.
- **Adoção de Zero Trust**: Aplique o princípio do menor privilégio, garantindo que apenas usuários autorizados consigam enviar e-mails utilizando modelos especificados por políticas IAM.
- **Referências**: Consulte as práticas recomendadas do [AWS SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-using-sdk.html) para robustecer processos de segurança.

Auferir consistência com as regulamentações específicas, como BACEN e LGPD, pode demandar controles adicionais focados em proteção da privacidade e integridade das comunicações.

## Action: SetActiveReceiptRuleSet
### Modelagem de Ameaças para Ação IAM: `SetActiveReceiptRuleSet`

#### Tabela de Ameaças

| **AWS IAM Action**          | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                  | **Recomendações de Segurança**                                                         |
|-----------------------------|---------------|-------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `SetActiveReceiptRuleSet`   | BUILD         | Define o conjunto de regras de recebimento especificado como o ativo.         | Persistence               | T1098.004 - Account Manipulation: Redirection | **Alto**   | **Requer Controle**   | Pode ser explorado para alterar regras de recebimento de e-mails, potencialmente redirecionando tráfego ou interferindo em comunicações. | Monitorar alterações em conjuntos de regras, implementar autorização estrita via políticas IAM. |

#### Recomendações Detalhadas
1. **Monitoramento e Alerta**
   - **AWS CloudTrail**: Configurar para registrar atividades de `SetActiveReceiptRuleSet` e gerar alertas para alterações não autorizadas.
   - **AWS Security Hub**: Integrar para reforçar a detecção de atividades suspeitas relacionadas a alterações nas regras de recebimento.

2. **Restrições de Acesso**
   - **IAM Policies**: Aplicar o princípio do menor privilégio, permitindo essa ação apenas a usuários ou funções específicas necessárias.
   - **MFA**: Requerer autenticação multifator para usuários com permissão para modificar conjuntos de regras.

3. **Práticas de Revisão e Auditoria**
   - Realizar auditorias regulares das alterações nos conjuntos de regras para garantir que seguem as políticas de segurança organizacionais.
   - Implementar revisão de pares ou mudanças, permitindo que múltiplos administradores aprovem ou verifiquem modificações nos conjuntos de regras.

Essas estratégias ajudarão a mitigar potenciais explorações dessa ação IAM e fortalecerão a segurança geral do ambiente AWS.

## Action: SetIdentityDkimEnabled
### 📊 Modelagem de Ameaças para Ação IAM

| **AWS IAM Action**         | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                                      | **Recomendações de Segurança**                                                                                                                                                            |
|----------------------------|--------------|-------------------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SetIdentityDkimEnabled`   | BUILD        | Ativa ou desativa a assinatura DKIM fácil de emails enviados de uma identidade.| Defense Evasion           | T1562.002 - Disable or Modify Tools   | **Médio** | **Melhor Prática** | Desativar a assinatura DKIM pode permitir que e-mails falsificados passem por filtros de segurança, reduzindo a capacidade de detectar e-mails maliciosos.                              | Monitorar mudanças nas configurações DKIM através de logs do AWS CloudTrail. Implementar políticas IAM restringindo essas ações a usuários autorizados.                                    |

### 📝 Notas
- **Justificativa**: A alteração do estado DKIM afeta a capacidade de verificar a autenticidade de mensagens de e-mail, o que pode ser explorado para evadir mecanismos de defesa.
- **Recomendações de Segurança**: É crucial monitorar quaisquer alterações no status DKIM através do AWS CloudTrail e estabelecer políticas rígidas para limitar quem pode executar essa ação.

## Action: SetIdentityFeedbackForwardingEnabled
### Tabela de Modelagem de Ameaças para a Ação IAM "SetIdentityFeedbackForwardingEnabled"

| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                                                                                                                     | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                       | **Recomendações de Segurança**                                                                                                                                                                           |
|--------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SetIdentityFeedbackForwardingEnabled` | BUILD         | Ativa ou desativa se o Amazon SES reencaminha notificações de erro e reclamação para uma identidade (um endereço de email ou um domínio). | Initial Access            | T1071 - Application Layer Protocol    | **Alto**  | **Requer Controle** | Esta ação pode ser utilizada para manipular notificações de feedback, redirecionando potenciais informações sensíveis ou alterando fluxos de comunicação. | Implementar logs detalhados das alterações de feedback no SES via AWS CloudTrail. Restringir permissões de uso através de políticas IAM e aplicar o princípio do menor privilégio. Monitorar e revisar regularmente as configurações de feedback. |

---

### Considerações Adicionais:

1. **Contexto de Segurança:** Manipulações inadvertidas ou maliciosas dessas configurações podem impactar serviços que dependem da integridade dos feedbacks de e-mails do SES, potencialmente violando conformidade com regulamentações de comunicação segura.

2. **Práticas Recomendadas:** A implementação de logs e monitoramento contínuo facilita a detecção de configurações inapropriadas ou maliciosas, enquanto o uso de controles de acesso rigorosos minimiza riscos de alterações não autorizadas.

## Action: SetIdentityHeadersInNotificationsEnabled
### **🛡️ Modelagem de Ameaças para AWS IAM Action**

Com base na entrada fornecida para a ação IAM `SetIdentityHeadersInNotificationsEnabled`, segue a análise detalhada de modelagem de ameaças:

| **AWS IAM Action**                        | **BUILD/RUN** | **Descrição**                                                                                                                                                                | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                        | **Recomendações de Segurança**                                                                                   |
|-------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `SetIdentityHeadersInNotificationsEnabled` | BUILD        | Define se o Amazon SES inclui os cabeçalhos originais do email nas notificações do Amazon SNS de um tipo especificado para uma identidade.                                  | Collection                | T1114 - Email Collection             | **Médio** | **Melhor Prática**  | Essa ação pode ser usada para coletar informações do cabeçalho de e-mails, o que pode ser explorado para fins de monitoramento ou interceptação de dados. | Revisar políticas IAM associadas a quem pode configurar notificações, aplicar o princípio do menor privilégio, e habilitar monitoramento via AWS CloudTrail. |

### **Análise e Justificativa**

1. **Tática e Técnica (MITRE ATT&CK)**:
   - **Tática**: Collection (Coleta)
   - **Técnica**: T1114 - Email Collection

2. **Classificação de Risco**: 
   - Avaliada como **Médio** devido ao potencial de exploração para interceptação ou coleta de dados de e-mails sem autorização adequada.

3. **Recomendações de Segurança**:
   - **Políticas IAM**: Acesso restrito a usuários que realmente necessitam configurar essa opção.
   - **Princípio do Menor Privilégio**: Garantir que apenas contas de confiança e com necessidade operacional tenham esse privilégio.
   - **Monitoramento e Detecção**: Utilizar o AWS CloudTrail para monitorar logs de configuração e alterações. Verificar comunicaçãos suspeitas regularmente.
   - **MFA e Auditoria Contínua**: Implementar autenticação multifator (MFA) e auditoria contínua para identificar comportamentos atípicos.

Ao seguir essas recomendações, é possível mitigar potenciais ameaças associadas à ação `SetIdentityHeadersInNotificationsEnabled`, minimizando riscos à segurança da informação.

## Action: SetIdentityMailFromDomain
## Modelagem de Ameaças para Ação IAM: `SetIdentityMailFromDomain`

| **AWS IAM Action**         | **BUILD/RUN** | **Descrição**                                                                                  | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                                                                                  | **Recomendações de Segurança**                                                              |
|----------------------------|--------------|-----------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `SetIdentityMailFromDomain` | BUILD        | Ativa ou desativa a configuração de domínio MAIL FROM personalizado para uma identidade verificada. | Defense Evasion           | T1078 - Valid Accounts               | **Médio** | **Melhor Prática** | A configuração inadequada de MAIL FROM pode ser usada para evadir controles de e-mail padrão, mas requer acesso a identidades previamente verificadas.                  | Restringir a ação a usuários autenticados e autorizar apenas contas e domínios conhecidos. Habilitar logs do CloudTrail para monitoramento contínuo.                    |

### Análise e Detalhamento

1. **Análise da Ação IAM**:
   - A ação `SetIdentityMailFromDomain` envolve modificar a configuração de domínios de e-mail que já foram verificados. Isso pode potencialmente ser explorado para redirecionar e-mails ou manipular cabeçalhos de e-mail.

2. **Mapeamento para MITRE ATT&CK**:
   - Esta ação está associada à tática de **Defense Evasion**, especificamente usando contas válidas para configurar domínios de e-mail de forma a evadir detecção.

3. **Classificação de Risco**:
   - A classificação como "Médio" reflete o fato de que, embora a ação possa ser usada de forma maliciosa, requer acesso já autenticado com privilégios para modificar configurações verificadas, limitando o risco.

4. **Recomendações de Segurança**:
   - **Práticas de Melhor Prática**: Implementar políticas de IAM restritivas para que apenas usuários autorizados possam executar essa ação. Monitorar continuamente o uso desta ação via **AWS CloudTrail**. Adicionar verificações de integridade para garantir que qualquer modificação no MAIL FROM seja validada e aprovada por pessoal qualificado.

## Action: SetIdentityNotificationTopic
Com base na entrada fornecida, vamos modelar a ameaça associada à ação IAM `SetIdentityNotificationTopic` usando o framework MITRE ATT&CK. 

### **Modelagem de Ameaças para `SetIdentityNotificationTopic`**

| **AWS IAM Action**            | **BUILD/RUN** | **Descrição**                                                                                       | **Tática (MITRE ATT&CK)**    | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                                                | **Recomendações de Segurança**                                                                                                                          |
|-------------------------------|---------------|-----------------------------------------------------------------------------------------------------|------------------------------|--------------------------------------|-----------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SetIdentityNotificationTopic`| BUILD         | Define um tópico do Amazon SNS a ser usado ao enviar notificações para uma identidade verificada.    | Initial Access               | T1071.001 - Application Layer Protocol (HTTPS)           | **Médio**  | **Melhor Prática** | Esta ação permite a configuração de tópicos SNS que podem ser usados para redirecionar ou interceptar notificações, mas requer identidade verificada, limitando o potencial de abuso. | Utilize IAM Policies para restringir quem pode definir tópicos SNS, habilite auditoria com AWS CloudTrail para monitorar mudanças em notificações e revise regularmente permissões atribuídas. |

A análise determina que essa ação é classificada como **Médio - Melhor Prática**, principalmente devido à sua capacidade de alterar destinos de notificações, o que pode ser explorado maliciosamente se permissões forem descontroladas, mas requer níveis adicionais de configuração e permissões para exploração efetiva.

#### **Recomendações Adicionais**
- **Princípio do Menor Privilégio**: Aplique os mínimos privilégios necessários aos usuários que podem realizar essa ação.
- **Monitoramento e Logging**: Ative o AWS CloudTrail para auditorar quem modifica os tópicos do SNS e identifique comportamentos não usual no uso dessas permissões.
- **Análise Regular de Permissões**: Faça revisões periódicas das permissões atribuídas aos usuários para garantir que somente indivíduos necessários mantenham esses acessos.

Essas práticas ajudarão a mitigar riscos associados a essa ação e proteger contra possíveis explorações.

## Action: SetReceiptRulePosition
### 🛡️ Modelagem de Ameaças AWS para Ação IAM "SetReceiptRulePosition"

Abaixo está a análise da ação IAM **"SetReceiptRulePosition"**, classificando-a em termos de riscos potenciais, mapeamento com o MITRE ATT&CK, e recomendações de segurança.

| **AWS IAM Action**         | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)**         | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                      | **Recomendações de Segurança**                                                                                                                                                       |
|----------------------------|---------------|-------------------------------------------------------------------------------|----------------------------------|--------------------------------------|-----------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SetReceiptRulePosition`   | BUILD         | Define a posição da regra de recebimento especificada no conjunto de regras. | Persistence                      | T1027 - Obfuscated Files or Information | **Médio**  | **Melhor Prática** | A modificação na ordem das regras de recebimento pode ser explorada para criar persistência em determinados fluxos de e-mails sem detecção imediata.                                   | Implementar o princípio do menor privilégio, monitorar alterações nas regras de recebimento via AWS CloudTrail e criar alertas no AWS Security Hub.                                             |

### 🛠️ Diretrizes Adicionais

1. **Práticas Recomendadas**: 
   - Utilizar **AWS IAM Policies** para restringir quem pode alterar regras de recebimento.
   - Configurar **AWS Config** para monitoramento contínuo das configurações de regras de e-mails.
   - Habilitar **AWS CloudTrail** para auditoria e investigação em caso de eventos suspeitos.

2. **Contextualização e Regulamentação**:
   - Garantir conformidade com regulamentações do setor financeiro como **ISO 27001** e **PCI-DSS** implementando segregação de funções e controles de acesso rigorosos.

3. **Zero Trust**:
   - Aplicar **Zero Trust**, assegurando que todas as ações IAM sejam apenas para usuários legitimamente autorizados e monitoráveis quanto ao uso.

Essa análise proporciona uma visão estruturada sobre como a ação **SetReceiptRulePosition** pode ser considerada e mitigada em termos de segurança em ambientes AWS.

## Action: TestRenderTemplate
### **📊 Tabela de Modelagem de Ameaças**

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                                                                                                                                     | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                           | **Recomendações de Segurança**                                                                                                                                                         |
|-------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TestRenderTemplate`    | BUILD        | Cria uma pré-visualização do conteúdo MIME de um email fornecendo um modelo e um conjunto de dados de substituição.                              | Initial Access             | T1189 - Drive-by Compromise           | Médio     | Melhor Prática      | A ação permite pré-visualizar conteúdo de e-mails, o que pode ser usado para testar modelos de phishing ou outros conteúdos maliciosos em preparação para uma campanha.  | Implementar políticas IAM restritivas, monitorar logs de acesso ao SES com AWS CloudTrail e ativar alertas no AWS Security Hub para alterações não autorizadas em modelos de e-mail. |

- **Contextualização:** No caso do `TestRenderTemplate`, a pré-visualização gera uma representação do que um destinatário potencial veria. Monitorar e controlar quem tem permissão para usar essa função ajuda a mitigar riscos de preparações para campanhas maliciosas, como phishing.

- **Tática/Técnica Racionada:** A ação é comparável à técnica `T1189 - Drive-by Compromise`, já que pode ser usada para preparar ou testar conteúdo de ataque (e.g., phishing) antes do lançamento, fornecendo acesso inicial ao sistema alvo.

- **Recomendações Detalhadas:** Assegure-se de que somente usuários autorizados podem executar essa ação, integrando com práticas de segurança como autenticação MFA e o princípio de menor privilégio. Monitore atividades usando o AWS CloudTrail para detectar comportamentos anômalos em tempo real.

## Action: UpdateAccountSendingEnabled
| **AWS IAM Action**                       | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                                   | **Recomendações de Segurança**                                                                                              |
|------------------------------------------|--------------|------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `UpdateAccountSendingEnabled`            | BUILD         | Ativa ou desativa o envio de email para sua conta.                           | Impact                     | T1499.004 - Network Denial of Service: Network DoS | **Médio**  | **Melhor Prática**     | Esta ação pode ser explorada para causar interrupção de serviço ao desativar envios de e-mail, afetando a disponibilidade. | Implementar CloudWatch para monitorar mudanças na configuração de envio, usar AWS Config para compliance e limitar acesso via IAM. |

### 🔒 Notas Adicionais
- O risco é considerado **médio** devido à possibilidade de interrupção do serviço de envio de e-mails, afetando a operacionalidade se mal configurado.
- **Mitigação**: Use grupos de segurança rígidos, alertas em tempo real para alterações e revisões de logs periódicos para atividades não autorizadas.

✅ **Certifique-se que todas as medidas de segurança são implementadas para prevenir uso indevido desta ação no ambiente AWS**.

## Action: UpdateConfigurationSetEventDestination
Com base nas informações fornecidas, vamos realizar a modelagem de ameaças para a ação IAM `UpdateConfigurationSetEventDestination`, considerando suas implicações de segurança, táticas e técnicas associadas no MITRE ATT&CK, avaliação de risco e recomendações de segurança.

### **🛠️ Modelagem de Ameaças: UpdateConfigurationSetEventDestination**

| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                             | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                           | **Recomendações de Segurança**                                                                                                                                                       |
|--------------------------------------------|---------------|-----------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UpdateConfigurationSetEventDestination` | BUILD         | Atualiza o destino de evento de um conjunto de configuração. | Execution | T1203 - Exploitation for Client Execution | **Alto** | **Requer Controle**   | Atualizar destinos de eventos pode levar à execução não autorizada de código se não for devidamente controlado, especialmente se os destinos processarem eventos críticos. | Implementar políticas IAM restritivas, usar AWS CloudTrail para monitorar alterações em configurações críticas e validar todas as solicitações de atualização.                  |

---

### **🔍 Detalhamento e Racionalização**

1. **Tática e Técnica (MITRE ATT&CK)**: A ação `UpdateConfigurationSetEventDestination`, associada à tática de **Execução**, reflete a capacidade de modificar destinos que possam inadvertidamente permitir a execução de código ou manipulação de dados confidenciais.

2. **Risco e Classificação**: Classificado como **Alto** devido ao potencial impacto que alterações não autorizadas em destinos de eventos podem ter, como redirecionar logs para locais desconhecidos ou inadvertidamente causar vazamentos de dados sensíveis.

3. **Recomendações de Segurança**:
   - **Políticas IAM Restritas**: Limitar quem pode realizar essa ação através do princípio do menor privilégio.
   - **Monitoramento e Auditoria**: Usar AWS CloudTrail para monitorar em tempo real alterações em configurações de eventos, permitindo resposta rápida a ações suspeitas.
   - **Validação de Atualizações**: Implementar processos para revisão e validação de solicitações de atualização, garantindo que sejam legítimas e em conformidade com as práticas de segurança.

Essas etapas e classificações asseguram que a ação `UpdateConfigurationSetEventDestination` seja realizada de maneira segura, mitigando riscos associados a usos maliciosos e mantendo a integridade e disponibilidade dos dados dentro da AWS.

## Action: UpdateConfigurationSetReputationMetricsEnabled
### 💻 Modelagem de Ameaças AWS: Ação IAM "UpdateConfigurationSetReputationMetricsEnabled"

| **AWS IAM Action**                          | **BUILD/RUN** | **Descrição**                                                                                       | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                                     | **Recomendações de Segurança**                                                                                                                                                                          |
|---------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UpdateConfigurationSetReputationMetricsEnabled` | BUILD         | Ativa ou desativa a publicação de métricas de reputação para emails enviados usando um conjunto de configuração específico. | Collection                | T1119 - Automated Collection         | **Médio**  | **Melhor Prática**  | A configuração de métricas de reputação poderia ser manipulada para monitorar a eficácia de campanhas maliciosas ou enviar SPAM, mas o impacto é limitado e fácil de detectar. | Implementar políticas de menor privilégio para ações sensíveis. Monitorar alterações nas configurações de reputação usando AWS CloudTrail. Aplicar SCPs para limitar quem pode alterar essas configurações. |

### 🔍 Notas Adicionais
- **Impacto na Segurança**: Alterações indevidas podem permitir que um invasor monitore a reputação de e-mails potencialmente maliciosos, ajustando suas táticas com base nos insights obtidos das métricas.
- **Possíveis Controles**: A implementação de AWS Config para monitorar mudanças e auditoria contínua através do AWS Security Hub pode ajudar a identificar abusos rapidamente.

### 📚 Referências
- [MITRE ATT&CK - T1119: Automated Collection](https://attack.mitre.org/techniques/T1119/)
- [Documentação AWS IAM](https://docs.aws.amazon.com/iam/)

## Action: UpdateConfigurationSetSendingEnabled
| **AWS IAM Action**                     | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                               | **Recomendações de Segurança**                                                                                                                                       |
|----------------------------------------|---------------|-------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UpdateConfigurationSetSendingEnabled` | BUILD         | Ativa ou desativa o envio de emails para mensagens enviadas usando um conjunto de configuração específico. | Execution                  | T1105 - Ingress Tool Transfer        | **Alto**  | **Requer Controle** | Essa ação pode ser explorada para alterar configurações de envio de e-mails, potencialmente facilitando a entrega de mensagens maliciosas. | Monitorar modificações nos conjuntos de configuração de envio, restringir permissões com políticas IAM e SCPs, e implementar logs de auditoria com AWS CloudTrail. |

### **Justificativas e Análise**

- **Ação IAM**: `UpdateConfigurationSetSendingEnabled` tem impacto direto na capacidade de enviar e-mails, o que pode ser explorado para fins maliciosos, como phishing.
- **Tática e Técnica MITRE ATT&CK**: Associado à tática de Execução e técnica de Transferência de Ferramentas de Entrada, já que ajustar o envio de e-mails pode ser um componente de campanhas maliciosas.
- **Risco Alto**: Pois a ação afeta a integridade e confiabilidade das comunicações por e-mail, sendo crucial que a capacidade de modificar essas configurações seja restrita apenas aos usuários autorizados.
- **Recomendações de Segurança**: Aplicar o princípio do menor privilégio, monitorar ações com AWS CloudTrail, e usar o AWS Config para garantir que as alterações nos conjuntos de configuração de envio sejam adequadamente revisadas e controladas.

## Action: UpdateConfigurationSetTrackingOptions
### 🔍 Modelagem de Ameaças para Ação IAM: `UpdateConfigurationSetTrackingOptions`

| **AWS IAM Action**                         | **BUILD/RUN** | **Descrição**                                                                                                                                                     | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                                         | **Recomendações de Segurança**                                                                                                                                                           |
|--------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------|-----------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UpdateConfigurationSetTrackingOptions`    | BUILD         | Modifica uma associação entre um conjunto de configuração e um domínio personalizado para rastreamento de eventos de abertura e clique.                          | Exfiltration              | T1567 - Exfiltration Over Web Service | **Alto**  | **Requer Controle**   | Esta ação pode ser explorada para modificar rastreamentos, redirecionando dados sensíveis para domínios não autorizados, facilitando exfiltração de dados ou compromissos de integridade. | Restrinja permissões de alteração em configurações de rastreamento, implemente monitoramento através do AWS Config e vincule alertas no AWS CloudTrail para mudanças desses rastreamentos. |

### 🛡️ Explicação
- **Risco e Classificação:** A capacidade de modificar opções de rastreamento pode ser crítica se for explorada por um ator mal-intencionado, visto que isso pode permitir a coleta não autorizada de dados sensíveis. Essa ação se enquadra na rota de exfiltração de dados via serviços web, tornando importante o controle rigoroso.
- **Recomendações de Segurança:** Controle de acesso dessa ação deve ser restrito a usuários ou serviços estritamente necessários. O monitoramento contínuo e alertas sobre mudanças nas configurações são essenciais para detecção precoce de tentativas de exploração maliciosa. Além disso, assegurar revisões regulares das políticas IAM ajuda a garantir o princípio do menor privilégio.

## Action: UpdateCustomVerificationEmailTemplate
Com base na análise da ação IAM fornecida, aqui está a tabela de modelagem de ameaças:

| **AWS IAM Action**                        | **BUILD/RUN** | **Descrição**                                                      | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**        | **Justificativa da Classificação**                                                                                                                         | **Recomendações de Segurança**                                                                                              |
|-------------------------------------------|--------------|-------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `UpdateCustomVerificationEmailTemplate`   | BUILD        | Atualiza um modelo de email de verificação personalizada existente. | Initial Access            | T1078 - Valid Accounts               | **Médio** | **Melhor Prática**       | A ação permite modificar templates de e-mail, podendo alterar mensagens para phishing, mas requer acesso IAM prévio.                                      | Monitorar alterações em templates de e-mail por meio do AWS CloudTrail, aplicar o princípio do menor privilégio e restringir acesso não autorizado.           |

### **Análise Detalhada**

- **Risco e Classificação**: A ação de `UpdateCustomVerificationEmailTemplate` possui risco médio devido à possibilidade de ser utilizada para modificar e-mails de verificação de forma maliciosa, o que pode comprometer a integridade das comunicações. No entanto, sua exploração requer acesso autenticado, o que coloca a classificação como "Melhor Prática" em vez de uma urgência crítica.

- **Recomendações de Segurança**: A monitoração contínua de mudanças nos templates, junto com a aplicação de políticas de acesso restritivo, pode mitigar riscos associados a essa ação. Ferramentas como o AWS CloudTrail podem ser essenciais para auditar e registrar essas modificações.

🔍 **Notas Adicionais**:
- **Revisão Constante**: A revisão contínua das políticas IAM pode ajudar a detectar permissões desnecessárias.
- **Educação e Conscientização**: Treinamento sobre práticas de segurança contra phishing deve ser promovido entre os usuários do sistema.

## Action: UpdateReceiptRule
### 📊 Modelagem de Ameaças para Ação IAM: `UpdateReceiptRule`

| **AWS IAM Action**       | **BUILD/RUN** | **Descrição**                     | **Tática (MITRE ATT&CK)**   | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação** | **Recomendações de Segurança**                                      |
|--------------------------|--------------|----------------------------------|----------------------------|-------------------------------------|-----------|-------------------|------------------------------------|--------------------------------------------------------------------|
| `UpdateReceiptRule`      | BUILD         | Atualiza uma regra de recebimento. | Defense Evasion             | T1562.001 - Disable or Modify Tools | **Alto**  | **Requer Controle** | A possibilidade de atualizar regras permite modificar filtros de segurança nas mensagens recebidas, potenciando evasão de mecanismos de defesa. | Monitorar cuidadosamente alterações em regras de recebimento; Limitar a permissão de update a usuários autenticados e usando MFA; Implementar logging completo com AWS CloudTrail. |

---

Esta análise reflete como a ação `UpdateReceiptRule`, classificada como BUILD, pode impactar a segurança ao ser potencialmente usada para alterar regras de recebimento de mensagens. Isso pode ser explorado para desviar ou modificar regras de segurança e filtragem de e-mails em um ambiente AWS, justificando a adoção de controles rigorosos e monitoramento contínuo.

## Action: UpdateTemplate
### Tabela de Modelagem de Ameaças

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                   | **Tática (MITRE ATT&CK)**       | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco**  | **Classificação**     | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                 |
|----------------------|---------------|--------------------------------|---------------------------------|---------------------------------------|------------|-----------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `UpdateTemplate`     | BUILD         | Atualiza um modelo de email.   | Defense Evasion                | T1070.004 - File Deletion             | **Médio**  | **Melhor Prática**    | A possibilidade de alteração de modelos pode ser usada para mascarar ou redirecionar informações sem detecção. | Ativar logs do AWS CloudTrail para monitorar alterações nos modelos de email e implementar políticas rígidas de IAM para limitar quem pode atualizar modelos. |

## Action: VerifyDomainDkim
### 📊 Modelagem de Ameaças para Ação IAM `VerifyDomainDkim`

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**                                                        | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                           | **Recomendações de Segurança**                                                                                                                                                                          |
|------------------------|--------------|----------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VerifyDomainDkim`     | BUILD        | Retorna um conjunto de tokens DKIM para um domínio.                 | Credential Access        | T1586.002 - Compromised Email Accounts | **Médio** | **Melhor Prática**   | A ação pode ser usada para gerar tokens DKIM que, se mal configurados, podem resultar em comprometimento de autenticidade de e-mails.                                                           | Implementar políticas de IAM que restrinjam o acesso a ações sensíveis, realizar auditorias regulares de configuração DKIM, monitorar logs do AWS CloudTrail para mudanças inesperadas nas configurações do DKIM.                                |

### 🔍 Detalhamento da Análise

- **Tática: Credential Access**
  - **Risco Médio**: Esta ação está relacionada à configuração de autenticação de domínio que, se explorada erroneamente, pode comprometer a integridade e autenticidade de e-mails enviados ou recebidos pelo domínio.

- **Justificativa do Risco:**
  - O impacto é focado no potencial comprometimento da confiabilidade das comunicações de e-mail, afetando principalmente a **integridade** das mensagens de e-mail.
  - A probabilidade de exploração é considerada média, dado que uma má configuração pode ser realizada involuntariamente por administradores descuidados ou através de scripts de automação maliciosos.

- **Recomendações Detalhadas:**
  - **IAM Policies**: Limitar o número de usuários com permissões para executar esta ação.
  - **Monitoramento Ativo**: Utilizar AWS CloudTrail para monitorar e registrar todas as chamadas feitas com relação ao `VerifyDomainDkim`, permitindo a detecção rápida de atividades suspeitas.
  - **Auditoria Regular**: Certificar-se de que as configurações DKIM estejam corretamente aplicadas e revisadas periodicamente como parte de procedimentos de segurança de e-mail.

As medidas de segurança sugeridas estão alinhadas com o conceito de **Zero Trust**, promovendo a implementação do princípio do menor privilégio e monitoramento contínuo para garantir que o ambiente AWS esteja seguro contra tentativas de exploração de ações IAM.

## Action: VerifyDomainIdentity
### 📊 Modelagem de Ameaças para a Ação IAM: `VerifyDomainIdentity`

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**         | **Tática (MITRE ATT&CK)**   | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco**  | **Classificação**  | **Justificativa da Classificação**                                                                                       | **Recomendações de Segurança**                                                                                                                                                       |
|-------------------------|---------------|-----------------------|-----------------------------|----------------------------------------|------------|------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `VerifyDomainIdentity`  | BUILD         | Verifica um domínio. | Initial Access              | T1078 - Valid Accounts                 | **Médio**  | **Melhor Prática** | Essa ação é crítica para validar domínios, podendo permitir acesso não autorizado se comprometida. | Restringir quem pode verificar domínios usando políticas IAM, auditando regularmente logs do CloudTrail para tentativas de verificação de domínio e implementando MFA sempre que possível. |

---

### 🛡️ Recomendações Detalhadas
1. **IAM Policies**: Utilize políticas restritivas para que apenas usuários ou grupos específicos possam realizar verificações de domínio. Adotar o princípio do menor privilégio.
2. **AWS CloudTrail**: Habilite logs para monitorar quem e quando a ação `VerifyDomainIdentity` é utilizada. Configure alertas para atividades fora do padrão.
3. **Multi-Factor Authentication (MFA)**: Exija MFA para qualquer usuário que precise realizar ações de verificação de domínio.
4. **Revisão Regular de Permissões**: Programe revisões periódicas dos direitos de acesso para garantir que apenas pessoas autorizadas mantenham permissão para verificar domínios.
5. **AWS Config Rules**: Estabeleça regras para garantir que as verificações de domínio ocorram apenas dentro das normas da organização.

Essas medidas são importantes para prevenir acessos não autorizados e proteger a integridade das operações de validação de domínio.

## Action: VerifyEmailAddress
### 🛡️ Modelagem de Ameaças para Ação IAM `VerifyEmailAddress`

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                            | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                 | **Recomendações de Segurança**                                                         |
|-------------------------|--------------|------------------------------------------|---------------------------|----------------------------------------|-----------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| `VerifyEmailAddress`    | BUILD        | Verifica um endereço de email.           | Initial Access            | T1078 - Valid Accounts                 | Baixo     | Melhor Prática  | Essa ação em si é de baixo impacto, pois apenas verifica endereços de e-mail. Não modifica diretamente configurações de envio de e-mail ou acessos.                | Implantar logs de auditoria para monitorar atividades anormais relacionadas à verificação de e-mails. Aplicar princípio do menor privilégio para quem pode realizar verificações. |
   
### 🔍 Análise

- **Impacto na confidencialidade, integridade e disponibilidade**: A ação isoladamente não compromete esses aspectos, já que apenas verifica se um endereço de e-mail é válido.
- **Probabilidade de exploração em um ambiente real**: Baixa, pois não concede acesso ou informações além da verificação.
- **Possibilidade de detecção e mitigação**: Log de auditoria pode facilmente monitorar seu uso, detectando qualquer padrão anômalo.

### 🛡️ Recomendações Adicionais

- **Implementar IAM Policies**: Limitar quem pode usar essa ação para evitar abuso.
- **Monitoramento Contínuo**: Usar AWS CloudTrail para monitorar logs de verificação de e-mails.
- **Princípio do Menor Privilégio**: Garantir que apenas usuários e funções que realmente necessitam tenham permissão para verificar e-mails.

🔹 **A ação `VerifyEmailAddress` é classificada como uma prática de melhor segurança, requerendo monitoramento e políticas restritivas para assegurar sua utilização segura.**

## Action: VerifyEmailIdentity
Com base nas informações fornecidas, aqui está a modelagem de ameaças para a ação IAM `VerifyEmailIdentity` no contexto AWS:

| **AWS IAM Action**        | **BUILD/RUN** | **Descrição**                           | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco**    | **Classificação** | **Justificativa da Classificação**                                                                                       | **Recomendações de Segurança**                                                                                   |
|---------------------------|--------------|----------------------------------------|---------------------------|---------------------------------------|--------------|-------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `VerifyEmailIdentity`     | BUILD        | Verifica uma identidade de email.      | Credential Access         | T1586.002 - Compromise Email Accounts | **Médio**    | **Melhor Prática** | Embora a verificação de identidade não comprometa diretamente um sistema, ela pode ser usada para facilitar ataques de phishing ou comprometimento de contas. | Limitar permissões de verificação de e-mail a usuários autorizados. Monitorar logs de API para detecção de atividades suspeitas.  |

### Justificativa Adicional:

- **Tática (MITRE ATT&CK):** A ação está associada à tática de *Credential Access*, já que pode facilitar etapas preliminares em campanhas de comprometimento de e-mails.
- **Técnica/Subtécnica:** Refere-se à técnica de comprometer contas de e-mail, sendo relevante no contexto de ataques que visam capturar ou verificar contas para fins maliciosos.
- **Recomendações de Segurança:** A prática do princípio de menor privilégio é essencial. Além disso, recomenda-se o uso de AWS CloudTrail para monitorar chamadas de API relacionadas a esta ação, garantindo que apenas usuários autorizados executem tais ações.

Essa modelagem ajuda a identificar os riscos potenciais e guiar a aplicação de controles adequados no contexto AWS, alinhando as medidas de segurança às táticas conhecidas do MITRE ATT&CK.
