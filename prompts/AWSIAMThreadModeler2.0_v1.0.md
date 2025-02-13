Dado um conjunto de ações do AWS IAM para um determinado serviço, fornecido no formato de tabela Markdown com as seguintes colunas:
- **Action IAM**: Nome da ação do IAM.
- **BUILD**: Indica se a ação é usada para configuração ou gerenciamento do serviço (✅ se aplicável).
- **RUN**: Indica se a ação é usada para execução ou operação do serviço (✅ se aplicável).
- **Descrição**: Explicação breve da funcionalidade da ação.

Seu objetivo é gerar uma tabela de modelagem de ameaças para essas ações, seguindo o modelo abaixo:

| Action IAM                | Categoria STRIDE  | Risco Potencial | Impacto | Mitigações |
|---------------------------|------------------|-----------------|---------|------------|
| `NomeDaAção`              | [Spoofing/Tampering/Repudiation/Information Disclosure/Denial of Service/Elevation of Privilege] | [Breve descrição do risco associado à ação] | [Impacto esperado] | [Mitigações possíveis] |

**Diretrizes para a modelagem de ameaças:**
1. **Identifique a categoria STRIDE** correspondente à ação do IAM:
   - **Spoofing**: Se a ação pode ser usada para falsificação de identidade.
   - **Tampering**: Se a ação pode modificar dados de forma não autorizada.
   - **Repudiation**: Se a ação pode dificultar a rastreabilidade de atividades.
   - **Information Disclosure**: Se a ação pode expor informações sensíveis.
   - **Denial of Service**: Se a ação pode ser usada para interromper serviços.
   - **Elevation of Privilege**: Se a ação pode conceder permissões indevidas.

2. **Determine o risco potencial** com base na função da ação IAM. Por exemplo:
   - `DeleteIdentityPolicy` pode causar **Information Disclosure** se permitir a remoção de políticas de acesso, expondo recursos indevidamente.
   - `SendRawEmail` pode ser explorada para **Spoofing**, permitindo envio de emails maliciosos.

3. **Avalie o impacto** da exploração dessa ameaça (ex.: vazamento de dados, interrupção de serviço).

4. **Sugira mitigações**, como:
   - Uso do **AWS IAM Least Privilege** (Princípio do Menor Privilégio).
   - **MFA** para operações sensíveis.
   - **Logs no AWS CloudTrail** para auditoria.

Gere a tabela de modelagem de ameaças para as ações fornecidas.
