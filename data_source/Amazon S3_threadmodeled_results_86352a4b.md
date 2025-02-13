
## Action: CreateAccessGrant
Aqui está a tabela de modelagem de ameaças para a ação IAM fornecida:

| **AWS IAM Action**    | **BUILD/RUN** | **Descrição**                                                                 | **Tática (MITRE ATT&CK)** | **Técnica/Subtécnica (MITRE ATT&CK)** | **Risco** | **Classificação**    | **Justificativa da Classificação**                                                                                                          | **Recomendações de Segurança**                                                                                                                                   |
|-----------------------|---------------|-------------------------------------------------------------------------------|---------------------------|----------------------------------------|-----------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CreateAccessGrant`   | BUILD         | Concede permissão para criar uma concessão de acesso, tipicamente usada para configurar novas permissões e recursos. | Privilege Escalation      | T1068 - Exploit Elevation of Privilege | **Crítico** | **Requer Controle**  | A ação pode ser usada maliciosamente para escalar privilégios, criando acessos que não deveriam ser permitidos. | Implementar políticas de menor privilégio, monitorar e auditar concessões de acesso criadas, utilizar AWS IAM Access Analyzer e registar logs com AWS CloudTrail. |

### **Recomendações de Mitigação**
1. **Políticas de Menor Privilégio**: Garanta que somente usuários ou entidades que realmente precisem dessa permissão a possuam.
2. **Monitoramento e Auditoria**: Utilize o AWS CloudTrail para monitorar a criação de concessões de acesso em busca de atividades suspeitas.
3. **IAM Access Analyzer**: Use esta ferramenta para verificar e analisar os usos de concessões de acesso, garantindo que não haja excessos de permissão.
4. **Revisões Regulares**: Realize revisões periódicas das políticas IAM e das concessões de acesso para identificar e corrigir permissões desnecessárias ou excessivas.
