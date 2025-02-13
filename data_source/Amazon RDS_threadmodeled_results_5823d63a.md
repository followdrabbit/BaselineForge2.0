
## Action: AddRoleToDBCluster
### 🔍 Tabela de Modelagem de Ameaças AWS IAM

| **AWS IAM Action**          | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                         | **Recomendações de Segurança**                                                                                               |
|-----------------------------|---------------|-------------------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|----------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `AddRoleToDBCluster`        | BUILD         | Concede permissão para associar uma função IAM a um cluster Aurora DB.         | Persistence               | T1078 - Valid Accounts                 | Alto      | Requer Controle      | A ação permite a alteração de permissões, potencialmente abusando de funções IAM para manter persistência ou modificar dados. | Limitar uso da ação a administradores, auditar associações de funções a clusters DB e revisar permissões conforme necessário. |

### 🛡️ Detalhes das Recomendações de Segurança

- **Monitoramento e Auditoria**: Utilize **AWS CloudTrail** para monitorar atividades dessa ação. Configure alertas em caso de adições inesperadas de funções a clusters de banco de dados.
- **Regras IAM Rigorosas**: Implemente **Policies IAM** para restringir essa ação apenas a usuários confiáveis.
- **Princípio do Menor Privilégio**: Garanta que privilégios mínimos necessários sejam concedidos.
- **Segregação de Funções**: Limitar a associação de papéis apenas a administradores, separando funções de usuários regulares de DBA.
- **Monitoramento Contínuo**: Habilite o uso do **AWS Security Hub** e **AWS GuardDuty** para notificações em tempo real de atividades suspeitas em clusters JDBC.
- **Revisões Periódicas**: Realize auditorias regulares nas permissões de IAM associadas a clusters Aurora para garantir conformidade contínua.

Estas medidas ajudam a mitigar riscos associados ao uso indevido da ação, garantindo a segurança e a integridade dos dados no ambiente AWS.

## Action: AddRoleToDBInstance
### 📊 Tabela de Modelagem de Ameaças para a Ação IAM

| **AWS IAM Action**  | **BUILD/RUN** | **Descrição**                                                                                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                                                                                    | **Recomendações de Segurança**                                                                                                                                                                     |
|---------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AddRoleToDBInstance` | BUILD        | Concede permissão para associar uma função do IAM a uma instância de banco de dados.                                                         | Privilege Escalation      | T1078 - Valid Accounts              | **Alto**  | **Requer Controle** | Ação pode ser explorada para conceder permissões elevadas por meio do IAM, comprometendo potencialmente a integridade e a confidencialidade dos dados no banco de dados.              | Restringir o uso dessa ação a contas e papéis específicos, monitorar alterações em associações de funções com instâncias de banco de dados usando o AWS CloudTrail, e aplicar o princípio do menor privilégio.                           |

### 🚩 Justificativa da Classificação
- **Privilege Escalation (T1078 - Valid Accounts)**: A associar essa ação a um papel IAM pode permitir que um atacante escale privilégios dentro do ambiente, obtendo acesso indevido a recursos sensíveis.
- **Impacto na Confidencialidade e Integridade**: Se explorada, essa ação pode comprometer dados sensíveis configurados na instância de banco de dados.

### 🛡️ Recomendações de Segurança
1. **Restringir Acesso**: Use políticas IAM rigorosas para garantir que apenas usuários ou grupos específicos tenham permissão para executar essa ação.
2. **Monitoramento Contínuo**: Utilize AWS CloudTrail para auditar alterações na associação de papéis às instâncias de banco de dados. Assim, desvios podem ser detectados rapidamente.
3. **Princípio de Menor Privilégio**: Sempre aplique o menor conjunto de permissões necessário para realizar tarefas específicas.
4. **Revisão Periódica**: Realize revisões periódicas das permissões IAM para identificar e corrigir permissões desnecessárias ou excessivas.

## Action: AddSourceIdentifierToSubscription
```markdown
| **AWS IAM Action**                        | **BUILD/RUN** | **Descrição**                                                                                      | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                               | **Recomendações de Segurança**                                                                                                      |
|-------------------------------------------|---------------|----------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------|-----------|------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `AddSourceIdentifierToSubscription`       | RUN           | Concede permissão para adicionar um identificador de origem a uma assinatura de notificação de eventos do RDS existente. | Collection                 | T1114 - Email Collection              | **Médio**  | **Melhor Prática**     | Essa ação tem impacto potencial na integridade dos dados de notificação, mas é pouco explorável diretamente. | Monitorar a alteração de assinaturas de notificação no RDS, aplicar o princípio do menor privilégio para uso dessa ação. |
```

**Notas**:
- **Tática e Técnica**: A ação foi mapeada sob a tática "Collection", técnica "Email Collection" (T1114), pois envolve a modificação de notificações que podem afetar a forma como os dados são coletados ou recebidos.
- **Classificação de Risco**: A ação tem um risco considerado médio, já que a sua exploração direta é limitada, mas pode afetar a integridade dos dados de notificação, alterando a composição das notificações recebidas.
- **Recomendações de Segurança**: Importante monitorar alterações em assinaturas de notificação, e garantir que apenas usuários com real necessidade de executar essa ação tenham permissões adequadas, seguindo o princípio do menor privilégio.

## Action: AddTagsToResource
### 🛡️ Modelagem de Ameaças para Ação IAM: AddTagsToResource

Abaixo está a tabela de modelagem de ameaças baseada nos dados fornecidos:

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                                                         | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                   |
|----------------------|---------------|-----------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|--------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `AddTagsToResource`  | RUN           | Concede permissão para adicionar tags de meta-dados a um recurso RDS. | Defense Evasion           | T1070.004 - Indicator Removal on Host  | Médio     | Melhor Prática      | Poderia ser explorada para alterar tags de recursos para ocultar atividades maliciosas ou enganar auditorias. | Implementar monitoramento contínuo com AWS CloudTrail para detecção de alterações em tags, usar políticas IAM para restringir ações de tag a usuários autorizados, aplicar monitoramento de conformidade com AWS Config. |

### 📝 Detalhes da Análise

- **Análise do Risco:** A capacidade de modificar tags pode ser usada de forma maliciosa para desviar auditorias ou ofuscar operações não autorizadas, alterando atributos que poderiam ser utilizados para rastreamento ou categorização de recursos.
- **Impacto em Confidencialidade, Integridade e Disponibilidade:** Principalmente um impacto na integridade, pois permite alterar metadados que podem ser críticos para identificação e gerenciamento de recursos.
- **Mitigação Recomendável:** Embora não seja considerada crítica, recomenda-se restrições e monitoramento para garantir a legitimidade das mudanças feitas.

Esta modelagem destaca como ações aparentemente benignas podem, em certas circunstâncias, ser usadas de forma nefasta e a importância de controles e monitoramentos adequados.

## Action: ApplyPendingMaintenanceAction
### Modelagem de Ameaças para Ação IAM: `ApplyPendingMaintenanceAction`

| **AWS IAM Action**                   | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                   | **Recomendações de Segurança**                                                                                                                                                 |
|--------------------------------------|--------------|------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ApplyPendingMaintenanceAction`      | BUILD         | Concede permissão para aplicar uma ação de manutenção pendente a um recurso. | Impact on Availability    | T1499.003 - Service Exhaustion Flood  | **Médio** | **Melhor Prática**  | Aplicar atualizações de manutenção pode ser interrompido por ataque, afetando a disponibilidade de recursos críticos. | Configurar AWS Config para monitorar alterações na configuração dos recursos, usar MFA e seguir o princípio do menor privilégio ao conceder permissões.                                                                  |

#### 🔍 Detalhes da Avaliação:

- **Tática**: A ação está associada à tática de impacto na disponibilidade, considerando que a manutenção pendente pode ser crítica e, se mal utilizada, pode levar a uma interrupção de serviço.
- **Risco**: Avaliado como médio porque, embora importante para a disponibilidade de serviços, é menos provável que seja explorado maliciosamente em comparação com outras ações de configuração.
- **Recomendações de Segurança**: Incluem o uso de AWS Config para monitoramento, a aplicação do princípio de menor privilégio e a exigência de autenticação multifator (MFA) para executar a ação.

Essa avaliação considera o ambiente regulatório exigente e reforça estratégias de zero trust como parte das práticas recomendadas de segurança.

## Action: AuthorizeDBSecurityGroupIngress
### 🛡️ Modelagem de Ameaças para Ação IAM: `AuthorizeDBSecurityGroupIngress`

| **AWS IAM Action**               | **BUILD/RUN** | **Descrição**                                                                                                                                                                      | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                             | **Recomendações de Segurança**                                                                                                                                                                             |
|----------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AuthorizeDBSecurityGroupIngress` | BUILD         | Concede permissão para habilitar ingressos a um DBSecurityGroup usando uma das duas formas de autorização.                                                                           | Defense Evasion           | T1562 - Impair Defenses             | **Alto** | **Requer Controle** | Essa ação pode ser utilizada para modificar regras de entrada em um grupo de segurança do banco de dados, o que pode levar à exposição indevida e potencial comprometimento de dados sensíveis. | Implementar políticas de controle estritas usando IAM, limitar quem pode autorizar ingressos a grupos de segurança, usar o princípio do menor privilégio. Monitorar alterações em grupos de segurança com AWS CloudTrail e AWS Config. |

### Detalhes e Justificativas

1. **Impacto e Exploração**: A capacidade de modificar regras de entrada em grupos de segurança de banco de dados pode expor o sistema a riscos significativos, incluindo a possibilidade de invasão de sistemas externos maliciosos.

2. **Contexto de Segurança**: No contexto da segurança, especialmente em setores como o financeiro, é crucial assegurar que apenas usuários autorizados possam alterar configurações críticas de segurança como essas.

3. **Detecção e Mitigação**: É possível monitorar essa ação usando serviços como AWS CloudTrail, que pode capturar e registrar chamadas de API para investigar atividades suspeitas. Além disso, AWS Config pode ajudar a garantir que a configuração dos grupos de segurança permaneça conforme o esperado.

4. **Conformidade e Regulações**: Alterações não autorizadas em grupos de segurança podem violar políticas de conformidade, como ISO 27001 e PCI-DSS, que exigem proteção rigorosa para dados sensíveis.

---

Essa tabela fornece uma análise estruturada e proativa das potenciais ameaças associadas à ação `AuthorizeDBSecurityGroupIngress`. Certifique-se de que as políticas de segurança e controles de acesso dentro do seu ambiente AWS sejam rigorosamente implementados e monitorados continuamente.

## Action: BacktrackDBCluster
### Modelagem de Ameaças para Ação IAM: BacktrackDBCluster

| **AWS IAM Action**    | **BUILD/RUN** | **Descrição**                                                                                   | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)**       | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                     | **Recomendações de Segurança**                                                                                       |
|-----------------------|--------------|---------------------------------------------------------------------------------------------|---------------------------|--------------------------------------------|-----------|---------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `BacktrackDBCluster` | BUILD        | Concede permissão para retroceder um cluster de banco de dados a um momento específico, sem criar um novo cluster de banco de dados. | Impact on Availability    | T1499 - Endpoint Denial of Service   | Alto     | **Requer Controle** | Essa ação pode ser usada para alterar o estado de um banco de dados crítico, potencialmente impactando a disponibilidade dos dados.  | Monitorar todas as operações de retrocesso, restringir uso através de políticas IAM detalhadas, habilitar auditoria detalhada via AWS CloudTrail. |

---

### Detalhes da Análise

#### 🔍 **Análise da Ação IAM**
- **Potencial de Exploração:** Ação que pode comprometer a integridade e disponibilidade ao retroceder dados críticos a um estado anterior.
- **Impactos Possíveis:** Risco de perda de integridade e/ou disponibilidade de informações críticas, se retrocedidas a um estado indesejado.

#### 🎯 **Mapeamento para MITRE ATT&CK**
- **Tática:** Impacto na Disponibilidade (Impact on Availability).
- **Técnica Relacionada:** Endpoint Denial of Service (T1499), que reflete interrupções planejadas ou realizadas no estado do sistema.

#### ⚠️ **Classificação de Risco**
- **Impacto:** Alto impacto na disponibilidade e integridade dos dados.
- **Mitigação:** Rigoroso controle de acesso e monitoramento das atividades relacionadas.

#### 🛡️ **Recomendações de Segurança**
1. **Controle de Acesso:** Implementar políticas de IAM baseadas no princípio de privilégios mínimos.
2. **Auditoria e Monitoramento:** Ativar o AWS CloudTrail para registrar e revisar todas as ações de retrocesso realizadas.
3. **Alertas de Segurança:** Configurar alertas para operações de retrocesso de DB clusters, utilizando AWS Security Hub.
4. **Práticas de Configuração Segura:** Validar que retrocessos não possam ser realizados sem aprovações adequadas em ambientes de produção.

Essas recomendações são alinhadas com a estratégia de segurança e requisitos regulatórios específicos do setor, garantindo proteção adequada dos ativos de dados.

## Action: CancelExportTask
### **Modelagem de Ameaças para Ação IAM: `CancelExportTask`**

| **AWS IAM Action**        | **BUILD/RUN** | **Descrição**                                                            | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                             | **Recomendações de Segurança**                                                                                                                                               |
|---------------------------|--------------|--------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CancelExportTask`        | RUN          | Grants permission to cancel an export task in progress.                  | Impact                    | T1485 - Data Destruction              | **Médio**  | **Melhor Prática** | Cancelar tarefas de exportação que podem ser críticas para operações. A exploração poderia comprometer a integridade dos dados ou atrasar operações.                         | Implantar controle de acesso rigoroso com políticas IAM para restringir permissões de cancelamento a usuários e funções específicas. Monitorar logs de CloudTrail para ações de cancelamento.                       |

🔍 **Análise Complementar:**
- **Contexto do Uso:** Essa ação está associada à execução de tarefas e tem o potencial de interromper a continuidade das operações se abusada.
- **Impacto no Ambiente:** Embora a ação por si só não destrua dados, ela pode impedir que dados importantes sejam exportados, causando interrupções operacionais.
- **Regulamentação e Compliance:** Especialmente importante para setores que dependem da integridade dos dados exportados, como o financeiro.

🔒 Ao seguir estas recomendações, você ajuda a minimizar os riscos associados ao uso da ação `CancelExportTask`, garantindo um controle mais eficaz dentro do ambiente AWS.

## Action: CopyCustomDBEngineVersion
### Modelagem de Ameaças para Ação IAM: `CopyCustomDBEngineVersion`

| **AWS IAM Action**                | **BUILD/RUN** | **Descrição**                                                | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                          | **Recomendações de Segurança**                                                                                                                               |
|-----------------------------------|---------------|--------------------------------------------------------------|---------------------------|---------------------------------------|-----------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CopyCustomDBEngineVersion`       | BUILD         | Concede permissão para copiar uma versão personalizada de mecanismo de banco de dados. | Persistence               | T1525 - Implantação de Ferramentas Personalizadas | **Médio**  | **Melhor Prática** | Essa ação pode ser utilizada para copiar versões de mecanismos de banco de dados que tenham configurações ou ferramentas maliciosas embutidas, comprometendo a integridade do sistema. | Restringir o uso dessa ação a usuários específicos através de políticas IAM baseadas no menor privilégio. Monitorar logs de atividade usando o AWS CloudTrail para detectar ações suspeitas. |

### Considerações

1. **Análise do Risco**:
   - A ação em si não resulta diretamente em uma violação de segurança imediata, mas pode ser usada de maneira inadvertida para introduzir customizações maliciosas.
   - A probabilidade de uso malicioso aumenta se não houver controle de acesso adequado.

2. **Estratégia de Mitigação**:
   - **IAM Policies** devem ser configuradas para garantir que apenas usuários autorizados possam efetuar cópias de versões personalizadas.
   - Habilitar e revisar as auditorias do **AWS CloudTrail** para identificar o uso irregular dessa ação.
   - Implementar o **princípio do menor privilégio**, assegurando que os usuários só tenham permissões essenciais para suas funções.

3. **Contexto do Cliente**:
   - Considerar incluir controles adicionais se operar em setores altamente regulamentados onde a integridade dos dados é crítica.
   - Reforçar a conformidade com as regulamentações financeiras adequadas, como LGPD, PCI-DSS e ISO 27001.

## Action: CopyDBClusterParameterGroup
### **📋 Tabela de Modelagem de Ameaças**

| **AWS IAM Action**                  | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                           | **Recomendações de Segurança**                                                                                                                                                  |
|-------------------------------------|---------------|-------------------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `CopyDBClusterParameterGroup`       | BUILD         | Concede permissão para copiar o grupo de parâmetros de um cluster de banco de dados específico. | Persistence                | T1098 - Account Manipulation           | **Médio** | **Melhor Prática** | Copiar um grupo de parâmetros pode ser potencialmente explorado para modificar parâmetros críticos que impactam o comportamento do banco de dados, afetando sua integridade. | Implementar políticas IAM rigorosas para controlar quem pode modificar grupos de parâmetros. Monitorar o uso dessa ação por meio de AWS CloudTrail para detecção de alterações não autorizadas. |

### **🔍 Análise Adicional**

- **Impacto na Segurança**: Embora a ação seja classificada como de construção (BUILD) e não afete diretamente os dados, ela tem potencial para afetar a **integridade e disponibilidade** do banco de dados ao alterar o comportamento por meio de parâmetros copiados.
- **Probabilidade de Exploração**: Moderada, pois requer acesso IAM adequado. Contudo, se explorada, pode ser usada para alterar configurações críticas.
- **Mitigação**: Uso de **políticas IAM** restritivas e **monitoramento** para evitar modificações não autorizadas e garantir que alterações no ambiente sejam realizadas de acordo com as práticas de segurança estabelecidas.

## Action: CopyDBClusterSnapshot
### **📊 Tabela de Modelagem de Ameaças para a Ação IAM `CopyDBClusterSnapshot`**

| **AWS IAM Action**       | **BUILD/RUN** | **Descrição**                                                            | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco**   | **Classificação**   | **Justificativa da Classificação**                                                                                                                                          | **Recomendações de Segurança**                                                                                                                                                                       |
|--------------------------|---------------|--------------------------------------------------------------------------|---------------------------|----------------------------------------|-------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CopyDBClusterSnapshot`  | BUILD         | Permissão para criar uma cópia de um snapshot de um cluster de banco de dados. | Exfiltration               | T1029 - Data Encrypted                 | **Alto**    | **Requer Controle** | A possibilidade de copiar um snapshot de um banco de dados pode levar à exfiltração de dados sensíveis, permitindo que dados críticos sejam transferidos para ambientes não monitorados. | Restringir permissões para usuários estritamente necessários, usar políticas IAM detalhadas. Implementar criptografia nos snapshots, aplicar monitoramento contínuo com AWS CloudTrail e AWS Config. |

### **🔍 Análise Adicional**
- **Impacto na Confidencialidade**: Dados sensíveis podem ser copiados e acessados por usuários não autorizados.
- **Impacto na Integridade**: Potencial para modificar ou expor dados durante a transferência.
- **Impacto na Disponibilidade**: A operação não impacta diretamente a disponibilidade, mas pode expor dados críticos.

- **Probabilidade de Exploração**: Alta, especialmente em ambientes com permissões mal configuradas.
- **Possibilidade de Detecção**: Boa se forem implementados monitoramentos e alertas adequados.

### **📌 Considerações Regulatórias**
- **LGPD/ISO 27001**: A transferência de dados sensíveis precisa de controle rigoroso para proteger a privacidade e a confidencialidade.
- **Zero Trust**: Aplique o princípio do menor privilégio e revise regularmente as permissões de IAM.

A ação `CopyDBClusterSnapshot` requer controle efetivo para evitar riscos de segurança significativos, garantindo que apenas usuários autorizados possuam tal permissão.

## Action: CopyDBParameterGroup
### 📊 Tabela de Modelagem de Ameaças

| **AWS IAM Action**         | **BUILD/RUN** | **Descrição**                                                   | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação**                                                                                             | **Recomendações de Segurança**                                                                                                 |
|----------------------------|---------------|-----------------------------------------------------------------|---------------------------|---------------------------------------|-----------|---------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `CopyDBParameterGroup`     | BUILD         | Concede permissão para copiar o grupo de parâmetros DB especificado. | Credential Access         | T1078 - Valid Accounts                | Médio     | Melhor Prática      | A ação pode ser usada para replicar configurações sensíveis do banco de dados, potencialmente expondo segredos ou credenciais.| Utilizar políticas IAM restritas. Habilitar logging com AWS CloudTrail para monitorar atividades de cópia de parâmetros. Aplicar o princípio do menor privilégio. |

---

### 🔧 Justificativa da Análise

- **Análise da Ação**: A ação `CopyDBParameterGroup` permite a cópia de configurações de bancos de dados, que podem incluir parâmetros críticos relacionados à segurança e performance. Em mãos erradas, isso pode levar a uma exploração indevida dos recursos configurados ou exposição de informações sensíveis.
  
- **Mapeamento MITRE ATT&CK**: Associada à tática de **Credential Access**, pois a cópia de grupos de parâmetros pode ser explorada para acesso não autorizado ou para ajuste de configurações que comprometam a segurança. A técnica relacionada é **T1078 - Valid Accounts**, devido ao potencial de uso inadequado das credenciais permitidas.
  
- **Classificação de Risco**: Avaliado como **Médio**, uma vez que a ação em si não compromete diretamente a segurança do banco de dados, mas cria uma possibilidade para mau uso se as informações copiadas forem sensíveis.
  
- **Recomendações de Segurança**: É crucial aplicar políticas de IAM restritivas, garantindo que somente usuários e roles absolutamente necessárias tenham essa permissão. A implementação de logging com AWS CloudTrail ajudará a auditar e revisar o uso dessas permissões, enquanto o princípio do menor privilégio deve ser respeitado para minimizar as chances de acesso indevido.

## Action: CopyDBSnapshot
### 📊 Tabela de Modelagem de Ameaças para Ação IAM: `CopyDBSnapshot`

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `CopyDBSnapshot` | BUILD | Concede permissão para copiar o snapshot de um banco de dados específico. | Exfiltration | T1020 - Automated Exfiltration | **Alto** | **Requer Controle** | A ação pode ser explorada para copiar dados sensíveis do banco de dados para uma localização fora do controle direto, facilitando a exfiltração de dados confidenciais. | Implementar IA Policies restritivas, registrar atividades com AWS CloudTrail e habilitar AWS Config para monitorar alterações em snapshots. |
| `CopyDBSnapshot` | BUILD | Concede permissão para copiar o snapshot de um banco de dados específico. | Defense Evasion | T1562.001 - Impair Defenses: Disable or Modify Tools | **Alto** | **Requer Controle** | Copiar snapshots pode ser parte de uma estratégia para modificar ou desativar defesas analíticas ao criar um estado persistente não detectado. | Aplicar políticas de acesso baseadas em tags, habilitar MFA e revisar regularmente permissões de cópia de snapshot. |

### 🛡️ Recomendações de Segurança Detalhadas
- **IAM Policies**: Limitar a capacidade de executar `CopyDBSnapshot` apenas aos usuários e serviços que realmente necessitam. Use condições em políticas para incluir restrições baseadas em hora e endereço IP.
- **AWS CloudTrail**: Ativar o registro de atividades de `CopyDBSnapshot`, garantindo que todas as cópias de snapshots sejam devidamente monitoradas e auditadas.
- **AWS Config**: Configurar para verificar conformidade continuamente, assegurando-se de que as cópias de snapshots estejam em linha com as políticas de segurança estabelecidas.
- **Multi-Factor Authentication (MFA)**: Exigir MFA para qualquer usuário que possa realizar operações críticas ou sensíveis ao executar `CopyDBSnapshot`.
- **Princípio do Menor Privilégio**: Revisar regularmente as permissões para assegurar que apenas os direitos necessários sejam concedidos.
- **AWS GuardDuty**: Utilizar para identificar comportamentos anômalos e possíveis tentativas de exfiltração, resultando de ações como `CopyDBSnapshot`.

Essas medidas não só reforçam a segurança, mas também garantem a conformidade com normas e regulamentos relevantes, protegendo contra riscos potenciais associados a essas ações IAM.

## Action: CopyOptionGroup
### 📋 Modelagem de Ameaças: Ação AWS IAM "CopyOptionGroup"

#### **Tabela de Modelagem de Ameaças**

| **AWS IAM Action**  | **BUILD/RUN** | **Descrição**                                                | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**  | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                     |
|---------------------|--------------|-------------------------------------------------------------|---------------------------|--------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `CopyOptionGroup`   | BUILD        | Concede permissão para copiar o grupo de opções especificado. | Persistence               | T1500 - Compromise Client Software Binary | **Médio** | **Melhor Prática** | Essa ação permite a duplicação de configurações de banco de dados, o que pode ser explorado para manter acesso persistente ou fazer alterações maliciosas. | Implementar monitoramento via CloudTrail para detectar cópias não autorizadas; aplicar o princípio do menor privilégio nas políticas IAM. |

#### **Análise e Contexto Adicional**
- **Contexto do Cliente**: Dado o setor financeiro, é essencial garantir que cópias de configuração de grupos de opções sejam feitas exclusivamente por administradores com uma justificativa clara, devido ao potencial de modificação de ambientes que suportam operações críticas.
- **Zero Trust**: A aplicação desse modelo sugere a revisão constante de permissões associadas a essas ações, garantindo que somente serviços e usuários autenticados e autorizados possam realizar tais operações.

#### **Justificativa para Classificação**
A ação "CopyOptionGroup" não impacta diretamente a confidencialidade, integridade ou disponibilidade de maneira crítica, mas a capacidade de duplicar configurações pode facilitar a persistência de um agente malicioso no ambiente se não monitorado adequadamente. A aplicação de melhores práticas contribui para mitigar riscos associados a alterações não autorizadas.

## Action: CreateBlueGreenDeployment
### Modelagem de Ameaças para `CreateBlueGreenDeployment`

| **AWS IAM Action**            | **BUILD/RUN** | **Descrição**                                                                        | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**      | **Justificativa da Classificação**                                                                 | **Recomendações de Segurança**                                                                                   |
|-------------------------------|---------------|-------------------------------------------------------------------------------------|---------------------------|---------------------------------------|-----------|------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `CreateBlueGreenDeployment`   | BUILD         | Concede permissão para criar uma implantação blue-green para um cluster ou instância. | Persistence               | T1090 - Connection Proxy              | **Alto**   | **Requer Controle**    | A criação de implantações pode ser explorada para desviar o tráfego de rede ou injetar código malicioso. | Restringir permissões de criação de implantações a usuários confiáveis. Monitorar mudanças e atividade de implantações. Usar SCPs para limitar usos. |

### Explicação

1. **Análise da Ação IAM**: 
   - A ação `CreateBlueGreenDeployment` envolve a capacidade de criar implantações blue-green, que, se mal configuradas ou maliciosamente manipuladas, podem redirecionar ou alterar os fluxos de tráfego e dados para diferentes ambientes.
   
2. **Mapeamento para MITRE ATT&CK**: 
   - A tática identificada é **Persistence**, considerando que uma implantação pode manter acesso contínuo ou mascarar atividades maliciosas.
   - A técnica identificada é **T1090 - Connection Proxy**, que permite ao adversário redirecionar o tráfego através de implantações maliciosas.

3. **Classificação de Risco e Justificativa**:
   - **Risco Alto** se justifica pela capacidade de potencialmente comprometer a integridade e a política de segurança dos dados, facilitando ataques subsequentes.

4. **Recomendações de Segurança**:
   - Restringir a ação de criação dessas implantações a um conjunto mínimo de usuários altamente confiáveis.
   - Implementar políticas de controle de serviço (SCPs) para garantir que apenas entidades devidamente autorizadas possam executar tais ações.
   - Monitorar ativamente a criação e as alterações em implantações blue-green usando AWS CloudTrail e alertas de segurança proativos como AWS GuardDuty.
