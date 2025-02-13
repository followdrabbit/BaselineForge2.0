```json
[
  {
    "action_iam": "CreateFunction",
    "build": true,
    "run": false,
    "descricao": "Grants permission to create an AWS Lambda function, which involves setting up the function's configuration, permissions, and resource needs."
  },
  {
    "action_iam": "InvokeFunction",
    "build": false,
    "run": true,
    "descricao": "Grants permission to invoke an AWS Lambda function, allowing it to run and execute its intended logic."
  },
  {
    "action_iam": "DeleteFunction",
    "build": true,
    "run": false,
    "descricao": "Grants permission to delete an AWS Lambda function, removing its code and configuration from AWS."
  },
  {
    "action_iam": "GetFunction",
    "build": false,
    "run": true,
    "descricao": "Grants permission to view details about an AWS Lambda function, which includes configuration and code references, supporting the execution of the function."
  },
  {
    "action_iam": "UpdateFunctionCode",
    "build": true,
    "run": false,
    "descricao": "Grants permission to update the code of an AWS Lambda function, modifying its execution logic."
  }
]
```