# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html'}

[Documentation](/index.html)[Service Authorization
Reference](/iam/index.html)[Service Authorization
Reference](list_amazonrds.html)

ActionsResource typesCondition keys

# Actions, resources, and condition keys for Amazon RDS

Amazon RDS (service prefix: `rds`) provides the following service-specific
resources, actions, and condition context keys for use in IAM permission
policies.

References:

  * Learn how to [configure this service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/).

  * View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/).

  * Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html) permission policies.

###### Topics

  * Actions defined by Amazon RDS
  * Resource types defined by Amazon RDS
  * Condition keys for Amazon RDS

## Actions defined by Amazon RDS

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
[AddRoleToDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddRoleToDBCluster.html) | Grants permission to associate an Identity and Access Management (IAM) role from an Aurora DB cluster | Write |  cluster* |  |  iam:PassRole   
[AddRoleToDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddRoleToDBInstance.html) | Grants permission to associate an AWS Identity and Access Management (IAM) role with a DB instance | Write |  db* |  |  iam:PassRole   
[AddSourceIdentifierToSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddSourceIdentifierToSubscription.html) | Grants permission to add a source identifier to an existing RDS event notification subscription | Write |  es* |  |   
[AddTagsToResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddTagsToResource.html) | Grants permission to add metadata tags to an Amazon RDS resource | Tagging |  cev |  |   
cluster |  |   
cluster-endpoint |  |   
cluster-pg |  |   
cluster-snapshot |  |   
db |  |   
deployment |  |   
es |  |   
integration |  |   
og |  |   
pg |  |   
proxy |  |   
proxy-endpoint |  |   
ri |  |   
secgrp |  |   
shardgrp |  |   
snapshot |  |   
snapshot-tenant-database |  |   
subgrp |  |   
target-group |  |   
tenant-database |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ApplyPendingMaintenanceAction.html) | Grants permission to apply a pending maintenance action to a resource | Write |  cluster |  |   
db |  |   
[AuthorizeDBSecurityGroupIngress](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AuthorizeDBSecurityGroupIngress.html) | Grants permission to enable ingress to a DBSecurityGroup using one of two forms of authorization | Permissions management |  secgrp* |  |   
[BacktrackDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_BacktrackDBCluster.html) | Grants permission to backtrack a DB cluster to a specific time, without creating a new DB cluster | Write |  cluster* |  |   
[CancelExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CancelExportTask.html) | Grants permission to cancel an export task in progress | Write |  |  |   
[CopyCustomDBEngineVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html) [permission only] | Grants permission to copy a custom engine version | Write |  cev* |  |   
[CopyDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBClusterParameterGroup.html) | Grants permission to copy the specified DB cluster parameter group | Write |  cluster-pg* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CopyDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBClusterSnapshot.html) | Grants permission to create a snapshot of a DB cluster | Write |  cluster-snapshot* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CopyDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBParameterGroup.html) | Grants permission to copy the specified DB parameter group | Write |  pg* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CopyDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyDBSnapshot.html) | Grants permission to copy the specified DB snapshot | Write |  snapshot* |  |  rds:AddTagsToResource  rds:CopyCustomDBEngineVersion   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:CopyOptionGroup |   
[CopyOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CopyOptionGroup.html) | Grants permission to copy the specified option group | Write |  og* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateBlueGreenDeployment](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateBlueGreenDeployment.html) | Grants permission to create a blue-green deployment for a given source cluster or instance | Write |  deployment* |  |  rds:AddTagsToResource  rds:CreateDBCluster  rds:CreateDBClusterEndpoint  rds:CreateDBInstance  rds:CreateDBInstanceReadReplica   
cluster |  |   
cluster-pg |  |   
db |  |   
pg |  |   
|  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys rds:cluster-tag/${TagKey} rds:cluster-pg-tag/${TagKey} rds:db-tag/${TagKey} rds:pg-tag/${TagKey} rds:req-tag/${TagKey} rds:DatabaseEngine rds:DatabaseName rds:StorageEncrypted rds:DatabaseClass rds:StorageSize rds:MultiAz rds:Piops rds:Vpc |   
[CreateCustomDBEngineVersion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateCustomDBEngineVersion.html) | Grants permission to create a custom engine version | Write |  cev* |  |  iam:CreateServiceLinkedRole  mediaimport:CreateDatabaseBinarySnapshot  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) | Grants permission to create a new DB cluster | Write |  cluster* |  |  iam:PassRole  kms:CreateGrant  kms:Decrypt  kms:DescribeKey  kms:GenerateDataKey  rds:AddTagsToResource  rds:CreateDBInstance  secretsmanager:CreateSecret  secretsmanager:TagResource   
cluster-pg* |  |   
og* |  |   
subgrp* |  |   
db |  |   
global-cluster |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} rds:DatabaseEngine rds:DatabaseName rds:StorageEncrypted rds:DatabaseClass rds:StorageSize rds:Piops rds:ManageMasterUserPassword |   
[CreateDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterEndpoint.html) | Grants permission to create a new custom endpoint and associates it with an Amazon Aurora DB cluster or Amazon DocumentDB cluster | Write |  cluster* |  |  rds:AddTagsToResource   
cluster-endpoint* |  |   
|  rds:EndpointType aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterParameterGroup.html) | Grants permission to create a new DB cluster parameter group | Write |  cluster-pg* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBClusterSnapshot.html) | Grants permission to create a snapshot of a DB cluster | Write |  cluster* |  |  rds:AddTagsToResource   
cluster-snapshot* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) | Grants permission to create a new DB instance | Write |  db* |  |  iam:PassRole  kms:CreateGrant  kms:Decrypt  kms:DescribeKey  kms:GenerateDataKey  rds:AddTagsToResource  rds:CreateTenantDatabase  secretsmanager:CreateSecret  secretsmanager:TagResource   
cluster |  |   
og |  |   
pg |  |   
secgrp |  |   
subgrp |  |   
|  rds:BackupTarget aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} rds:ManageMasterUserPassword |   
[CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html) | Grants permission to create a DB instance that acts as a Read Replica of a source DB instance | Write |  cluster* |  |  iam:PassRole  rds:AddTagsToResource   
db* |  |   
og* |  |   
pg* |  |   
subgrp* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBParameterGroup.html) | Grants permission to create a new DB parameter group | Write |  pg* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBProxy.html) | Grants permission to create a database proxy | Write |  |  aws:RequestTag/${TagKey} aws:TagKeys |  iam:PassRole   
[CreateDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBProxyEndpoint.html) | Grants permission to create a database proxy endpoint | Write |  proxy* |  |   
proxy-endpoint* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateDBSecurityGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSecurityGroup.html) | Grants permission to create a new DB security group. DB security groups control access to a DB instance | Write |  secgrp* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBShardGroup.html) | Grants permission to create a new Aurora Limitless Database DB shard group | Write |  cluster* |  |  rds:AddTagsToResource   
shardgrp* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[CreateDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSnapshot.html) | Grants permission to create a DBSnapshot | Write |  db* |  |  rds:AddTagsToResource   
snapshot* |  |   
|  rds:BackupTarget aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateDBSubnetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSubnetGroup.html) | Grants permission to create a new DB subnet group | Write |  subgrp* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateEventSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateEventSubscription.html) | Grants permission to create an RDS event notification subscription | Write |  es* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateGlobalCluster.html) | Grants permission to create an Aurora global database or DocumentDB global database spread across multiple regions | Write |  cluster* |  |   
global-cluster* |  |   
[CreateIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateIntegration.html) | Grants permission to create an Aurora zero-ETL integration with Redshift | Write |  cluster* |  |  kms:CreateGrant  kms:DescribeKey  rds:AddTagsToResource   
integration* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateOptionGroup.html) | Grants permission to create a new option group | Write |  og* |  |  rds:AddTagsToResource   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[CreateTenantDatabase](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateTenantDatabase.html) | Grants permission to create a new tenant database | Write |  db* |  |  rds:AddTagsToResource   
tenant-database* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:TenantDatabaseName |   
[CrossRegionCommunication](https://docs.aws.amazon.com/AmazonRDS/latest/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) [permission only] | Grants permission to access a resource in the remote Region when executing cross-Region operations, such as cross-Region snapshot copy or cross-Region read replica creation | Write |  |  |   
[DeleteBlueGreenDeployment](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteBlueGreenDeployment.html) | Grants permission to delete blue green deployments | Write |  deployment* |  |  rds:DeleteDBCluster  rds:DeleteDBClusterEndpoint  rds:DeleteDBInstance  rds:PromoteReadReplica  rds:PromoteReadReplicaDBCluster   
|  aws:ResourceTag/${TagKey} |   
[DeleteCustomDBEngineVersion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteCustomDBEngineVersion.html) | Grants permission to delete an existing custom engine version | Write |  cev* |  |   
[DeleteDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBCluster.html) | Grants permission to delete a previously provisioned DB cluster | Write |  cluster* |  |  rds:AddTagsToResource  rds:CreateDBClusterSnapshot  rds:DeleteDBInstance   
cluster-snapshot* |  |   
[DeleteDBClusterAutomatedBackup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterAutomatedBackup.html) | Grants permission to delete cluster automated backups based on the source cluster's DbClusterResourceId value or the restorable cluster's resource ID | Write |  cluster-auto-backup* |  |   
[DeleteDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterEndpoint.html) | Grants permission to delete a custom endpoint and removes it from an Amazon Aurora DB cluster or Amazon DocumentDB cluster | Write |  cluster-endpoint* |  |   
[DeleteDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterParameterGroup.html) | Grants permission to delete a specified DB cluster parameter group | Write |  cluster-pg* |  |   
[DeleteDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterSnapshot.html) | Grants permission to delete a DB cluster snapshot | Write |  cluster-snapshot* |  |   
[DeleteDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBInstance.html) | Grants permission to delete a previously provisioned DB instance | Write |  db* |  |  rds:AddTagsToResource  rds:CreateDBSnapshot  rds:DeleteTenantDatabase   
[DeleteDBInstanceAutomatedBackup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBInstanceAutomatedBackup.html) | Grants permission to delete automated backups based on the source instance's DbiResourceId value or the restorable instance's resource ID | Write |  auto-backup* |  |   
[DeleteDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBParameterGroup.html) | Grants permission to delete a specified DBParameterGroup | Write |  pg* |  |   
[DeleteDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBProxy.html) | Grants permission to delete a database proxy | Write |  proxy* |  |   
[DeleteDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBProxyEndpoint.html) | Grants permission to delete a database proxy endpoint | Write |  proxy-endpoint* |  |   
[DeleteDBSecurityGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBSecurityGroup.html) | Grants permission to delete a DB security group | Write |  secgrp* |  |   
[DeleteDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBShardGroup.html) | Grants permission to delete an Aurora Limitless Database DB shard group | Write |  shardgrp* |  |   
[DeleteDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBSnapshot.html) | Grants permission to delete a DBSnapshot | Write |  snapshot* |  |   
[DeleteDBSubnetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBSubnetGroup.html) | Grants permission to delete a DB subnet group | Write |  subgrp* |  |   
[DeleteEventSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteEventSubscription.html) | Grants permission to delete an RDS event notification subscription | Write |  es* |  |   
[DeleteGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteGlobalCluster.html) | Grants permission to delete a global database cluster | Write |  global-cluster* |  |   
[DeleteIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteIntegration.html) | Grants permission to delete an Aurora zero-ETL integration with Redshift | Write |  integration* |  |   
[DeleteOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteOptionGroup.html) | Grants permission to delete an existing option group | Write |  og* |  |   
[DeleteTenantDatabase](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteTenantDatabase.html) | Grants permission to delete a tenant database | Write |  db* |  |  rds:AddTagsToResource  rds:CreateDBSnapshot   
tenant-database* |  |   
[DeregisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeregisterDBProxyTargets.html) | Grants permission to remove targets from a database proxy target group | Write |  cluster* |  |   
db* |  |   
proxy* |  |   
target-group* |  |   
[DescribeAccountAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeAccountAttributes.html) | Grants permission to list all of the attributes for a customer account | List |  |  |   
[DescribeBlueGreenDeployments](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeBlueGreenDeployments.html) | Grants permission to describe blue green deployments | List |  deployment |  |   
[DescribeCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeCertificates.html) | Grants permission to list the set of CA certificates provided by Amazon RDS for this AWS account | List |  |  |   
[DescribeDBClusterAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterAutomatedBackups.html) | Grants permission to return a list of cluster automated backups for both current and deleted clusters | List |  cluster-auto-backup* |  |   
cluster |  |   
[DescribeDBClusterBacktracks](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterBacktracks.html) | Grants permission to return information about backtracks for a DB cluster | List |  cluster* |  |   
[DescribeDBClusterEndpoints](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterEndpoints.html) | Grants permission to return information about endpoints for an Amazon Aurora DB cluster | List |  cluster |  |   
cluster-endpoint |  |   
[DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterParameterGroups.html) | Grants permission to return a list of DBClusterParameterGroup descriptions | List |  cluster-pg* |  |   
[DescribeDBClusterParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterParameters.html) | Grants permission to return the detailed parameter list for a particular DB cluster parameter group | List |  cluster-pg* |  |   
[DescribeDBClusterSnapshotAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterSnapshotAttributes.html) | Grants permission to return a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot | List |  cluster-snapshot* |  |   
[DescribeDBClusterSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterSnapshots.html) | Grants permission to return information about DB cluster snapshots | List |  cluster |  |   
cluster-snapshot |  |   
[DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) | Grants permission to return information about provisioned Aurora DB clusters or DocumentDB clusters | List |  cluster* |  |   
[DescribeDBEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBEngineVersions.html) | Grants permission to return a list of the available DB engines | List |  |  |   
[DescribeDBInstanceAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstanceAutomatedBackups.html) | Grants permission to return a list of automated backups for both current and deleted instances | List |  auto-backup |  |   
db |  |   
[DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) | Grants permission to return information about provisioned RDS instances | List |  db* |  |   
[DescribeDBLogFiles](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBLogFiles.html) | Grants permission to return a list of DB log files for the DB instance | List |  db* |  |   
[DescribeDBParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameterGroups.html) | Grants permission to return a list of DBParameterGroup descriptions | List |  pg* |  |   
[DescribeDBParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBParameters.html) | Grants permission to return the detailed parameter list for a particular DB parameter group | List |  pg* |  |   
[DescribeDBProxies](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxies.html) | Grants permission to view proxies | List |  proxy* |  |   
[DescribeDBProxyEndpoints](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyEndpoints.html) | Grants permission to view proxy endpoints | List |  proxy* |  |   
proxy-endpoint* |  |   
[DescribeDBProxyTargetGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyTargetGroups.html) | Grants permission to view database proxy target group details | List |  proxy* |  |   
[DescribeDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBProxyTargets.html) | Grants permission to view database proxy target details | List |  proxy* |  |   
target-group* |  |   
[DescribeDBRecommendations](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBRecommendations.html) | Grants permission to list recommendation details | List |  |  |   
[DescribeDBSecurityGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSecurityGroups.html) | Grants permission to return a list of DBSecurityGroup descriptions | List |  secgrp* |  |   
[DescribeDBShardGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBShardGroups.html) | Grants permission to return information about all Aurora Limitless Database DB shard groups for this account. You can filter by shard group(s) | List |  shardgrp* |  |   
[DescribeDBSnapshotAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshotAttributes.html) | Grants permission to return a list of DB snapshot attribute names and values for a manual DB snapshot | List |  snapshot* |  |   
[DescribeDBSnapshotTenantDatabases](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshotTenantDatabases.html) | Grants permission to return information about tenant databases in DB snapshots. You can filter by Region or snapshot | List |  snapshot-tenant-database* |  |   
db |  |   
snapshot |  |   
[DescribeDBSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshots.html) | Grants permission to return information about DB snapshots | List |  db |  |   
snapshot |  |   
[DescribeDBSubnetGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSubnetGroups.html) | Grants permission to return a list of DBSubnetGroup descriptions | List |  subgrp* |  |   
[DescribeEngineDefaultClusterParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEngineDefaultClusterParameters.html) | Grants permission to return the default engine and system parameter information for the cluster database engine | List |  |  |   
[DescribeEngineDefaultParameters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEngineDefaultParameters.html) | Grants permission to return the default engine and system parameter information for the specified database engine | List |  |  |   
[DescribeEventCategories](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventCategories.html) | Grants permission to display a list of categories for all event source types, or, if specified, for a specified source type | List |  |  |   
[DescribeEventSubscriptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEventSubscriptions.html) | Grants permission to list all the subscription descriptions for a customer account | List |  es* |  |   
[DescribeEvents](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html) | Grants permission to return events related to DB instances, DB security groups, DB snapshots, and DB parameter groups for the past 14 days | List |  |  |   
[DescribeExportTasks](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeExportTasks.html) | Grants permission to return information about the export tasks | List |  cluster |  |   
cluster-snapshot |  |   
snapshot |  |   
[DescribeGlobalClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeGlobalClusters.html) | Grants permission to return information about Aurora global database clusters or DocumentDB global database clusters | List |  global-cluster* |  |   
[DescribeIntegrations](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeIntegrations.html) | Grants permission to describe an Aurora zero-ETL integration with Redshift | List |  integration* |  |   
|  aws:ResourceTag/${TagKey} |   
[DescribeOptionGroupOptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOptionGroupOptions.html) | Grants permission to describe all available options | List |  |  |   
[DescribeOptionGroups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOptionGroups.html) | Grants permission to describe the available option groups | List |  og* |  |   
[DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeOrderableDBInstanceOptions.html) | Grants permission to return a list of orderable DB instance options for the specified engine | List |  |  |   
[DescribePendingMaintenanceActions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribePendingMaintenanceActions.html) | Grants permission to return a list of resources (for example, DB instances) that have at least one pending maintenance action | List |  cluster |  |   
db |  |   
[DescribeRecommendationGroups](https://docs.aws.amazon.com/AmazonRDS/latest/USER_Recommendations.html) [permission only] | Grants permission to return information about recommendation groups | Read |  |  |   
[DescribeRecommendations](https://docs.aws.amazon.com/AmazonRDS/latest/USER_Recommendations.html) [permission only] | Grants permission to return information about recommendations | Read |  |  |   
[DescribeReservedDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstances.html) | Grants permission to return information about reserved DB instances for this account, or about a specified reserved DB instance | List |  ri* |  |   
[DescribeReservedDBInstancesOfferings](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeReservedDBInstancesOfferings.html) | Grants permission to list available reserved DB instance offerings | List |  |  |   
[DescribeSourceRegions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeSourceRegions.html) | Grants permission to return a list of the source AWS Regions where the current AWS Region can create a Read Replica or copy a DB snapshot from | List |  |  |   
[DescribeTenantDatabases](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeTenantDatabases.html) | Grants permission to return information about provisioned tenant databases. You can filter by Region or snapshot | List |  tenant-database* |  |   
db |  |   
[DescribeValidDBInstanceModifications](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeValidDBInstanceModifications.html) | Grants permission to list available modifications you can make to your DB instance | List |  db* |  |   
[DisableHttpEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DisableHttpEndpoint.html) | Grants permission to disable http endpoint for a DB cluster | Write |  cluster* |  |   
[DownloadCompleteDBLogFile](https://docs.aws.amazon.com/AmazonRDS/latest/USER_LogAccess.html) | Grants permission to download specified log file | Read |  db* |  |   
[DownloadDBLogFilePortion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DownloadDBLogFilePortion.html) | Grants permission to download all or a portion of the specified log file, up to 1 MB in size | Read |  db* |  |   
[EnableHttpEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_EnableHttpEndpoint.html) | Grants permission to enable http endpoint for a DB cluster | Write |  cluster* |  |   
[FailoverDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_FailoverDBCluster.html) | Grants permission to force a failover for a DB cluster | Write |  cluster* |  |   
[FailoverGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_FailoverGlobalCluster.html) | Grants permission to failover a global cluster | Write |  cluster* |  |   
global-cluster* |  |   
[ListTagsForResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ListTagsForResource.html) | Grants permission to list all tags on an Amazon RDS resource | Read |  cev |  |   
cluster |  |   
cluster-endpoint |  |   
cluster-pg |  |   
cluster-snapshot |  |   
db |  |   
es |  |   
integration |  |   
og |  |   
pg |  |   
proxy |  |   
proxy-endpoint |  |   
ri |  |   
secgrp |  |   
shardgrp |  |   
snapshot |  |   
snapshot-tenant-database |  |   
subgrp |  |   
target-group |  |   
tenant-database |  |   
[ModifyActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyActivityStream.html) | Grants permission to modify a database activity stream | Write |  db* |  |   
[ModifyCertificates](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyCertificates.html) | Grants permission to modify the system-default Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificate for Amazon RDS for new DB instances | Write |  |  |   
[ModifyCurrentDBClusterCapacity](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyCurrentDBClusterCapacity.html) | Grants permission to modify current cluster capacity for an Amazon Aurora Serverless DB cluster | Write |  cluster* |  |   
[ModifyCustomDBEngineVersion](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyCustomDBEngineVersion.html) | Grants permission to modify an existing custom engine version | Write |  cev* |  |   
[ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) | Grants permission to modify a setting for an Amazon Aurora DB cluster or Amazon DocumentDB cluster | Write |  cluster* |  |  iam:PassRole  kms:CreateGrant  kms:Decrypt  kms:DescribeKey  kms:GenerateDataKey  rds:ModifyDBInstance  secretsmanager:CreateSecret  secretsmanager:RotateSecret  secretsmanager:TagResource   
cluster-pg |  |   
og |  |   
pg |  |   
|  rds:DatabaseClass rds:StorageSize rds:Piops rds:ManageMasterUserPassword |   
[ModifyDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterEndpoint.html) | Grants permission to modify the properties of an endpoint in an Amazon Aurora DB cluster or Amazon DocumentDB cluster | Write |  cluster-endpoint* |  |   
[ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterParameterGroup.html) | Grants permission to modify the parameters of a DB cluster parameter group | Write |  cluster-pg* |  |   
[ModifyDBClusterSnapshotAttribute](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBClusterSnapshotAttribute.html) | Grants permission to add an attribute and values to, or removes an attribute and values from, a manual DB cluster snapshot | Write |  cluster-snapshot* |  |   
[ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) | Grants permission to modify settings for a DB instance | Write |  db* |  |  iam:PassRole  kms:CreateGrant  kms:Decrypt  kms:DescribeKey  kms:GenerateDataKey  rds:AddTagsToResource  rds:CreateTenantDatabase  secretsmanager:CreateSecret  secretsmanager:RotateSecret  secretsmanager:TagResource   
og |  |   
pg |  |   
secgrp |  |   
subgrp |  |   
|  rds:ManageMasterUserPassword |   
[ModifyDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBParameterGroup.html) | Grants permission to modify the parameters of a DB parameter group | Write |  pg* |  |   
[ModifyDBProxy](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxy.html) | Grants permission to modify database proxy | Write |  proxy* |  |  iam:PassRole   
[ModifyDBProxyEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxyEndpoint.html) | Grants permission to modify database proxy endpoint | Write |  proxy-endpoint* |  |   
[ModifyDBProxyTargetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBProxyTargetGroup.html) | Grants permission to modify target group for a database proxy | Write |  target-group* |  |   
[ModifyDBRecommendation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBRecommendation.html) | Grants permission to modify recommendation | Write |  |  |   
[ModifyDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBShardGroup.html) | Grants permission to modify properties of an Aurora Limitless Database DB shard group | Write |  shardgrp* |  |   
[ModifyDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshot.html) | Grants permission to update a manual DB snapshot, which can be encrypted or not encrypted, with a new engine version | Write |  snapshot* |  |   
og |  |   
[ModifyDBSnapshotAttribute](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSnapshotAttribute.html) | Grants permission to add an attribute and values to, or removes an attribute and values from, a manual DB snapshot | Write |  snapshot* |  |   
[ModifyDBSubnetGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBSubnetGroup.html) | Grants permission to modify an existing DB subnet group | Write |  subgrp* |  |   
[ModifyEventSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyEventSubscription.html) | Grants permission to modify an existing RDS event notification subscription | Write |  es* |  |   
[ModifyGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyGlobalCluster.html) | Grants permission to modify a setting for an Amazon Aurora global cluster or Amazon DocumentDB global cluster | Write |  global-cluster* |  |   
[ModifyIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyIntegration.html) | Grants permission to modify an Aurora zero-ETL integration with Redshift | Write |  integration* |  |   
[ModifyOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyOptionGroup.html) | Grants permission to modify an existing option group | Write |  og* |  |  iam:PassRole   
[ModifyRecommendation](https://docs.aws.amazon.com/AmazonRDS/latest/USER_Recommendations.html) [permission only] | Grants permission to modify recommendation | Write |  |  |   
[ModifyTenantDatabase](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyTenantDatabase.html) | Grants permission to modify a tenant database | Write |  db* |  |   
tenant-database* |  |   
|  rds:TenantDatabaseName |   
[PromoteReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PromoteReadReplica.html) | Grants permission to promote a Read Replica DB instance to a standalone DB instance | Write |  db* |  |   
[PromoteReadReplicaDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PromoteReadReplicaDBCluster.html) | Grants permission to promote a Read Replica DB cluster to a standalone DB cluster | Write |  cluster* |  |   
[PurchaseReservedDBInstancesOffering](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PurchaseReservedDBInstancesOffering.html) | Grants permission to purchase a reserved DB instance offering | Write |  ri* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys |   
[RebootDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBCluster.html) | Grants permission to reboot a previously provisioned DB cluster | Write |  cluster* |  |  rds:RebootDBInstance   
[RebootDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBInstance.html) | Grants permission to restart the database engine service | Write |  db* |  |   
[RebootDBShardGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBShardGroup.html) | Grants permission to reboot an Aurora Limitless Database DB shard group | Write |  shardgrp* |  |   
[RegisterDBProxyTargets](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RegisterDBProxyTargets.html) | Grants permission to add targets to a database proxy target group | Write |  target-group* |  |   
[RemoveFromGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveFromGlobalCluster.html) | Grants permission to detach an Aurora secondary cluster from an Aurora global database cluster or DocumentDB global cluster | Write |  cluster* |  |   
global-cluster* |  |   
[RemoveRoleFromDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveRoleFromDBCluster.html) | Grants permission to disassociate an AWS Identity and Access Management (IAM) role from an Amazon Aurora DB cluster | Write |  cluster* |  |  iam:PassRole   
[RemoveRoleFromDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveRoleFromDBInstance.html) | Grants permission to disassociate an AWS Identity and Access Management (IAM) role from a DB instance | Write |  db* |  |  iam:PassRole   
[RemoveSourceIdentifierFromSubscription](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveSourceIdentifierFromSubscription.html) | Grants permission to remove a source identifier from an existing RDS event notification subscription | Write |  es* |  |   
[RemoveTagsFromResource](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveTagsFromResource.html) | Grants permission to remove metadata tags from an Amazon RDS resource | Tagging |  cev |  |   
cluster |  |   
cluster-endpoint |  |   
cluster-pg |  |   
cluster-snapshot |  |   
db |  |   
deployment |  |   
es |  |   
integration |  |   
og |  |   
pg |  |   
proxy |  |   
proxy-endpoint |  |   
ri |  |   
secgrp |  |   
shardgrp |  |   
snapshot |  |   
snapshot-tenant-database |  |   
subgrp |  |   
target-group |  |   
tenant-database |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[ResetDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBClusterParameterGroup.html) | Grants permission to modify the parameters of a DB cluster parameter group to the default value | Write |  cluster-pg* |  |   
[ResetDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ResetDBParameterGroup.html) | Grants permission to modify the parameters of a DB parameter group to the engine/system default value | Write |  pg* |  |   
[RestoreDBClusterFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromS3.html) | Grants permission to create an Amazon Aurora DB cluster from data stored in an Amazon S3 bucket | Write |  cluster* |  |  iam:PassRole  kms:CreateGrant  kms:Decrypt  kms:DescribeKey  kms:GenerateDataKey  rds:AddTagsToResource  secretsmanager:CreateSecret  secretsmanager:TagResource   
cluster-pg* |  |   
og* |  |   
subgrp* |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} rds:DatabaseEngine rds:DatabaseName rds:StorageEncrypted rds:ManageMasterUserPassword |   
[RestoreDBClusterFromSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.html) | Grants permission to create a new DB cluster from a DB cluster snapshot | Write |  cluster* |  |  iam:PassRole  rds:AddTagsToResource  rds:CreateDBInstance   
cluster-pg* |  |   
og* |  |   
subgrp* |  |   
cluster-snapshot |  |   
snapshot |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} rds:DatabaseClass rds:StorageSize rds:Piops |   
[RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.html) | Grants permission to restore a DB cluster to an arbitrary point in time | Write |  cluster* |  |  iam:PassRole  rds:AddTagsToResource  rds:CreateDBInstance   
cluster-pg* |  |   
og* |  |   
subgrp* |  |   
cluster-auto-backup |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} rds:DatabaseClass rds:StorageSize rds:Piops |   
[RestoreDBInstanceFromDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html) | Grants permission to create a new DB instance from a DB snapshot | Write |  db* |  |  iam:PassRole  rds:AddTagsToResource  rds:CreateTenantDatabase   
og* |  |   
pg* |  |   
subgrp* |  |   
cluster-snapshot |  |   
snapshot |  |   
|  rds:BackupTarget aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[RestoreDBInstanceFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html) | Grants permission to create a new DB instance from an Amazon S3 bucket | Write |  db* |  |  iam:PassRole  kms:CreateGrant  kms:Decrypt  kms:DescribeKey  kms:GenerateDataKey  rds:AddTagsToResource  secretsmanager:CreateSecret  secretsmanager:TagResource   
og* |  |   
pg* |  |   
subgrp* |  |   
secgrp |  |   
|  aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} rds:ManageMasterUserPassword |   
[RestoreDBInstanceToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html) | Grants permission to restore a DB instance to an arbitrary point in time | Write |  db* |  |  iam:PassRole  rds:AddTagsToResource  rds:CreateTenantDatabase   
og* |  |   
pg* |  |   
subgrp* |  |   
auto-backup |  |   
|  rds:BackupTarget aws:RequestTag/${TagKey} aws:TagKeys rds:req-tag/${TagKey} |   
[RevokeDBSecurityGroupIngress](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RevokeDBSecurityGroupIngress.html) | Grants permission to revoke ingress from a DBSecurityGroup for previously authorized IP ranges or EC2 or VPC Security Groups | Write |  secgrp* |  |   
[StartActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartActivityStream.html) | Grants permission to start Activity Stream | Write |  cluster |  |   
db |  |   
[StartDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBCluster.html) | Grants permission to start the DB cluster | Write |  cluster* |  |   
[StartDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstance.html) | Grants permission to start the DB instance | Write |  db* |  |   
[StartDBInstanceAutomatedBackupsReplication](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstanceAutomatedBackupsReplication.html) | Grants permission to start replication of automated backups to a different AWS Region | Write |  auto-backup* |  |   
db* |  |   
[StartExportTask](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartExportTask.html) | Grants permission to start a new Export task for a DB snapshot | Write |  cluster |  |  iam:PassRole   
cluster-snapshot |  |   
snapshot |  |   
[StopActivityStream](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopActivityStream.html) | Grants permission to stop Activity Stream | Write |  cluster |  |   
db |  |   
[StopDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBCluster.html) | Grants permission to stop the DB cluster | Write |  cluster* |  |   
[StopDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstance.html) | Grants permission to stop the DB instance | Write |  db* |  |  rds:AddTagsToResource  rds:CreateDBSnapshot   
snapshot |  |   
[StopDBInstanceAutomatedBackupsReplication](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstanceAutomatedBackupsReplication.html) | Grants permission to stop automated backup replication for a DB instance | Write |  db* |  |   
[SwitchoverBlueGreenDeployment](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverBlueGreenDeployment.html) | Grants permission to switch a blue-green deployment from source instance or cluster to target | Write |  deployment* |  |  rds:ModifyDBCluster  rds:ModifyDBInstance  rds:PromoteReadReplica  rds:PromoteReadReplicaDBCluster   
|  aws:ResourceTag/${TagKey} |   
[SwitchoverGlobalCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverGlobalCluster.html) | Grants permission to switchover a global cluster | Write |  cluster* |  |   
global-cluster* |  |   
[SwitchoverReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverReadReplica.html) | Grants permission to switch over a read replica, making it the new primary database | Write |  db* |  |   
  
## Resource types defined by Amazon RDS

The following resource types are defined by this service and can be used in
the `Resource` element of IAM permission policy statements. Each action in the
Actions table identifies the resource types that can be specified with that
action. A resource type can also define which condition keys you can include
in a policy. These keys are displayed in the last column of the table. For
details about the columns in the following table, see [Resource types
table](reference_policies_actions-resources-contextkeys.html#resources_table).

Resource types | ARN | Condition keys  
---|---|---  
[cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Aurora.html) |  `arn:${Partition}:rds:${Region}:${Account}:cluster:${DbClusterInstanceName}` |  aws:ResourceTag/${TagKey} rds:cluster-tag/${TagKey}  
[shardgrp](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.DBShardGroup.html) |  `arn:${Partition}:rds:${Region}:${Account}:shard-group:${DbShardGroupResourceId}` |  aws:ResourceTag/${TagKey}  
[cluster-auto-backup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html) |  `arn:${Partition}:rds:${Region}:${Account}:cluster-auto-backup:${DbClusterAutomatedBackupId}` |   
[auto-backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) |  `arn:${Partition}:rds:${Region}:${Account}:auto-backup:${DbInstanceAutomatedBackupId}` |   
[cluster-endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html) |  `arn:${Partition}:rds:${Region}:${Account}:cluster-endpoint:${DbClusterEndpoint}` |  aws:ResourceTag/${TagKey}  
[cluster-pg](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html) |  `arn:${Partition}:rds:${Region}:${Account}:cluster-pg:${ClusterParameterGroupName}` |  aws:ResourceTag/${TagKey} rds:cluster-pg-tag/${TagKey}  
[cluster-snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html) |  `arn:${Partition}:rds:${Region}:${Account}:cluster-snapshot:${ClusterSnapshotName}` |  aws:ResourceTag/${TagKey} rds:cluster-snapshot-tag/${TagKey}  
[db](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html) |  `arn:${Partition}:rds:${Region}:${Account}:db:${DbInstanceName}` |  aws:ResourceTag/${TagKey} rds:DatabaseClass rds:DatabaseEngine rds:DatabaseName rds:MultiAz rds:Piops rds:StorageEncrypted rds:StorageSize rds:Vpc rds:db-tag/${TagKey}  
[es](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) |  `arn:${Partition}:rds:${Region}:${Account}:es:${SubscriptionName}` |  aws:ResourceTag/${TagKey} rds:es-tag/${TagKey}  
[global-cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) |  `arn:${Partition}:rds::${Account}:global-cluster:${GlobalCluster}` |   
[og](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html) |  `arn:${Partition}:rds:${Region}:${Account}:og:${OptionGroupName}` |  aws:ResourceTag/${TagKey} rds:og-tag/${TagKey}  
[pg](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) |  `arn:${Partition}:rds:${Region}:${Account}:pg:${ParameterGroupName}` |  aws:ResourceTag/${TagKey} rds:pg-tag/${TagKey}  
[proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) |  `arn:${Partition}:rds:${Region}:${Account}:db-proxy:${DbProxyId}` |  aws:ResourceTag/${TagKey}  
[proxy-endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) |  `arn:${Partition}:rds:${Region}:${Account}:db-proxy-endpoint:${DbProxyEndpointId}` |  aws:ResourceTag/${TagKey}  
[ri](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html) |  `arn:${Partition}:rds:${Region}:${Account}:ri:${ReservedDbInstanceName}` |  aws:ResourceTag/${TagKey} rds:ri-tag/${TagKey}  
[secgrp](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html) |  `arn:${Partition}:rds:${Region}:${Account}:secgrp:${SecurityGroupName}` |  aws:ResourceTag/${TagKey} rds:secgrp-tag/${TagKey}  
[snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) |  `arn:${Partition}:rds:${Region}:${Account}:snapshot:${SnapshotName}` |  aws:ResourceTag/${TagKey} rds:snapshot-tag/${TagKey}  
[subgrp](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1) |  `arn:${Partition}:rds:${Region}:${Account}:subgrp:${SubnetGroupName}` |  aws:ResourceTag/${TagKey} rds:subgrp-tag/${TagKey}  
[target-group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) |  `arn:${Partition}:rds:${Region}:${Account}:target-group:${TargetGroupId}` |  aws:ResourceTag/${TagKey}  
[cev](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html) |  `arn:${Partition}:rds:${Region}:${Account}:cev:${Engine}/${EngineVersion}/${CustomDbEngineVersionId}` |  aws:ResourceTag/${TagKey}  
[deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) |  `arn:${Partition}:rds:${Region}:${Account}:deployment:${BlueGreenDeploymentIdentifier}` |  aws:ResourceTag/${TagKey}  
[integration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html) |  `arn:${Partition}:rds:${Region}:${Account}:integration:${IntegrationIdentifier}` |  aws:ResourceTag/${TagKey}  
[snapshot-tenant-database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.single-tenant.snapshots.html#br-cdb.db-snapshots) |  `arn:${Partition}:rds:${Region}:${Account}:snapshot-tenant-database:${SnapshotName}:${TenantResourceId}` |  aws:ResourceTag/${TagKey}  
[tenant-database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.CDBs.html#multi-tenant-configuration) |  `arn:${Partition}:rds:${Region}:${Account}:tenant-database:${TenantResourceId}` |  aws:ResourceTag/${TagKey}  
  
## Condition keys for Amazon RDS

Amazon RDS defines the following condition keys that can be used in the
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
[aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) | Filters access by the set of tag key-value pairs in the request | String  
[aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) | Filters access by the set of tag key-value pairs attached to the resource | String  
[aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) | Filters access by the set of tag keys in the request | ArrayOfString  
[rds:BackupTarget](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the type of backup target. One of: region, outposts | String  
[rds:CopyOptionGroup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the value that specifies whether the CopyDBSnapshot action requires copying the DB option group | Bool  
[rds:DatabaseClass](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the type of DB instance class | String  
[rds:DatabaseEngine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the database engine. For possible values refer to the engine parameter in CreateDBInstance API | String  
[rds:DatabaseName](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the user-defined name of the database on the DB instance | String  
[rds:EndpointType](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the type of the endpoint. One of: READER, WRITER, CUSTOM | String  
[rds:ManageMasterUserPassword](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the value that specifies whether RDS manages master user password in AWS Secrets Manager for the DB instance or cluster | Bool  
[rds:MultiAz](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the value that specifies whether the DB instance runs in multiple Availability Zones. To indicate that the DB instance is using Multi-AZ, specify true | Bool  
[rds:Piops](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the value that contains the number of Provisioned IOPS (PIOPS) that the instance supports. To indicate a DB instance that does not have PIOPS enabled, specify 0 | Numeric  
[rds:StorageEncrypted](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the value that specifies whether the DB instance storage should be encrypted. To enforce storage encryption, specify true | Bool  
[rds:StorageSize](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the storage volume size (in GB) | Numeric  
[rds:TenantDatabaseName](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tenant database name in CreateTenantDatabase and by the new tenant database name in ModifyTenantDatabase | String  
[rds:Vpc](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the value that specifies whether the DB instance runs in an Amazon Virtual Private Cloud (Amazon VPC). To indicate that the DB instance runs in an Amazon VPC, specify true | Bool  
[rds:cluster-pg-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB cluster parameter group | String  
[rds:cluster-snapshot-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB cluster snapshot | String  
[rds:cluster-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB cluster | String  
[rds:db-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB instance | String  
[rds:es-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to an event subscription | String  
[rds:og-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB option group | String  
[rds:pg-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB parameter group | String  
[rds:req-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the set of tag keys and values that can be used to tag a resource | String  
[rds:ri-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a reserved DB instance | String  
[rds:secgrp-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB security group | String  
[rds:snapshot-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB snapshot | String  
[rds:subgrp-tag/${TagKey}](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html#UsingWithRDS.IAM.Conditions) | Filters access by the tag attached to a DB subnet group | String  
  
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

