
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
