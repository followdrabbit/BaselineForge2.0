# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonapigateway.html'}

[](/pdfs/service-authorization/latest/reference/service-
authorization.pdf#list_amazonapigateway "Open PDF")

[Documentation](/index.html)[Service Authorization
Reference](/iam/index.html)[Service Authorization Reference](reference.html)

ActionsResource typesCondition keys

# Actions, resources, and condition keys for Amazon API Gateway

Amazon API Gateway (service prefix: `execute-api`) provides the following
service-specific resources, actions, and condition context keys for use in IAM
permission policies.

References:

  * Learn how to [configure this service](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

  * View a list of the [API operations available for this service](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html).

  * Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) permission policies.

###### Topics

  * Actions defined by Amazon API Gateway
  * Resource types defined by Amazon API Gateway
  * Condition keys for Amazon API Gateway

## Actions defined by Amazon API Gateway

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
[InvalidateCache](https://docs.aws.amazon.com/apigateway/api-reference/api-gateway-caching.html) | Used to invalidate API cache upon a client request | Write |  execute-api-general* |  |   
[Invoke](https://docs.aws.amazon.com/apigateway/api-reference/how-to-call-api.html) | Used to invoke an API upon a client request | Write |  execute-api-domain |  |   
execute-api-general |  |   
[ManageConnections](https://docs.aws.amazon.com/apigateway/api-reference/apigateway-websocket-control-access-iam.html) | ManageConnections controls access to the @connections API | Write |  execute-api-general* |  |   
  
## Resource types defined by Amazon API Gateway

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
[execute-api-general](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) |  `arn:${Partition}:execute-api:${Region}:${Account}:${ApiId}/${Stage}/${Method}/${ApiSpecificResourcePath}` |  execute-api:viaDomainArn  
[execute-api-domain](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) |  `arn:${Partition}:execute-api:${Region}:${Account}:/domainnames/${DomainName}+${DomainIdentifier}` |   
  
## Condition keys for Amazon API Gateway

Amazon API Gateway defines the following condition keys that can be used in
the `Condition` element of an IAM policy. You can use these keys to further
refine the conditions under which the policy statement applies. For details
about the columns in the following table, see [Condition keys
table](reference_policies_actions-resources-
contextkeys.html#context_keys_table).

To view the global condition keys that are available to all services, see
[Available global condition
keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#AvailableKeys).

Condition keys | Description | Type  
---|---|---  
[execute-api:viaDomainArn](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html) | Filters access by the domain name ARN the API is called from | String  
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Apache Kafka APIs for Amazon MSK clusters

Amazon API Gateway Management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

