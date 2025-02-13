
## Action: AbortMultipartUpload
### 📊 Modelagem de Ameaças para Ação IAM: AbortMultipartUpload

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `AbortMultipartUpload` | BUILD | Aborta um upload multipart em curso, interrompendo a criação parcial de um objeto em um bucket do S3. | Impact Execution | T1565.003 - Data Manipulation: Disk Content Wipe | **Médio** | **Melhor Prática** | Apesar de não envolver a execução direta de código malicioso, o cancelamento de uploads pode ser usado para impedir a criação completa de arquivos importantes ou sincronizações, afetando potencialmente operações reativas. | Aplique o princípio do menor privilégio nas políticas IAM para limitar quem pode cancelar uploads, e utilize logs do AWS CloudTrail para monitorar abortos de upload. |

### 📝 Notas e Justificativas
- **Risco Médio**: A ação de abortar uploads multipart tem impacto moderado na integridade dos dados, uma vez que pode resultar na perda de dados parcialmente carregados se explorada indevidamente.
- **Mitigações Recomendas**: Monitorar o uso dessa ação é essencial para garantir que ela não está sendo utilizada para interromper uploads críticos de dados. Implementar práticas de logging e auditoria para ações em S3, além de garantir que apenas usuários ou roles específicas tenham esse nível de permissão.

## Action: CreateBucket
### Modelagem de Ameaças - Ação IAM: CreateBucket

A seguir, apresento a análise detalhada da ação **CreateBucket** no contexto do serviço **Amazon S3**, mapendo-a para táticas e técnicas do MITRE ATT&CK.

| **AWS IAM Action** | **BUILD/RUN** | **Descrição**                                        | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**   | **Justificativa da Classificação** | **Recomendações de Segurança**                                                                                                                                                           |
|--------------------|--------------|-----------------------------------------------------|---------------------------|--------------------------------------|-----------|---------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateBucket`     | BUILD        | Cria um novo bucket no Amazon S3.                   | Defense Evasion           | T1078 - Valid Accounts               | **Alto**  | **Requer Controle** | Criar buckets pode levar ao armazenamento não autorizado de dados, servindo como vetor para evasão ou ocultação de atividades maliciosas. | Restringir a criação de buckets através de IAM Policies, revisar regularmente as permissões, habilitar logs do S3 e monitorar atividades usando o AWS CloudTrail. Implementar o princípio do menor privilégio e, se aplicável, restringir as contas autorizadas para essa ação. |

### Considerações Adicionais
- **Impacto na Confidencialidade**: Buckets mal configurados ou não monitorados podem expor dados sensíveis.
- **Impacto na Integridade**: Dados armazenados podem ser modificados se o acesso não for adequadamente controlado.
- **Impacto na Disponibilidade**: Possível sequestro de buckets.
- **Conformidade**: Garantir que os controles SIG e LGPD sejam seguidos ajuda a manter a conformidade regulatória.
  
### Referências
- [MITRE ATT&CK - Valid Accounts](https://attack.mitre.org/techniques/T1078/)
- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

A abordagem aqui descrita visa não apenas classificar os riscos, mas também equipar as organizações com estratégias práticas para mitigação e monitoramento contínuo.

## Action: DeleteBucket
| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `DeleteBucket` | BUILD | Exclui um bucket no Amazon S3. | Impact | T1485 - Data Destruction | **Crítico** | **Requer Controle** | A exclusão de buckets pode resultar em perda permanente de dados críticos, impactando a disponibilidade e integridade do ambiente. | Implementar políticas de IAM rigorosas, restringindo quem pode excluir buckets. Configurar versionamento e MFA Delete no S3. Monitorar atividade usando AWS CloudTrail. |

### **Explicação Detalhada:**
- **Tática e Técnica (MITRE ATT&CK):** A ação de `DeleteBucket` está associada à tática de Impacto, especificamente a técnica T1485 - Data Destruction, uma vez que sua execução pode levar à destruição completa de dados armazenados no S3.
- **Classificação e Justificativa:** Classificada como Crítico, pois a ação de deletar um bucket pode resultar em perda irreversível de dados armazenados, que pode incluir informações sensíveis e impactar a operação do negócio.
- **Recomendações de Segurança:**
  - **Políticas IAM:** Aplicar políticas rigorosas de IAM que limitem a capacidade de excluir buckets a um conjunto mínimo e auditado de usuários.
  - **Versionamento e MFA Delete:** Habilitar o versionamento dos objetos dentro dos buckets e o recurso de MFA Delete para adicionar uma camada adicional de segurança.
  - **Monitoramento:** Utilizar o AWS CloudTrail para monitorar as chamadas de API relacionadas à exclusão de buckets, possibilitando alertas e auditoria.

## Action: GetObject
### Modelagem de Ameaças para Ação IAM: `GetObject`

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `GetObject` | RUN | Obtém um objeto de um bucket do Amazon S3. | Collection | T1537.002 - Transfer Data to Commonly Used Port | **Médio** | **Melhor Prática** | Essa ação é usada para acessar dados armazenados, podendo ser explorada em caso de credenciais comprometidas para extrair informações sensíveis. | Implementar controles de acesso e políticas de princípio de menor privilégio, auditar acessos e eventos com AWS CloudTrail, aplicar criptografia em repouso e em trânsito. |
| `GetObject` | RUN | Obtém um objeto de um bucket do Amazon S3. | Exfiltration | T1020.001 - Automated Exfiltration | **Alto** | **Requer Controle** | A ação pode ser explorada para exfiltrar grandes volumes de dados automaticamente, representando risco significativo de vazamento de informações. | Usar AWS Macie para identificar dados sensíveis e AWS GuardDuty para monitorar acessos incomuns ou não autorizados, ativar logging detalhado dos acessos ao S3. |

**Notas Adicionais:**
- A ação `GetObject` é muito comum em ambientes AWS para leitura de dados armazenados. A correta configuração de políticas de IAM e monitoramento contínuo são essenciais para mitigar possíveis riscos associados a acessos não autorizados.
- Considerar o uso de AWS Config para assegurar que as configurações do bucket do S3 estão alinhadas com as melhores práticas de segurança e conformidade.
- Aplique práticas de Zero Trust, limitando acessos apenas quando absolutamente necessário e sempre revendo permissões periodicamente.

## Action: ListBucket
### Modelagem de Ameaças AWS para Ação IAM: `ListBucket`

Com base na entrada fornecida, aqui está a análise detalhada usando o framework MITRE ATT&CK:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `ListBucket` | RUN | Lista alguns ou todos os objetos em um bucket do Amazon S3. | Discovery | T1530 - Data from Cloud Storage Object | **Médio** | **Melhor Prática** | A ação pode ser utilizada para descobrir dados sensíveis armazenados no S3, porém o impacto é limitado a descoberta e não inclui modificação ou acesso direto ao conteúdo. | Implementar políticas de IAM que restrinjam o acesso baseado no princípio do menor privilégio, ativar o logging de acesso aos buckets S3 com o AWS CloudTrail e utilizar o IAM Access Analyzer para monitoramento contínuo. |

### 🛡️ Recomendações Detalhadas de Segurança
- **Princípio do Menor Privilégio**: Garantir que apenas usuários e serviços que necessitem listar objetos em buckets S3 possuam essa permissão.
- **AWS CloudTrail**: Ativar o CloudTrail para monitorar e registrar solicitações de `ListBucket`, possibilitando a auditoria e resposta a atividade suspeita.
- **IAM Access Analyzer**: Utilizar para identificar permissões excessivas ou desnecessárias nos buckets.
- **Políticas de Bucket S3**: Implementar políticas de bucket restritivas que definam quem pode listar objetos e em quais circunstâncias isso é permitido.
- **MFA (Autenticação Multi-fator)**: Garantir que usuários com permissão para listar objetos tenham MFA habilitado para um acesso mais seguro.

Essas ações visam reduzir a superfície de ataque, aumentar a visibilidade sobre atividades e limitar as possibilidades de uso indevido.

## Action: PutObject
### Tabela de Modelagem de Ameaças para AWS IAM Action

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `PutObject` | BUILD | Adiciona um objeto a um bucket do Amazon S3. | Collection | T1537 - Data from Cloud Storage Object | **Alto** | **Requer Controle** | Ação pode ser explorada para persistir dados sensíveis ou maliciosos no ambiente, comprometendo a confidencialidade e integridade dos dados armazenados. | Implementar políticas de restrição de acesso por meio de IAM Policies e SCPs, utilizar encriptação de dados S3, habilitar logs de auditoria com AWS CloudTrail para monitoramento de acessos e atividades.|

| `PutObject` | BUILD | Adiciona um objeto a um bucket do Amazon S3. | Defense Evasion | T1562.001 - Impair Defenses: Disable or Modify Tools | **Médio** | **Melhor Prática** | Ação pode ser utilizada para substituir ou modificar arquivos e objetos críticos, ocultando a presença ou atividade de invasores. | Estabelecer regras rigorosas de IAM e políticas de bucket S3, além de monitoramento contínuo com AWS Security Hub e registros detalhados de acesso com AWS CloudTrail.|

🔹 Se necessário, ajuste as recomendações e classificações com base em políticas e requisitos específicos da sua organização, bem como na sensibilidade dos dados armazenados.

## Action: DeleteObject
### ⚔️ Modelagem de Ameaças - DeleteObject (AWS S3)

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|--------------------------|--------------------------------------|-----------|------------------|------------------------------------|-------------------------------|
| `DeleteObject` | BUILD | Remove a versão nula de um objeto e insere um marcador de exclusão, se tornando a versão atual. | Impacto | T1485 - Data Destruction | **Crítico** | **Requer Controle** | Ação permite exclusão de dados, potencialmente irrecuperável, afetando disponibilidade e integridade. | Implementar políticas de versão e retenção, habilitar MFA Delete em buckets S3, monitorar alterações com AWS CloudTrail, aplicar o princípio do menor privilégio.|

### **Detalhes da Análise**

1. **🕵️ Análise da Ação:**
   - A ação `DeleteObject` no Amazon S3 é crítica pois permite a remoção de objetos, afetando diretamente a disponibilidade e integridade dos dados armazenados.
   - Essencial em contextos onde a exclusão de dados pode levar à perda irreversível, tornando essenciais medidas de controle.

2. **🗺️ Mapeamento para MITRE ATT&CK:**
   - **Tática: Impacto** busca um efeito destrutivo ou desestabilizador.
   - **Técnica: T1485 - Data Destruction** indica o impacto de destruição de dados como parte de um ataque.

3. **🔍 Classificação de Risco:**
   - Avaliado como **Crítico**, pois a exclusão de objetos pode afetar severamente a operação ou a recuperação em um incidente.

4. **🔐 Recomendações de Segurança:**
   - **Políticas de Versão e Retenção:** Configurar buckets S3 para manter versões anteriores dos objetos, permitindo recuperação em caso de exclusão.
   - **MFA Delete:** Habilitar Multi-Factor Authentication (MFA) para operações de delete, adicionando uma camada extra de verificação.
   - **Monitoramento Contínuo:** Utilizar AWS CloudTrail para registrar e auditar atividades de exclusão, permitindo resposta rápida a atividades suspeitas.
   - **Princípio do Menor Privilégio:** Restringir permissões de exclusão apenas a usuários ou roles absolutamente necessários.

Esta análise garante uma abordagem abrangente para a mitigação de riscos associados à ação `DeleteObject` no AWS S3, alinhando-se às melhores práticas de segurança e referências do MITRE ATT&CK.

## Action: PutBucketVersioning
Para a ação IAM fornecida, aqui está a modelagem de ameaças detalhada:

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)**  | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                                                                                                            | **Recomendações de Segurança**                                                                                                                                                                                                       |
|------------------------|---------------|------------------------------------------------------------------------------|----------------------------|---------------------------------------|-----------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PutBucketVersioning`  | BUILD         | Define o estado de controle de versões de um bucket existente no Amazon S3.  | Defense Evasion            | T1070.004 - File Deletion             | **Alto**  | **Requer Controle** | Alterar o versionamento de um bucket pode ser usado para ocultar a exclusão de arquivos ou alterações indevidas, impedindo a recuperação de dados críticos.                                 | Monitorar e auditar alterações nas configurações de versionamento usando AWS CloudTrail; aplicar políticas rígidas de IAM para controlar quem pode modificar o versionamento; implementar o princípio do menor privilégio.               |

### **Detalhamento**
- **Tática e Técnica**: A ação `PutBucketVersioning` pode ser associada à tática de **Defense Evasion**, especificamente à técnica de **File Deletion** (T1070.004), pois alterar o versionamento de um bucket pode esconder exclusões ou modificações de arquivos.
- **Risco e Classificação**: Classificada como **Alto**, a ação deve ser controlada devido ao seu potencial de impactar a capacidade de recuperação de dados, caso o versionamento seja desativado.
- **Recomendações de Segurança**:
  - **Monitoramento**: Utilize o **AWS CloudTrail** para monitorar quaisquer alterações nas configurações de versionamento dos buckets do S3.
  - **Controle de Acesso**: Restringir essa ação a usuários e roles específicos, aplicando o princípio de **menor privilégio**.
  - **Alertas e Audito**rias: Configurar o **AWS Security Hub** para gerar alertas quando mudanças de versionamento ocorrerem.

## Action: RestoreObject
### 📊 Modelagem de Ameaças AWS para Ação IAM RestoreObject

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|----------------------|---------------|----------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `RestoreObject`      | BUILD         | Restaura uma cópia arquivada de um objeto de volta para o Amazon S3.       | Impacto                    | T1565.001 - Manipulation: Stored Data Manipulation | **Médio**  | Melhor Prática  | A restauração de objetos pode levar à exposição de dados antigos ou sensíveis que podem ser manipulados de forma inadequada. Conhecido principalmente por riscos associados a mudanças na integridade dos dados. | Implementar o princípio de menor privilégio para restaurar objetos. Monitorar logs de restauração com AWS CloudTrail. Configurar alertas no AWS Security Hub para atividades de restauração suspeitas. |

---

### 🌐 Contextualização Detalhada:

1. **Análise da Ação IAM:**
   - **Risco de Segurança:** Restaurar dados arquivados pode potencialmente permitir que dados desprotegidos sejam acessados indevidamente, ou dados manipulados sejam inadvertidamente recuperados e reintegrados aos sistemas.
   
2. **Mapeamento para MITRE ATT&CK:**
   - **Tática (Impacto)**: O adversário pode tentar causar dano à integridade dos dados restaurando versões anteriores modificadas ou comprometidas.

3. **Classificação de Risco:**
   - **Justificativa:** Classificação de risco Médio foi atribuída considerando que a ação de restaurar pode ser utilizada como parte de uma cadeia de ataque mais ampla, embora o próprio ato de restaurar não permita diretamente ações destrutivas sem limitações.
   
4. **Recomendações de Segurança:**
   - **Princípio do Menor Privilégio:** Restringir a capacidade de restaurar objetos apenas a usuários ou roles que realmente necessitam.
   - **Monitoramento Contínuo:** Usar AWS CloudTrail para monitorar e registrar todas as atividades de restauração para auditoria e resposta a incidentes.
   - **Alertas de Segurança:** Configurar o AWS Security Hub para identificar padrões suspeitos, permitindo uma resposta rápida a atividades anômalas.

---

🔍 **Notas Finais:**
Adaptações no ambiente AWS para maximizar a segurança devem ser feitas considerando o contexto operacional e as exigências legais, garantindo que controles monitorados estejam sempre em conformidade com políticas internas e externas vigentes.

## Action: GetBucketPolicy
### 📊 Modelagem de Ameaças para Ação IAM

Utilizando a ação IAM fornecida, segue a modelagem de ameaças com mapeamento para MITRE ATT&CK:

| **AWS IAM Action**      | **BUILD/RUN** | **Descrição**                                          | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco**   | **Classificação**   | **Justificativa da Classificação**                                                                              | **Recomendações de Segurança**                                                                                                                      |
|-------------------------|--------------|--------------------------------------------------------|---------------------------|---------------------------------------|-------------|---------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetBucketPolicy`       | RUN          | Retorna a política de um bucket específico.             | Discovery                 | T1007 - Application Window Discovery  | **Médio**   | **Melhor Prática**  | A ação permite que um usuário visualize a política de um bucket, potencialmente revelando configurações que podem ser exploradas. | Limitar quem pode visualizar políticas de buckets, usando IAM Policies e habilitar o logging e monitoramento com AWS CloudTrail.                           |

### 🛠️ Considerações Adicionais
- **Práticas de segurança**: Certifique-se de que o princípio do menor privilégio é seguido, garantindo que apenas usuários autorizados possam executar a ação `GetBucketPolicy`.
- **Monitoramento contínuo**: Utilize AWS Config ou AWS Security Hub para verificar configurações de política de bucket e detectar acessos não autorizados.
- **Detecção de anomalias**: Implemente monitoramento com AWS GuardDuty para identificar atividades suspeitas.

Essas medidas ajudarão a mitigar potenciais riscos associados à ação, protegendo informações sensíveis e garantindo conformidade com políticas de segurança.
