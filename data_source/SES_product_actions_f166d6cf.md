# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonses.html'}

[](/pdfs/service-authorization/latest/reference/service-
authorization.pdf#list_amazonses "Open PDF")

[Documentation](/index.html)[Service Authorization
Reference](/iam/index.html)[Service Authorization Reference](reference.html)

ActionsResource typesCondition keys

# Actions, resources, and condition keys for Amazon SES

Amazon SES (service prefix: `ses`) provides the following service-specific
resources, actions, and condition context keys for use in IAM permission
policies.

References:

  * Learn how to [configure this service](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/).

  * View a list of the [API operations available for this service](https://docs.aws.amazon.com/ses/latest/APIReference/).

  * Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/control-user-access.html) permission policies.

###### Topics

  * Actions defined by Amazon SES
  * Resource types defined by Amazon SES
  * Condition keys for Amazon SES

## Actions defined by Amazon SES

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
[CloneReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CloneReceiptRuleSet.html) | Grants permission to create a receipt rule set by cloning an existing one | Write |  |  ses:ApiVersion |   
[CreateConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSet.html) | Grants permission to create a new configuration set | Write |  |  ses:ApiVersion |   
[CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetEventDestination.html) | Grants permission to create a configuration set event destination | Write |  |  ses:ApiVersion |   
[CreateConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetTrackingOptions.html) | Grants permission to creates an association between a configuration set and a custom domain for open and click event tracking | Write |  |  ses:ApiVersion |   
[CreateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateCustomVerificationEmailTemplate.html) | Grants permission to create a new custom verification email template | Write |  |  ses:ApiVersion |   
[CreateReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptFilter.html) | Grants permission to create a new IP address filter | Write |  |  ses:ApiVersion |   
[CreateReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRule.html) | Grants permission to create a receipt rule | Write |  |  ses:ApiVersion |   
[CreateReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRuleSet.html) | Grants permission to create an empty receipt rule set | Write |  |  ses:ApiVersion |   
[CreateTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateTemplate.html) | Grants permission to creates an email template | Write |  |  ses:ApiVersion |   
[DeleteConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSet.html) | Grants permission to delete an existing configuration set | Write |  |  ses:ApiVersion |   
[DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetEventDestination.html) | Grants permission to delete an event destination | Write |  |  ses:ApiVersion |   
[DeleteConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetTrackingOptions.html) | Grants permission to delete an association between a configuration set and a custom domain for open and click event tracking | Write |  |  ses:ApiVersion |   
[DeleteCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteCustomVerificationEmailTemplate.html) | Grants permission to delete an existing custom verification email template | Write |  |  ses:ApiVersion |   
[DeleteIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentity.html) | Grants permission to delete the specified identity | Write |  |  ses:ApiVersion |   
[DeleteIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentityPolicy.html) | Grants permission to delete the specified sending authorization policy for the given identity (an email address or a domain) | Permissions management |  |  ses:ApiVersion |   
[DeleteReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptFilter.html) | Grants permission to delete the specified IP address filter | Write |  |  ses:ApiVersion |   
[DeleteReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRule.html) | Grants permission to delete the specified receipt rule | Write |  |  ses:ApiVersion |   
[DeleteReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRuleSet.html) | Grants permission to delete the specified receipt rule set and all of the receipt rules it contains | Write |  |  ses:ApiVersion |   
[DeleteTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteTemplate.html) | Grants permission to delete an email template | Write |  |  ses:ApiVersion |   
[DeleteVerifiedEmailAddress](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteVerifiedEmailAddress.html) | Grants permission to delete the specified email address from the list of verified addresses | Write |  |  ses:ApiVersion |   
[DescribeActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeActiveReceiptRuleSet.html) | Grants permission to return the metadata and receipt rules for the receipt rule set that is currently active | Read |  |  ses:ApiVersion |   
[DescribeConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeConfigurationSet.html) | Grants permission to return the details of the specified configuration set | Read |  |  ses:ApiVersion |   
[DescribeReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRule.html) | Grants permission to return the details of the specified receipt rule | Read |  |  ses:ApiVersion |   
[DescribeReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRuleSet.html) | Grants permission to return the details of the specified receipt rule set | Read |  |  ses:ApiVersion |   
[GetAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetAccountSendingEnabled.html) | Grants permission to return the email sending status of your account | Read |  |  ses:ApiVersion |   
[GetCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetCustomVerificationEmailTemplate.html) | Grants permission to return the custom email verification template for the template name you specify | Read |  |  ses:ApiVersion |   
[GetIdentityDkimAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityDkimAttributes.html) | Grants permission to return the current status of Easy DKIM signing for an entity | Read |  |  ses:ApiVersion |   
[GetIdentityMailFromDomainAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityMailFromDomainAttributes.html) | Grants permission to return the custom MAIL FROM attributes for a list of identities (email addresses and/or domains) | Read |  |  ses:ApiVersion |   
[GetIdentityNotificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityNotificationAttributes.html) | Grants permission to return a structure describing identity notification attributes for a list of verified identities (email addresses and/or domains), | Read |  |  ses:ApiVersion |   
[GetIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityPolicies.html) | Grants permission to return the requested sending authorization policies for the given identity (an email address or a domain) | Read |  |  ses:ApiVersion |   
[GetIdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html) | Grants permission to return the verification status and (for domain identities) the verification token for a list of identities | Read |  |  ses:ApiVersion |   
[GetSendQuota](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html) | Grants permission to return the user's current sending limits | Read |  |  ses:ApiVersion |   
[GetSendStatistics](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendStatistics.html) | Grants permission to returns the user's sending statistics | Read |  |  ses:ApiVersion |   
[GetTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html) | Grants permission to return the template object, which includes the subject line, HTML par, and text part for the template you specify | Read |  |  ses:ApiVersion |   
[ListConfigurationSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListConfigurationSets.html) | Grants permission to list all of the configuration sets for your account | List |  |  ses:ApiVersion |   
[ListCustomVerificationEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListCustomVerificationEmailTemplates.html) | Grants permission to list all of the existing custom verification email templates for your account | List |  |  ses:ApiVersion |   
[ListIdentities](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html) | Grants permission to list the email identities for your account | List |  |  ses:ApiVersion |   
[ListIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentityPolicies.html) | Grants permission to list all of the email templates for your account | List |  |  ses:ApiVersion |   
[ListReceiptFilters](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptFilters.html) | Grants permission to list the IP address filters associated with your account | Read |  |  ses:ApiVersion |   
[ListReceiptRuleSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptRuleSets.html) | Grants permission to list the receipt rule sets that exist under your account | Read |  |  ses:ApiVersion |   
[ListTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html) | Grants permission to list the email templates present in your account | List |  |  ses:ApiVersion |   
[ListVerifiedEmailAddresses](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListVerifiedEmailAddresses.html) | Grants permission to list all of the email addresses that have been verified in your account | Read |  |  ses:ApiVersion |   
[PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html) | Grants permission to add or update the delivery options for a configuration set | Write |  |  ses:ApiVersion |   
[PutIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutIdentityPolicy.html) | Grants permission to add or update a sending authorization policy for the specified identity (an email address or a domain) | Permissions management |  |  ses:ApiVersion |   
[ReorderReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReorderReceiptRuleSet.html) | Grants permission to reorder the receipt rules within a receipt rule set | Write |  |  ses:ApiVersion |   
[SendBounce](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBounce.html) | Grants permission to generate and send a bounce message to the sender of an email you received through Amazon SES | Write |  identity* |  |   
|  ses:ApiVersion ses:FromAddress |   
[SendBulkTemplatedEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBulkTemplatedEmail.html) | Grants permission to compose an email message to multiple destinations | Write |  identity* |  |   
template* |  |   
configuration-set |  |   
|  ses:ApiVersion ses:FeedbackAddress ses:FromAddress ses:FromDisplayName ses:Recipients |   
[SendCustomVerificationEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendCustomVerificationEmail.html) | Grants permission to add an email address to the list of identities and attempts to verify it for your account | Write |  identity* |  |   
|  ses:ApiVersion ses:FeedbackAddress ses:FromAddress ses:FromDisplayName ses:Recipients |   
[SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendEmail.html) | Grants permission to send an email message | Write |  identity* |  |   
configuration-set |  |   
|  ses:ApiVersion ses:FeedbackAddress ses:FromAddress ses:FromDisplayName ses:Recipients |   
[SendRawEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendRawEmail.html) | Grants permission to send an email message, with header and content specified by the client | Write |  identity* |  |   
configuration-set |  |   
|  ses:ApiVersion ses:FeedbackAddress ses:FromAddress ses:FromDisplayName ses:Recipients |   
[SendTemplatedEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html) | Grants permission to compose an email message using an email template | Write |  identity* |  |   
template* |  |   
configuration-set |  |   
|  ses:ApiVersion ses:FeedbackAddress ses:FromAddress ses:FromDisplayName ses:Recipients |   
[SetActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetActiveReceiptRuleSet.html) | Grants permission to set the specified receipt rule set as the active receipt rule set | Write |  |  ses:ApiVersion |   
[SetIdentityDkimEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityDkimEnabled.html) | Grants permission to enable or disable Easy DKIM signing of email sent from an identity | Write |  |  ses:ApiVersion |   
[SetIdentityFeedbackForwardingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityFeedbackForwardingEnabled.html) | Grants permission to enable or disable whether Amazon SES forwards bounce and complaint notifications for an identity (an email address or a domain) | Write |  |  ses:ApiVersion |   
[SetIdentityHeadersInNotificationsEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityHeadersInNotificationsEnabled.html) | Grants permission to set whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type for a given identity (an email address or a domain) | Write |  |  ses:ApiVersion |   
[SetIdentityMailFromDomain](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) | Grants permission to enable or disable the custom MAIL FROM domain setup for a verified identity | Write |  |  ses:ApiVersion |   
[SetIdentityNotificationTopic](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityNotificationTopic.html) | Grants permission to set an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications for a verified identity | Write |  |  ses:ApiVersion |   
[SetReceiptRulePosition](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetReceiptRulePosition.html) | Grants permission to set the position of the specified receipt rule in the receipt rule set | Write |  |  ses:ApiVersion |   
[TestRenderTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_TestRenderTemplate.html) | Grants permission to create a preview of the MIME content of an email when provided with a template and a set of replacement data | Write |  |  ses:ApiVersion |   
[UpdateAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html) | Grants permission to enable or disable email sending for your account | Write |  |  ses:ApiVersion |   
[UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetEventDestination.html) | Grants permission to update the event destination of a configuration set | Write |  |  ses:ApiVersion |   
[UpdateConfigurationSetReputationMetricsEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetReputationMetricsEnabled.html) | Grants permission to enable or disable the publishing of reputation metrics for emails sent using a specific configuration set | Write |  |  ses:ApiVersion |   
[UpdateConfigurationSetSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html) | Grants permission to enable or disable email sending for messages sent using a specific configuration set | Write |  |  ses:ApiVersion |   
[UpdateConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetTrackingOptions.html) | Grants permission to modify an association between a configuration set and a custom domain for open and click event tracking | Write |  |  ses:ApiVersion |   
[UpdateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateCustomVerificationEmailTemplate.html) | Grants permission to update an existing custom verification email template | Write |  |  ses:ApiVersion |   
[UpdateReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateReceiptRule.html) | Grants permission to update a receipt rule | Write |  |  ses:ApiVersion |   
[UpdateTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateTemplate.html) | Grants permission to update an email template | Write |  |  ses:ApiVersion |   
[VerifyDomainDkim](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainDkim.html) | Grants permission to return a set of DKIM tokens for a domain | Write |  |  ses:ApiVersion |   
[VerifyDomainIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainIdentity.html) | Grants permission to verify a domain | Write |  |  ses:ApiVersion |   
[VerifyEmailAddress](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailAddress.html) | Grants permission to verify an email address | Write |  |  ses:ApiVersion |   
[VerifyEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailIdentity.html) | Grants permission to verify an email identity | Write |  |  ses:ApiVersion |   
  
## Resource types defined by Amazon SES

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
[configuration-set](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html) |  `arn:${Partition}:ses:${Region}:${Account}:configuration-set/${ConfigurationSetName}` |   
[custom-verification-email-template](https://docs.aws.amazon.com/ses/latest/APIReference/API_CustomVerificationEmailTemplate.html) |  `arn:${Partition}:ses:${Region}:${Account}:custom-verification-email-template/${TemplateName}` |   
[identity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_IdentityInfo.html) |  `arn:${Partition}:ses:${Region}:${Account}:identity/${IdentityName}` |   
[template](https://docs.aws.amazon.com/ses/latest/APIReference/API_Template.html) |  `arn:${Partition}:ses:${Region}:${Account}:template/${TemplateName}` |   
  
## Condition keys for Amazon SES

Amazon SES defines the following condition keys that can be used in the
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
[ses:ApiVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys) | Filters actions based on the SES API version | String  
[ses:FeedbackAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys) | Filters actions based on the "Return-Path" address, which specifies where bounces and complaints are sent by email feedback forwarding | String  
[ses:FromAddress](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys) | Filters actions based on the "From" address of a message | String  
[ses:FromDisplayName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys) | Filters actions based on the "From" address that is used as the display name of a message | String  
[ses:Recipients](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonses.html#amazonses-policy-keys) | Filters actions based on the recipient addresses of a message, which include the "To", "CC", and "BCC" addresses | ArrayOfString  
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Service Quotas

AWS Shield

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

