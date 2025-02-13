
## Action: InvalidateCache
Com base na ação IAM fornecida, aqui está a tabela de modelagem de ameaças refletindo a análise seguindo o framework MITRE ATT&CK:

| **AWS IAM Action**   | **BUILD/RUN** | **Descrição**                                                               | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                                                                         | **Recomendações de Segurança**                                                                                                                                                                                    |
|----------------------|---------------|-----------------------------------------------------------------------------|---------------------------|--------------------------------------|-----------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `InvalidateCache`    | RUN           | Usada para invalidar o cache da API mediante solicitação do cliente no Amazon API Gateway. | Impact Execution        | T1222 - File and Directory Permissions Modification | **Médio**   | **Melhor Prática**   | Invalidation do cache pode causar impactos momentâneos na performance ao sobrecarregar a API, mas é um cenário comum no uso legítimo. Não representa um risco direto de segurança quando utilizado de forma controlada. | Monitorar logs do API Gateway para identificar padrões anômalos de invalidações. Garantir que somente usuários ou sistemas autorizados possuam permissões adequadas para execução dessa ação. Implementar políticas de IAM restritivas. |

🔹 **Nota:** A técnica associada é um exemplo ilustrativo, considerando similaridades no impacto de execução de ações no ambiente AWS. A precisão pode variar dependendo dos cenários específicos de segurança.

## Action: Invoke
Para a ação IAM fornecida, aqui está a modelagem de ameaças associada com seus detalhamentos:

| **AWS IAM Action** | **BUILD/RUN** | **Descrição** | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação** | **Recomendações de Segurança** |
|--------------------|--------------|--------------|-------------------------|--------------------------------------|-----------|-----------------|------------------------------------|-------------------------------|
| `Invoke` | RUN | Usado para invocar uma API a pedido de clientes no Amazon API Gateway. | Execution | T1203 - Exploitation for Client Execution | **Alto** | **Requer Controle** | Esta ação pode ser usada para executar código malicioso se mal configurada ou se uma API vulnerável for exposta publicamente. | Implementar políticas de IAM restritivas, utilizar WAF para proteger APIs, monitorar logs de execução e padronizar o uso de TLS. |

### **Justificativa Detalhada**
A ação `Invoke` está associada à tática de Execução no MITRE ATT&CK, pois pode ser usada para executar operações através de APIs. O risco é considerado alto devido ao potencial de exploração, especialmente se as APIs não estiverem devidamente protegidas. Isso pode resultar em execução não autorizada de código, resultando em comprometimentos de segurança significativos.

### **Recomendações Adicionais**
- **Monitoramento Contínuo**: Utilize o AWS CloudTrail para acompanhar chamadas `Invoke`, assegurando que sejam provenientes de fontes legítimas.
- **Princípio do Menor Privilégio**: Configurar IAM Policies para garantir que apenas usuários e serviços autorizados possam fazer uso desta ação.
- **Multi-Factor Authentication (MFA)**: Implementar MFA para todas as contas que têm permissões para invocar APIs.
- **Auditoria Regular**: Realizar auditorias frequentes das configurações de API e revisar logs de acesso a fim de detectar atividades suspeitas.

## Action: ManageConnections
Com base nas informações fornecidas, apresento a análise detalhada da ação IAM `ManageConnections`:

---

### **Modelagem de Ameaças para AWS IAM: `ManageConnections`**

| **AWS IAM Action**     | **BUILD/RUN** | **Descrição**                                                                              | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação** | **Justificativa da Classificação**                                                                               | **Recomendações de Segurança**                                                                                                                                                                         |
|------------------------|--------------|-----------------------------------------------------------------------------------------|-------------------------------|------------------------------------------|-----------|-----------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ManageConnections`    | RUN          | Controla o acesso à API @connections para gerenciar conexões WebSocket no Amazon API Gateway. | Collection                    | T1029 - Data Staged                      | **Médio** | **Melhor Prática** | A ação pode ser explorada para capturar, modificar ou interromper o tráfego de WebSocket se não for adequadamente controlada. | Implementar o princípio do menor privilégio, restringindo o uso da ação em políticas IAM. Monitorar e registrar atividades usando AWS CloudTrail e AWS Config. Utilizar o AWS Shield para proteção contra DDoS. |

---

### **Explicação Detalhada**
- **Tática e Técnica Associada**: A ação `ManageConnections` é mapeada para a tática de **Collection** e técnica **T1029 - Data Staged**. Essa técnica pode envolver a manipulação de dados através de WebSockets, estando vulnerável a interceptações e alterações de tráfego, caso as políticas de acesso não sejam rigorosas.
  
- **Justificativa do Risco**: Considerando que a ação se aplica ao gerenciamento de conexões de WebSocket, o risco é classificado como **Médio**. Isso se deve à possibilidade de interceptação ou manipulação do tráfego de dados, afetando a integridade e potencialmente a confidencialidade das informações.

- **Recomendações de Segurança**: 
  - **Princípio do Menor Privilégio**: Limitar os acessos às APIs apenas para os usuários e serviços estritamente necessários, minimizando a superfície de ataque.
  - **Monitoramento Contínuo**: Usar AWS CloudTrail para registrar e monitorar todas as alterações e tentativas de acesso à API. AWS Config pode ajudar a garantir que a configuração não se desvie das práticas de segurança definidas.
  - **Proteções Adicionais**: Considerar o uso do AWS Shield para proteger os WebSockets contra ataques de negação de serviço (DDoS).

Essas medidas visam proteger contra o uso indevido e garantir que quaisquer anomalias possam ser detectadas rapidamente.
