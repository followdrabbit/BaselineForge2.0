# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html'}

[Documentation](/index.html)[Service Authorization
Reference](/iam/index.html)[Service Authorization
Reference](list_amazonec2.html)

ActionsResource typesCondition keys

# Actions, resources, and condition keys for Amazon EC2

Amazon EC2 (service prefix: `ec2`) provides the following service-specific
resources, actions, and condition context keys for use in IAM permission
policies.

References:

  * Learn how to [configure this service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

  * View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/).

  * Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html) permission policies.

###### Topics

  * Actions defined by Amazon EC2
  * Resource types defined by Amazon EC2
  * Condition keys for Amazon EC2

## Actions defined by Amazon EC2

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
[AcceptAddressTransfer](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptAddressTransfer.html) | Grants permission to accept an Elastic IP address transfer | Write |  elastic-ip* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AllocationId ec2:Domain ec2:PublicIpAddress |  ec2:CreateTags   
|  ec2:Region |   
[AcceptCapacityReservationBillingOwnership](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptCapacityReservationBillingOwnership.html) | Grants permission to accept assign billing of the available capacity of a shared Capacity Reservation to the calling account | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[AcceptReservedInstancesExchangeQuote](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptReservedInstancesExchangeQuote.html) | Grants permission to accept a Convertible Reserved Instance exchange quote | Write |  |  ec2:Region |   
[AcceptTransitGatewayMulticastDomainAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptTransitGatewayMulticastDomainAssociations.html) | Grants permission to accept a request to associate subnets with a transit gateway multicast domain | Write |  transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-multicast-domain |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[AcceptTransitGatewayPeeringAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptTransitGatewayPeeringAttachment.html) | Grants permission to accept a transit gateway peering attachment request | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[AcceptTransitGatewayVpcAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptTransitGatewayVpcAttachment.html) | Grants permission to accept a request to attach a VPC to a transit gateway | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[AcceptVpcEndpointConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcEndpointConnections.html) | Grants permission to accept one or more interface VPC endpoint connections to your VPC endpoint service | Write |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[AcceptVpcPeeringConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceptVpcPeeringConnection.html) | Grants permission to accept a VPC peering connection request | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
vpc-peering-connection* |  aws:ResourceTag/${TagKey} ec2:AccepterVpc ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID |   
|  ec2:Region |   
[AdvertiseByoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdvertiseByoipCidr.html) | Grants permission to advertise an IP address range that is provisioned for use in AWS through bring your own IP addresses (BYOIP) | Write |  |  ec2:Region |   
[AllocateAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateAddress.html) | Grants permission to allocate an Elastic IP address (EIP) to your account | Write |  elastic-ip* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipv4pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AllocateHosts](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateHosts.html) | Grants permission to allocate a Dedicated Host to your account | Write |  dedicated-host* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AutoPlacement ec2:AvailabilityZone ec2:HostRecovery ec2:InstanceType ec2:Quantity |  ec2:CreateTags   
|  ec2:Region |   
[AllocateIpamPoolCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AllocateIpamPoolCidr.html) | Grants permission to allocate a CIDR from an Amazon VPC IP Address Manager (IPAM) pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ApplySecurityGroupsToClientVpnTargetNetwork](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplySecurityGroupsToClientVpnTargetNetwork.html) | Grants permission to apply a security group to the association between a Client VPN endpoint and a target network | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[AssignIpv6Addresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignIpv6Addresses.html) | Grants permission to assign one or more IPv6 addresses to a network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[AssignPrivateIpAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.html) | Grants permission to assign one or more secondary private IP addresses to a network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[AssignPrivateNatGatewayAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignPrivateNatGatewayAddress.html) | Grants permission to assign one or more secondary private IP addresses to a private NAT gateway | Write |  natgateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AssociateAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateAddress.html) | Grants permission to associate an Elastic IP address (EIP) with an instance or a network interface | Write |  elastic-ip |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
instance |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[AssociateCapacityReservationBillingOwner](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateCapacityReservationBillingOwner.html) | Grants permission to assign billing of the unused capacity of a shared Capacity Reservation to a consumer account | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[AssociateClientVpnTargetNetwork](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateClientVpnTargetNetwork.html) | Grants permission to associate a target network with a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
subnet* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SubnetID |   
|  ec2:Region |   
[AssociateDhcpOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateDhcpOptions.html) | Grants permission to associate or disassociate a set of DHCP options with a VPC | Write |  dhcp-options* |  aws:ResourceTag/${TagKey} ec2:DhcpOptionsID ec2:ResourceTag/${TagKey} |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[AssociateEnclaveCertificateIamRole](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateEnclaveCertificateIamRole.html) | Grants permission to associate an ACM certificate with an IAM role to be used in an EC2 Enclave | Write |  certificate* |  |   
role* |  |   
|  ec2:Region |   
[AssociateIamInstanceProfile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html) | Grants permission to associate an IAM instance profile with a running or stopped instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:NewInstanceProfile ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |  iam:PassRole   
|  ec2:Region |   
[AssociateInstanceEventWindow](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateInstanceEventWindow.html) | Grants permission to associate one or more targets with an event window | Write |  instance-event-window* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AssociateIpamByoasn](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIpamByoasn.html) | Grants permission to associate an Autonomous System Number (ASN) with a BYOIP CIDR | Write |  |  ec2:Region |   
[AssociateIpamResourceDiscovery](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIpamResourceDiscovery.html) | Grants permission to associate an IPAM resource discovery with an Amazon VPC IPAM | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
ipam-resource-discovery* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipam-resource-discovery-association* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[AssociateNatGatewayAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateNatGatewayAddress.html) | Grants permission to associate an Elastic IP address and private IP address with a public Nat gateway | Write |  elastic-ip* |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
natgateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AssociateRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateRouteTable.html) | Grants permission to associate a subnet or gateway with a route table | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
internet-gateway |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
vpn-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AssociateSecurityGroupVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSecurityGroupVpc.html) | Grants permission to associate a security group with another VPC in the same Region | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
vpc* |  aws:ResourceTag/${TagKey} ec2:Ipv4IpamPoolId ec2:Ipv6IpamPoolId ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[AssociateSubnetCidrBlock](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSubnetCidrBlock.html) | Grants permission to associate a CIDR block with a subnet | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AssociateTransitGatewayMulticastDomain](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayMulticastDomain.html) | Grants permission to associate an attachment and list of subnets with a transit gateway multicast domain | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[AssociateTransitGatewayPolicyTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayPolicyTable.html) | Grants permission to associate a policy table with a transit gateway attachment | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-policy-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId |   
|  ec2:Region |   
[AssociateTransitGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayRouteTable.html) | Grants permission to associate an attachment with a transit gateway route table | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[AssociateTrunkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTrunkInterface.html) | Grants permission to associate a branch network interface with a trunk network interface | Write |  |  ec2:Region |   
[AssociateVerifiedAccessInstanceWebAcl](https://docs.aws.amazon.com/verified-access/latest/ug/waf-integration.html) [permission only] | Grants permission to associate an AWS Web Application Firewall (WAF) web access control list (ACL) with a Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AssociateVpcCidrBlock](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateVpcCidrBlock.html) | Grants permission to associate a CIDR block with a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:Ipv4IpamPoolId ec2:Ipv6IpamPoolId ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipv6pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AttachClassicLinkVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachClassicLinkVpc.html) | Grants permission to link an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC's security groups | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[AttachInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachInternetGateway.html) | Grants permission to attach an internet gateway to a VPC | Write |  internet-gateway* |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[AttachNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachNetworkInterface.html) | Grants permission to attach a network interface to an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[AttachVerifiedAccessTrustProvider](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVerifiedAccessTrustProvider.html) | Grants permission to attach a trust provider to a Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
verified-access-trust-provider* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AttachVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVolume.html) | Grants permission to attach an EBS volume to a running or stopped instance and expose it to the instance with the specified device name | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[AttachVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVpnGateway.html) | Grants permission to attach a virtual private gateway to a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
vpn-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[AuthorizeClientVpnIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeClientVpnIngress.html) | Grants permission to add an inbound authorization rule to a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html) | Grants permission to add one or more outbound rules to a VPC security group. Policies using the security-group-rule resource-level permission are only enforced when the API request includes TagSpecifications | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |  ec2:CreateTags   
security-group-rule |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html) | Grants permission to add one or more inbound rules to a VPC security group. Policies using the security-group-rule resource-level permission are only enforced when the API request includes TagSpecifications | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |  ec2:CreateTags   
security-group-rule |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[BundleInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BundleInstance.html) | Grants permission to bundle an instance store-backed Windows instance | Write |  |  ec2:Region |   
[CancelBundleTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelBundleTask.html) | Grants permission to cancel a bundling operation | Write |  |  ec2:Region |   
[CancelCapacityReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelCapacityReservation.html) | Grants permission to cancel a Capacity Reservation and release the reserved capacity | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:CapacityReservationFleet |   
|  ec2:Region |   
[CancelCapacityReservationFleets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelCapacityReservationFleets.html) | Grants permission to cancel one or more Capacity Reservation Fleets | Write |  capacity-reservation-fleet* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CancelCapacityReservation   
|  ec2:Region |   
[CancelConversionTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelConversionTask.html) | Grants permission to cancel an active conversion task | Write |  |  ec2:Region |   
[CancelDeclarativePoliciesReport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelDeclarativePoliciesReport.html) | Grants permission to cancel a declarative policies report | Write |  declarative-policies-report* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CancelExportTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelExportTask.html) | Grants permission to cancel an active export task | Write |  export-image-task |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
export-instance-task |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CancelImageLaunchPermission](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelImageLaunchPermission.html) | Grants permission to remove your AWS account from the launch permissions for the specified AMI | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[CancelImportTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelImportTask.html) | Grants permission to cancel an in-process import virtual machine or import snapshot task | Write |  import-image-task |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
import-snapshot-task |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CancelReservedInstancesListing](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelReservedInstancesListing.html) | Grants permission to cancel a Reserved Instance listing on the Reserved Instance Marketplace | Write |  |  ec2:Region |   
[CancelSpotFleetRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests.html) | Grants permission to cancel one or more Spot Fleet requests | Write |  spot-fleet-request* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CancelSpotInstanceRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotInstanceRequests.html) | Grants permission to cancel one or more Spot Instance requests | Write |  spot-instances-request* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ConfirmProductInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConfirmProductInstance.html) | Grants permission to determine whether an owned product code is associated with an instance | Write |  |  ec2:Region |   
[CopyFpgaImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyFpgaImage.html) | Grants permission to copy a source Amazon FPGA image (AFI) to the current Region. Resource-level permissions specified for this action apply to the new AFI only. They do not apply to the source AFI | Write |  fpga-image* |  ec2:Owner |   
|  ec2:Region |   
[CopyImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyImage.html) | Grants permission to copy an Amazon Machine Image (AMI) from a source Region to the current Region | Write |  image* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ImageID ec2:Owner |  ec2:CreateTags   
snapshot* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[CopySnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopySnapshot.html) | Grants permission to copy a point-in-time snapshot of an EBS volume and store it in Amazon S3. Resource-level permissions specified for this action apply to the new snapshot only. They do not apply to the source snapshot | Write |  snapshot* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:OutpostArn ec2:SnapshotID |  ec2:CreateTags   
|  ec2:Region |   
[CreateCapacityReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservation.html) | Grants permission to create a Capacity Reservation | Write |  capacity-reservation* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:CapacityReservationFleet |  ec2:CreateTags   
|  ec2:Region |   
[CreateCapacityReservationBySplitting](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservationBySplitting.html) | Grants permission to create a new Capacity Reservation by splitting the available capacity of the source Capacity Reservation | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |  ec2:CreateTags   
|  ec2:Region |   
[CreateCapacityReservationFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservationFleet.html) | Grants permission to create a Capacity Reservation Fleet | Write |  capacity-reservation-fleet* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateCapacityReservation  ec2:CreateTags  ec2:DescribeCapacityReservations  ec2:DescribeInstances   
|  ec2:Region |   
[CreateCarrierGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCarrierGateway.html) | Grants permission to create a carrier gateway and provides CSP connectivity to VPC customers | Write |  carrier-gateway* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateClientVpnEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnEndpoint.html) | Grants permission to create a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:SamlProviderArn ec2:ServerCertificateArn |  ec2:CreateTags   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID |   
vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:VpcID |   
|  ec2:Region |   
[CreateClientVpnRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnRoute.html) | Grants permission to add a network route to a Client VPN endpoint's route table | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
subnet* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SubnetID |   
|  ec2:Region |   
[CreateCoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCoipCidr.html) | Grants permission to create a range of customer-owned IP (CoIP) addresses | Write |  coip-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateCoipPool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCoipPool.html) | Grants permission to create a pool of customer-owned IP (CoIP) addresses | Write |  coip-pool* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateCoipPoolPermission](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html) [permission only] | Grants permission to allow a service to access a customer-owned IP (CoIP) pool | Write |  coip-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateCustomerGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCustomerGateway.html) | Grants permission to create a customer gateway, which provides information to AWS about your customer gateway device | Write |  customer-gateway* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateDefaultSubnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultSubnet.html) | Grants permission to create a default subnet in a specified Availability Zone in a default VPC | Write |  |  ec2:Region |   
[CreateDefaultVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultVpc.html) | Grants permission to create a default VPC with a default subnet in each Availability Zone | Write |  |  ec2:Region |   
[CreateDhcpOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDhcpOptions.html) | Grants permission to create a set of DHCP options for a VPC | Write |  dhcp-options* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:DhcpOptionsID |  ec2:CreateTags   
|  ec2:Region |   
[CreateEgressOnlyInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateEgressOnlyInternetGateway.html) | Grants permission to create an egress-only internet gateway for a VPC | Write |  egress-only-internet-gateway* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html) | Grants permission to launch an EC2 Fleet. Resource-level permissions for this action do not include the resources specified in a launch template. To specify resource-level permissions for resources specified in a launch template, you must include the resources in the RunInstances action statement | Write |  fleet* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
instance* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:PlacementGroup ec2:RootDeviceType ec2:Tenancy |   
image |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
launch-template |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
volume |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:Encrypted ec2:KmsKeyId ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[CreateFlowLogs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFlowLogs.html) | Grants permission to create one or more flow logs to capture IP traffic for a network interface | Write |  vpc-flow-log* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags  ecs:ListClusters  ecs:ListContainerInstances  ecs:ListServices  ecs:ListTaskDefinitions  ecs:ListTasks  iam:PassRole   
network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
transit-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateFpgaImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFpgaImage.html) | Grants permission to create an Amazon FPGA Image (AFI) from a design checkpoint (DCP) | Write |  fpga-image* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:Owner ec2:Public |  ec2:CreateTags   
|  ec2:Region |   
[CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) | Grants permission to create an Amazon EBS-backed AMI from a stopped or running Amazon EBS-backed instance | Write |  image* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ImageID ec2:Owner |  ec2:CreateTags   
instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
snapshot* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:OutpostArn ec2:ParentVolume ec2:SnapshotID ec2:SnapshotTime ec2:SourceOutpostArn ec2:VolumeSize |   
|  ec2:Region |   
[CreateInstanceConnectEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceConnectEndpoint.html) | Grants permission to create an EC2 Instance Connect Endpoint that allows you to connect to an instance without a public IPv4 address | Write |  instance-connect-endpoint* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:SubnetID |  ec2:CreateTags   
subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[CreateInstanceEventWindow](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceEventWindow.html) | Grants permission to create an event window in which scheduled events for the associated Amazon EC2 instances can run | Write |  instance-event-window* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateInstanceExportTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceExportTask.html) | Grants permission to export a running or stopped instance to an Amazon S3 bucket | Write |  export-instance-task* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[CreateInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInternetGateway.html) | Grants permission to create an internet gateway for a VPC | Write |  internet-gateway* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:InternetGatewayID |  ec2:CreateTags   
|  ec2:Region |   
[CreateIpam](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpam.html) | Grants permission to create an Amazon VPC IP Address Manager (IPAM) | Write |  ipam* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags  iam:CreateServiceLinkedRole   
|  ec2:Region |   
[CreateIpamExternalResourceVerificationToken](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamExternalResourceVerificationToken.html) | Grants permission to create a verification token, which proves ownership of an external resource | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
ipam-external-resource-verification-token* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[CreateIpamPool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamPool.html) | Grants permission to create an IP address pool for Amazon VPC IP Address Manager (IPAM), which is a collection of contiguous IP address CIDRs | Write |  ipam-pool* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
ipam-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateIpamResourceDiscovery](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamResourceDiscovery.html) | Grants permission to create an IPAM resource discovery | Write |  ipam-resource-discovery* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags  iam:CreateServiceLinkedRole   
|  ec2:Region |   
[CreateIpamScope](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamScope.html) | Grants permission to create an Amazon VPC IP Address Manager (IPAM) scope, which is the highest-level container within IPAM | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
ipam-scope* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[CreateKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html) | Grants permission to create a 2048-bit RSA key pair | Write |  key-pair* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:KeyPairType |  ec2:CreateTags   
|  ec2:Region |   
[CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) | Grants permission to create a launch template | Write |  launch-template* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ManagedResourceOperator |  ec2:CreateTags  ssm:GetParameters   
|  ec2:Region |   
[CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) | Grants permission to create a new version of a launch template | Write |  launch-template* |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |  ssm:GetParameters   
|  ec2:Region |   
[CreateLocalGatewayRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLocalGatewayRoute.html) | Grants permission to create a static route for a local gateway route table | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
local-gateway-virtual-interface-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
prefix-list |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateLocalGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLocalGatewayRouteTable.html) | Grants permission to create a local gateway route table | Write |  local-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
local-gateway-route-table* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[CreateLocalGatewayRouteTablePermission](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html) [permission only] | Grants permission to allow a service to access a local gateway route table | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation.html) | Grants permission to create a local gateway route table virtual interface group association | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
local-gateway-route-table-virtual-interface-group-association* |  aws:RequestTag/${TagKey} aws:TagKeys |   
local-gateway-virtual-interface-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateLocalGatewayRouteTableVpcAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLocalGatewayRouteTableVpcAssociation.html) | Grants permission to associate a VPC with a local gateway route table | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
local-gateway-route-table-vpc-association* |  aws:RequestTag/${TagKey} aws:TagKeys |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateManagedPrefixList](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateManagedPrefixList.html) | Grants permission to create a managed prefix list | Write |  prefix-list* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateNatGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNatGateway.html) | Grants permission to create a NAT gateway in a subnet | Write |  natgateway* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
elastic-ip |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateNetworkAcl](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAcl.html) | Grants permission to create a network ACL in a VPC | Write |  network-acl* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:NetworkAclID |  ec2:CreateTags   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateNetworkAclEntry](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAclEntry.html) | Grants permission to create a numbered entry (a rule) in a network ACL | Write |  network-acl* |  aws:ResourceTag/${TagKey} ec2:NetworkAclID ec2:ResourceTag/${TagKey} ec2:Vpc |   
|  ec2:Region |   
[CreateNetworkInsightsAccessScope](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInsightsAccessScope.html) | Grants permission to create a Network Access Scope | Write |  network-insights-access-scope* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateNetworkInsightsPath](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInsightsPath.html) | Grants permission to create a path to analyze for reachability | Write |  network-insights-path* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
instance |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
internet-gateway |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
transit-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
vpc-endpoint |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
vpc-peering-connection |  aws:ResourceTag/${TagKey} ec2:AccepterVpc ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID |   
vpn-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html) | Grants permission to create a network interface in a subnet | Write |  network-interface* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ManagedResourceOperator ec2:NetworkInterfaceID |  ec2:CreateTags   
subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[CreateNetworkInterfacePermission](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterfacePermission.html) | Grants permission to create a permission for an AWS-authorized user to perform certain operations on a network interface | Permissions management |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AuthorizedService ec2:AuthorizedUser ec2:AvailabilityZone ec2:NetworkInterfaceID ec2:Permission ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[CreatePlacementGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePlacementGroup.html) | Grants permission to create a placement group | Write |  placement-group* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:PlacementGroupName ec2:PlacementGroupStrategy |  ec2:CreateTags   
|  ec2:Region |   
[CreatePublicIpv4Pool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePublicIpv4Pool.html) | Grants permission to create a public IPv4 address pool for public IPv4 CIDRs that you own and bring to Amazon to manage with Amazon VPC IP Address Manager (IPAM) | Write |  ipv4pool-ec2* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateReplaceRootVolumeTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateReplaceRootVolumeTask.html) | Grants permission to create a root volume replacement task | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |  ec2:CreateTags   
replace-root-volume-task* |  aws:RequestTag/${TagKey} aws:TagKeys |   
volume* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ManagedResourceOperator ec2:VolumeID |   
image |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
snapshot |  aws:ResourceTag/${TagKey} ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[CreateReservedInstancesListing](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateReservedInstancesListing.html) | Grants permission to create a listing for Standard Reserved Instances to be sold in the Reserved Instance Marketplace | Write |  |  ec2:Region |   
[CreateRestoreImageTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRestoreImageTask.html) | Grants permission to start a task that restores an AMI from an S3 object previously created by using CreateStoreImageTask | Write |  image* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ImageID ec2:Owner |  ec2:CreateTags   
|  ec2:Region |   
[CreateRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRoute.html) | Grants permission to create a route in a VPC route table | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
|  ec2:Region |   
[CreateRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRouteTable.html) | Grants permission to create a route table for a VPC | Write |  route-table* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:RouteTableID |  ec2:CreateTags   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html) | Grants permission to create a security group | Write |  security-group* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:SecurityGroupID |  ec2:CreateTags   
vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshot.html) | Grants permission to create a snapshot of an EBS volume and store it in Amazon S3 | Write |  snapshot* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:Location ec2:OutpostArn ec2:ParentVolume ec2:SnapshotID ec2:SourceAvailabilityZone ec2:SourceOutpostArn ec2:VolumeSize |  ec2:CreateTags   
volume* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[CreateSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSnapshots.html) | Grants permission to create crash-consistent snapshots of multiple EBS volumes and store them in Amazon S3 | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceProfile ec2:InstanceType ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |  ec2:CreateTags   
snapshot* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:Location ec2:OutpostArn ec2:ParentVolume ec2:SnapshotID ec2:SourceAvailabilityZone ec2:SourceOutpostArn ec2:VolumeSize |   
volume* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[CreateSpotDatafeedSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSpotDatafeedSubscription.html) | Grants permission to create a data feed for Spot Instances to view Spot Instance usage logs | Write |  |  ec2:Region |   
[CreateStoreImageTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateStoreImageTask.html) | Grants permission to store an AMI as a single object in an S3 bucket | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[CreateSubnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSubnet.html) | Grants permission to create a subnet in a VPC | Write |  subnet* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:SubnetID |  ec2:CreateTags   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateSubnetCidrReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSubnetCidrReservation.html) | Grants permission to create a subnet CIDR reservation | Write |  |  ec2:Region |   
[CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html) | Grants permission to add or overwrite one or more tags for Amazon EC2 resources | Tagging |  capacity-reservation |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys |   
capacity-reservation-fleet |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
carrier-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:Vpc |   
client-vpn-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
coip-pool |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
customer-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
declarative-policies-report |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
dedicated-host |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AutoPlacement ec2:AvailabilityZone ec2:HostRecovery ec2:InstanceType ec2:Quantity ec2:ResourceTag/${TagKey} |   
dhcp-options |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:DhcpOptionsID ec2:ResourceTag/${TagKey} |   
egress-only-internet-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
elastic-gpu |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ElasticGpuType ec2:ResourceTag/${TagKey} |   
elastic-ip |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
export-image-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
export-instance-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
fleet |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
fpga-image |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} |   
host-reservation |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
image |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
import-image-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
import-snapshot-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
instance |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
instance-connect-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:SubnetID |   
instance-event-window |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
internet-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
ipam |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-external-resource-verification-token |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-pool |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-resource-discovery |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-resource-discovery-association |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-scope |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipv4pool-ec2 |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipv6pool-ec2 |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
key-pair |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:KeyPairName ec2:KeyPairType ec2:ResourceTag/${TagKey} |   
launch-template |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
local-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-route-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-route-table-virtual-interface-group-association |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-route-table-vpc-association |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-virtual-interface |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-virtual-interface-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
natgateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-acl |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:NetworkAclID ec2:ResourceTag/${TagKey} ec2:Vpc |   
network-insights-access-scope |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-access-scope-analysis |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-analysis |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-path |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-interface |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AuthorizedUser ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Permission ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
placement-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
prefix-list |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
replace-root-volume-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
reserved-instances |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:InstanceType ec2:ReservedInstancesOfferingType ec2:ResourceTag/${TagKey} ec2:Tenancy |   
route-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
security-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
security-group-rule |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
snapshot |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
spot-fleet-request |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
spot-instances-request |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
subnet |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
subnet-cidr-reservation |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter-rule |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-session |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-target |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
transit-gateway-attachment |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-connect-peer |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayConnectPeerId |   
transit-gateway-multicast-domain |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
transit-gateway-policy-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId |   
transit-gateway-route-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-route-table-announcement |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableAnnouncementId |   
verified-access-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-endpoint-target |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-instance |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-policy |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-trust-provider |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
volume |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
vpc |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
vpc-block-public-access-exclusion |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint-connection |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceServiceRegion ec2:vpceSupportedRegion |   
vpc-endpoint-service-permission |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-flow-log |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-peering-connection |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AccepterVpc ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID |   
vpn-connection |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AuthenticationType ec2:DPDTimeoutSeconds ec2:GatewayType ec2:IKEVersions ec2:InsideTunnelCidr ec2:InsideTunnelIpv6Cidr ec2:Phase1DHGroup ec2:Phase1EncryptionAlgorithms ec2:Phase1IntegrityAlgorithms ec2:Phase1LifetimeSeconds ec2:Phase2DHGroup ec2:Phase2EncryptionAlgorithms ec2:Phase2IntegrityAlgorithms ec2:Phase2LifetimeSeconds ec2:RekeyFuzzPercentage ec2:RekeyMarginTimeSeconds ec2:ReplayWindowSizePackets ec2:ResourceTag/${TagKey} ec2:RoutingType |   
vpn-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
|  ec2:CreateAction ec2:Region |   
[CreateTrafficMirrorFilter](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilter.html) | Grants permission to create a traffic mirror filter | Write |  traffic-mirror-filter* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateTrafficMirrorFilterRule](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorFilterRule.html) | Grants permission to create a traffic mirror filter rule | Write |  traffic-mirror-filter* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
traffic-mirror-filter-rule* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[CreateTrafficMirrorSession](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorSession.html) | Grants permission to create a traffic mirror session | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |  ec2:CreateTags   
traffic-mirror-filter* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
traffic-mirror-session* |  aws:RequestTag/${TagKey} aws:TagKeys |   
traffic-mirror-target* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateTrafficMirrorTarget](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTrafficMirrorTarget.html) | Grants permission to create a traffic mirror target | Write |  traffic-mirror-target* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
network-interface |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} |   
vpc-endpoint |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:VpceServiceName ec2:VpceServiceOwner |   
|  ec2:Region |   
[CreateTransitGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGateway.html) | Grants permission to create a transit gateway | Write |  transit-gateway* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayId |  ec2:CreateTags   
|  ec2:Region |   
[CreateTransitGatewayConnect](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayConnect.html) | Grants permission to create a Connect attachment from a specified transit gateway attachment | Write |  transit-gateway-attachment* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayAttachmentId |  ec2:CreateTags   
|  ec2:Region |   
[CreateTransitGatewayConnectPeer](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayConnectPeer.html) | Grants permission to create a Connect peer between a transit gateway and an appliance | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |  ec2:CreateTags   
transit-gateway-connect-peer* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayConnectPeerId |   
|  ec2:Region |   
[CreateTransitGatewayMulticastDomain](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayMulticastDomain.html) | Grants permission to create a multicast domain for a transit gateway | Write |  transit-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |  ec2:CreateTags   
transit-gateway-multicast-domain* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[CreateTransitGatewayPeeringAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPeeringAttachment.html) | Grants permission to request a transit gateway peering attachment between a requester and accepter transit gateway | Write |  transit-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |  ec2:CreateTags   
transit-gateway-attachment* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[CreateTransitGatewayPolicyTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPolicyTable.html) | Grants permission to create a transit gateway policy table | Write |  transit-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |  ec2:CreateTags   
transit-gateway-policy-table* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayPolicyTableId |   
|  ec2:Region |   
[CreateTransitGatewayPrefixListReference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPrefixListReference.html) | Grants permission to create a transit gateway prefix list reference | Write |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[CreateTransitGatewayRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRoute.html) | Grants permission to create a static route for a transit gateway route table | Write |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[CreateTransitGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRouteTable.html) | Grants permission to create a route table for a transit gateway | Write |  transit-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |  ec2:CreateTags   
transit-gateway-route-table* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[CreateTransitGatewayRouteTableAnnouncement](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayRouteTableAnnouncement.html) | Grants permission to create an announcement for a transit gateway route table | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |  ec2:CreateTags   
transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-route-table-announcement* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayRouteTableAnnouncementId |   
|  ec2:Region |   
[CreateTransitGatewayVpcAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayVpcAttachment.html) | Grants permission to attach a VPC to a transit gateway | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |  ec2:CreateTags   
transit-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
transit-gateway-attachment* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:transitGatewayAttachmentId |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateVerifiedAccessEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessEndpoint.html) | Grants permission to create a Verified Access endpoint | Write |  verified-access-endpoint* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
verified-access-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AuthorizedUser ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Permission ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[CreateVerifiedAccessGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessGroup.html) | Grants permission to create a Verified Access group | Write |  verified-access-group* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateVerifiedAccessInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessInstance.html) | Grants permission to create a Verified Access instance | Write |  verified-access-instance* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateVerifiedAccessTrustProvider](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessTrustProvider.html) | Grants permission to create a verified trust provider | Write |  verified-access-trust-provider* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[CreateVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html) | Grants permission to create an EBS volume | Write |  volume* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:Encrypted ec2:KmsKeyId ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |  ec2:CreateTags   
snapshot |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[CreateVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpc.html) | Grants permission to create a VPC with a specified CIDR block | Write |  vpc* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:Ipv4IpamPoolId ec2:Ipv6IpamPoolId ec2:VpcID |  ec2:CreateTags   
ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipv6pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateVpcBlockPublicAccessExclusion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcBlockPublicAccessExclusion.html) | Grants permission to create an exclusion list for blocked public access on a VPC | Write |  vpc-block-public-access-exclusion* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
vpc |  aws:ResourceTag/${TagKey} ec2:Ipv4IpamPoolId ec2:Ipv6IpamPoolId ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[CreateVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpoint.html) | Grants permission to create a VPC endpoint for an AWS service | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:VpcID |  ec2:CreateTags  route53:AssociateVPCWithHostedZone   
vpc-endpoint* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:VpceServiceName ec2:VpceServiceOwner |   
route-table |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID |   
subnet |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SubnetID |   
|  ec2:Region |   
[CreateVpcEndpointConnectionNotification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html) | Grants permission to create a connection notification for a VPC endpoint or VPC endpoint service | Write |  vpc-endpoint |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceServiceRegion |   
|  ec2:Region |   
[CreateVpcEndpointServiceConfiguration](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointServiceConfiguration.html) | Grants permission to create a VPC endpoint service configuration to which service consumers (AWS accounts, IAM users, and IAM roles) can connect | Write |  vpc-endpoint-service* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:VpceServicePrivateDnsName ec2:vpceMultiRegion ec2:vpceServiceRegion |  ec2:CreateTags   
|  ec2:Region |   
[CreateVpcPeeringConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcPeeringConnection.html) | Grants permission to request a VPC peering connection between two VPCs | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |  ec2:CreateTags   
vpc-peering-connection* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AccepterVpc ec2:RequesterVpc ec2:VpcPeeringConnectionID |   
|  ec2:Region |   
[CreateVpnConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnection.html) | Grants permission to create a VPN connection between a virtual private gateway or transit gateway and a customer gateway | Write |  customer-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
vpn-connection* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AuthenticationType ec2:DPDTimeoutSeconds ec2:GatewayType ec2:IKEVersions ec2:InsideTunnelCidr ec2:InsideTunnelIpv6Cidr ec2:Phase1DHGroup ec2:Phase1EncryptionAlgorithms ec2:Phase1IntegrityAlgorithms ec2:Phase1LifetimeSeconds ec2:Phase2DHGroup ec2:Phase2EncryptionAlgorithms ec2:Phase2IntegrityAlgorithms ec2:Phase2LifetimeSeconds ec2:RekeyFuzzPercentage ec2:RekeyMarginTimeSeconds ec2:ReplayWindowSizePackets ec2:RoutingType |   
transit-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
vpn-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateVpnConnectionRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.html) | Grants permission to create a static route for a VPN connection between a virtual private gateway and a customer gateway | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[CreateVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnGateway.html) | Grants permission to create a virtual private gateway | Write |  vpn-gateway* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[DeleteCarrierGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCarrierGateway.html) | Grants permission to delete a carrier gateway | Write |  carrier-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteClientVpnEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnEndpoint.html) | Grants permission to delete a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[DeleteClientVpnRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnRoute.html) | Grants permission to delete a route from a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[DeleteCoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCoipCidr.html) | Grants permission to delete a range of customer-owned IP (CoIP) addresses | Write |  coip-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteCoipPool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCoipPool.html) | Grants permission to delete a pool of customer-owned IP (CoIP) addresses | Write |  coip-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteCoipPoolPermission](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html) [permission only] | Grants permission to deny a service from accessing a customer-owned IP (CoIP) pool | Write |  coip-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteCustomerGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCustomerGateway.html) | Grants permission to delete a customer gateway | Write |  customer-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteDhcpOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteDhcpOptions.html) | Grants permission to delete a set of DHCP options | Write |  dhcp-options* |  aws:ResourceTag/${TagKey} ec2:DhcpOptionsID ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteEgressOnlyInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteEgressOnlyInternetGateway.html) | Grants permission to delete an egress-only internet gateway | Write |  egress-only-internet-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteFleets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFleets.html) | Grants permission to delete one or more EC2 Fleets | Write |  fleet* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteFlowLogs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFlowLogs.html) | Grants permission to delete one or more flow logs | Write |  vpc-flow-log* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteFpgaImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFpgaImage.html) | Grants permission to delete an Amazon FPGA Image (AFI) | Write |  fpga-image* |  aws:ResourceTag/${TagKey} ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteInstanceConnectEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteInstanceConnectEndpoint.html) | Grants permission to delete an EC2 Instance Connect Endpoint | Write |  instance-connect-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SubnetID |   
|  ec2:Region |   
[DeleteInstanceEventWindow](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteInstanceEventWindow.html) | Grants permission to delete the specified event window | Write |  instance-event-window* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteInternetGateway.html) | Grants permission to delete an internet gateway | Write |  internet-gateway* |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteIpam](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpam.html) | Grants permission to delete an Amazon VPC IP Address Manager (IPAM) and remove all monitored data associated with the IPAM including the historical data for CIDRs | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteIpamExternalResourceVerificationToken](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpamExternalResourceVerificationToken.html) | Grants permission to delete a verification token, which proves ownership of an external resource | Write |  ipam-external-resource-verification-token* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteIpamPool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpamPool.html) | Grants permission to delete an Amazon VPC IP Address Manager (IPAM) pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteIpamResourceDiscovery](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpamResourceDiscovery.html) | Grants permission to delete an IPAM resource discovery | Write |  ipam-resource-discovery* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteIpamScope](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpamScope.html) | Grants permission to delete the scope for an Amazon VPC IP Address Manager (IPAM) | Write |  ipam-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteKeyPair.html) | Grants permission to delete a key pair by removing the public key from Amazon EC2 | Write |  key-pair |  aws:ResourceTag/${TagKey} ec2:KeyPairName ec2:KeyPairType ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplate.html) | Grants permission to delete a launch template and its associated versions | Write |  launch-template* |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplateVersions.html) | Grants permission to delete one or more versions of a launch template | Write |  launch-template* |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLocalGatewayRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLocalGatewayRoute.html) | Grants permission to delete a route from a local gateway route table | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
prefix-list |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLocalGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLocalGatewayRouteTable.html) | Grants permission to delete a local gateway route table | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLocalGatewayRouteTablePermission](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html) [permission only] | Grants permission to deny a service from accessing a local gateway route table | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation.html) | Grants permission to delete a local gateway route table virtual interface group association | Write |  local-gateway-route-table-virtual-interface-group-association* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteLocalGatewayRouteTableVpcAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLocalGatewayRouteTableVpcAssociation.html) | Grants permission to delete an association between a VPC and local gateway route table | Write |  local-gateway-route-table-vpc-association* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteManagedPrefixList](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteManagedPrefixList.html) | Grants permission to delete a managed prefix list | Write |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteNatGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNatGateway.html) | Grants permission to delete a NAT gateway | Write |  natgateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteNetworkAcl](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAcl.html) | Grants permission to delete a network ACL | Write |  network-acl* |  aws:ResourceTag/${TagKey} ec2:NetworkAclID ec2:ResourceTag/${TagKey} ec2:Vpc |   
|  ec2:Region |   
[DeleteNetworkAclEntry](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAclEntry.html) | Grants permission to delete an inbound or outbound entry (rule) from a network ACL | Write |  network-acl* |  aws:ResourceTag/${TagKey} ec2:NetworkAclID ec2:ResourceTag/${TagKey} ec2:Vpc |   
|  ec2:Region |   
[DeleteNetworkInsightsAccessScope](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInsightsAccessScope.html) | Grants permission to delete a Network Access Scope | Write |  network-insights-access-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteNetworkInsightsAccessScopeAnalysis](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInsightsAccessScopeAnalysis.html) | Grants permission to delete a Network Access Scope analysis | Write |  network-insights-access-scope-analysis* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteNetworkInsightsAnalysis](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInsightsAnalysis.html) | Grants permission to delete a network insights analysis | Write |  network-insights-analysis* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteNetworkInsightsPath](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInsightsPath.html) | Grants permission to delete a network insights path | Write |  network-insights-path* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterface.html) | Grants permission to delete a detached network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[DeleteNetworkInterfacePermission](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkInterfacePermission.html) | Grants permission to delete a permission that is associated with a network interface | Permissions management |  network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[DeletePlacementGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeletePlacementGroup.html) | Grants permission to delete a placement group | Write |  placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeletePublicIpv4Pool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeletePublicIpv4Pool.html) | Grants permission to delete a public IPv4 address pool for public IPv4 CIDRs that you own and brought to Amazon to manage with Amazon VPC IP Address Manager (IPAM) | Write |  ipv4pool-ec2* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteQueuedReservedInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteQueuedReservedInstances.html) | Grants permission to delete the queued purchases for the specified Reserved Instances | Write |  |  ec2:Region |   
[DeleteResourcePolicy](https://docs.aws.amazon.com/vpc/latest/ipam/share-pool-ipam.html) [permission only] | Grants permission to remove an IAM policy that enables cross-account sharing from a resource | Write |  ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
verified-access-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html) | Grants permission to delete a route from a route table | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
|  ec2:Region |   
[DeleteRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRouteTable.html) | Grants permission to delete a route table | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
|  ec2:Region |   
[DeleteSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html) | Grants permission to delete a security group | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[DeleteSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html) | Grants permission to delete a snapshot of an EBS volume | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:OutpostArn ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[DeleteSpotDatafeedSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSpotDatafeedSubscription.html) | Grants permission to delete a data feed for Spot Instances | Write |  |  ec2:Region |   
[DeleteSubnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSubnet.html) | Grants permission to delete a subnet | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[DeleteSubnetCidrReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSubnetCidrReservation.html) | Grants permission to delete a subnet CIDR reservation | Write |  |  ec2:Region |   
[DeleteTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTags.html) | Grants permission to delete one or more tags from Amazon EC2 resources | Tagging |  capacity-reservation |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
capacity-reservation-fleet |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
carrier-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
client-vpn-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
coip-pool |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
customer-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
declarative-policies-report |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
dedicated-host |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
dhcp-options |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
egress-only-internet-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
elastic-gpu |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
elastic-ip |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
export-image-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
export-instance-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
fleet |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
fpga-image |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
host-reservation |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
image |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
import-image-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
import-snapshot-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
instance |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
instance-connect-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
instance-event-window |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
internet-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-external-resource-verification-token |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-pool |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-resource-discovery |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-resource-discovery-association |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipam-scope |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipv4pool-ec2 |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
ipv6pool-ec2 |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
key-pair |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
launch-template |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-route-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-route-table-virtual-interface-group-association |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-route-table-vpc-association |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-virtual-interface |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
local-gateway-virtual-interface-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
natgateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-acl |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-access-scope |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-access-scope-analysis |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-analysis |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-insights-path |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
network-interface |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
placement-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
prefix-list |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
replace-root-volume-task |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
reserved-instances |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
route-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
security-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
security-group-rule |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
snapshot |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
spot-fleet-request |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
spot-instances-request |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
subnet |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
subnet-cidr-reservation |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter-rule |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-session |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
traffic-mirror-target |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway-attachment |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway-connect-peer |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway-multicast-domain |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway-policy-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway-route-table |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
transit-gateway-route-table-announcement |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-endpoint-target |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-group |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-instance |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-policy |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
verified-access-trust-provider |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
volume |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-block-public-access-exclusion |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint-connection |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service-permission |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-flow-log |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpc-peering-connection |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpn-connection |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
vpn-gateway |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ResourceTag/${TagKey} |   
|  aws:TagKeys ec2:Region |   
[DeleteTrafficMirrorFilter](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorFilter.html) | Grants permission to delete a traffic mirror filter | Write |  traffic-mirror-filter* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteTrafficMirrorFilterRule](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorFilterRule.html) | Grants permission to delete a traffic mirror filter rule | Write |  traffic-mirror-filter* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter-rule* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteTrafficMirrorSession](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorSession.html) | Grants permission to delete a traffic mirror session | Write |  traffic-mirror-session* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteTrafficMirrorTarget](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTrafficMirrorTarget.html) | Grants permission to delete a traffic mirror target | Write |  traffic-mirror-target* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteTransitGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGateway.html) | Grants permission to delete a transit gateway | Write |  transit-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
|  ec2:Region |   
[DeleteTransitGatewayConnect](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayConnect.html) | Grants permission to delete a transit gateway connect attachment | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[DeleteTransitGatewayConnectPeer](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayConnectPeer.html) | Grants permission to delete a transit gateway connect peer | Write |  transit-gateway-connect-peer* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayConnectPeerId |   
|  ec2:Region |   
[DeleteTransitGatewayMulticastDomain](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayMulticastDomain.html) | Grants permission to delete a transit gateway multicast domain | Write |  transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[DeleteTransitGatewayPeeringAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayPeeringAttachment.html) | Grants permission to delete a peering attachment from a transit gateway | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[DeleteTransitGatewayPolicyTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayPolicyTable.html) | Grants permission to delete a transit gateway policy table | Write |  transit-gateway-policy-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId |   
|  ec2:Region |   
[DeleteTransitGatewayPrefixListReference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayPrefixListReference.html) | Grants permission to delete a transit gateway prefix list reference | Write |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[DeleteTransitGatewayRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRoute.html) | Grants permission to delete a route from a transit gateway route table | Write |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[DeleteTransitGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRouteTable.html) | Grants permission to delete a transit gateway route table | Write |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[DeleteTransitGatewayRouteTableAnnouncement](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayRouteTableAnnouncement.html) | Grants permission to delete a transit gateway route table announcement | Write |  transit-gateway-route-table-announcement* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableAnnouncementId |   
|  ec2:Region |   
[DeleteTransitGatewayVpcAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayVpcAttachment.html) | Grants permission to delete a VPC attachment from a transit gateway | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[DeleteVerifiedAccessEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVerifiedAccessEndpoint.html) | Grants permission to delete a Verified Access endpoint | Write |  verified-access-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVerifiedAccessGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVerifiedAccessGroup.html) | Grants permission to delete a Verified Access group | Write |  verified-access-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVerifiedAccessInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVerifiedAccessInstance.html) | Grants permission to delete a Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVerifiedAccessTrustProvider](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVerifiedAccessTrustProvider.html) | Grants permission to delete a verified trust provider | Write |  verified-access-trust-provider* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVolume.html) | Grants permission to delete an EBS volume | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[DeleteVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpc.html) | Grants permission to delete a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DeleteVpcBlockPublicAccessExclusion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcBlockPublicAccessExclusion.html) | Grants permission to delete an exclusion list for blocked public access on a VPC | Write |  vpc-block-public-access-exclusion* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVpcEndpointConnectionNotifications](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointConnectionNotifications.html) | Grants permission to delete one or more VPC endpoint connection notifications | Write |  vpc-endpoint |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[DeleteVpcEndpointServiceConfigurations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointServiceConfigurations.html) | Grants permission to delete one or more VPC endpoint service configurations | Write |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[DeleteVpcEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpoints.html) | Grants permission to delete one or more VPC endpoints | Write |  vpc-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:VpceServiceName |   
|  ec2:Region |   
[DeleteVpcPeeringConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcPeeringConnection.html) | Grants permission to delete a VPC peering connection | Write |  vpc-peering-connection* |  aws:ResourceTag/${TagKey} ec2:AccepterVpc ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID |   
|  ec2:Region |   
[DeleteVpnConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnection.html) | Grants permission to delete a VPN connection | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVpnConnectionRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.html) | Grants permission to delete a static route for a VPN connection between a virtual private gateway and a customer gateway | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeleteVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnGateway.html) | Grants permission to delete a virtual private gateway | Write |  vpn-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeprovisionByoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionByoipCidr.html) | Grants permission to release an IP address range that was provisioned through bring your own IP addresses (BYOIP), and to delete the corresponding address pool | Write |  |  ec2:Region |   
[DeprovisionIpamByoasn](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionIpamByoasn.html) | Grants permission to deprovision an Autonomous System Number (ASN) from an Amazon Web Services account | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeprovisionIpamPoolCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionIpamPoolCidr.html) | Grants permission to deprovision a CIDR provisioned from an Amazon VPC IP Address Manager (IPAM) pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeprovisionPublicIpv4PoolCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionPublicIpv4PoolCidr.html) | Grants permission to deprovision a CIDR from a public IPv4 pool | Write |  ipv4pool-ec2* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DeregisterImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterImage.html) | Grants permission to deregister an Amazon Machine Image (AMI) | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[DeregisterInstanceEventNotificationAttributes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterInstanceEventNotificationAttributes.html) | Grants permission to remove tags from the set of tags to include in notifications about scheduled events for your instances | Write |  |  ec2:Region |   
[DeregisterTransitGatewayMulticastGroupMembers](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterTransitGatewayMulticastGroupMembers.html) | Grants permission to deregister one or more network interface members from a group IP address in a transit gateway multicast domain | Write |  network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
transit-gateway-multicast-domain |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[DeregisterTransitGatewayMulticastGroupSources](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterTransitGatewayMulticastGroupSources.html) | Grants permission to deregister one or more network interface sources from a group IP address in a transit gateway multicast domain | Write |  network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
transit-gateway-multicast-domain |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[DescribeAccountAttributes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAccountAttributes.html) | Grants permission to describe the attributes of the AWS account | List |  |  ec2:Region |   
[DescribeAddressTransfers](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddressTransfers.html) | Grants permission to describe an Elastic IP address transfer | List |  |  ec2:Region |   
[DescribeAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html) | Grants permission to describe one or more Elastic IP addresses | List |  |  ec2:Region |   
[DescribeAddressesAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddressesAttribute.html) | Grants permission to describe the attributes of the specified Elastic IP addresses | List |  |  ec2:Region |   
[DescribeAggregateIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAggregateIdFormat.html) | Grants permission to describe the longer ID format settings for all resource types | List |  |  ec2:Region |   
[DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) | Grants permission to describe one or more of the Availability Zones that are available to you | List |  |  ec2:Region |   
[DescribeAwsNetworkPerformanceMetricSubscriptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAwsNetworkPerformanceMetricSubscriptions.html) | Grants permission to describe the current infrastructure performance metric subscriptions | List |  |  ec2:Region |   
[DescribeBundleTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeBundleTasks.html) | Grants permission to describe one or more bundling tasks | List |  |  ec2:Region |   
[DescribeByoipCidrs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeByoipCidrs.html) | Grants permission to describe the IP address ranges that were provisioned through bring your own IP addresses (BYOIP) | List |  |  ec2:Region |   
[DescribeCapacityBlockExtensionHistory](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityBlockExtensionHistory.html) | Grants permission to describe Capacity Block extensions history | List |  capacity-reservation |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[DescribeCapacityBlockExtensionOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityBlockExtensionOfferings.html) | Grants permission to describe Capacity Block extensions offerings | List |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[DescribeCapacityBlockOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityBlockOfferings.html) | Grants permission to describe Capacity Block offerings available for purchase | List |  |  ec2:Region |   
[DescribeCapacityReservationBillingRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservationBillingRequests.html) | Grants permission to describe one or more requests to assign the billing of the unused capacity of a Capacity Reservation | List |  |  ec2:Region |   
[DescribeCapacityReservationFleets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservationFleets.html) | Grants permission to describe one or more Capacity Reservation Fleets | List |  |  ec2:Region |   
[DescribeCapacityReservations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html) | Grants permission to describe one or more Capacity Reservations | List |  |  ec2:Region |   
[DescribeCarrierGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCarrierGateways.html) | Grants permission to describe one or more Carrier Gateways | List |  |  ec2:Region |   
[DescribeClassicLinkInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html) | Grants permission to describe one or more linked EC2-Classic instances | List |  |  ec2:Region |   
[DescribeClientVpnAuthorizationRules](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnAuthorizationRules.html) | Grants permission to describe the authorization rules for a Client VPN endpoint | List |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeClientVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnConnections.html) | Grants permission to describe active client connections and connections that have been terminated within the last 60 minutes for a Client VPN endpoint | List |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[DescribeClientVpnEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnEndpoints.html) | Grants permission to describe one or more Client VPN endpoints | List |  client-vpn-endpoint |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[DescribeClientVpnRoutes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnRoutes.html) | Grants permission to describe the routes for a Client VPN endpoint | List |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[DescribeClientVpnTargetNetworks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnTargetNetworks.html) | Grants permission to describe the target networks that are associated with a Client VPN endpoint | List |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[DescribeCoipPools](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCoipPools.html) | Grants permission to describe the specified customer-owned address pools or all of your customer-owned address pools | List |  |  ec2:Region |   
[DescribeConversionTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeConversionTasks.html) | Grants permission to describe one or more conversion tasks | List |  |  ec2:Region |   
[DescribeCustomerGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCustomerGateways.html) | Grants permission to describe one or more customer gateways | List |  |  ec2:Region |   
[DescribeDeclarativePoliciesReports](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDeclarativePoliciesReports.html) | Grants permission to describe one or more declarative policies reports | List |  |  ec2:Region |   
[DescribeDhcpOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDhcpOptions.html) | Grants permission to describe one or more DHCP options sets | List |  |  ec2:Region |   
[DescribeEgressOnlyInternetGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeEgressOnlyInternetGateways.html) | Grants permission to describe one or more egress-only internet gateways | List |  |  ec2:Region |   
[DescribeElasticGpus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeElasticGpus.html) | Grants permission to describe an Elastic Graphics accelerator that is associated with an instance | List |  |  ec2:Region |   
[DescribeExportImageTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeExportImageTasks.html) | Grants permission to describe one or more export image tasks | List |  |  ec2:Region |   
[DescribeExportTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeExportTasks.html) | Grants permission to describe one or more export instance tasks | List |  |  ec2:Region |   
[DescribeFastLaunchImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFastLaunchImages.html) | Grants permission to describe fast-launch enabled Windows AMIs | List |  |  ec2:Region |   
[DescribeFastSnapshotRestores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFastSnapshotRestores.html) | Grants permission to describe the state of fast snapshot restores for snapshots | List |  |  ec2:Region |   
[DescribeFleetHistory](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetHistory.html) | Grants permission to describe the events for an EC2 Fleet during a specified time | List |  fleet* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeFleetInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetInstances.html) | Grants permission to describe the running instances for an EC2 Fleet | List |  fleet* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeFleets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleets.html) | Grants permission to describe one or more EC2 Fleets | List |  |  ec2:Region |   
[DescribeFlowLogs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html) | Grants permission to describe one or more flow logs | List |  |  ec2:Region |   
[DescribeFpgaImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImageAttribute.html) | Grants permission to describe the attributes of an Amazon FPGA Image (AFI) | List |  fpga-image* |  aws:ResourceTag/${TagKey} ec2:Owner ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeFpgaImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImages.html) | Grants permission to describe one or more Amazon FPGA Images (AFIs) | List |  |  ec2:Region |   
[DescribeHostReservationOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservationOfferings.html) | Grants permission to describe the Dedicated Host Reservations that are available to purchase | List |  |  ec2:Region |   
[DescribeHostReservations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservations.html) | Grants permission to describe the Dedicated Host Reservations that are associated with Dedicated Hosts in the AWS account | List |  |  ec2:Region |   
[DescribeHosts](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHosts.html) | Grants permission to describe one or more Dedicated Hosts | List |  |  ec2:Region |   
[DescribeIamInstanceProfileAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.html) | Grants permission to describe the IAM instance profile associations | List |  |  ec2:Region |   
[DescribeIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdFormat.html) | Grants permission to describe the ID format settings for resources | List |  |  ec2:Region |   
[DescribeIdentityIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIdentityIdFormat.html) | Grants permission to describe the ID format settings for resources for an IAM user, IAM role, or root user | List |  |  ec2:Region |   
[DescribeImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute.html) | Grants permission to describe an attribute of an Amazon Machine Image (AMI) | List |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) | Grants permission to describe one or more images (AMIs, AKIs, and ARIs) | List |  |  ec2:Region |   
[DescribeImportImageTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportImageTasks.html) | Grants permission to describe import virtual machine or import snapshot tasks | List |  |  ec2:Region |   
[DescribeImportSnapshotTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportSnapshotTasks.html) | Grants permission to describe import snapshot tasks | List |  |  ec2:Region |   
[DescribeInstanceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceAttribute.html) | Grants permission to describe the attributes of an instance | List |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[DescribeInstanceConnectEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceConnectEndpoints.html) | Grants permission to describe EC2 Instance Connect Endpoints | List |  |  ec2:Region |   
[DescribeInstanceCreditSpecifications](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceCreditSpecifications.html) | Grants permission to describe the credit option for CPU usage of one or more burstable performance instances | List |  |  ec2:Region |   
[DescribeInstanceEventNotificationAttributes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceEventNotificationAttributes.html) | Grants permission to describe the set of tags to include in notifications about scheduled events for your instances | List |  |  ec2:Region |   
[DescribeInstanceEventWindows](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceEventWindows.html) | Grants permission to describe the specified event windows or all event windows | List |  |  ec2:Region |   
[DescribeInstanceImageMetadata](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceImageMetadata.html) | Grants permission to describe the AMI that was used to launch an instance | List |  |  ec2:Region |   
[DescribeInstanceStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html) | Grants permission to describe the status of one or more instances | List |  |  ec2:Region |   
[DescribeInstanceTopology](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTopology.html) | Grants permission to describe a tree-based hierarchy that represents the physical host placement of EC2 instances | List |  |  ec2:Region |   
[DescribeInstanceTypeOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypeOfferings.html) | Grants permission to describe the set of instance types that are offered in a location | List |  |  ec2:Region |   
[DescribeInstanceTypes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.html) | Grants permission to describe the details of instance types that are offered in a location | List |  |  ec2:Region |   
[DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) | Grants permission to describe one or more instances | List |  |  ec2:Region |   
[DescribeInternetGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInternetGateways.html) | Grants permission to describe one or more internet gateways | List |  |  ec2:Region |   
[DescribeIpamByoasn](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamByoasn.html) | Grants permission to describe a bring your own Autonomous System Number (BYOASN) that you've brought to IPAM | List |  |  ec2:Region |   
[DescribeIpamExternalResourceVerificationTokens](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamExternalResourceVerificationTokens.html) | Grants permission to describe verification tokens, which proves ownership of an external resource | List |  |  ec2:Region |   
[DescribeIpamPools](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamPools.html) | Grants permission to describe Amazon VPC IP Address Manager (IPAM) pools | List |  |  ec2:Region |   
[DescribeIpamResourceDiscoveries](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamResourceDiscoveries.html) | Grants permission to describe IPAM resource discoveries | List |  |  ec2:Region |   
[DescribeIpamResourceDiscoveryAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamResourceDiscoveryAssociations.html) | Grants permission to describe resource discovery associations with an Amazon VPC IPAM | List |  |  ec2:Region |   
[DescribeIpamScopes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpamScopes.html) | Grants permission to describe Amazon VPC IP Address Manager (IPAM) scopes | List |  |  ec2:Region |   
[DescribeIpams](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpams.html) | Grants permission to describe an Amazon VPC IP Address Manager (IPAM) | List |  |  ec2:Region |   
[DescribeIpv6Pools](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIpv6Pools.html) | Grants permission to describe one or more IPv6 address pools | List |  |  ec2:Region |   
[DescribeKeyPairs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeKeyPairs.html) | Grants permission to describe one or more key pairs | List |  |  ec2:Region |   
[DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) | Grants permission to describe one or more launch template versions | List |  |  ec2:Region |  ssm:GetParameters   
[DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) | Grants permission to describe one or more launch templates | List |  |  ec2:Region |   
[DescribeLocalGatewayRouteTablePermissions](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html) [permission only] | Grants permission to allow a service to describe local gateway route table permissions | List |  |  ec2:Region |   
[DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.html) | Grants permission to describe the associations between virtual interface groups and local gateway route tables | List |  |  ec2:Region |   
[DescribeLocalGatewayRouteTableVpcAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayRouteTableVpcAssociations.html) | Grants permission to describe an association between VPCs and local gateway route tables | List |  |  ec2:Region |   
[DescribeLocalGatewayRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayRouteTables.html) | Grants permission to describe one or more local gateway route tables | List |  |  ec2:Region |   
[DescribeLocalGatewayVirtualInterfaceGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayVirtualInterfaceGroups.html) | Grants permission to describe local gateway virtual interface groups | List |  |  ec2:Region |   
[DescribeLocalGatewayVirtualInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayVirtualInterfaces.html) | Grants permission to describe local gateway virtual interfaces | List |  |  ec2:Region |   
[DescribeLocalGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGateways.html) | Grants permission to describe one or more local gateways | List |  |  ec2:Region |   
[DescribeLockedSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLockedSnapshots.html) | Grants permission to describe the lock status for a snapshot | List |  |  ec2:Region |   
[DescribeMacHosts](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeMacHosts.html) | Grants permission to describe your EC2 Mac Dedicated hosts | List |  |  ec2:Region |   
[DescribeManagedPrefixLists](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeManagedPrefixLists.html) | Grants permission to describe your managed prefix lists and any AWS-managed prefix lists | List |  |  ec2:Region |   
[DescribeMovingAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeMovingAddresses.html) | Grants permission to describe Elastic IP addresses that are being moved to the EC2-VPC platform | List |  |  ec2:Region |   
[DescribeNatGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html) | Grants permission to describe one or more NAT gateways | List |  |  ec2:Region |   
[DescribeNetworkAcls](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkAcls.html) | Grants permission to describe one or more network ACLs | List |  |  ec2:Region |   
[DescribeNetworkInsightsAccessScopeAnalyses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInsightsAccessScopeAnalyses.html) | Grants permission to describe one or more Network Access Scope analyses | List |  |  ec2:Region |   
[DescribeNetworkInsightsAccessScopes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInsightsAccessScopes.html) | Grants permission to describe the Network Access Scopes | List |  |  ec2:Region |   
[DescribeNetworkInsightsAnalyses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInsightsAnalyses.html) | Grants permission to describe one or more network insights analyses | List |  |  ec2:Region |   
[DescribeNetworkInsightsPaths](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInsightsPaths.html) | Grants permission to describe one or more network insights paths | List |  |  ec2:Region |   
[DescribeNetworkInterfaceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaceAttribute.html) | Grants permission to describe a network interface attribute | List |  |  ec2:Region |   
[DescribeNetworkInterfacePermissions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfacePermissions.html) | Grants permission to describe the permissions that are associated with a network interface | List |  |  ec2:Region |   
[DescribeNetworkInterfaces](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html) | Grants permission to describe one or more network interfaces | List |  |  ec2:Region |   
[DescribePlacementGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePlacementGroups.html) | Grants permission to describe one or more placement groups | List |  |  ec2:Region |   
[DescribePrefixLists](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html) | Grants permission to describe available AWS services in a prefix list format | List |  |  ec2:Region |   
[DescribePrincipalIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrincipalIdFormat.html) | Grants permission to describe the ID format settings for the root user and all IAM roles and IAM users that have explicitly specified a longer ID (17-character ID) preference | List |  |  ec2:Region |   
[DescribePublicIpv4Pools](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePublicIpv4Pools.html) | Grants permission to describe one or more IPv4 address pools | List |  |  ec2:Region |   
[DescribeRegions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html) | Grants permission to describe one or more AWS Regions that are currently available in your account | List |  |  ec2:Region |   
[DescribeReplaceRootVolumeTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReplaceRootVolumeTasks.html) | Grants permission to describe a root volume replacement task | List |  |  ec2:Region |   
[DescribeReservedInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstances.html) | Grants permission to describe one or more purchased Reserved Instances in your account | List |  |  ec2:Region |   
[DescribeReservedInstancesListings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesListings.html) | Grants permission to describe your account's Reserved Instance listings in the Reserved Instance Marketplace | List |  |  ec2:Region |   
[DescribeReservedInstancesModifications](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesModifications.html) | Grants permission to describe the modifications made to one or more Reserved Instances | List |  |  ec2:Region |   
[DescribeReservedInstancesOfferings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html) | Grants permission to describe the Reserved Instance offerings that are available for purchase | List |  |  ec2:Region |   
[DescribeRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html) | Grants permission to describe one or more route tables | List |  |  ec2:Region |   
[DescribeScheduledInstanceAvailability](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstanceAvailability.html) | Grants permission to find available schedules for Scheduled Instances | List |  |  ec2:Region |   
[DescribeScheduledInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstances.html) | Grants permission to describe one or more Scheduled Instances in your account | List |  |  ec2:Region |   
[DescribeSecurityGroupReferences](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroupReferences.html) | Grants permission to describe the VPCs on the other side of a VPC peering connection that are referencing specified VPC security groups | List |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[DescribeSecurityGroupRules](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroupRules.html) | Grants permission to describe one or more of your security group rules | List |  |  ec2:Region |   
[DescribeSecurityGroupVpcAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroupVpcAssociations.html) | Grants permission to describe security group VPC associations | List |  |  ec2:Region |   
[DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) | Grants permission to describe one or more security groups | List |  |  ec2:Region |   
[DescribeSnapshotAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshotAttribute.html) | Grants permission to describe an attribute of a snapshot | List |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:OutpostArn ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:SourceOutpostArn ec2:VolumeSize |   
|  ec2:Region |   
[DescribeSnapshotTierStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshotTierStatus.html) | Grants permission to describe the storage tier status for Amazon EBS snapshots | List |  |  ec2:Region |   
[DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) | Grants permission to describe one or more EBS snapshots | List |  |  ec2:Region |   
[DescribeSpotDatafeedSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotDatafeedSubscription.html) | Grants permission to describe the data feed for Spot Instances | List |  |  ec2:Region |   
[DescribeSpotFleetInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetInstances.html) | Grants permission to describe the running instances for a Spot Fleet | List |  spot-fleet-request* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeSpotFleetRequestHistory](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequestHistory.html) | Grants permission to describe the events for a Spot Fleet request during a specified time | List |  spot-fleet-request* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeSpotFleetRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequests.html) | Grants permission to describe one or more Spot Fleet requests | List |  |  ec2:Region |   
[DescribeSpotInstanceRequests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotInstanceRequests.html) | Grants permission to describe one or more Spot Instance requests | List |  |  ec2:Region |   
[DescribeSpotPriceHistory](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotPriceHistory.html) | Grants permission to describe the Spot Instance price history | List |  |  ec2:Region |   
[DescribeStaleSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeStaleSecurityGroups.html) | Grants permission to describe the stale security group rules for security groups in a specified VPC | List |  |  ec2:Region |   
[DescribeStoreImageTasks](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeStoreImageTasks.html) | Grants permission to describe the progress of the AMI store tasks | List |  |  ec2:Region |   
[DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html) | Grants permission to describe one or more subnets | List |  |  ec2:Region |   
[DescribeTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTags.html) | Grants permission to describe one or more tags for an Amazon EC2 resource | List |  |  ec2:Region |   
[DescribeTrafficMirrorFilterRules](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorFilterRules.html) | Grants permission to describe traffic mirror filters that determine the traffic that is mirrored | List |  |  ec2:Region |   
[DescribeTrafficMirrorFilters](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorFilters.html) | Grants permission to describe one or more traffic mirror filters | List |  |  ec2:Region |   
[DescribeTrafficMirrorSessions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorSessions.html) | Grants permission to describe one or more traffic mirror sessions | List |  |  ec2:Region |   
[DescribeTrafficMirrorTargets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrafficMirrorTargets.html) | Grants permission to describe one or more traffic mirror targets | List |  |  ec2:Region |   
[DescribeTransitGatewayAttachments](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html) | Grants permission to describe one or more attachments between resources and transit gateways | List |  |  ec2:Region |   
[DescribeTransitGatewayConnectPeers](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayConnectPeers.html) | Grants permission to describe one or more transit gateway connect peers | List |  |  ec2:Region |   
[DescribeTransitGatewayConnects](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayConnects.html) | Grants permission to describe one or more transit gateway connect attachments | List |  |  ec2:Region |   
[DescribeTransitGatewayMulticastDomains](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayMulticastDomains.html) | Grants permission to describe one or more transit gateway multicast domains | List |  |  ec2:Region |   
[DescribeTransitGatewayPeeringAttachments](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayPeeringAttachments.html) | Grants permission to describe one or more transit gateway peering attachments | List |  |  ec2:Region |   
[DescribeTransitGatewayPolicyTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayPolicyTables.html) | Grants permission to describe a transit gateway policy table | List |  |  ec2:Region |   
[DescribeTransitGatewayRouteTableAnnouncements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayRouteTableAnnouncements.html) | Grants permission to describe a transit gateway route table announcement | List |  |  ec2:Region |   
[DescribeTransitGatewayRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayRouteTables.html) | Grants permission to describe one or more transit gateway route tables | List |  |  ec2:Region |   
[DescribeTransitGatewayVpcAttachments](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayVpcAttachments.html) | Grants permission to describe one or more VPC attachments on a transit gateway | List |  |  ec2:Region |   
[DescribeTransitGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html) | Grants permission to describe one or more transit gateways | List |  |  ec2:Region |   
[DescribeTrunkInterfaceAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTrunkInterfaceAssociations.html) | Grants permission to describe one or more network interface trunk associations | List |  |  ec2:Region |   
[DescribeVerifiedAccessEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVerifiedAccessEndpoints.html) | Grants permission to describe the specified Verified Access endpoints or all Verified Access endpoints | List |  |  ec2:Region |   
[DescribeVerifiedAccessGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVerifiedAccessGroups.html) | Grants permission to describe the specified Verified Access groups or all Verified Access groups | List |  |  ec2:Region |   
[DescribeVerifiedAccessInstanceLoggingConfigurations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVerifiedAccessInstanceLoggingConfigurations.html) | Grants permission to describe the current logging configuration for the Verified Access instances | List |  |  ec2:Region |   
[DescribeVerifiedAccessInstanceWebAclAssociations](https://docs.aws.amazon.com/verified-access/latest/ug/waf-integration.html) [permission only] | Grants permission to describe the AWS Web Application Firewall (WAF) web access control list (ACL) associations for a Verified Access instance | List |  |  ec2:Region |   
[DescribeVerifiedAccessInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVerifiedAccessInstances.html) | Grants permission to describe the specified Verified Access instances or all Verified Access instances | List |  |  ec2:Region |   
[DescribeVerifiedAccessTrustProviders](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVerifiedAccessTrustProviders.html) | Grants permission to describe details of existing Verified Access trust providers | List |  |  ec2:Region |   
[DescribeVolumeAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeAttribute.html) | Grants permission to describe an attribute of an EBS volume | List |  volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[DescribeVolumeStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeStatus.html) | Grants permission to describe the status of one or more EBS volumes | List |  |  ec2:Region |   
[DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html) | Grants permission to describe one or more EBS volumes | List |  |  ec2:Region |   
[DescribeVolumesModifications](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumesModifications.html) | Grants permission to describe the current modification status of one or more EBS volumes | List |  |  ec2:Region |   
[DescribeVpcAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcAttribute.html) | Grants permission to describe an attribute of a VPC | List |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DescribeVpcBlockPublicAccessExclusions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcBlockPublicAccessExclusions.html) | Grants permission to describe an exclusion list for blocked public access on a VPC | List |  vpc-block-public-access-exclusion |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DescribeVpcBlockPublicAccessOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcBlockPublicAccessOptions.html) | Grants permission to describe options for blocked public access on a VPC | List |  |  ec2:Region |   
[DescribeVpcClassicLink](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcClassicLink.html) | Grants permission to describe the ClassicLink status of one or more VPCs | List |  |  ec2:Region |   
[DescribeVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcClassicLinkDnsSupport.html) | Grants permission to describe the ClassicLink DNS support status of one or more VPCs | List |  |  ec2:Region |   
[DescribeVpcEndpointAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointAssociations.html) | Grants permission to describe the VPC endpoint associations | List |  vpc-endpoint |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:VpceServiceName ec2:VpceServiceOwner |   
|  ec2:Region |   
[DescribeVpcEndpointConnectionNotifications](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnectionNotifications.html) | Grants permission to describe the connection notifications for VPC endpoints and VPC endpoint services | List |  |  ec2:Region |   
[DescribeVpcEndpointConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnections.html) | Grants permission to describe the VPC endpoint connections to your VPC endpoint services | List |  |  ec2:Region |   
[DescribeVpcEndpointServiceConfigurations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServiceConfigurations.html) | Grants permission to describe VPC endpoint service configurations (your services) | List |  |  ec2:Region |   
[DescribeVpcEndpointServicePermissions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServicePermissions.html) | Grants permission to describe the principals (service consumers) that are permitted to discover your VPC endpoint service | List |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[DescribeVpcEndpointServices](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServices.html) | Grants permission to describe all supported AWS services that can be specified when creating a VPC endpoint | List |  |  ec2:Region |   
[DescribeVpcEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html) | Grants permission to describe one or more VPC endpoints | List |  |  ec2:Region |   
[DescribeVpcPeeringConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcPeeringConnections.html) | Grants permission to describe one or more VPC peering connections | List |  |  ec2:Region |   
[DescribeVpcs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcs.html) | Grants permission to describe one or more VPCs | List |  |  ec2:Region |   
[DescribeVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html) | Grants permission to describe one or more VPN connections | List |  |  ec2:Region |   
[DescribeVpnGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html) | Grants permission to describe one or more virtual private gateways | List |  |  ec2:Region |   
[DetachClassicLinkVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachClassicLinkVpc.html) | Grants permission to unlink (detach) a linked EC2-Classic instance from a VPC | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DetachInternetGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachInternetGateway.html) | Grants permission to detach an internet gateway from a VPC | Write |  internet-gateway* |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DetachNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachNetworkInterface.html) | Grants permission to detach a network interface from an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[DetachVerifiedAccessTrustProvider](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVerifiedAccessTrustProvider.html) | Grants permission to detach a trust provider from a Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
verified-access-trust-provider* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DetachVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVolume.html) | Grants permission to detach an EBS volume from an instance | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
instance |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[DetachVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVpnGateway.html) | Grants permission to detach a virtual private gateway from a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
vpn-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisableAddressTransfer](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAddressTransfer.html) | Grants permission to disable Elastic IP address transfer | Write |  elastic-ip* |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisableAllowedImagesSettings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAllowedImagesSettings.html) | Grants permission to disable allowed images settings | Write |  |  ec2:Region |   
[DisableAwsNetworkPerformanceMetricSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAwsNetworkPerformanceMetricSubscription.html) | Grants permission to disable infrastructure performance metric subscriptions | Write |  |  ec2:Region |   
[DisableEbsEncryptionByDefault](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableEbsEncryptionByDefault.html) | Grants permission to disable EBS encryption by default for your account | Write |  |  ec2:Region |   
[DisableFastLaunch](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableFastLaunch.html) | Grants permission to disable faster launching for Windows AMIs | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[DisableFastSnapshotRestores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableFastSnapshotRestores.html) | Grants permission to disable fast snapshot restores for one or more snapshots in specified Availability Zones | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[DisableImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableImage.html) | Grants permission to disable an AMI | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[DisableImageBlockPublicAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableImageBlockPublicAccess.html) | Grants permission to disable block public access for AMIs at the account level in the specified AWS Region | Write |  |  ec2:Region |   
[DisableImageDeprecation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableImageDeprecation.html) | Grants permission to cancel the deprecation of the specified AMI | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[DisableImageDeregistrationProtection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableImageDeregistrationProtection.html) | Grants permission to disable deregistration protection for an AMI. When deregistration protection is disabled, the AMI can be deregistered | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[DisableIpamOrganizationAdminAccount](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableIpamOrganizationAdminAccount.html) | Grants permission to disable an AWS Organizations member account as an Amazon VPC IP Address Manager (IPAM) admin account | Write |  |  ec2:Region |  organizations:DeregisterDelegatedAdministrator   
[DisableSerialConsoleAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableSerialConsoleAccess.html) | Grants permission to disable access to the EC2 serial console of all instances for your account | Write |  |  ec2:Region |   
[DisableSnapshotBlockPublicAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableSnapshotBlockPublicAccess.html) | Grants permission to disable the block public access for snapshots setting for a Region | Write |  |  ec2:Region |   
[DisableTransitGatewayRouteTablePropagation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableTransitGatewayRouteTablePropagation.html) | Grants permission to disable a resource attachment from propagating routes to the specified propagation route table | Write |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-route-table-announcement |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableAnnouncementId |   
|  ec2:Region |   
[DisableVgwRoutePropagation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVgwRoutePropagation.html) | Grants permission to disable a virtual private gateway from propagating routes to a specified route table of a VPC | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
vpn-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisableVpcClassicLink](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLink.html) | Grants permission to disable ClassicLink for a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DisableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLinkDnsSupport.html) | Grants permission to disable ClassicLink DNS support for a VPC | Write |  vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DisassociateAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateAddress.html) | Grants permission to disassociate an Elastic IP address from an instance or network interface | Write |  elastic-ip |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[DisassociateCapacityReservationBillingOwner](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateCapacityReservationBillingOwner.html) | Grants permission to cancel a pending request to assign billing of the unused capacity of a Capacity Reservation to a consumer account | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[DisassociateClientVpnTargetNetwork](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateClientVpnTargetNetwork.html) | Grants permission to disassociate a target network from a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[DisassociateEnclaveCertificateIamRole](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateEnclaveCertificateIamRole.html) | Grants permission to disassociate an ACM certificate from a IAM role | Write |  certificate* |  |   
role* |  |   
|  ec2:Region |   
[DisassociateIamInstanceProfile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html) | Grants permission to disassociate an IAM instance profile from a running or stopped instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[DisassociateInstanceEventWindow](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateInstanceEventWindow.html) | Grants permission to disassociate one or more targets from an event window | Write |  instance-event-window* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisassociateIpamByoasn](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIpamByoasn.html) | Grants permission to disassociate an Autonomous System Number (ASN) from a BYOIP CIDR | Write |  |  ec2:Region |   
[DisassociateIpamResourceDiscovery](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIpamResourceDiscovery.html) | Grants permission to disassociate a resource discovery from an Amazon VPC IPAM | Write |  ipam-resource-discovery-association* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisassociateNatGatewayAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateNatGatewayAddress.html) | Grants permission to disassociate a secondary Elastic IP address from a public NAT gateway | Write |  elastic-ip* |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
natgateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
network-interface* |  aws:ResourceTag/${TagKey} ec2:AuthorizedUser ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Permission ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[DisassociateRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateRouteTable.html) | Grants permission to disassociate a subnet from a route table | Write |  internet-gateway |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
ipv4pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipv6pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
route-table |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
vpn-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisassociateSecurityGroupVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateSecurityGroupVpc.html) | Grants permission to disassociate a security group from a VPC | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
vpc |  aws:ResourceTag/${TagKey} ec2:Ipv4IpamPoolId ec2:Ipv6IpamPoolId ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[DisassociateSubnetCidrBlock](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateSubnetCidrBlock.html) | Grants permission to disassociate a CIDR block from a subnet | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[DisassociateTransitGatewayMulticastDomain](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTransitGatewayMulticastDomain.html) | Grants permission to disassociate one or more subnets from a transit gateway multicast domain | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[DisassociateTransitGatewayPolicyTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTransitGatewayPolicyTable.html) | Grants permission to disassociate a policy table from a transit gateway | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-policy-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId |   
|  ec2:Region |   
[DisassociateTransitGatewayRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTransitGatewayRouteTable.html) | Grants permission to disassociate a resource attachment from a transit gateway route table | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[DisassociateTrunkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTrunkInterface.html) | Grants permission to disassociate a branch network interface to a trunk network interface | Write |  |  ec2:Region |   
[DisassociateVerifiedAccessInstanceWebAcl](https://docs.aws.amazon.com/verified-access/latest/ug/waf-integration.html) [permission only] | Grants permission to disassociate an AWS Web Application Firewall (WAF) web access control list (ACL) from a Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[DisassociateVpcCidrBlock](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateVpcCidrBlock.html) | Grants permission to disassociate a CIDR block from a VPC | Write |  vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[EnableAddressTransfer](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAddressTransfer.html) | Grants permission to enable Elastic IP address transfer | Write |  elastic-ip* |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[EnableAllowedImagesSettings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAllowedImagesSettings.html) | Grants permission to enable allowed images settings | Write |  |  ec2:Region |   
[EnableAwsNetworkPerformanceMetricSubscription](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAwsNetworkPerformanceMetricSubscription.html) | Grants permission to enable infrastructure performance subscriptions | Write |  |  ec2:Region |   
[EnableEbsEncryptionByDefault](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableEbsEncryptionByDefault.html) | Grants permission to enable EBS encryption by default for your account | Write |  |  ec2:Region |   
[EnableFastLaunch](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableFastLaunch.html) | Grants permission to enable faster launching for Windows AMIs | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |  ec2:CreateLaunchTemplate  ec2:CreateSnapshot  ec2:CreateTags  ec2:DeleteSnapshot  ec2:DescribeImages  ec2:DescribeInstanceAttribute  ec2:DescribeInstanceStatus  ec2:DescribeInstanceTypeOfferings  ec2:DescribeInstances  ec2:DescribeLaunchTemplateVersions  ec2:DescribeLaunchTemplates  ec2:DescribeSnapshots  ec2:DescribeSubnets  ec2:RunInstances  ec2:StopInstances  ec2:TerminateInstances  iam:PassRole   
launch-template |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[EnableFastSnapshotRestores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableFastSnapshotRestores.html) | Grants permission to enable fast snapshot restores for one or more snapshots in specified Availability Zones | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[EnableImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImage.html) | Grants permission to re-enable a disabled AMI | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[EnableImageBlockPublicAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImageBlockPublicAccess.html) | Grants permission to enable block public access for AMIs at the account level in the specified AWS Region | Write |  |  ec2:Region |   
[EnableImageDeprecation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImageDeprecation.html) | Grants permission to enable deprecation of the specified AMI at the specified date and time | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[EnableImageDeregistrationProtection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImageDeregistrationProtection.html) | Grants permission to enable deregistration protection for an AMI. When deregistration protection is enabled, the AMI can't be deregistered | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[EnableIpamOrganizationAdminAccount](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableIpamOrganizationAdminAccount.html) | Grants permission to enable an AWS Organizations member account as an Amazon VPC IP Address Manager (IPAM) admin account | Write |  |  ec2:Region |  iam:CreateServiceLinkedRole  organizations:EnableAWSServiceAccess  organizations:RegisterDelegatedAdministrator   
[EnableReachabilityAnalyzerOrganizationSharing](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableReachabilityAnalyzerOrganizationSharing.html) | Grants permission to enable organization sharing of reachability analyzer | Write |  |  ec2:Region |  iam:CreateServiceLinkedRole  organizations:EnableAWSServiceAccess   
[EnableSerialConsoleAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableSerialConsoleAccess.html) | Grants permission to enable access to the EC2 serial console of all instances for your account | Write |  |  ec2:Region |   
[EnableSnapshotBlockPublicAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableSnapshotBlockPublicAccess.html) | Grants permission to enable or modify the block public access for snapshots setting for a Region | Write |  |  ec2:Region |   
[EnableTransitGatewayRouteTablePropagation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableTransitGatewayRouteTablePropagation.html) | Grants permission to enable an attachment to propagate routes to a propagation route table | Write |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-route-table-announcement |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableAnnouncementId |   
|  ec2:Region |   
[EnableVgwRoutePropagation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.html) | Grants permission to enable a virtual private gateway to propagate routes to a VPC route table | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
vpn-gateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[EnableVolumeIO](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVolumeIO.html) | Grants permission to enable I/O operations for a volume that had I/O operations disabled | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[EnableVpcClassicLink](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVpcClassicLink.html) | Grants permission to enable a VPC for ClassicLink | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[EnableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVpcClassicLinkDnsSupport.html) | Grants permission to enable a VPC to support DNS hostname resolution for ClassicLink | Write |  vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[ExportClientVpnClientCertificateRevocationList](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientCertificateRevocationList.html) | Grants permission to download the client certificate revocation list for a Client VPN endpoint | Read |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[ExportClientVpnClientConfiguration](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportClientVpnClientConfiguration.html) | Grants permission to download the contents of the Client VPN endpoint configuration file for a Client VPN endpoint | Read |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[ExportImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportImage.html) | Grants permission to export an Amazon Machine Image (AMI) to a VM file | Write |  export-image-task* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[ExportTransitGatewayRoutes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportTransitGatewayRoutes.html) | Grants permission to export routes from a transit gateway route table to an Amazon S3 bucket | Write |  |  ec2:Region |   
[ExportVerifiedAccessInstanceClientConfiguration](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ExportVerifiedAccessInstanceClientConfiguration.html) | Grants permission to export a verified access instance client configuration | Read |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetAllowedImagesSettings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAllowedImagesSettings.html) | Grants permission to get the allowed settings for images | Read |  |  ec2:Region |   
[GetAssociatedEnclaveCertificateIamRoles](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAssociatedEnclaveCertificateIamRoles.html) | Grants permission to get the list of roles associated with an ACM certificate | Read |  certificate* |  |   
|  ec2:Region |   
[GetAssociatedIpv6PoolCidrs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAssociatedIpv6PoolCidrs.html) | Grants permission to get information about the IPv6 CIDR block associations for a specified IPv6 address pool | Read |  |  ec2:Region |   
[GetAwsNetworkPerformanceData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.html) | Grants permission to get network performance data | Read |  |  ec2:Region |   
[GetCapacityReservationUsage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityReservationUsage.html) | Grants permission to get usage information about a Capacity Reservation | Read |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:CapacityReservationFleet |   
|  ec2:Region |   
[GetCoipPoolUsage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCoipPoolUsage.html) | Grants permission to describe the allocations from the specified customer-owned address pool | Read |  coip-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetConsoleOutput](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleOutput.html) | Grants permission to get the console output for an instance | Read |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[GetConsoleScreenshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleScreenshot.html) | Grants permission to retrieve a JPG-format screenshot of a running instance | Read |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:NewInstanceProfile ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[GetDeclarativePoliciesReportSummary](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetDeclarativePoliciesReportSummary.html) | Grants permission to get the report summary of declarative policies | Read |  declarative-policies-report* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetDefaultCreditSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetDefaultCreditSpecification.html) | Grants permission to get the default credit option for CPU usage of a burstable performance instance family | Read |  |  ec2:Region |   
[GetEbsDefaultKmsKeyId](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsDefaultKmsKeyId.html) | Grants permission to get the ID of the default customer master key (CMK) for EBS encryption by default | Read |  |  ec2:Region |   
[GetEbsEncryptionByDefault](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsEncryptionByDefault.html) | Grants permission to describe whether EBS encryption by default is enabled for your account | Read |  |  ec2:Region |   
[GetFlowLogsIntegrationTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetFlowLogsIntegrationTemplate.html) | Grants permission to generate a CloudFormation template to streamline the integration of VPC flow logs with Amazon Athena | Read |  vpc-flow-log* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetGroupsForCapacityReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetGroupsForCapacityReservation.html) | Grants permission to list the resource groups to which a Capacity Reservation has been added | List |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:CapacityReservationFleet |   
|  ec2:Region |   
[GetHostReservationPurchasePreview](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetHostReservationPurchasePreview.html) | Grants permission to preview a reservation purchase with configurations that match those of a Dedicated Host | Read |  |  ec2:Region |   
[GetImageBlockPublicAccessState](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetImageBlockPublicAccessState.html) | Grants permission to get the current state of block public access for AMIs at the account level in the specified AWS Region | Read |  |  ec2:Region |   
[GetInstanceMetadataDefaults](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceMetadataDefaults.html) | Grants permission to view the default instance metadata service (IMDS) settings set for your account in the specified Region | List |  |  ec2:Region |   
[GetInstanceTpmEkPub](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTpmEkPub.html) | Grants permission to get the public endorsement key associated with the Nitro Trusted Platform Module (NitroTPM) for the specified instance | Read |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) | Grants permission to view a list of instance types with specified instance attributes | List |  |  ec2:Region |   
[GetInstanceUefiData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData.html) | Grants permission to retrieve the binary representation of the UEFI variable store | Read |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:NewInstanceProfile ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[GetIpamAddressHistory](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamAddressHistory.html) | Grants permission to retrieve historical information about a CIDR within an Amazon VPC IP Address Manager (IPAM) scope | Read |  ipam-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetIpamDiscoveredAccounts](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamDiscoveredAccounts.html) | Grants permission to retrieve IPAM discovered accounts | Read |  ipam-resource-discovery* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetIpamDiscoveredPublicAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamDiscoveredPublicAddresses.html) | Grants permission to retrieve the public IP addresses that have been discovered by IPAM | Read |  ipam-resource-discovery* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetIpamDiscoveredResourceCidrs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamDiscoveredResourceCidrs.html) | Grants permission to retrieve the resource CIDRs that are monitored as part of a resource discovery | Read |  ipam-resource-discovery* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetIpamPoolAllocations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamPoolAllocations.html) | Grants permission to get a list of all the CIDR allocations in an Amazon VPC IP Address Manager (IPAM) pool | List |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetIpamPoolCidrs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamPoolCidrs.html) | Grants permission to get the CIDRs provisioned to an Amazon VPC IP Address Manager (IPAM) pool | Read |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetIpamResourceCidrs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamResourceCidrs.html) | Grants permission to get information about the resources in an Amazon VPC IP Address Manager (IPAM) scope | Read |  ipam-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetLaunchTemplateData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetLaunchTemplateData.html) | Grants permission to get the configuration data of the specified instance for use with a new launch template or launch template version | Read |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[GetManagedPrefixListAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetManagedPrefixListAssociations.html) | Grants permission to get information about the resources that are associated with the specified managed prefix list | Read |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetManagedPrefixListEntries](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetManagedPrefixListEntries.html) | Grants permission to get information about the entries for a specified managed prefix list | Read |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetNetworkInsightsAccessScopeAnalysisFindings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetNetworkInsightsAccessScopeAnalysisFindings.html) | Grants permission to get the findings for one or more Network Access Scope analyses | Read |  network-insights-access-scope-analysis* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetNetworkInsightsAccessScopeContent](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetNetworkInsightsAccessScopeContent.html) | Grants permission to get the content for a specified Network Access Scope | Read |  network-insights-access-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetPasswordData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html) | Grants permission to retrieve the encrypted administrator password for a running Windows instance | Read |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[GetReservedInstancesExchangeQuote](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetReservedInstancesExchangeQuote.html) | Grants permission to return a quote and exchange information for exchanging one or more Convertible Reserved Instances for a new Convertible Reserved Instance | Read |  |  ec2:Region |   
[GetResourcePolicy](https://docs.aws.amazon.com/vpc/latest/ipam/share-pool-ipam.html) [permission only] | Grants permission to describe an IAM policy that enables cross-account sharing | Read |  ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
verified-access-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetSecurityGroupsForVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSecurityGroupsForVpc.html) | Grants permission to retrieve a list of security groups for a specified VPC | Read |  vpc* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[GetSerialConsoleAccessStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSerialConsoleAccessStatus.html) | Grants permission to retrieve the access status of your account to the EC2 serial console of all instances | Read |  |  ec2:Region |   
[GetSnapshotBlockPublicAccessState](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSnapshotBlockPublicAccessState.html) | Grants permission to retrieve the current state of the block public access for snapshots setting for a Region | Read |  |  ec2:Region |   
[GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) | Grants permission to calculate the Spot placement score for a Region or Availability Zone based on the specified target capacity and compute requirements | Read |  |  ec2:Region |   
[GetSubnetCidrReservations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSubnetCidrReservations.html) | Grants permission to retrieve information about the subnet CIDR reservations | Read |  |  ec2:Region |   
[GetTransitGatewayAttachmentPropagations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayAttachmentPropagations.html) | Grants permission to list the route tables to which a resource attachment propagates routes | List |  |  ec2:Region |   
[GetTransitGatewayMulticastDomainAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayMulticastDomainAssociations.html) | Grants permission to get information about the associations for a transit gateway multicast domain | List |  transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[GetTransitGatewayPolicyTableAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayPolicyTableAssociations.html) | Grants permission to get information about associations for a transit gateway policy table | List |  transit-gateway-policy-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId |   
|  ec2:Region |   
[GetTransitGatewayPolicyTableEntries](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayPolicyTableEntries.html) | Grants permission to get information about associations for a transit gateway policy table entry | List |  transit-gateway-policy-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId |   
|  ec2:Region |   
[GetTransitGatewayPrefixListReferences](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayPrefixListReferences.html) | Grants permission to get information about prefix list references for a transit gateway route table | List |  |  ec2:Region |   
[GetTransitGatewayRouteTableAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayRouteTableAssociations.html) | Grants permission to get information about associations for a transit gateway route table | List |  |  ec2:Region |   
[GetTransitGatewayRouteTablePropagations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayRouteTablePropagations.html) | Grants permission to get information about the route table propagations for a transit gateway route table | List |  |  ec2:Region |   
[GetVerifiedAccessEndpointPolicy](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVerifiedAccessEndpointPolicy.html) | Grants permission to show the Verified Access policy associated with the endpoint | List |  verified-access-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetVerifiedAccessEndpointTargets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVerifiedAccessEndpointTargets.html) | Grants permission to get verified access endpoint targets | List |  verified-access-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetVerifiedAccessGroupPolicy](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVerifiedAccessGroupPolicy.html) | Grants permission to show the contents of the Verified Access policy associated with the group | List |  verified-access-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetVerifiedAccessInstanceWebAcl](https://docs.aws.amazon.com/verified-access/latest/ug/waf-integration.html) [permission only] | Grants permission to show the AWS Web Application Firewall (WAF) web access control list (ACL) for a Verified Access instance | List |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[GetVpnConnectionDeviceSampleConfiguration](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceSampleConfiguration.html) | Grants permission to download an AWS-provided sample configuration file to be used with the customer gateway device | List |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
vpn-connection-device-type* |  |   
|  ec2:Region |   
[GetVpnConnectionDeviceTypes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVpnConnectionDeviceTypes.html) | Grants permission to obtain a list of customer gateway devices for which sample configuration files can be provided | List |  |  ec2:Region |   
[GetVpnTunnelReplacementStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVpnTunnelReplacementStatus.html) | Grants permission to view available tunnel endpoint maintenance events | List |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ImportByoipCidrToIpam](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-transfer-ipv4.html) [permission only] | Grants permission to transfer existing BYOIP IPv4 CIDRs to IPAM | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ImportClientVpnClientCertificateRevocationList](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportClientVpnClientCertificateRevocationList.html) | Grants permission to upload a client certificate revocation list to a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[ImportImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) | Grants permission to import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI) | Write |  image* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:RootDeviceType |  ec2:CreateTags   
import-image-task* |  aws:RequestTag/${TagKey} aws:TagKeys |   
snapshot |  aws:ResourceTag/${TagKey} ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[ImportInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html) | Grants permission to create an import instance task using metadata from a disk image | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ImportKeyPair](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html) | Grants permission to import a public key from an RSA key pair that was created with a third-party tool | Write |  key-pair* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
|  ec2:Region |   
[ImportSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportSnapshot.html) | Grants permission to import a disk into an EBS snapshot | Write |  import-snapshot-task* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
snapshot* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:Owner ec2:ParentVolume ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[ImportVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportVolume.html) | Grants permission to create an import volume task using metadata from a disk image | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[InjectApiError](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html) [permission only] | Grants permission to temporarily inject errors for target API requests | Write |  |  ec2:FisActionId ec2:FisTargetArns ec2:Region |   
[ListImagesInRecycleBin](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ListImagesInRecycleBin.html) | Grants permission to list Amazon Machine Images (AMIs) that are currently in the Recycle Bin | List |  |  ec2:Region |   
[ListSnapshotsInRecycleBin](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ListSnapshotsInRecycleBin.html) | Grants permission to list the Amazon EBS snapshots that are currently in the Recycle Bin | List |  |  ec2:Region |   
[LockSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LockSnapshot.html) | Grants permission to lock an Amazon EBS snapshot in either governance or compliance mode to protect it against accidental or malicious deletions | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotCoolOffPeriod ec2:SnapshotID ec2:SnapshotLockDuration ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[ModifyAddressAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyAddressAttribute.html) | Grants permission to modify an attribute of the specified Elastic IP address | Write |  elastic-ip* |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Attribute ec2:Attribute/${AttributeName} ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyAvailabilityZoneGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyAvailabilityZoneGroup.html) | Grants permission to modify the opt-in status of the Local Zone and Wavelength Zone group for your account | Write |  |  ec2:Region |   
[ModifyCapacityReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyCapacityReservation.html) | Grants permission to modify a Capacity Reservation's capacity and the conditions under which it is to be released | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:CapacityReservationFleet |   
|  ec2:Region |   
[ModifyCapacityReservationFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyCapacityReservationFleet.html) | Grants permission to modify a Capacity Reservation Fleet | Write |  capacity-reservation-fleet* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |  ec2:ModifyCapacityReservation   
|  ec2:Region |   
[ModifyClientVpnEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyClientVpnEndpoint.html) | Grants permission to modify a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
vpc |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[ModifyDefaultCreditSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyDefaultCreditSpecification.html) | Grants permission to change the account level default credit option for CPU usage of burstable performance instances | Write |  |  ec2:Region |   
[ModifyEbsDefaultKmsKeyId](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyEbsDefaultKmsKeyId.html) | Grants permission to change the default customer master key (CMK) for EBS encryption by default for your account | Write |  |  ec2:Region |   
[ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet.html) | Grants permission to modify an EC2 Fleet | Write |  fleet* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
image |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
launch-template |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ModifyFpgaImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFpgaImageAttribute.html) | Grants permission to modify an attribute of an Amazon FPGA Image (AFI) | Write |  fpga-image* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyHosts](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyHosts.html) | Grants permission to modify a Dedicated Host | Write |  dedicated-host* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdFormat.html) | Grants permission to modify the ID format for a resource | Write |  |  ec2:Region |   
[ModifyIdentityIdFormat](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIdentityIdFormat.html) | Grants permission to modify the ID format of a resource for a specific principal in your account | Write |  |  ec2:Region |   
[ModifyImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html) | Grants permission to modify an attribute of an Amazon Machine Image (AMI) | Write |  image* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[ModifyInstanceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.html) | Grants permission to modify an attribute of an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
volume |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[ModifyInstanceCapacityReservationAttributes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCapacityReservationAttributes.html) | Grants permission to modify the Capacity Reservation settings for a stopped instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
capacity-reservation |  aws:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyInstanceCpuOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCpuOptions.html) | Grants permission to modify the CPU options on an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyInstanceCreditSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html) | Grants permission to modify the credit option for CPU usage on an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyInstanceEventStartTime](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceEventStartTime.html) | Grants permission to modify the start time for a scheduled EC2 instance event | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyInstanceEventWindow](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceEventWindow.html) | Grants permission to modify the specified event window | Write |  instance-event-window* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyInstanceMaintenanceOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMaintenanceOptions.html) | Grants permission to modify the recovery behaviour for an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyInstanceMetadataDefaults](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataDefaults.html) | Grants permission to modify the default instance metadata service (IMDS) settings for your account in the specified Region | Write |  |  ec2:Attribute/${AttributeName} ec2:Region |   
[ModifyInstanceMetadataOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html) | Grants permission to modify the metadata options for an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyInstanceNetworkPerformanceOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceNetworkPerformanceOptions.html) | Grants permission to modify the network performance options for an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyInstancePlacement](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstancePlacement.html) | Grants permission to modify the placement attributes for an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
dedicated-host |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyIpam](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpam.html) | Grants permission to modify the configurations of an Amazon VPC IP Address Manager (IPAM) | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyIpamPool](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamPool.html) | Grants permission to modify the configurations of an Amazon VPC IP Address Manager (IPAM) pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyIpamResourceCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamResourceCidr.html) | Grants permission to modify the configurations of an Amazon VPC IP Address Manager (IPAM) resource CIDR | Write |  ipam-scope* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyIpamResourceDiscovery](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamResourceDiscovery.html) | Grants permission to modify a resource discovery | Write |  ipam-resource-discovery* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyIpamScope](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamScope.html) | Grants permission to modify the configurations of an Amazon VPC IP Address Manager (IPAM) scope | Write |  ipam-scope* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyLaunchTemplate.html) | Grants permission to modify a launch template | Write |  launch-template* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyLocalGatewayRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyLocalGatewayRoute.html) | Grants permission to modify a local gateway route | Write |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
local-gateway-virtual-interface-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AuthorizedUser ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Permission ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
prefix-list |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyManagedPrefixList](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyManagedPrefixList.html) | Grants permission to modify a managed prefix list | Write |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html) | Grants permission to modify an attribute of a network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
instance |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[ModifyPrivateDnsNameOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyPrivateDnsNameOptions.html) | Grants permission to modify the options for instance hostnames for the specified instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:NewInstanceProfile ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ModifyReservedInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyReservedInstances.html) | Grants permission to modify attributes of one or more Reserved Instances | Write |  reserved-instances* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:InstanceType ec2:ReservedInstancesOfferingType ec2:ResourceTag/${TagKey} ec2:Tenancy |   
|  ec2:Region |   
[ModifySecurityGroupRules](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySecurityGroupRules.html) | Grants permission to modify the rules of a security group | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
security-group-rule* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
prefix-list |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifySnapshotAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotAttribute.html) | Grants permission to add or remove permission settings for a snapshot | Permissions management |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Add/group ec2:Add/userId ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:Owner ec2:ParentVolume ec2:Remove/group ec2:Remove/userId ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[ModifySnapshotTier](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySnapshotTier.html) | Grants permission to archive Amazon EBS snapshots | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest.html) | Grants permission to modify a Spot Fleet request | Write |  spot-fleet-request* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
launch-template |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ModifySubnetAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySubnetAttribute.html) | Grants permission to modify an attribute of a subnet | Write |  subnet* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ModifyTrafficMirrorFilterNetworkServices](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterNetworkServices.html) | Grants permission to allow or restrict mirroring network services | Write |  traffic-mirror-filter* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyTrafficMirrorFilterRule](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterRule.html) | Grants permission to modify a traffic mirror rule | Write |  traffic-mirror-filter* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter-rule* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyTrafficMirrorSession](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorSession.html) | Grants permission to modify a traffic mirror session | Write |  traffic-mirror-session* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
traffic-mirror-filter |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
traffic-mirror-target |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyTransitGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGateway.html) | Grants permission to modify a transit gateway | Write |  transit-gateway* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:transitGatewayId |   
transit-gateway-route-table |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[ModifyTransitGatewayPrefixListReference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayPrefixListReference.html) | Grants permission to modify a transit gateway prefix list reference | Write |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[ModifyTransitGatewayVpcAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayVpcAttachment.html) | Grants permission to modify a VPC attachment on a transit gateway | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ModifyVerifiedAccessEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessEndpoint.html) | Grants permission to modify the configuration of a Verified Access endpoint | Write |  verified-access-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
verified-access-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVerifiedAccessEndpointPolicy](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessEndpointPolicy.html) | Grants permission to modify the specified Verified Access endpoint policy | Write |  verified-access-endpoint* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVerifiedAccessGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessGroup.html) | Grants permission to modify the specified Verified Access Group configuration | Write |  verified-access-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
verified-access-instance |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVerifiedAccessGroupPolicy](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessGroupPolicy.html) | Grants permission to modify the specified Verified Access group policy | Write |  verified-access-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVerifiedAccessInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessInstance.html) | Grants permission to modify the configuration of the specified Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVerifiedAccessInstanceLoggingConfiguration](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessInstanceLoggingConfiguration.html) | Grants permission to modify the logging configuration for the specified Verified Access instance | Write |  verified-access-instance* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVerifiedAccessTrustProvider](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessTrustProvider.html) | Grants permission to modify the configuration of the specified Verified Access trust provider | Write |  verified-access-trust-provider* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolume.html) | Grants permission to modify the parameters of an EBS volume | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[ModifyVolumeAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolumeAttribute.html) | Grants permission to modify an attribute of a volume | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
[ModifyVpcAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcAttribute.html) | Grants permission to modify an attribute of a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[ModifyVpcBlockPublicAccessExclusion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcBlockPublicAccessExclusion.html) | Grants permission to modify an exclusion list for blocked public access on a VPC | Write |  vpc-block-public-access-exclusion* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVpcBlockPublicAccessOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcBlockPublicAccessOptions.html) | Grants permission to modify options for blocked public access on a VPC | Write |  |  ec2:Region |   
[ModifyVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html) | Grants permission to modify an attribute of a VPC endpoint | Write |  vpc-endpoint* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
route-table |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ModifyVpcEndpointConnectionNotification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointConnectionNotification.html) | Grants permission to modify a connection notification for a VPC endpoint or VPC endpoint service | Write |  vpc-endpoint |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
vpc-endpoint-service |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[ModifyVpcEndpointServiceConfiguration](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServiceConfiguration.html) | Grants permission to modify the attributes of a VPC endpoint service configuration | Write |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:VpceServicePrivateDnsName ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[ModifyVpcEndpointServicePayerResponsibility](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServicePayerResponsibility.html) | Grants permission to modify the payer responsibility for a VPC endpoint service | Write |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[ModifyVpcEndpointServicePermissions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServicePermissions.html) | Grants permission to modify the permissions for a VPC endpoint service | Permissions management |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[ModifyVpcPeeringConnectionOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcPeeringConnectionOptions.html) | Grants permission to modify the VPC peering connection options on one side of a VPC peering connection | Write |  vpc-peering-connection* |  aws:ResourceTag/${TagKey} ec2:AccepterVpc ec2:Attribute ec2:Attribute/${AttributeName} ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID |   
|  ec2:Region |   
[ModifyVpcTenancy](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcTenancy.html) | Grants permission to modify the instance tenancy attribute of a VPC | Write |  vpc* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID |   
|  ec2:Region |   
[ModifyVpnConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnConnection.html) | Grants permission to modify the target gateway of a Site-to-Site VPN connection | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AuthenticationType ec2:DPDTimeoutSeconds ec2:GatewayType ec2:IKEVersions ec2:InsideTunnelCidr ec2:InsideTunnelIpv6Cidr ec2:Phase1DHGroup ec2:Phase1EncryptionAlgorithms ec2:Phase1IntegrityAlgorithms ec2:Phase1LifetimeSeconds ec2:Phase2DHGroup ec2:Phase2EncryptionAlgorithms ec2:Phase2IntegrityAlgorithms ec2:Phase2LifetimeSeconds ec2:RekeyFuzzPercentage ec2:RekeyMarginTimeSeconds ec2:ReplayWindowSizePackets ec2:ResourceTag/${TagKey} ec2:RoutingType |   
|  ec2:Region |   
[ModifyVpnConnectionOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnConnectionOptions.html) | Grants permission to modify the connection options for your Site-to-Site VPN connection | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVpnTunnelCertificate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelCertificate.html) | Grants permission to modify the certificate for a Site-to-Site VPN connection | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ModifyVpnTunnelOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.html) | Grants permission to modify the options for a Site-to-Site VPN connection | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:AuthenticationType ec2:DPDTimeoutSeconds ec2:GatewayType ec2:IKEVersions ec2:InsideTunnelCidr ec2:InsideTunnelIpv6Cidr ec2:Phase1DHGroup ec2:Phase1EncryptionAlgorithms ec2:Phase1IntegrityAlgorithms ec2:Phase1LifetimeSeconds ec2:Phase2DHGroup ec2:Phase2EncryptionAlgorithms ec2:Phase2IntegrityAlgorithms ec2:Phase2LifetimeSeconds ec2:RekeyFuzzPercentage ec2:RekeyMarginTimeSeconds ec2:ReplayWindowSizePackets ec2:ResourceTag/${TagKey} ec2:RoutingType |   
|  ec2:Region |   
[MonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MonitorInstances.html) | Grants permission to enable detailed monitoring for a running instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[MoveAddressToVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveAddressToVpc.html) | Grants permission to move an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform | Write |  |  ec2:Region |   
[MoveByoipCidrToIpam](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveByoipCidrToIpam.html) | Grants permission to move a BYOIP IPv4 CIDR to Amazon VPC IP Address Manager (IPAM) from a public IPv4 pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[MoveCapacityReservationInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveCapacityReservationInstances.html) | Grants permission to move available capacity from a source Capacity Reservation to a destination Capacity Reservation | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[PauseVolumeIO](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#ebs-actions-reference) [permission only] | Grants permission to temporarily pause I/O operations for a target Amazon EBS volume | Write |  volume* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:Encrypted ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
instance |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ProvisionByoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionByoipCidr.html) | Grants permission to provision an address range for use in AWS through bring your own IP addresses (BYOIP), and to create a corresponding address pool | Write |  |  ec2:Region |   
[ProvisionIpamByoasn](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionIpamByoasn.html) | Grants permission to provision an Autonomous System Number (ASN) for use in an Amazon Web Services account | Write |  ipam* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ProvisionIpamPoolCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionIpamPoolCidr.html) | Grants permission to provision a CIDR to an Amazon VPC IP Address Manager (IPAM) pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipam-external-resource-verification-token |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ProvisionPublicIpv4PoolCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionPublicIpv4PoolCidr.html) | Grants permission to provision a CIDR to a public IPv4 pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipv4pool-ec2* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[PurchaseCapacityBlock](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseCapacityBlock.html) | Grants permission to purchase a Capacity Block offering | Write |  capacity-reservation* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:CapacityReservationFleet |  ec2:CreateTags   
|  ec2:Region |   
[PurchaseCapacityBlockExtension](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseCapacityBlockExtension.html) | Grants permission to purchase a Capacity Block extension | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:CapacityReservationFleet |   
|  ec2:Region |   
[PurchaseHostReservation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseHostReservation.html) | Grants permission to purchase a reservation with configurations that match those of a Dedicated Host | Write |  dedicated-host* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
|  ec2:Region |   
[PurchaseReservedInstancesOffering](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseReservedInstancesOffering.html) | Grants permission to purchase a Reserved Instance offering | Write |  |  ec2:Region |   
[PurchaseScheduledInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseScheduledInstances.html) | Grants permission to purchase one or more Scheduled Instances with a specified schedule | Write |  |  ec2:Region |   
[PutResourcePolicy](https://docs.aws.amazon.com/vpc/latest/ipam/share-pool-ipam.html) [permission only] | Grants permission to attach an IAM policy that enables cross-account sharing to a resource | Write |  ipam-pool |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
verified-access-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[RebootInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html) | Grants permission to request a reboot of one or more instances | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[RegisterImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html) | Grants permission to register an Amazon Machine Image (AMI) | Write |  image* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:ImageID ec2:Owner |  ec2:CreateTags   
snapshot |  aws:ResourceTag/${TagKey} ec2:OutpostArn ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:SourceOutpostArn ec2:VolumeSize |   
|  ec2:Region |   
[RegisterInstanceEventNotificationAttributes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterInstanceEventNotificationAttributes.html) | Grants permission to add tags to the set of tags to include in notifications about scheduled events for your instances | Write |  |  ec2:Region |   
[RegisterTransitGatewayMulticastGroupMembers](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterTransitGatewayMulticastGroupMembers.html) | Grants permission to register one or more network interfaces as a member of a group IP address in a transit gateway multicast domain | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[RegisterTransitGatewayMulticastGroupSources](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterTransitGatewayMulticastGroupSources.html) | Grants permission to register one or more network interfaces as a source of a group IP address in a transit gateway multicast domain | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[RejectCapacityReservationBillingOwnership](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectCapacityReservationBillingOwnership.html) | Grants permission to reject a request to assign billing of the available capacity of a shared Capacity Reservation to your account | Write |  capacity-reservation* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:OutpostArn ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy |   
|  ec2:Region |   
[RejectTransitGatewayMulticastDomainAssociations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectTransitGatewayMulticastDomainAssociations.html) | Grants permission to reject requests to associate cross-account subnets with a transit gateway multicast domain | Write |  transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
transit-gateway-multicast-domain |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[RejectTransitGatewayPeeringAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectTransitGatewayPeeringAttachment.html) | Grants permission to reject a transit gateway peering attachment request | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[RejectTransitGatewayVpcAttachment](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectTransitGatewayVpcAttachment.html) | Grants permission to reject a request to attach a VPC to a transit gateway | Write |  transit-gateway-attachment* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[RejectVpcEndpointConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcEndpointConnections.html) | Grants permission to reject one or more VPC endpoint connection requests to a VPC endpoint service | Write |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[RejectVpcPeeringConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RejectVpcPeeringConnection.html) | Grants permission to reject a VPC peering connection request | Write |  vpc-peering-connection* |  aws:ResourceTag/${TagKey} ec2:AccepterVpc ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID |   
|  ec2:Region |   
[ReleaseAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseAddress.html) | Grants permission to release an Elastic IP address | Write |  elastic-ip |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ReleaseHosts](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseHosts.html) | Grants permission to release one or more On-Demand Dedicated Hosts | Write |  dedicated-host* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ReleaseIpamPoolAllocation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseIpamPoolAllocation.html) | Grants permission to release an allocation within an Amazon VPC IP Address Manager (IPAM) pool | Write |  ipam-pool* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ReplaceIamInstanceProfileAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceIamInstanceProfileAssociation.html) | Grants permission to replace an IAM instance profile for an instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:NewInstanceProfile ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |  iam:PassRole   
|  ec2:Region |   
[ReplaceImageCriteriaInAllowedImagesSettings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceImageCriteriaInAllowedImagesSettings.html) | Grants permission to replace image criteria in allowed images settings | Write |  |  ec2:Region |   
[ReplaceNetworkAclAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclAssociation.html) | Grants permission to change which network ACL a subnet is associated with | Write |  network-acl* |  aws:ResourceTag/${TagKey} ec2:NetworkAclID ec2:ResourceTag/${TagKey} ec2:Vpc |   
subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ReplaceNetworkAclEntry](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclEntry.html) | Grants permission to replace an entry (rule) in a network ACL | Write |  network-acl* |  aws:ResourceTag/${TagKey} ec2:NetworkAclID ec2:ResourceTag/${TagKey} ec2:Vpc |   
|  ec2:Region |   
[ReplaceRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRoute.html) | Grants permission to replace a route within a route table in a VPC | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
|  ec2:Region |   
[ReplaceRouteTableAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRouteTableAssociation.html) | Grants permission to change the route table that is associated with a subnet | Write |  route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc |   
internet-gateway |  aws:ResourceTag/${TagKey} ec2:InternetGatewayID ec2:ResourceTag/${TagKey} |   
ipv4pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
ipv6pool-ec2 |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
vpn-gateway |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ReplaceTransitGatewayRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceTransitGatewayRoute.html) | Grants permission to replace a route in a transit gateway route table | Write |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
transit-gateway-attachment |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId |   
|  ec2:Region |   
[ReplaceVpnTunnel](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceVpnTunnel.html) | Grants permission to replace a VPN tunnel | Write |  vpn-connection* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ReportInstanceStatus](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReportInstanceStatus.html) | Grants permission to submit feedback about the status of an instance | Write |  instance* |  ec2:InstanceBandwidthWeighting ec2:InstanceID |   
|  ec2:Region |   
[RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet.html) | Grants permission to create a Spot Fleet request | Write |  spot-fleet-request* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
image |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
key-pair |  aws:ResourceTag/${TagKey} ec2:KeyPairName ec2:KeyPairType ec2:ResourceTag/${TagKey} |   
launch-template |  aws:ResourceTag/${TagKey} ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
snapshot |  aws:ResourceTag/${TagKey} ec2:OutpostArn ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:SourceOutpostArn ec2:VolumeSize |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[RequestSpotInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html) | Grants permission to create a Spot Instance request | Write |  spot-instances-request* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags  iam:PassRole   
image |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
key-pair |  aws:ResourceTag/${TagKey} ec2:KeyPairName ec2:KeyPairType ec2:ResourceTag/${TagKey} |   
network-interface |  aws:ResourceTag/${TagKey} ec2:AuthorizedUser ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Permission ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
placement-group |  aws:ResourceTag/${TagKey} ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
security-group |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
snapshot |  aws:ResourceTag/${TagKey} ec2:OutpostArn ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:SourceOutpostArn ec2:VolumeSize |   
subnet |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
|  ec2:Region |   
[ResetAddressAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetAddressAttribute.html) | Grants permission to reset the attribute of the specified IP address | Write |  elastic-ip* |  aws:ResourceTag/${TagKey} ec2:AllocationId ec2:Attribute ec2:Attribute/${AttributeName} ec2:Domain ec2:PublicIpAddress ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ResetEbsDefaultKmsKeyId](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetEbsDefaultKmsKeyId.html) | Grants permission to reset the default customer master key (CMK) for EBS encryption for your account to use the AWS-managed CMK for EBS | Write |  |  ec2:Region |   
[ResetFpgaImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetFpgaImageAttribute.html) | Grants permission to reset an attribute of an Amazon FPGA Image (AFI) to its default value | Write |  fpga-image* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[ResetImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetImageAttribute.html) | Grants permission to reset an attribute of an Amazon Machine Image (AMI) to its default value | Write |  image* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[ResetInstanceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetInstanceAttribute.html) | Grants permission to reset an attribute of an instance to its default value | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[ResetNetworkInterfaceAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetNetworkInterfaceAttribute.html) | Grants permission to reset an attribute of a network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[ResetSnapshotAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResetSnapshotAttribute.html) | Grants permission to reset permission settings for a snapshot | Permissions management |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Attribute ec2:Attribute/${AttributeName} ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[RestoreAddressToClassic](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreAddressToClassic.html) | Grants permission to restore an Elastic IP address that was previously moved to the EC2-VPC platform back to the EC2-Classic platform | Write |  |  ec2:Region |   
[RestoreImageFromRecycleBin](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreImageFromRecycleBin.html) | Grants permission to restore an Amazon Machine Image (AMI) from the Recycle Bin | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |   
|  ec2:Region |   
[RestoreManagedPrefixListVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreManagedPrefixListVersion.html) | Grants permission to restore the entries from a previous version of a managed prefix list to a new version of the prefix list | Write |  prefix-list* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[RestoreSnapshotFromRecycleBin](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreSnapshotFromRecycleBin.html) | Grants permission to restore an Amazon EBS snapshot from the Recycle Bin | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[RestoreSnapshotTier](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreSnapshotTier.html) | Grants permission to restore an archived Amazon EBS snapshot for use temporarily or permanently, or modify the restore period or restore type for a snapshot that was previously temporarily restored | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[RevokeClientVpnIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeClientVpnIngress.html) | Grants permission to remove an inbound authorization rule from a Client VPN endpoint | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html) | Grants permission to remove one or more outbound rules from a VPC security group | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[RevokeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html) | Grants permission to remove one or more inbound rules from a security group | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) | Grants permission to launch one or more instances | Write |  image* |  aws:ResourceTag/${TagKey} ec2:ImageID ec2:ImageType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Owner ec2:Public ec2:ResourceTag/${TagKey} ec2:RootDeviceType |  ec2:CreateTags  iam:PassRole  ssm:GetParameters   
instance* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:RootDeviceType ec2:Tenancy |   
network-interface* |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AssociatePublicIpAddress ec2:AuthorizedService ec2:AvailabilityZone ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Subnet ec2:Vpc |   
security-group* |  aws:ResourceTag/${TagKey} ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
subnet* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc |   
capacity-reservation |  aws:ResourceTag/${TagKey} ec2:IsLaunchTemplateResource ec2:LaunchTemplate |   
elastic-gpu |  aws:ResourceTag/${TagKey} ec2:ElasticGpuType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ResourceTag/${TagKey} |   
elastic-inference |  |   
group |  |   
key-pair |  aws:ResourceTag/${TagKey} ec2:IsLaunchTemplateResource ec2:KeyPairName ec2:KeyPairType ec2:LaunchTemplate ec2:ResourceTag/${TagKey} |   
launch-template |  aws:ResourceTag/${TagKey} ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:ResourceTag/${TagKey} |   
license-configuration |  |   
placement-group |  aws:ResourceTag/${TagKey} ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:ResourceTag/${TagKey} |   
snapshot |  aws:ResourceTag/${TagKey} ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotID ec2:SnapshotTime ec2:VolumeSize |   
volume |  aws:RequestTag/${TagKey} aws:TagKeys ec2:AvailabilityZone ec2:Encrypted ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType |   
|  ec2:Region |   
**SCENARIO:** EC2-Classic-EBS  |  |  image* instance* security-group* volume* key-pair placement-group snapshot |  |   
**SCENARIO:** EC2-Classic-InstanceStore  |  |  image* instance* security-group* key-pair placement-group snapshot |  |   
**SCENARIO:** EC2-VPC-EBS  |  |  image* instance* network-interface* security-group* volume* key-pair placement-group snapshot |  |   
**SCENARIO:** EC2-VPC-EBS-Subnet  |  |  image* instance* network-interface* security-group* subnet* volume* key-pair placement-group snapshot |  |   
**SCENARIO:** EC2-VPC-InstanceStore  |  |  image* instance* network-interface* security-group* key-pair placement-group snapshot |  |   
**SCENARIO:** EC2-VPC-InstanceStore-Subnet  |  |  image* instance* network-interface* security-group* subnet* key-pair placement-group snapshot |  |   
[RunScheduledInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunScheduledInstances.html) | Grants permission to launch one or more Scheduled Instances | Write |  |  ec2:Region |   
[SearchLocalGatewayRoutes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchLocalGatewayRoutes.html) | Grants permission to search for routes in a local gateway route table | List |  local-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[SearchTransitGatewayMulticastGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayMulticastGroups.html) | Grants permission to search for groups, sources, and members in a transit gateway multicast domain | List |  transit-gateway-multicast-domain* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId |   
|  ec2:Region |   
[SearchTransitGatewayRoutes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SearchTransitGatewayRoutes.html) | Grants permission to search for routes in a transit gateway route table | List |  transit-gateway-route-table* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId |   
|  ec2:Region |   
[SendDiagnosticInterrupt](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SendDiagnosticInterrupt.html) | Grants permission to send a diagnostic interrupt to an Amazon EC2 instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[SendSpotInstanceInterruptions](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#send-spot-instance-interruptions) [permission only] | Grants permission to interrupt a Spot Instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[StartDeclarativePoliciesReport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.html) | Grants permission to start a declarative policies report | Read |  |  ec2:Region |   
[StartInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html) | Grants permission to start a stopped instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
license-configuration |  |   
|  ec2:Region |   
[StartNetworkInsightsAccessScopeAnalysis](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartNetworkInsightsAccessScopeAnalysis.html) | Grants permission to start a Network Access Scope analysis | Write |  network-insights-access-scope* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |  ec2:CreateTags   
network-insights-access-scope-analysis* |  aws:RequestTag/${TagKey} aws:TagKeys |   
|  ec2:Region |   
[StartNetworkInsightsAnalysis](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartNetworkInsightsAnalysis.html) | Grants permission to start analyzing a specified path | Write |  network-insights-analysis* |  aws:RequestTag/${TagKey} aws:TagKeys |  ec2:CreateTags   
network-insights-path* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[StartVpcEndpointServicePrivateDnsVerification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartVpcEndpointServicePrivateDnsVerification.html) | Grants permission to start the private DNS verification process for a VPC endpoint service | Write |  vpc-endpoint-service* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:vpceMultiRegion ec2:vpceSupportedRegion |   
|  ec2:Region |   
[StopInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) | Grants permission to stop an Amazon EBS-backed instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[TerminateClientVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateClientVpnConnections.html) | Grants permission to terminate active Client VPN endpoint connections | Write |  client-vpn-endpoint* |  aws:ResourceTag/${TagKey} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn |   
|  ec2:Region |   
[TerminateInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html) | Grants permission to shut down one or more instances | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[UnassignIpv6Addresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignIpv6Addresses.html) | Grants permission to unassign one or more IPv6 addresses from a network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[UnassignPrivateIpAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html) | Grants permission to unassign one or more secondary private IP addresses from a network interface | Write |  network-interface* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc |   
|  ec2:Region |   
[UnassignPrivateNatGatewayAddress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateNatGatewayAddress.html) | Grants permission to unassign secondary private IPv4 addresses from a private NAT gateway | Write |  natgateway* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} |   
|  ec2:Region |   
[UnlockSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnlockSnapshot.html) | Grants permission to unlock a snapshot that is locked in governance mode or in compliance mode while still in the cooling-off period | Write |  snapshot* |  aws:ResourceTag/${TagKey} ec2:Encrypted ec2:Owner ec2:ParentVolume ec2:ResourceTag/${TagKey} ec2:SnapshotCoolOffPeriod ec2:SnapshotID ec2:SnapshotLockDuration ec2:SnapshotTime ec2:VolumeSize |   
|  ec2:Region |   
[UnmonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html) | Grants permission to disable detailed monitoring for a running instance | Write |  instance* |  aws:ResourceTag/${TagKey} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:PlacementGroup ec2:ProductCode ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy |   
|  ec2:Region |   
[UpdateSecurityGroupRuleDescriptionsEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html) | Grants permission to update descriptions for one or more outbound rules in a VPC security group | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[UpdateSecurityGroupRuleDescriptionsIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html) | Grants permission to update descriptions for one or more inbound rules in a security group | Write |  security-group* |  aws:ResourceTag/${TagKey} ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc |   
|  ec2:Region |   
[WithdrawByoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_WithdrawByoipCidr.html) | Grants permission to stop advertising an address range that was provisioned for use in AWS through bring your own IP addresses (BYOIP) | Write |  |  ec2:Region |   
  
## Resource types defined by Amazon EC2

The following resource types are defined by this service and can be used in
the `Resource` element of IAM permission policy statements. Each action in the
Actions table identifies the resource types that can be specified with that
action. A resource type can also define which condition keys you can include
in a policy. These keys are displayed in the last column of the table. For
details about the columns in the following table, see [Resource types
table](reference_policies_actions-resources-contextkeys.html#resources_table).

Resource types | ARN | Condition keys  
---|---|---  
[elastic-ip](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) |  `arn:${Partition}:ec2:${Region}:${Account}:elastic-ip/${AllocationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AllocationId ec2:Attribute ec2:Attribute/${AttributeName} ec2:Domain ec2:PublicIpAddress ec2:Region ec2:ResourceTag/${TagKey}  
[capacity-reservation-fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:capacity-reservation-fleet/${CapacityReservationFleetId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[capacity-reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) |  `arn:${Partition}:ec2:${Region}:${Account}:capacity-reservation/${CapacityReservationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CapacityReservationFleet ec2:CreateDate ec2:DestinationCapacityReservationId ec2:EbsOptimized ec2:EndDate ec2:EndDateType ec2:InstanceCount ec2:InstanceMatchCriteria ec2:InstancePlatform ec2:InstanceType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:OutpostArn ec2:PlacementGroup ec2:Region ec2:ResourceTag/${TagKey} ec2:SourceCapacityReservationId ec2:Tenancy  
[carrier-gateway](https://docs.aws.amazon.com/vpc/latest/userguide/Carrier_Gateway.html) |  `arn:${Partition}:ec2:${Region}:${Account}:carrier-gateway/${CarrierGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:Vpc  
[certificate](https://docs.aws.amazon.com/acm/latest/userguide/authen-overview.html#acm-resources-operations) |  `arn:${Partition}:acm:${Region}:${Account}:certificate/${CertificateId}` |   
[client-vpn-endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html) |  `arn:${Partition}:ec2:${Region}:${Account}:client-vpn-endpoint/${ClientVpnEndpointId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:ClientRootCertificateChainArn ec2:CloudwatchLogGroupArn ec2:CloudwatchLogStreamArn ec2:DirectoryArn ec2:Region ec2:ResourceTag/${TagKey} ec2:SamlProviderArn ec2:ServerCertificateArn  
[customer-gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) |  `arn:${Partition}:ec2:${Region}:${Account}:customer-gateway/${CustomerGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[declarative-policies-report](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:declarative-policies-report/${DeclarativePoliciesReportId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[dedicated-host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html) |  `arn:${Partition}:ec2:${Region}:${Account}:dedicated-host/${DedicatedHostId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AutoPlacement ec2:AvailabilityZone ec2:HostRecovery ec2:InstanceType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Quantity ec2:Region ec2:ResourceTag/${TagKey}  
[dhcp-options](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) |  `arn:${Partition}:ec2:${Region}:${Account}:dhcp-options/${DhcpOptionsId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:DhcpOptionsID ec2:Region ec2:ResourceTag/${TagKey}  
[egress-only-internet-gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html) |  `arn:${Partition}:ec2:${Region}:${Account}:egress-only-internet-gateway/${EgressOnlyInternetGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[elastic-gpu](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-gpus.html) |  `arn:${Partition}:ec2:${Region}:${Account}:elastic-gpu/${ElasticGpuId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:ElasticGpuType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Region ec2:ResourceTag/${TagKey}  
[elastic-inference](https://docs.aws.amazon.com/elastic-inference/latest/developerguide/what-is-ei.html) |  `arn:${Partition}:elastic-inference:${Region}:${Account}:elastic-inference-accelerator/${AcceleratorId}` |   
[export-image-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#export-vm-image) |  `arn:${Partition}:ec2:${Region}:${Account}:export-image-task/${ExportImageTaskId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[export-instance-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html) |  `arn:${Partition}:ec2:${Region}:${Account}:export-instance-task/${ExportTaskId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) |  `arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[fpga-image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:fpga-image/${FpgaImageId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Owner ec2:Public ec2:Region ec2:ResourceTag/${TagKey}  
[host-reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:host-reservation/${HostReservationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) |  `arn:${Partition}:ec2:${Region}::image/${ImageId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:ImageID ec2:ImageType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Owner ec2:Public ec2:Region ec2:ResourceTag/${TagKey} ec2:RootDeviceType  
[import-image-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#import-vm-image) |  `arn:${Partition}:ec2:${Region}:${Account}:import-image-task/${ImportImageTaskId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[import-snapshot-task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html) |  `arn:${Partition}:ec2:${Region}:${Account}:import-snapshot-task/${ImportSnapshotTaskId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[instance-connect-endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:instance-connect-endpoint/${InstanceConnectEndpointId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey} ec2:SubnetID  
[instance-event-window](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:instance-event-window/${InstanceEventWindowId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html) |  `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:CpuOptionsAmdSevSnp ec2:EbsOptimized ec2:InstanceAutoRecovery ec2:InstanceBandwidthWeighting ec2:InstanceID ec2:InstanceMarketType ec2:InstanceMetadataTags ec2:InstanceProfile ec2:InstanceType ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:MetadataHttpEndpoint ec2:MetadataHttpPutResponseHopLimit ec2:MetadataHttpTokens ec2:NewInstanceProfile ec2:PlacementGroup ec2:ProductCode ec2:Region ec2:ResourceTag/${TagKey} ec2:RootDeviceType ec2:Tenancy  
[internet-gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) |  `arn:${Partition}:ec2:${Region}:${Account}:internet-gateway/${InternetGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:InternetGatewayID ec2:Region ec2:ResourceTag/${TagKey}  
[ipam-external-resource-verification-token](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2::${Account}:ipam-external-resource-verification-token/${IpamExternalResourceVerificationTokenId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[ipam](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2::${Account}:ipam/${IpamId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[ipam-pool](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2::${Account}:ipam-pool/${IpamPoolId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[ipam-resource-discovery-association](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2::${Account}:ipam-resource-discovery-association/${IpamResourceDiscoveryAssociationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[ipam-resource-discovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2::${Account}:ipam-resource-discovery/${IpamResourceDiscoveryId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[ipam-scope](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2::${Account}:ipam-scope/${IpamScopeId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[coip-pool](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:coip-pool/${Ipv4PoolCoipId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[ipv4pool-ec2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ip-addressing-eips) |  `arn:${Partition}:ec2:${Region}:${Account}:ipv4pool-ec2/${Ipv4PoolEc2Id}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[ipv6pool-ec2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ipv6-addressing) |  `arn:${Partition}:ec2:${Region}:${Account}:ipv6pool-ec2/${Ipv6PoolEc2Id}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[key-pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) |  `arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyPairName}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:IsLaunchTemplateResource ec2:KeyPairName ec2:KeyPairType ec2:LaunchTemplate ec2:Region ec2:ResourceTag/${TagKey}  
[launch-template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) |  `arn:${Partition}:ec2:${Region}:${Account}:launch-template/${LaunchTemplateId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:Region ec2:ResourceTag/${TagKey}  
[license-configuration](https://docs.aws.amazon.com/license-manager/latest/userguide/create-license-configuration.html) |  `arn:${Partition}:license-manager:${Region}:${Account}:license-configuration:${LicenseConfigurationId}` |   
[local-gateway](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#lgw) |  `arn:${Partition}:ec2:${Region}:${Account}:local-gateway/${LocalGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[local-gateway-route-table-virtual-interface-group-association](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) |  `arn:${Partition}:ec2:${Region}:${Account}:local-gateway-route-table-virtual-interface-group-association/${LocalGatewayRouteTableVirtualInterfaceGroupAssociationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[local-gateway-route-table-vpc-association](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#vpc-associations) |  `arn:${Partition}:ec2:${Region}:${Account}:local-gateway-route-table-vpc-association/${LocalGatewayRouteTableVpcAssociationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[local-gateway-route-table](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html#route-tables) |  `arn:${Partition}:ec2:${Region}:${Account}:local-gateway-route-table/${LocalGatewayRoutetableId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[local-gateway-virtual-interface-group](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) |  `arn:${Partition}:ec2:${Region}:${Account}:local-gateway-virtual-interface-group/${LocalGatewayVirtualInterfaceGroupId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[local-gateway-virtual-interface](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html) |  `arn:${Partition}:ec2:${Region}:${Account}:local-gateway-virtual-interface/${LocalGatewayVirtualInterfaceId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[natgateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |  `arn:${Partition}:ec2:${Region}:${Account}:natgateway/${NatGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[network-acl](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |  `arn:${Partition}:ec2:${Region}:${Account}:network-acl/${NaclId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:NetworkAclID ec2:Region ec2:ResourceTag/${TagKey} ec2:Vpc  
[network-insights-access-scope-analysis](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:network-insights-access-scope-analysis/${NetworkInsightsAccessScopeAnalysisId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[network-insights-access-scope](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:network-insights-access-scope/${NetworkInsightsAccessScopeId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[network-insights-analysis](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:network-insights-analysis/${NetworkInsightsAnalysisId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[network-insights-path](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:network-insights-path/${NetworkInsightsPathId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[network-interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) |  `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AssociatePublicIpAddress ec2:Attribute ec2:Attribute/${AttributeName} ec2:AuthorizedService ec2:AuthorizedUser ec2:AvailabilityZone ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:NetworkInterfaceID ec2:Permission ec2:Region ec2:ResourceTag/${TagKey} ec2:Subnet ec2:Vpc  
[placement-group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) |  `arn:${Partition}:ec2:${Region}:${Account}:placement-group/${PlacementGroupName}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:PlacementGroupName ec2:PlacementGroupStrategy ec2:Region ec2:ResourceTag/${TagKey}  
[prefix-list](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) |  `arn:${Partition}:ec2:${Region}:${Account}:prefix-list/${PrefixListId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[replace-root-volume-task](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replace-root.html) |  `arn:${Partition}:ec2:${Region}:${Account}:replace-root-volume-task/${ReplaceRootVolumeTaskId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[reserved-instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) |  `arn:${Partition}:ec2:${Region}:${Account}:reserved-instances/${ReservationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:InstanceType ec2:Region ec2:ReservedInstancesOfferingType ec2:ResourceTag/${TagKey} ec2:Tenancy  
[group](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) |  `arn:${Partition}:resource-groups:${Region}:${Account}:group/${GroupName}` |   
[role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) |  `arn:${Partition}:iam::${Account}:role/${RoleNameWithPath}` |   
[route-table](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) |  `arn:${Partition}:ec2:${Region}:${Account}:route-table/${RouteTableId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey} ec2:RouteTableID ec2:Vpc  
[security-group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) |  `arn:${Partition}:ec2:${Region}:${Account}:security-group/${SecurityGroupId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Region ec2:ResourceTag/${TagKey} ec2:SecurityGroupID ec2:Vpc  
[security-group-rule](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:security-group-rule/${SecurityGroupRuleId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) |  `arn:${Partition}:ec2:${Region}::snapshot/${SnapshotId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Add/group ec2:Add/userId ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:Encrypted ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Location ec2:OutpostArn ec2:Owner ec2:ParentVolume ec2:Region ec2:Remove/group ec2:Remove/userId ec2:ResourceTag/${TagKey} ec2:SnapshotCoolOffPeriod ec2:SnapshotID ec2:SnapshotLockDuration ec2:SnapshotTime ec2:SourceAvailabilityZone ec2:SourceOutpostArn ec2:VolumeSize  
[spot-fleet-request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[spot-instances-request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) |  `arn:${Partition}:ec2:${Region}:${Account}:spot-instances-request/${SpotInstanceRequestId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[subnet-cidr-reservation](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html) |  `arn:${Partition}:ec2:${Region}:${Account}:subnet-cidr-reservation/${SubnetCidrReservationId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[subnet](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) |  `arn:${Partition}:ec2:${Region}:${Account}:subnet/${SubnetId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:IsLaunchTemplateResource ec2:LaunchTemplate ec2:Region ec2:ResourceTag/${TagKey} ec2:SubnetID ec2:Vpc  
[traffic-mirror-filter](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html) |  `arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-filter/${TrafficMirrorFilterId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[traffic-mirror-filter-rule](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html) |  `arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-filter-rule/${TrafficMirrorFilterRuleId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[traffic-mirror-session](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html) |  `arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-session/${TrafficMirrorSessionId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey}  
[traffic-mirror-target](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-target.html) |  `arn:${Partition}:ec2:${Region}:${Account}:traffic-mirror-target/${TrafficMirrorTargetId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[transit-gateway-attachment](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-attachment/${TransitGatewayAttachmentId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayAttachmentId  
[transit-gateway-connect-peer](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-connect-peer/${TransitGatewayConnectPeerId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayConnectPeerId  
[transit-gateway](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway/${TransitGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayId  
[transit-gateway-multicast-domain](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-multicast-domain/${TransitGatewayMulticastDomainId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayMulticastDomainId  
[transit-gateway-policy-table](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-policy-table/${TransitGatewayPolicyTableId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayPolicyTableId  
[transit-gateway-route-table-announcement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-route-table-announcement/${TransitGatewayRouteTableAnnouncementId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableAnnouncementId  
[transit-gateway-route-table](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) |  `arn:${Partition}:ec2:${Region}:${Account}:transit-gateway-route-table/${TransitGatewayRouteTableId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey} ec2:transitGatewayRouteTableId  
[verified-access-endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:verified-access-endpoint/${VerifiedAccessEndpointId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[verified-access-endpoint-target](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:verified-access-endpoint-target/${VerifiedAccessEndpointTargetId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[verified-access-group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:verified-access-group/${VerifiedAccessGroupId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[verified-access-instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:verified-access-instance/${VerifiedAccessInstanceId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[verified-access-policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:verified-access-policy/${VerifiedAccessPolicyId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[verified-access-trust-provider](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#EC2_ARN_Format) |  `arn:${Partition}:ec2:${Region}:${Account}:verified-access-trust-provider/${VerifiedAccessTrustProviderId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html) |  `arn:${Partition}:ec2:${Region}:${Account}:volume/${VolumeId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AvailabilityZone ec2:Encrypted ec2:IsLaunchTemplateResource ec2:KmsKeyId ec2:LaunchTemplate ec2:ManagedResourceOperator ec2:ParentSnapshot ec2:Region ec2:ResourceTag/${TagKey} ec2:VolumeID ec2:VolumeIops ec2:VolumeSize ec2:VolumeThroughput ec2:VolumeType  
[vpc-block-public-access-exclusion](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-block-public-access.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-block-public-access-exclusion/${VpcBlockPublicAccessExclusionId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[vpc-endpoint-connection](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint-connection/${VpcEndpointConnectionId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[vpc-endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint/${VpcEndpointId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey} ec2:VpceServiceName ec2:VpceServiceOwner  
[vpc-endpoint-service](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint-service/${VpcEndpointServiceId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:ResourceTag/${TagKey} ec2:VpceServicePrivateDnsName ec2:vpceMultiRegion ec2:vpceServiceRegion ec2:vpceSupportedRegion  
[vpc-endpoint-service-permission](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html#vpc-endpoint-policies) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint-service-permission/${VpcEndpointServicePermissionId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[vpc-flow-log](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-flow-log/${VpcFlowLogId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
[vpc](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc/${VpcId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:Ipv4IpamPoolId ec2:Ipv6IpamPoolId ec2:Region ec2:ResourceTag/${TagKey} ec2:Tenancy ec2:VpcID  
[vpc-peering-connection](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpc-peering-connection/${VpcPeeringConnectionId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:AccepterVpc ec2:Attribute ec2:Attribute/${AttributeName} ec2:Region ec2:RequesterVpc ec2:ResourceTag/${TagKey} ec2:VpcPeeringConnectionID  
[vpn-connection-device-type](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpn-connection-device-type/${VpnConnectionDeviceTypeId}` |  ec2:Region  
[vpn-connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpn-connection/${VpnConnectionId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Attribute ec2:Attribute/${AttributeName} ec2:AuthenticationType ec2:DPDTimeoutSeconds ec2:GatewayType ec2:IKEVersions ec2:InsideTunnelCidr ec2:InsideTunnelIpv6Cidr ec2:Phase1DHGroup ec2:Phase1EncryptionAlgorithms ec2:Phase1IntegrityAlgorithms ec2:Phase1LifetimeSeconds ec2:Phase2DHGroup ec2:Phase2EncryptionAlgorithms ec2:Phase2IntegrityAlgorithms ec2:Phase2LifetimeSeconds ec2:Region ec2:RekeyFuzzPercentage ec2:RekeyMarginTimeSeconds ec2:ReplayWindowSizePackets ec2:ResourceTag/${TagKey} ec2:RoutingType  
[vpn-gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) |  `arn:${Partition}:ec2:${Region}:${Account}:vpn-gateway/${VpnGatewayId}` |  aws:RequestTag/${TagKey} aws:ResourceTag/${TagKey} aws:TagKeys ec2:Region ec2:ResourceTag/${TagKey}  
  
## Condition keys for Amazon EC2

Amazon EC2 defines the following condition keys that can be used in the
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
[aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.html#control-tagging) | Filters access by a tag key and value pair that is allowed in the request | String  
[aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/control-access-with-tags.html) | Filters access by a tag key and value pair of a resource | String  
[aws:TagKeys](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.html#control-tagging) | Filters access by a list of tag keys that are allowed in the request | ArrayOfString  
[ec2:AccepterVpc](https://docs.aws.amazon.com/vpc/latest/peering/security-iam.html) | Filters access by the ARN of an accepter VPC in a VPC peering connection | ARN  
[ec2:Add/group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the group being added to a snapshot | String  
[ec2:Add/userId](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the account id being added to a snapshot | String  
[ec2:AllocationId](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the allocation ID of the Elastic IP address | String  
[ec2:AssociatePublicIpAddress](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the user wants to associate a public IP address with the instance | Bool  
[ec2:Attribute](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#attribute-key) | Filters access by an attribute of a resource | String  
[ec2:Attribute/${AttributeName}](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#attribute-key) | Filters access by an attribute being set on a resource | String  
[ec2:AuthenticationType](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the authentication type for the VPN tunnel endpoints | String  
[ec2:AuthorizedService](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the AWS service that has permission to use a resource | String  
[ec2:AuthorizedUser](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by an IAM principal that has permission to use a resource | String  
[ec2:AutoPlacement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the Auto Placement properties of a Dedicated Host | String  
[ec2:AvailabilityZone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the name of an Availability Zone in an AWS Region | String  
[ec2:CapacityReservationFleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the Capacity Reservation Fleet | ARN  
[ec2:ClientRootCertificateChainArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the client root certificate chain | ARN  
[ec2:CloudwatchLogGroupArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the CloudWatch Logs log group | ARN  
[ec2:CloudwatchLogStreamArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the CloudWatch Logs log stream | ARN  
[ec2:CpuOptionsAmdSevSnp](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html) | Filters access by the state of AMD SEV-SNP CPU Options. Currently, only US East (Ohio) and Europe (Ireland) are supported | String  
[ec2:CreateAction](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.html) | Filters access by the name of a resource-creating API action | String  
[ec2:CreateDate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the date and time at which the Capacity Reservation was created | Date  
[ec2:DPDTimeoutSeconds](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the duration after which DPD timeout occurs on a VPN tunnel | Numeric  
[ec2:DestinationCapacityReservationId](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ID of the Capacity Reservation that you want to move capacity into | ARN  
[ec2:DhcpOptionsID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a dynamic host configuration protocol (DHCP) options set | String  
[ec2:DirectoryArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the directory | ARN  
[ec2:Domain](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the domain of the Elastic IP address | String  
[ec2:EbsOptimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the instance is enabled for EBS optimization | Bool  
[ec2:ElasticGpuType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of Elastic Graphics accelerator | String  
[ec2:Encrypted](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the EBS volume is encrypted | Bool  
[ec2:EndDate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the date and time at which the Capacity Reservation ends | Date  
[ec2:EndDateType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the way in which the Capacity Reservation ends | String  
[ec2:FisActionId](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html) | Filters access by the ID of an AWS FIS action | String  
[ec2:FisTargetArns](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html) | Filters access by the ARN of an AWS FIS target | ArrayOfARN  
[ec2:GatewayType](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the gateway type for a VPN endpoint on the AWS side of a VPN connection | String  
[ec2:HostRecovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether host recovery is enabled for a Dedicated Host | String  
[ec2:IKEVersions](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the internet key exchange (IKE) versions that are permitted for a VPN tunnel | ArrayOfString  
[ec2:ImageID](iam-policy-structure.html#imageId-key) | Filters access by the ID of an image | String  
[ec2:ImageType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of image (machine, aki, or ari) | String  
[ec2:InsideTunnelCidr](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the range of inside IP addresses for a VPN tunnel | String  
[ec2:InsideTunnelIpv6Cidr](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by a range of inside IPv6 addresses for a VPN tunnel | String  
[ec2:InstanceAutoRecovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the instance type supports auto recovery | String  
[ec2:InstanceBandwidthWeighting](iam-policy-structure.html#imageId-key) | Filters access by the bandwidth weighting of an instance | String  
[ec2:InstanceCount](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the number of instances | Numeric  
[ec2:InstanceID](iam-policy-structure.html#imageId-key) | Filters access by the ID of an instance | String  
[ec2:InstanceMarketType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the market or purchasing option of an instance (capacity-block, on-demand, or spot) | String  
[ec2:InstanceMatchCriteria](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of instance launches that the Capacity Reservation accepts | String  
[ec2:InstanceMetadataTags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the instance allows access to instance tags from the instance metadata | String  
[ec2:InstancePlatform](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of operating system for which the Capacity Reservation reserves capacity | ARN  
[ec2:InstanceProfile](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of an instance profile | ARN  
[ec2:InstanceType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of instance | String  
[ec2:InternetGatewayID](iam-policy-structure.html#imageId-key) | Filters access by the ID of an internet gateway | String  
[ec2:Ipv4IpamPoolId](iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ID of an IPAM pool provided for IPv4 CIDR block allocation | String  
[ec2:Ipv6IpamPoolId](iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ID of an IPAM pool provided for IPv6 CIDR block allocation | String  
[ec2:IsLaunchTemplateResource](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether users are able to override resources that are specified in the launch template | Bool  
[ec2:KeyPairName](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the name of a key pair | String  
[ec2:KeyPairType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of a key pair | String  
[ec2:KmsKeyId](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ID of an AWS KMS key provided in the request | String  
[ec2:LaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of a launch template | ARN  
[ec2:Location](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the destination for the snapshot copy | String  
[ec2:ManagedResourceOperator](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the presence of an EC2 operator provisioning a managed resource | String  
[ec2:MetadataHttpEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the HTTP endpoint is enabled for the instance metadata service | String  
[ec2:MetadataHttpPutResponseHopLimit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the allowed number of hops when calling the instance metadata service | Numeric  
[ec2:MetadataHttpTokens](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether tokens are required when calling the instance metadata service (optional or required) | String  
[ec2:NetworkAclID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a network access control list (ACL) | String  
[ec2:NetworkInterfaceID](iam-policy-structure.html#imageId-key) | Filters access by the ID of an elastic network interface | String  
[ec2:NewInstanceProfile](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the instance profile being attached | ARN  
[ec2:OutpostArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the Outpost | ARN  
[ec2:Owner](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the owner of the resource (amazon, aws-marketplace, or an AWS account ID) | String  
[ec2:ParentSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the parent snapshot | ARN  
[ec2:ParentVolume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the parent volume from which the snapshot was created | ARN  
[ec2:Permission](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of permission for a resource (INSTANCE-ATTACH or EIP-ASSOCIATE) | String  
[ec2:Phase1DHGroup](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the Diffie-Hellman group numbers that are permitted for a VPN tunnel for the phase 1 IKE negotiations | ArrayOfString  
[ec2:Phase1EncryptionAlgorithms](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the encryption algorithms that are permitted for a VPN tunnel for the phase 1 IKE negotiations | ArrayOfString  
[ec2:Phase1IntegrityAlgorithms](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the integrity algorithms that are permitted for a VPN tunnel for the phase 1 IKE negotiations | ArrayOfString  
[ec2:Phase1LifetimeSeconds](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the lifetime in seconds for phase 1 of the IKE negotiations for a VPN tunnel | Numeric  
[ec2:Phase2DHGroup](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the Diffie-Hellman group numbers that are permitted for a VPN tunnel for the phase 2 IKE negotiations | ArrayOfString  
[ec2:Phase2EncryptionAlgorithms](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the encryption algorithms that are permitted for a VPN tunnel for the phase 2 IKE negotiations | ArrayOfString  
[ec2:Phase2IntegrityAlgorithms](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the integrity algorithms that are permitted for a VPN tunnel for the phase 2 IKE negotiations | ArrayOfString  
[ec2:Phase2LifetimeSeconds](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the lifetime in seconds for phase 2 of the IKE negotiations for a VPN tunnel | Numeric  
[ec2:PlacementGroup](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the placement group | ARN  
[ec2:PlacementGroupName](iam-policy-structure.html#imageId-key) | Filters access by the name of a placement group | String  
[ec2:PlacementGroupStrategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the instance placement strategy used by the placement group (cluster, spread, or partition) | String  
[ec2:ProductCode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the product code that is associated with the AMI | String  
[ec2:Public](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by whether the image has public launch permissions | Bool  
[ec2:PublicIpAddress](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by a public IP address | String  
[ec2:Quantity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the number of Dedicated Hosts in a request | Numeric  
[ec2:Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the name of the AWS Region | String  
[ec2:RekeyFuzzPercentage](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the percentage of increase of the rekey window (determined by the rekey margin time) within which the rekey time is randomly selected for a VPN tunnel | Numeric  
[ec2:RekeyMarginTimeSeconds](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the margin time before the phase 2 lifetime expires for a VPN tunnel | Numeric  
[ec2:Remove/group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the group being removed from a snapshot | String  
[ec2:Remove/userId](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the account id being removed from a snapshot | String  
[ec2:ReplayWindowSizePackets](iam-policy-structure.html#amazon-ec2-keys) | Filters access by the number of packets in an IKE replay window | String  
[ec2:RequesterVpc](https://docs.aws.amazon.com/vpc/latest/peering/security-iam.html) | Filters access by the ARN of a requester VPC in a VPC peering connection | ARN  
[ec2:ReservedInstancesOfferingType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html#ri-payment-options) | Filters access by the payment option of the Reserved Instance offering (No Upfront, Partial Upfront, or All Upfront) | String  
[ec2:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/control-access-with-tags.html) | Filters access by a tag key and value pair of a resource | String  
[ec2:RoleDelivery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the version of the instance metadata service for retrieving IAM role credentials for EC2 | Numeric  
[ec2:RootDeviceType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the root device type of the instance (ebs or instance-store) | String  
[ec2:RouteTableID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a route table | String  
[ec2:RoutingType](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-authentication-access-control.html) | Filters access by the routing type for the VPN connection | String  
[ec2:SamlProviderArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the IAM SAML identity provider | ARN  
[ec2:SecurityGroupID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a security group | String  
[ec2:ServerCertificateArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the server certificate | ARN  
[ec2:SnapshotCoolOffPeriod](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the compliance mode cooling-off period | Numeric  
[ec2:SnapshotID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a snapshot | String  
[ec2:SnapshotLockDuration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the snapshot lock duration | Numeric  
[ec2:SnapshotTime](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the initiation time of a snapshot | String  
[ec2:SourceAvailabilityZone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the name of the Availability Zone from which the request originated | String  
[ec2:SourceCapacityReservationId](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ID of the Capacity Reservation from which you want to move capacity | ARN  
[ec2:SourceInstanceARN](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the instance from which the request originated | ARN  
[ec2:SourceOutpostArn](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the Outpost from which the request originated | ARN  
[ec2:Subnet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the subnet | ARN  
[ec2:SubnetID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a subnet | String  
[ec2:Tenancy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the tenancy of the VPC or instance (default, dedicated, or host) | String  
[ec2:VolumeID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a volume | String  
[ec2:VolumeIops](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the the number of input/output operations per second (IOPS) provisioned for the volume | Numeric  
[ec2:VolumeSize](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the size of the volume, in GiB | Numeric  
[ec2:VolumeThroughput](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the throughput of the volume, in MiBps | Numeric  
[ec2:VolumeType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the type of volume (gp2, gp3, io1, io2, st1, sc1, or standard) | String  
[ec2:Vpc](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys) | Filters access by the ARN of the VPC | ARN  
[ec2:VpcID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a virtual private cloud (VPC) | String  
[ec2:VpcPeeringConnectionID](iam-policy-structure.html#imageId-key) | Filters access by the ID of a VPC peering connection | String  
[ec2:VpceServiceName](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-iam.html) | Filters access by the name of the VPC endpoint service | String  
[ec2:VpceServiceOwner](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-iam.html) | Filters access by the service owner of the VPC endpoint service (amazon, aws-marketplace, or an AWS account ID) | String  
[ec2:VpceServicePrivateDnsName](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-iam.html) | Filters access by the private DNS name of the VPC endpoint service | String  
[ec2:transitGatewayAttachmentId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway attachment | String  
[ec2:transitGatewayConnectPeerId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway connect peer | String  
[ec2:transitGatewayId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway | String  
[ec2:transitGatewayMulticastDomainId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway multicast domain | String  
[ec2:transitGatewayPolicyTableId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway policy table | String  
[ec2:transitGatewayRouteTableAnnouncementId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway route table announcement | String  
[ec2:transitGatewayRouteTableId](iam-policy-structure.html#imageId-key) | Filters access by the ID of a transit gateway route table | String  
[ec2:vpceMultiRegion](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-iam.html) | Filters access by multi region of the VPC endpoint service | String  
[ec2:vpceServiceRegion](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-iam.html) | Filters access by the region of the VPC endpoint service | String  
[ec2:vpceSupportedRegion](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-iam.html) | Filters access by the supported region of the VPC endpoint service | String  
  
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

