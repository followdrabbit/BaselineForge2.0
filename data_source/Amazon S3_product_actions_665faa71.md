# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html'}

[Documentation](/index.html)[Service Authorization
Reference](/iam/index.html)[Service Authorization
Reference](list_amazons3.html)

ActionsResource typesCondition keys

# Actions, resources, and condition keys for Amazon S3

Amazon S3 (service prefix: `s3`) provides the following service-specific
resources, actions, and condition context keys for use in IAM permission
policies.

References:

  * Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

  * View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).

  * Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-overview.html) permission policies.

###### Topics

  * Actions defined by Amazon S3
  * Resource types defined by Amazon S3
  * Condition keys for Amazon S3

## Actions defined by Amazon S3

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
[AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) | Grants permission to abort a multipart upload | Write |  object* |  |   
|  s3:DataAccessPointArn s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[AssociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html) | Grants permission to associate Access Grants identity center | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[BypassGovernanceRetention](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-managing-bypass) | Grants permission to allow circumvention of governance-mode object retention settings | Permissions management |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:RequestObjectTag/<key> s3:RequestObjectTagKeys s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-acl s3:x-amz-content-sha256 s3:x-amz-copy-source s3:x-amz-grant-full-control s3:x-amz-grant-read s3:x-amz-grant-read-acp s3:x-amz-grant-write s3:x-amz-grant-write-acp s3:x-amz-metadata-directive s3:x-amz-server-side-encryption s3:x-amz-server-side-encryption-aws-kms-key-id s3:x-amz-server-side-encryption-customer-algorithm s3:x-amz-storage-class s3:x-amz-website-redirect-location s3:object-lock-mode s3:object-lock-retain-until-date s3:object-lock-remaining-retention-days s3:object-lock-legal-hold |   
[CreateAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrant.html) | Grants permission to create Access Grant | Write |  accessgrantslocation* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html) | Grants permission to Create Access Grants Instance | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys |   
[CreateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html) | Grants permission to create Access Grants location | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html) | Grants permission to create a new access point | Write |  accesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:locationconstraint s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-acl s3:x-amz-content-sha256 |   
[CreateAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html) | Grants permission to create an object lambda enabled accesspoint | Write |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) | Grants permission to create a new bucket | Write |  bucket* |  |   
|  s3:authType s3:locationconstraint s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-acl s3:x-amz-content-sha256 s3:x-amz-grant-full-control s3:x-amz-grant-read s3:x-amz-grant-read-acp s3:x-amz-grant-write s3:x-amz-grant-write-acp s3:x-amz-object-ownership |   
[CreateBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataTableConfiguration.html) | Grants permission to create a new S3 Metadata configuration for a specified bucket | Write |  bucket* |  |  s3tables:CreateNamespace  s3tables:CreateTable  s3tables:GetTable  s3tables:PutTablePolicy   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html) | Grants permission to create a new Amazon S3 Batch Operations job | Write |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:RequestJobPriority s3:RequestJobOperation aws:TagKeys aws:RequestTag/${TagKey} |  iam:PassRole   
[CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html) | Grants permission to create a new Multi-Region Access Point | Write |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[CreateStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html) | Grants permission to create an Amazon S3 Storage Lens group | Write |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:RequestTag/${TagKey} aws:TagKeys |   
[DeleteAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html) | Grants permission to delete Access Grant | Write |  accessgrant* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[DeleteAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstance.html) | Grants permission to Delete Access Grants Instance | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[DeleteAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstanceResourcePolicy.html) | Grants permission to read Access grants instance resource policy | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[DeleteAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html) | Grants permission to delete Access Grants location | Write |  accessgrantslocation* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html) | Grants permission to delete the access point named in the URI | Write |  accesspoint* |  |   
|  s3:DataAccessPointArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html) | Grants permission to delete the object lambda enabled access point named in the URI | Write |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html) | Grants permission to delete the policy on a specified access point | Permissions management |  accesspoint* |  |   
|  s3:DataAccessPointArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html) | Grants permission to delete the policy on a specified object lambda enabled access point | Permissions management |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html) | Grants permission to delete the bucket named in the URI | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html) | Grants permission to delete the S3 Metadata configuration for a specified bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html) | Grants permission to delete the policy on a specified bucket | Permissions management |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html) | Grants permission to remove the website configuration for a bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html) | Grants permission to remove tags from an existing Amazon S3 Batch Operations job | Tagging |  job* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:ExistingJobPriority s3:ExistingJobOperation |   
[DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html) | Grants permission to delete the Multi-Region Access Point named in the URI | Write |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) | Grants permission to remove the null version of an object and insert a delete marker, which becomes the current version of the object | Write |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) | Grants permission to use the tagging subresource to remove the entire tag set from the specified object | Tagging |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) | Grants permission to remove a specific version of an object | Write |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[DeleteObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) | Grants permission to remove the entire tag set for a specific version of the object | Tagging |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[DeleteStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfiguration.html) | Grants permission to delete an existing Amazon S3 Storage Lens configuration | Write |  storagelensconfiguration* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfigurationTagging.html) | Grants permission to remove tags from an existing Amazon S3 Storage Lens configuration | Tagging |  storagelensconfiguration* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DeleteStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensGroup.html) | Grants permission to delete an existing S3 Storage Lens group | Write |  storagelensgroup* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html) | Grants permission to retrieve the configuration parameters and status for a batch operations job | Read |  job* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[DescribeMultiRegionAccessPointOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html) | Grants permission to retrieve the configurations for a Multi-Region Access Point | Read |  multiregionaccesspointrequestarn* |  |   
|  s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[DissociateAccessGrantsIdentityCenter](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html) | Grants permission to disassociate Access Grants identity center | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html) | Grants permission to uses the accelerate subresource to return the Transfer Acceleration state of a bucket, which is either Enabled or Suspended | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrant.html) | Grants permission to read Access Grant | Read |  accessgrant* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetAccessGrantsInstance](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstance.html) | Grants permission to Read Access Grants Instance | Read |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetAccessGrantsInstanceForPrefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceForPrefix.html) | Grants permission to Read Access Grants Instance by prefix | Read |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceResourcePolicy.html) | Grants permission to read Access grants instance resource policy | Read |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsLocation.html) | Grants permission to read Access Grants location | Read |  accessgrantslocation* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html) | Grants permission to return configuration information about the specified access point | Read |  |  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html) | Grants permission to retrieve the configuration of the object lambda enabled access point | Read |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessPointForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html) | Grants permission to create an object lambda enabled accesspoint | Read |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html) | Grants permission to return the access point policy associated with the specified access point | Read |  accesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html) | Grants permission to return the access point policy associated with the specified object lambda enabled access point | Read |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html) | Grants permission to return the policy status for a specific access point policy | Read |  accesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccessPointPolicyStatusForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatusForObjectLambda.html) | Grants permission to return the policy status for a specific object lambda access point policy | Read |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAccountPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html) | Grants permission to retrieve the PublicAccessBlock configuration for an AWS account | Read |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html) | Grants permission to get an analytics configuration from an Amazon S3 bucket, identified by the analytics configuration ID | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html) | Grants permission to use the acl subresource to return the access control list (ACL) of an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketCORS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html) | Grants permission to return the CORS configuration information set for an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html) | Grants permission to return the Region that an Amazon S3 bucket resides in | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html) | Grants permission to return the logging status of an Amazon S3 bucket and the permissions users have to view or modify that status | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketMetadataTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html) | Grants permission to return the S3 Metadata configuration for a specified bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotification.html) | Grants permission to get the notification configuration of an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html) | Grants permission to get the Object Lock configuration of an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:signatureversion |   
[GetBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html) | Grants permission to retrieve ownership controls on a bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html) | Grants permission to return the policy of the specified bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html) | Grants permission to retrieve the policy status for a specific Amazon S3 bucket, which indicates whether the bucket is public | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html) | Grants permission to retrieve the PublicAccessBlock configuration for an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html) | Grants permission to return the request payment configuration for an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html) | Grants permission to return the tag set associated with an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) | Grants permission to return the versioning state of an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html) | Grants permission to return the website configuration for an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetDataAccess](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetDataAccess.html) | Grants permission to get Access | Read |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[GetEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html) | Grants permission to return the default encryption configuration an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html) | Grants permission to get an or list all Amazon S3 Intelligent Tiering configuration in a S3 Bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html) | Grants permission to return an inventory configuration from an Amazon S3 bucket, identified by the inventory configuration ID | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html) | Grants permission to return the tag set of an existing Amazon S3 Batch Operations job | Read |  job* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html) | Grants permission to return the lifecycle configuration information set on an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html) | Grants permission to get a metrics configuration from an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html) | Grants permission to return configuration information about the specified Multi-Region Access Point | Read |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[GetMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html) | Grants permission to return the access point policy associated with the specified Multi-Region Access Point | Read |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[GetMultiRegionAccessPointPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html) | Grants permission to return the policy status for a specific Multi-Region Access Point policy | Read |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[GetMultiRegionAccessPointRoutes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointRoutes.html) | Grants permission to return the route configuration for a Multi-Region Access Point | Read |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | Grants permission to retrieve objects from Amazon S3 | Read |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:if-match s3:if-none-match |   
[GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html) | Grants permission to return the access control list (ACL) of an object | Read |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html) | Grants permission to retrieve attributes related to a specific object | Read |  accesspoint* |  |   
object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html) | Grants permission to get an object's current Legal Hold status | Read |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html) | Grants permission to retrieve the retention settings for an object | Read |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) | Grants permission to return the tag set of an object | Read |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectTorrent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html) | Grants permission to return torrent files from an Amazon S3 bucket | Read |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | Grants permission to retrieve a specific version of an object | Read |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[GetObjectVersionAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html) | Grants permission to return the access control list (ACL) of a specific object version | Read |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[GetObjectVersionAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html) | Grants permission to retrieve attributes related to a specific version of an object | Read |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[GetObjectVersionForReplication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html) | Grants permission to replicate both unencrypted objects and objects encrypted with SSE-S3 or SSE-KMS | Read |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html) | Grants permission to return the tag set for a specific version of the object | Read |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[GetObjectVersionTorrent](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html) | Grants permission to get Torrent files about a different version using the versionId subresource | Read |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[GetReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html) | Grants permission to get the replication configuration information set on an Amazon S3 bucket | Read |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfiguration.html) | Grants permission to get an Amazon S3 Storage Lens configuration | Read |  storagelensconfiguration* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfigurationTagging.html) | Grants permission to get the tag set of an existing Amazon S3 Storage Lens configuration | Read |  storagelensconfiguration* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetStorageLensDashboard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_dashboard.html) | Grants permission to get an Amazon S3 Storage Lens dashboard | Read |  storagelensconfiguration* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[GetStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensGroup.html) | Grants permission to get an Amazon S3 Storage Lens group | Read |  storagelensgroup* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[InitiateReplication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html) [permission only] | Grants permission to initiate the replication process by setting replication status of an object to pending | Write |  object* |  |   
|  s3:ResourceAccount |   
[ListAccessGrants](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrants.html) | Grants permission to list Access Grant | List |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[ListAccessGrantsInstances](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstances.html) | Grants permission to List Access Grants Instances | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListAccessGrantsLocations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocations.html) | Grants permission to list Access Grants locations | List |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html) | Grants permission to list access points | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListAccessPointsForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html) | Grants permission to list object lambda enabled accesspoints | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListAllMyBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) | Grants permission to list all buckets owned by the authenticated sender of the request | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) | Grants permission to list some or all of the objects in an Amazon S3 bucket (up to 1000) | List |  bucket* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:delimiter s3:max-keys s3:prefix s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListBucketMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html) | Grants permission to list in-progress multipart uploads | List |  bucket* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListBucketVersions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html) | Grants permission to list metadata about all the versions of objects in an Amazon S3 bucket | List |  bucket* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:delimiter s3:max-keys s3:prefix s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListCallerAccessGrants](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrants.html) | Grants permission to list caller's Access Grant | List |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html) | Grants permission to list current jobs and jobs that have ended recently | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html) | Grants permission to list Multi-Region Access Points | List |  |  s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[ListMultipartUploadParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html) | Grants permission to list the parts that have been uploaded for a specific multipart upload | List |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListStorageLensConfigurations](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurations.html) | Grants permission to list Amazon S3 Storage Lens configurations | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListStorageLensGroups](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html) | Grants permission to list S3 Storage Lens groups | List |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html) | Grants permission to list the tags attached to the specified resource | List |  accessgrant |  |   
accessgrantsinstance |  |   
accessgrantslocation |  |   
storagelensgroup |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ObjectOwnerOverrideToBucketOwner](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-change-owner.html#repl-ownership-add-role-permission) | Grants permission to change replica ownership | Permissions management |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PauseReplication](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#bucket-pause-replication) [permission only] | Grants permission to pause S3 Replication from target source buckets to destination buckets | Write |  bucket* |  |  s3:GetReplicationConfiguration  s3:PutReplicationConfiguration   
|  s3:destinationRegion s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutAccelerateConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html) | Grants permission to use the accelerate subresource to set the Transfer Acceleration state of an existing S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutAccessGrantsInstanceResourcePolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessGrantsInstanceResourcePolicy.html) | Grants permission to put Access grants instance resource policy | Write |  accessgrantsinstance* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[PutAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointConfigurationForObjectLambda.html) | Grants permission to set the configuration of the object lambda enabled access point | Write |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointArn s3:DataAccessPointAccount s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html) | Grants permission to associate an access policy with a specified access point | Permissions management |  accesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html) | Grants permission to associate an access policy with a specified object lambda enabled access point | Permissions management |  objectlambdaaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutAccessPointPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html#access-control-block-public-access-examples-access-point) | Grants permission to associate public access block configurations with a specified access point, while creating a access point | Permissions management |  |  |   
[PutAccountPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html) | Grants permission to create or modify the PublicAccessBlock configuration for an AWS account | Permissions management |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutAnalyticsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html) | Grants permission to set an analytics configuration for the bucket, specified by the analytics configuration ID | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html) | Grants permission to set the permissions on an existing bucket using access control lists (ACLs) | Permissions management |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-acl s3:x-amz-content-sha256 s3:x-amz-grant-full-control s3:x-amz-grant-read s3:x-amz-grant-read-acp s3:x-amz-grant-write s3:x-amz-grant-write-acp |   
[PutBucketCORS](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html) | Grants permission to set the CORS configuration for an Amazon S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketLogging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html) | Grants permission to set the logging parameters for an Amazon S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketNotification](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html) | Grants permission to receive notifications when certain events happen in an Amazon S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketObjectLockConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html) | Grants permission to put Object Lock configuration on a specific bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:TlsVersion s3:signatureversion |   
[PutBucketOwnershipControls](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketOwnershipControls.html) | Grants permission to add, replace or delete ownership controls on a bucket | Permissions management |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html) | Grants permission to add or replace a bucket policy on a bucket | Permissions management |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html) | Grants permission to create or modify the PublicAccessBlock configuration for a specific Amazon S3 bucket | Permissions management |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketRequestPayment](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html) | Grants permission to set the request payment configuration of a bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html) | Grants permission to add a set of tags to an existing Amazon S3 bucket | Tagging |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) | Grants permission to set the versioning state of an existing Amazon S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutBucketWebsite](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html) | Grants permission to set the configuration of the website that is specified in the website subresource | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutEncryptionConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) | Grants permission to set the encryption configuration for an Amazon S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutIntelligentTieringConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html) | Grants permission to create new or update or delete an existing Amazon S3 Intelligent Tiering configuration | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutInventoryConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html) | Grants permission to add an inventory configuration to the bucket, identified by the inventory ID | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:InventoryAccessibleOptionalFields |   
[PutJobTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html) | Grants permission to replace tags on an existing Amazon S3 Batch Operations job | Tagging |  job* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:ExistingJobPriority s3:ExistingJobOperation aws:TagKeys aws:RequestTag/${TagKey} |   
[PutLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html) | Grants permission to create a new lifecycle configuration for the bucket or replace an existing lifecycle configuration | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html) | Grants permission to set or update a metrics configuration for the CloudWatch request metrics from an Amazon S3 bucket | Write |  bucket* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutMultiRegionAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html) | Grants permission to associate an access policy with a specified Multi-Region Access Point | Permissions management |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) | Grants permission to add an object to a bucket | Write |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:RequestObjectTag/<key> s3:RequestObjectTagKeys s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-acl s3:x-amz-content-sha256 s3:x-amz-copy-source s3:x-amz-grant-full-control s3:x-amz-grant-read s3:x-amz-grant-read-acp s3:x-amz-grant-write s3:x-amz-grant-write-acp s3:x-amz-metadata-directive s3:x-amz-server-side-encryption s3:x-amz-server-side-encryption-aws-kms-key-id s3:x-amz-server-side-encryption-customer-algorithm s3:x-amz-storage-class s3:x-amz-website-redirect-location s3:object-lock-mode s3:object-lock-retain-until-date s3:object-lock-remaining-retention-days s3:object-lock-legal-hold s3:if-match s3:if-none-match s3:ObjectCreationOperation |   
[PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) | Grants permission to set the access control list (ACL) permissions for new or existing objects in an S3 bucket | Permissions management |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-acl s3:x-amz-content-sha256 s3:x-amz-grant-full-control s3:x-amz-grant-read s3:x-amz-grant-read-acp s3:x-amz-grant-write s3:x-amz-grant-write-acp s3:x-amz-storage-class |   
[PutObjectLegalHold](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html) | Grants permission to apply a Legal Hold configuration to the specified object | Write |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:object-lock-legal-hold |   
[PutObjectRetention](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html) | Grants permission to place an Object Retention configuration on an object | Write |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:object-lock-mode s3:object-lock-retain-until-date s3:object-lock-remaining-retention-days |   
[PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) | Grants permission to set the supplied tag-set to an object that already exists in a bucket | Tagging |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:RequestObjectTag/<key> s3:RequestObjectTagKeys s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[PutObjectVersionAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) | Grants permission to use the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket | Permissions management |  object* |  |   
|  s3:AccessGrantsInstanceArn s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-acl s3:x-amz-content-sha256 s3:x-amz-grant-full-control s3:x-amz-grant-read s3:x-amz-grant-read-acp s3:x-amz-grant-write s3:x-amz-grant-write-acp s3:x-amz-storage-class |   
[PutObjectVersionTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) | Grants permission to set the supplied tag-set for a specific version of an object | Tagging |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:ExistingObjectTag/<key> s3:RequestObjectTag/<key> s3:RequestObjectTagKeys s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:versionid s3:x-amz-content-sha256 |   
[PutReplicationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html) | Grants permission to create a new replication configuration or replace an existing one | Write |  bucket* |  |  iam:PassRole   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:isReplicationPauseRequest |   
[PutStorageLensConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html) | Grants permission to create or update an Amazon S3 Storage Lens configuration | Write |  |  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:TagKeys aws:RequestTag/${TagKey} |   
[PutStorageLensConfigurationTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfigurationTagging.html) | Grants permission to put or replace tags on an existing Amazon S3 Storage Lens configuration | Tagging |  storagelensconfiguration* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:TagKeys aws:RequestTag/${TagKey} |   
[ReplicateDelete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html) | Grants permission to replicate delete markers to the destination bucket | Write |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[ReplicateObject](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html) | Grants permission to replicate objects and object tags to the destination bucket | Write |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:x-amz-server-side-encryption s3:x-amz-server-side-encryption-aws-kms-key-id s3:x-amz-server-side-encryption-customer-algorithm |   
[ReplicateTags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html) | Grants permission to replicate object tags to the destination bucket | Tagging |  object* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) | Grants permission to restore an archived copy of an object back into Amazon S3 | Write |  object* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
[SubmitMultiRegionAccessPointRoutes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SubmitMultiRegionAccessPointRoutes.html) | Grants permission to submit a route configuration update for a Multi-Region Access Point | Write |  multiregionaccesspoint* |  |   
|  s3:DataAccessPointAccount s3:DataAccessPointArn s3:AccessPointNetworkOrigin s3:authType s3:ResourceAccount s3:signatureversion s3:signatureAge s3:TlsVersion |   
[TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) | Grants permission to add tags to the specified resource | Tagging |  accessgrant |  |   
accessgrantsinstance |  |   
accessgrantslocation |  |   
storagelensgroup |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:TagKeys aws:RequestTag/${TagKey} |   
[UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) | Grants permission to remove tags from the specified resource | Tagging |  accessgrant |  |   
accessgrantsinstance |  |   
accessgrantslocation |  |   
storagelensgroup |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:TagKeys |   
[UpdateAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateAccessGrantsLocation.html) | Grants permission to update Access Grants location | Write |  accessgrantslocation* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 aws:ResourceTag/${TagKey} |   
[UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html) | Grants permission to update the priority of an existing job | Write |  job* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:RequestJobPriority s3:ExistingJobPriority s3:ExistingJobOperation |   
[UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html) | Grants permission to update the status for the specified job | Write |  job* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 s3:ExistingJobPriority s3:ExistingJobOperation s3:JobSuspendedCause |   
[UpdateStorageLensGroup](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateStorageLensGroup.html) | Grants permission to update an existing S3 Storage Lens group | Write |  storagelensgroup* |  |   
|  s3:authType s3:ResourceAccount s3:signatureAge s3:signatureversion s3:TlsVersion s3:x-amz-content-sha256 |   
  
## Resource types defined by Amazon S3

The following resource types are defined by this service and can be used in
the `Resource` element of IAM permission policy statements. Each action in the
Actions table identifies the resource types that can be specified with that
action. A resource type can also define which condition keys you can include
in a policy. These keys are displayed in the last column of the table. For
details about the columns in the following table, see [Resource types
table](reference_policies_actions-resources-contextkeys.html#resources_table).

Resource types | ARN | Condition keys  
---|---|---  
[accesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) |  `arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}` |   
[bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) |  `arn:${Partition}:s3:::${BucketName}` |   
[object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html) |  `arn:${Partition}:s3:::${BucketName}/${ObjectName}` |   
[job](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-managing-jobs.html) |  `arn:${Partition}:s3:${Region}:${Account}:job/${JobId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys  
[storagelensconfiguration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) |  `arn:${Partition}:s3:${Region}:${Account}:storage-lens/${ConfigId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys  
[storagelensgroup](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_group.html) |  `arn:${Partition}:s3:${Region}:${Account}:storage-lens-group/${Name}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys  
[objectlambdaaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html) |  `arn:${Partition}:s3-object-lambda:${Region}:${Account}:accesspoint/${AccessPointName}` |   
[multiregionaccesspoint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html) |  `arn:${Partition}:s3::${Account}:accesspoint/${AccessPointAlias}` |   
[multiregionaccesspointrequestarn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html) |  `arn:${Partition}:s3:us-west-2:${Account}:async-request/mrap/${Operation}/${Token}` |   
[accessgrantsinstance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-instance.html) |  `arn:${Partition}:s3:${Region}:${Account}:access-grants/default` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys  
[accessgrantslocation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html) |  `arn:${Partition}:s3:${Region}:${Account}:access-grants/default/location/${Token}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys  
[accessgrant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant.html) |  `arn:${Partition}:s3:${Region}:${Account}:access-grants/default/grant/${Token}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys  
  
## Condition keys for Amazon S3

Amazon S3 defines the following condition keys that can be used in the
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
[s3:AccessGrantsInstanceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-grants-instance.html) | Filters access by access grants instance ARN | ARN  
[s3:AccessPointNetworkOrigin](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies) | Filters access by the network origin (Internet or VPC) | String  
[s3:DataAccessPointAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies) | Filters access by the AWS Account ID that owns the access point | String  
[s3:DataAccessPointArn](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-access-points.html#access-points-policies) | Filters access by an access point Amazon Resource Name (ARN) | ARN  
[s3:ExistingJobOperation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html) | Filters access by operation to updating the job priority | String  
[s3:ExistingJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html) | Filters access by priority range to cancelling existing jobs | Numeric  
[s3:ExistingObjectTag/<key>](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies) | Filters access by existing object tag key and value | String  
[s3:InventoryAccessibleOptionalFields](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-s3-inventory-2) | Filters access by restricting which optional metadata fields a user can add when configuring S3 Inventory reports | ArrayOfString  
[s3:JobSuspendedCause](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html) | Filters access by a specific job suspended cause (for example, AWAITING_CONFIRMATION) to cancelling suspended jobs | String  
[s3:ObjectCreationOperation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html) | Filters access by whether or not the operation creates an object | Bool  
[s3:RequestJobOperation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html) | Filters access by operation to creating jobs | String  
[s3:RequestJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-job-tags-examples.html) | Filters access by priority range to creating new jobs | Numeric  
[s3:RequestObjectTag/<key>](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies) | Filters access by the tag keys and values to be added to objects | String  
[s3:RequestObjectTagKeys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html#tagging-and-policies) | Filters access by the tag keys to be added to objects | ArrayOfString  
[s3:ResourceAccount](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-object-resource-account) | Filters access by the resource owner AWS account ID | String  
[s3:TlsVersion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-object-tls-version) | Filters access by the TLS version used by the client | Numeric  
[s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) | Filters access by authentication method | String  
[s3:delimiter](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html) | Filters access by delimiter parameter | String  
[s3:destinationRegion](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) | Filters access by a specific replication destination region for targeted buckets of the AWS FIS action aws:s3:bucket-pause-replication | String  
[s3:if-match](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html) | Filters access by the request's 'If-Match' conditional header | String  
[s3:if-none-match](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes-enforce.html) | Filters access by the request's 'If-None-Match' conditional header | String  
[s3:isReplicationPauseRequest](https://docs.aws.amazon.com/fis/latest/userguide/security_iam_id-based-policy-examples.html#security-iam-policy-examples-s3) | Filters access by request made via AWS FIS action aws:s3:bucket-pause-replication | Bool  
[s3:locationconstraint](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#condition-key-bucket-ops-1) | Filters access by a specific Region | String  
[s3:max-keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#example-numeric-condition-operators) | Filters access by maximum number of keys returned in a ListBucket request | Numeric  
[s3:object-lock-legal-hold](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-legal-holds) | Filters access by object legal hold status | String  
[s3:object-lock-mode](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-modes) | Filters access by object retention mode (COMPLIANCE or GOVERNANCE) | String  
[s3:object-lock-remaining-retention-days](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-managing.html#object-lock-managing-retention-limits) | Filters access by remaining object retention days | Numeric  
[s3:object-lock-retain-until-date](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html#object-lock-retention-periods) | Filters access by object retain-until date | Date  
[s3:prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#condition-key-bucket-ops-2) | Filters access by key name prefix | String  
[s3:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) | Filters access by the age in milliseconds of the request signature | Numeric  
[s3:signatureversion](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) | Filters access by the version of AWS Signature used on the request | String  
[s3:versionid](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#getobjectversion-limit-access-to-specific-version-3) | Filters access by a specific object version | String  
[s3:x-amz-acl](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions) | Filters access by canned ACL in the request's x-amz-acl header | String  
[s3:x-amz-content-sha256](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) | Filters access by unsigned content in your bucket | String  
[s3:x-amz-copy-source](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html#putobject-limit-copy-source-3) | Filters access by copy source bucket, prefix, or object in the copy object requests | String  
[s3:x-amz-grant-full-control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions) | Filters access by x-amz-grant-full-control (full control) header | String  
[s3:x-amz-grant-read](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions) | Filters access by x-amz-grant-read (read access) header | String  
[s3:x-amz-grant-read-acp](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions) | Filters access by the x-amz-grant-read-acp (read permissions for the ACL) header | String  
[s3:x-amz-grant-write](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions) | Filters access by the x-amz-grant-write (write access) header | String  
[s3:x-amz-grant-write-acp](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#permissions) | Filters access by the x-amz-grant-write-acp (write permissions for the ACL) header | String  
[s3:x-amz-metadata-directive](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) | Filters access by object metadata behavior (COPY or REPLACE) when objects are copied | String  
[s3:x-amz-object-ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ensure-object-ownership.html#object-ownership-requiring-bucket-owner-enforced) | Filters access by Object Ownership | String  
[s3:x-amz-server-side-encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) | Filters access by server-side encryption | String  
[s3:x-amz-server-side-encryption-aws-kms-key-id](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html#require-sse-kms) | Filters access by AWS KMS customer managed CMK for server-side encryption | ARN  
[s3:x-amz-server-side-encryption-customer-algorithm](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) | Filters access by customer specified algorithm for server-side encryption | String  
[s3:x-amz-storage-class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-howtoset) | Filters access by storage class | String  
[s3:x-amz-website-redirect-location](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html#page-redirect-using-rest-api) | Filters access by a specific website redirect location for buckets that are configured as static websites | String  
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Previous

Next

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

