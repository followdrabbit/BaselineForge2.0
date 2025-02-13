# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslambda.html'}

[](/pdfs/service-authorization/latest/reference/service-
authorization.pdf#list_awslambda "Open PDF")

[Documentation](/index.html)[Service Authorization
Reference](/iam/index.html)[Service Authorization Reference](reference.html)

ActionsResource typesCondition keys

# Actions, resources, and condition keys for AWS Lambda

AWS Lambda (service prefix: `lambda`) provides the following service-specific
resources, actions, and condition context keys for use in IAM permission
policies.

References:

  * Learn how to [configure this service](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

  * View a list of the [API operations available for this service](https://docs.aws.amazon.com/lambda/latest/dg/API_Reference.html).

  * Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lambda/latest/dg/lambda-auth-and-access-control.html) permission policies.

###### Topics

  * Actions defined by AWS Lambda
  * Resource types defined by AWS Lambda
  * Condition keys for AWS Lambda

## Actions defined by AWS Lambda

You can specify the following actions in the `Action` element of an IAM policy
statement. Use policies to grant permissions to perform an operation in AWS.
When you use an action in a policy, you usually allow or deny access to the
API operation or CLI command with the same name. However, in some cases, a
single action controls access to more than one operation. Alternatively, some
operations require several different actions.

The **Resource types** column of the Actions table indicates whether each
action supports resource-level permissions. If there is no value for this
column, you must specify all resources ("*") to which the policy applies in
the `Resource` element of your policy statement. If the column includes a
resource type, then you can specify an ARN of that type in a statement with
that action. If the action has one or more required resources, the caller must
have permission to use the action with those resources. Required resources are
indicated in the table with an asterisk (*). If you limit resource access with
the `Resource` element in an IAM policy, you must include an ARN or pattern
for each required resource type. Some actions support multiple resource types.
If the resource type is optional (not indicated as required), then you can
choose to use one of the optional resource types.

The **Condition keys** column of the Actions table includes keys that you can
specify in a policy statement's `Condition` element. For more information on
the condition keys that are associated with resources for the service, see the
**Condition keys** column of the Resource types table.

###### Note

Resource condition keys are listed in the Resource types table. You can find a
link to the resource type that applies to an action in the **Resource types
(*required)** column of the Actions table. The resource type in the Resource
types table includes the **Condition keys** column, which are the resource
condition keys that apply to an action in the Actions table.

For details about the columns in the following table, see [Actions
table](reference_policies_actions-resources-contextkeys.html#actions_table).

Actions | Description | Access level | Resource types (*required) | Condition keys | Dependent actions  
---|---|---|---|---|---  
[AddLayerVersionPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_AddLayerVersionPermission.html) | Grants permission to add permissions to the resource-based policy of a version of an AWS Lambda layer | Permissions management |  layerVersion* |  |   
[AddPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html) | Grants permission to give an AWS service or another account permission to use an AWS Lambda function | Permissions management |  function* |  |   
|  lambda:Principal lambda:FunctionUrlAuthType |   
[CreateAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateAlias.html) | Grants permission to create an alias for a Lambda function version | Write |  function* |  |   
[CreateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateCodeSigningConfig.html) | Grants permission to create an AWS Lambda code signing config | Write |  |  aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html) | Grants permission to create a mapping between an event source and an AWS Lambda function | Write |  |  lambda:FunctionArn aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html) | Grants permission to create an AWS Lambda function | Write |  function* |  |  iam:PassRole   
|  lambda:Layer lambda:VpcIds lambda:SubnetIds lambda:SecurityGroupIds lambda:CodeSigningConfigArn aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunctionUrlConfig.html) | Grants permission to create a function url configuration for a Lambda function | Write |  function* |  |   
|  lambda:FunctionUrlAuthType lambda:FunctionArn |   
[DeleteAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteAlias.html) | Grants permission to delete an AWS Lambda function alias | Write |  function* |  |   
[DeleteCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteCodeSigningConfig.html) | Grants permission to delete an AWS Lambda code signing config | Write |  code signing config* |  |   
[DeleteEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteEventSourceMapping.html) | Grants permission to delete an AWS Lambda event source mapping | Write |  eventSourceMapping* |  |   
|  lambda:FunctionArn |   
[DeleteFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunction.html) | Grants permission to delete an AWS Lambda function | Write |  function* |  |   
[DeleteFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionCodeSigningConfig.html) | Grants permission to detach a code signing config from an AWS Lambda function | Write |  function* |  |   
[DeleteFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionConcurrency.html) | Grants permission to remove a concurrent execution limit from an AWS Lambda function | Write |  function* |  |   
[DeleteFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionEventInvokeConfig.html) | Grants permission to delete the configuration for asynchronous invocation for an AWS Lambda function, version, or alias | Write |  function* |  |   
[DeleteFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionUrlConfig.html) | Grants permission to delete function url configuration for a Lambda function | Write |  function* |  |   
|  lambda:FunctionUrlAuthType lambda:FunctionArn |   
[DeleteLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteLayerVersion.html) | Grants permission to delete a version of an AWS Lambda layer | Write |  layerVersion* |  |   
[DeleteProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteProvisionedConcurrencyConfig.html) | Grants permission to delete the provisioned concurrency configuration for an AWS Lambda function | Write |  function alias |  |   
function version |  |   
[DisableReplication](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-permissions.html) [permission only] | Grants permission to disable replication for a Lambda@Edge function | Permissions management |  function* |  |   
[EnableReplication](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-permissions.html) [permission only] | Grants permission to enable replication for a Lambda@Edge function | Permissions management |  function* |  |   
[GetAccountSettings](https://docs.aws.amazon.com/lambda/latest/dg/API_GetAccountSettings.html) | Grants permission to view details about an account's limits and usage in an AWS Region | Read |  |  |   
[GetAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_GetAlias.html) | Grants permission to view details about an AWS Lambda function alias | Read |  function* |  |   
[GetCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetCodeSigningConfig.html) | Grants permission to view details about an AWS Lambda code signing config | Read |  code signing config* |  |   
[GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_GetEventSourceMapping.html) | Grants permission to view details about an AWS Lambda event source mapping | Read |  eventSourceMapping* |  |   
|  lambda:FunctionArn |   
[GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html) | Grants permission to view details about an AWS Lambda function | Read |  function* |  |   
[GetFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionCodeSigningConfig.html) | Grants permission to view the code signing config arn attached to an AWS Lambda function | Read |  function* |  |   
[GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConcurrency.html) | Grants permission to view details about the reserved concurrency configuration for a function | Read |  function* |  |   
[GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html) | Grants permission to view details about the version-specific settings of an AWS Lambda function or version | Read |  function* |  |   
[GetFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionEventInvokeConfig.html) | Grants permission to view the configuration for asynchronous invocation for a function, version, or alias | Read |  function* |  |   
[GetFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionRecursionConfig.html) | Grants permission to view the recursion configuration of an AWS Lambda function | Read |  function* |  |   
[GetFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionUrlConfig.html) | Grants permission to read function url configuration for a Lambda function | Read |  function* |  |   
|  lambda:FunctionUrlAuthType lambda:FunctionArn |   
[GetLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersion.html) | Grants permission to view details about a version of an AWS Lambda layer. Note this action also supports GetLayerVersionByArn API | Read |  layerVersion* |  |   
[GetLayerVersionPolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersionPolicy.html) | Grants permission to view the resource-based policy for a version of an AWS Lambda layer | Read |  layerVersion* |  |   
[GetPolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetPolicy.html) | Grants permission to view the resource-based policy for an AWS Lambda function, version, or alias | Read |  function* |  |   
[GetProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetProvisionedConcurrencyConfig.html) | Grants permission to view the provisioned concurrency configuration for an AWS Lambda function's alias or version | Read |  function alias |  |   
function version |  |   
[GetRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetRuntimeManagementConfig.html) | Grants permission to view the runtime management configuration of an AWS Lambda function | Read |  function* |  |   
[InvokeAsync](https://docs.aws.amazon.com/lambda/latest/dg/API_InvokeAsync.html) | Grants permission to invoke a function asynchronously (Deprecated) | Write |  function* |  |   
[InvokeFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html) | Grants permission to invoke an AWS Lambda function | Write |  function* |  |   
|  lambda:EventSourceToken |   
[InvokeFunctionUrl](https://docs.aws.amazon.com/lambda/latest/dg/API_InvokeFunctionUrl.html) [permission only] | Grants permission to invoke an AWS Lambda function through url | Write |  function* |  |   
|  lambda:FunctionUrlAuthType lambda:FunctionArn lambda:EventSourceToken |   
[ListAliases](https://docs.aws.amazon.com/lambda/latest/dg/API_ListAliases.html) | Grants permission to retrieve a list of aliases for an AWS Lambda function | List |  function* |  |   
[ListCodeSigningConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListCodeSigningConfigs.html) | Grants permission to retrieve a list of AWS Lambda code signing configs | List |  |  |   
[ListEventSourceMappings](https://docs.aws.amazon.com/lambda/latest/dg/API_ListEventSourceMappings.html) | Grants permission to retrieve a list of AWS Lambda event source mappings | List |  |  |   
[ListFunctionEventInvokeConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionEventInvokeConfigs.html) | Grants permission to retrieve a list of configurations for asynchronous invocation for a function | List |  function* |  |   
[ListFunctionUrlConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionUrlConfigs.html) | Grants permission to read function url configurations for a function | List |  function* |  |   
|  lambda:FunctionUrlAuthType |   
[ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html) | Grants permission to retrieve a list of AWS Lambda functions, with the version-specific configuration of each function | List |  |  |   
[ListFunctionsByCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionsByCodeSigningConfig.html) | Grants permission to retrieve a list of AWS Lambda functions by the code signing config assigned  | List |  code signing config* |  |   
[ListLayerVersions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayerVersions.html) | Grants permission to retrieve a list of versions of an AWS Lambda layer | List |  |  |   
[ListLayers](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayers.html) | Grants permission to retrieve a list of AWS Lambda layers, with details about the latest version of each layer | List |  |  |   
[ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListProvisionedConcurrencyConfigs.html) | Grants permission to retrieve a list of provisioned concurrency configurations for an AWS Lambda function | List |  function* |  |   
[ListTags](https://docs.aws.amazon.com/lambda/latest/dg/API_ListTags.html) | Grants permission to retrieve a list of tags for an AWS Lambda function, event source mapping or code signing configuration resource | Read |  code signing config |  |   
eventSourceMapping |  |   
function |  |   
[ListVersionsByFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_ListVersionsByFunction.html) | Grants permission to retrieve a list of versions for an AWS Lambda function | List |  function* |  |   
[PublishLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_PublishLayerVersion.html) | Grants permission to create an AWS Lambda layer | Write |  layer* |  |   
[PublishVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_PublishVersion.html) | Grants permission to create an AWS Lambda function version | Write |  function* |  |   
[PutFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionCodeSigningConfig.html) | Grants permission to attach a code signing config to an AWS Lambda function | Write |  code signing config* |  |   
function* |  |   
|  lambda:CodeSigningConfigArn |   
[PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionConcurrency.html) | Grants permission to configure reserved concurrency for an AWS Lambda function | Write |  function* |  |   
[PutFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionEventInvokeConfig.html) | Grants permission to configures options for asynchronous invocation on an AWS Lambda function, version, or alias | Write |  function* |  |   
[PutFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionRecursionConfig.html) | Grants permission to update the recursion configuration of an AWS Lambda function | Write |  function* |  |   
[PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutProvisionedConcurrencyConfig.html) | Grants permission to configure provisioned concurrency for an AWS Lambda function's alias or version | Write |  function alias |  |   
function version |  |   
[PutRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutRuntimeManagementConfig.html) | Grants permission to update the runtime management configuration of an AWS Lambda function | Write |  function* |  |   
[RemoveLayerVersionPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_RemoveLayerVersionPermission.html) | Grants permission to remove a statement from the permissions policy for a version of an AWS Lambda layer | Permissions management |  layerVersion* |  |   
[RemovePermission](https://docs.aws.amazon.com/lambda/latest/dg/API_RemovePermission.html) | Grants permission to revoke function-use permission from an AWS service or another account | Permissions management |  function* |  |   
|  lambda:Principal lambda:FunctionUrlAuthType |   
[TagResource](https://docs.aws.amazon.com/lambda/latest/dg/API_TagResources.html) | Grants permission to add tags to an AWS Lambda function, event source mapping or code signing configuration resource | Tagging |  code signing config |  |   
eventSourceMapping |  |   
function |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[UntagResource](https://docs.aws.amazon.com/lambda/latest/dg/API_UntagResource.html) | Grants permission to remove tags from an AWS Lambda function, event source mapping or code signing configuration resource | Tagging |  code signing config |  |   
eventSourceMapping |  |   
function |  |   
|  aws:TagKeys |   
[UpdateAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateAlias.html) | Grants permission to update the configuration of an AWS Lambda function's alias | Write |  function* |  |   
[UpdateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateCodeSigningConfig.html) | Grants permission to update an AWS Lambda code signing config | Write |  code signing config* |  |   
[UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateEventSourceMapping.html) | Grants permission to update the configuration of an AWS Lambda event source mapping | Write |  eventSourceMapping* |  |   
|  lambda:FunctionArn |   
[UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionCode.html) | Grants permission to update the code of an AWS Lambda function | Write |  function* |  |   
[UpdateFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionCodeSigningConfig.html) | Grants permission to update the code signing config of an AWS Lambda function | Write |  code signing config* |  |   
function* |  |   
[UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionConfiguration.html) | Grants permission to modify the version-specific settings of an AWS Lambda function | Write |  function* |  |   
|  lambda:Layer lambda:VpcIds lambda:SubnetIds lambda:SecurityGroupIds |   
[UpdateFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionEventInvokeConfig.html) | Grants permission to modify the configuration for asynchronous invocation for an AWS Lambda function, version, or alias | Write |  function* |  |   
[UpdateFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionUrlConfig.html) | Grants permission to update a function url configuration for a Lambda function | Write |  function* |  |   
|  lambda:FunctionUrlAuthType lambda:FunctionArn |   
  
## Resource types defined by AWS Lambda

The following resource types are defined by this service and can be used in
the `Resource` element of IAM permission policy statements. Each action in the
Actions table identifies the resource types that can be specified with that
action. A resource type can also define which condition keys you can include
in a policy. These keys are displayed in the last column of the Resource types
table. For details about the columns in the following table, see [Resource
types table](reference_policies_actions-resources-
contextkeys.html#resources_table).

Resource types | ARN | Condition keys  
---|---|---  
[code signing config](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:code-signing-config:${CodeSigningConfigId}` |  aws:ResourceTag/${TagKey}  
[eventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:event-source-mapping:${UUID}` |  aws:ResourceTag/${TagKey}  
[function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}` |  aws:ResourceTag/${TagKey}  
[function alias](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}:${Alias}` |  aws:ResourceTag/${TagKey}  
[function version](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}:${Version}` |  aws:ResourceTag/${TagKey}  
[layer](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:layer:${LayerName}` |   
[layerVersion](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) |  `arn:${Partition}:lambda:${Region}:${Account}:layer:${LayerName}:${LayerVersion}` |   
  
## Condition keys for AWS Lambda

AWS Lambda defines the following condition keys that can be used in the
`Condition` element of an IAM policy. You can use these keys to further refine
the conditions under which the policy statement applies. For details about the
columns in the following table, see [Condition keys
table](reference_policies_actions-resources-
contextkeys.html#context_keys_table).

To view the global condition keys that are available to all services, see
[Available global condition
keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#AvailableKeys).

Condition keys | Description | Type  
---|---|---  
[aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) | Filters access by the tags that are passed in the request | String  
[aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) | Filters access by the tags associated with the resource | String  
[aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) | Filters access by the tag keys that are passed in the request | ArrayOfString  
[lambda:CodeSigningConfigArn](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ARN of an AWS Lambda code signing config | ARN  
[lambda:EventSourceToken](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ID from a non-AWS event source configured for the AWS Lambda function | String  
[lambda:FunctionArn](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ARN of an AWS Lambda function | ARN  
[lambda:FunctionUrlAuthType](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by authorization type specified in request. Available during CreateFunctionUrlConfig, UpdateFunctionUrlConfig, DeleteFunctionUrlConfig, GetFunctionUrlConfig, ListFunctionUrlConfig, AddPermission and RemovePermission operations | String  
[lambda:Layer](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ARN of a version of an AWS Lambda layer | ArrayOfString  
[lambda:Principal](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by restricting the AWS service or account that can invoke a function | String  
[lambda:SecurityGroupIds](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ID of security groups configured for the AWS Lambda function | ArrayOfString  
[lambda:SourceFunctionArn](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ARN of the AWS Lambda function from which the request originated | ARN  
[lambda:SubnetIds](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ID of subnets configured for the AWS Lambda function | ArrayOfString  
[lambda:VpcIds](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) | Filters access by the ID of the VPC configured for the AWS Lambda function | String  
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AWS Lake Formation

AWS Launch Wizard

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

