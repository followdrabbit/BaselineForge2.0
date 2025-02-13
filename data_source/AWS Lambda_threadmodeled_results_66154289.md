
## Action: CreateFunction
### **Modelagem de Ameaças para ação IAM "CreateFunction" do AWS Lambda**

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                                                                                                                                               | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                                                                            | **Recomendações de Segurança**                                                                                                                                                               |
|----------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateFunction`     | BUILD         | Concede permissão para criar uma função AWS Lambda, configurando suas configurações, permissões e necessidades de recursos.                                  | Execution                 | T1059/003 - Command and Scripting Interpreter: Windows Command Shell            | **Alto** | **Requer Controle**   | A criação de funções Lambda pode ser explorada para executar código malicioso ou desviar dados, caso permissões e configurações incorretas sejam aplicadas.                    | Implementar políticas restritivas de IAM, habilitar AWS CloudTrail para monitoramento de criação/modificação, aplicar o princípio de menor privilégio, utilizar AWS Config para conformidade.    |
| `CreateFunction`     | BUILD         | Concede permissão para criar uma função AWS Lambda, configurando suas configurações, permissões e necessidades de recursos.                                  | Initial Access            | T1078 - Valid Accounts                                                   | **Alto** | **Requer Controle**   | Permissões inadequadas ao criar funções Lambda podem conceder aos invasores uma porta de entrada inicial em caso de comprometimento de credenciais.                           | Habilitar a autenticação multifatorial (MFA), restringir o uso de funções Lambda através de políticas SCP, e realizar auditorias regulares das permissões concedidas.                            |

### **Contextualização Adicional**
Para a ação "CreateFunction", é essencial assegurar que as funções Lambda criadas sejam cuidadosamente configuradas para evitar brechas de segurança que possam ser exploradas por adversários. Ao aplicar a técnica de **Command and Scripting Interpreter**, invasores podem usar funções Lambda para executar comandos não autorizados. Em termos de **Initial Access**, credenciais válidas com permissões excessivas podem ser exploradas para criar backdoors ou aumentar o acesso.

### **Diretrizes Complementares**
- **Monitoramento Contínuo e Auditoria**: Utilize AWS CloudTrail e AWS Config para garantir que todas as criações de funções sejam rastreadas e avaliadas continuamente. 
- **Vigilância sobre Configurações de Segurança**: Assegure que qualquer recurso sensível associado às funções Lambda seja gerido adequadamente, minimizando a superfície de ataque.
- **Educação e Treinamento**: Capacite suas equipes sobre as melhores práticas de segurança em ambientes de computação sem servidor (serverless), focando em princípios de acesso seguro e desenvolvimento seguro.

🚨 Esta análise e as recomendações fornecidas devem ser parte de um plano maior de segurança e gestão de ameaças, alinhado às regulamentações do setor financeiro, como BACEN e LGPD, visando garantir a segurança e conformidade contínua dos ambientes AWS.

## Action: InvokeFunction
Para a ação IAM fornecida, aqui está a modelagem de ameaças conforme solicitado:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `InvokeFunction` | RUN | Concede permissão para invocar uma função AWS Lambda, permitindo que ela execute sua lógica pretendida. | Execution | T1203 - Exploitation for Client Execution | **Alto** | **Requer Controle** | A ação pode ser explorada para executar código malicioso caso um adversário obtenha permissão inadequada para invocar funções sensíveis. | Utilize IAM Policies para restringir quem pode invocar a função, monitore logs de execução com AWS CloudTrail para detectar acessos suspeitos e implemente práticas de princípio de menor privilégio. |
| `InvokeFunction` | RUN | Concede permissão para invocar uma função AWS Lambda, permitindo que ela execute sua lógica pretendida. | Impact | T1485 - Data Destruction | **Alto** | **Requer Controle** | Invocar funções Lambda permite a execução de operações que podem alterar ou destruir dados críticos se controladas por um invasor. | Monitore atividades no AWS Lambda com AWS Config e AWS Security Hub, e restrinja o uso de funções Lambda sensíveis com políticas detalhadas. |

### Observações Adicionais:
- A ação `InvokeFunction` é crítica quando se refere à execução de código, pois pode ser usada para comprometer a integridade e disponibilidade do sistema.
- Recomenda-se também implementar Multi-Factor Authentication (MFA) para usuários que têm permissões elevadas e revisar frequentemente logs de auditoria para assegurar que somente ações autorizadas estão ocorrendo.
- Considere a implementação de AWS GuardDuty para detectar comportamentos anômalos associados à execução de funções Lambda.

Essas recomendações visam mitigar os riscos associados e garantir a segurança das operações na AWS.

## Action: DeleteFunction
Com base na ação IAM descrita, a seguir está a modelagem de ameaças considerando o framework MITRE ATT&CK e diretrizes para segurança AWS:

| **AWS IAM Action**    | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**     | **Justificativa da Classificação**                                                                                          | **Recomendações de Segurança**                                                                                                                                                           |
|-----------------------|--------------|------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeleteFunction`      | BUILD        | Concede permissão para excluir uma função AWS Lambda, removendo seu código e configuração da AWS. | Impact Execution          | T1565 - Data Destruction              | Alto      | Requer Controle       | A exclusão de funções Lambda pode ser usada para interromper operações e serviços críticos, afetando a disponibilidade e integridade. | Implementar políticas de IAM restritivas para controlar quem pode excluir funções Lambda. Habilitar logs de auditoria com AWS CloudTrail e monitoramento com AWS Config para detectar atividades de exclusão. |

### Detalhes:

1. **Tática e Técnica MITRE ATT&CK**:
   - **Tática**: **Impact Execution**. A exclusão de funções Lambda pode comprometer a execução de aplicativos críticos ou serviços dependentes.
   - **Técnica/Subtécnica**: **T1565 - Data Destruction**. Remover diretamente código e configuração necessários para operação.

2. **Classificação de Risco**:
   - **Alto - Requer Controle**: A capacidade de deletar funções Lambda é um alvo significativo para um invasor buscando causar interrupções nas operações ou destruir dados críticos. A falta de função pode parar serviços instantaneamente.

3. **Recomendações de Segurança**:
   - **IAM Policies**: Aplicar o princípio do menor privilégio para garantir que apenas usuários e roles adequados possam executar esta ação.
   - **Auditoria e Monitoramento**: Utilize AWS CloudTrail para rastreamento de APIs e AWS Config para verificar conformidades.
   - **Práticas Adicionais**: Introduzir alertas através do AWS Security Hub quando funções críticas são alteradas ou excluídas.

## Action: GetFunction
Com base na ação IAM fornecida, vamos proceder com a modelagem de ameaças utilizando a metodologia MITRE ATT&CK.

### 🛡️ Modelagem de Ameaças: `GetFunction`

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `GetFunction` | RUN | Concede permissão para visualizar detalhes sobre uma função Lambda, incluindo configuração e referências de código, apoiando a execução da função. | Discovery | T1082 - System Information Discovery | **Médio** | **Melhor Prática** | A ação permite a descoberta e visualização de configurações que podem ser usadas por um atacante para planejamento de outras ações, mas não permite modificações diretas. | Restrição do acesso através de políticas IAM baseada no princípio do menor privilégio; monitoramento de logs com AWS CloudTrail; ativação do AWS Config para auditoria das configurações. |

### 🎯 Pontos Considerados
- **Tática e Técnica**: A ação é mapeada para a tática de **Discovery**, técnica **System Information Discovery (T1082)**, pois permite ao usuário obter informações sobre a configuração e o código de funções Lambda.
- **Classificação de Risco**: Classificado como **Médio**, já que o acesso à configuração pode informar um atacante sobre a arquitetura e apoiá-lo em estágios posteriores do ataque, mas não permite acesso direto aos dados ou execução de código malicioso.
- **Recomendações de Segurança**: Aplicação do princípio de menor privilégio para garantir que apenas usuários autorizados possam visualizar essas informações, juntamente com o monitoramento contínuo por ferramentas como AWS CloudTrail para auditoria e detecção de acesso não autorizado.

## Action: UpdateFunctionCode
### Segurança

- **MFA (Autenticação Multifator)** deve ser habilitado para todos os usuários com permissão de atualização de código.
- **Revisão Regular de Logs**: Configure o AWS CloudTrail para registrar e monitorar atividades de atualização de código, permitindo revisões periódicas.
- **Controle de Acesso Rigoroso**: Utilize políticas do IAM para garantir que apenas usuários ou roles específicas possam executar a ação `UpdateFunctionCode`.
- **Automatização de Alertas**: Configure alertas no AWS Security Hub e AWS GuardDuty para notificações em tempo real de atividades suspeitas relacionadas a atualizações de funções.

### Considerações Finais

Adotar uma abordagem de segurança em camadas pode ajudar a proteger contra possíveis riscos associados à ação `UpdateFunctionCode`. Manter as permissões estritamente necessárias e monitorar alterações são passos críticos na mitigação de riscos. Ao implementar essas recomendações, é possível reduzir significativamente a superfície de ataque potencial no ambiente AWS.
### Modelagem de Ameaças para a Ação IAM "UpdateFunctionCode"

| **AWS IAM Action**            | **BUILD/RUN** | **Descrição**                                                                                   | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                                                                         |
|-------------------------------|---------------|------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|--------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UpdateFunctionCode`          | BUILD         | Permite atualizar o código de uma função AWS Lambda, modificando sua lógica de execução.       | Execution                 | T1059 - Command and Scripting Interpreter | **Crítico**| **Requer Controle** | A ação pode ser explorada para introduzir códigos maliciosos que executem comandos não autorizados na infraestrutura. | Restringir a permissão de atualizar funções apenas para usuários e roles essenciais, implementar o princípio do menor privilégio, monitorar alterações de código através do AWS CloudTrail.                 |
| `UpdateFunctionCode`          | BUILD         | Permite atualizar o código de uma função AWS Lambda, modificando sua lógica de execução.       | Persistence               | T1078 - Valid Accounts               | **Alto**   | **Requer Controle** | A atualização de código pode ser utilizada para estabelecer persistência através da execução de payloads maliciosos. | Verificar alterações suspeitas no código da função, usar AWS Config para auditar e rastrear revisões de configuração, garantindo que acesso à atualização seja cuidadosamente controlado. |

### Justificativas Adicionais:
1. **Impacto na Confidencialidade**: Se explorada, pode comprometer dados processados pela função Lambda.
2. **Impacto na Integridade**: Código malicioso pode alterar o comportamento esperado das funções.
3. **Impacto na Disponibilidade**: Código novo pode interromper a operação normal das funções.

### Considerações de
