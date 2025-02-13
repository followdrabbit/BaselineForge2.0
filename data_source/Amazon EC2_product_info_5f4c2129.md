# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/concepts.html'}

[](ec2-ug.pdf#concepts "Abrir em PDF")

[DocumentaÃ§Ã£o](/index.html)[Amazon EC2](/ec2/index.html)[Manual do
usuÃ¡rio](concepts.html)

AtributosServiÃ§os relacionadosAcesso ao EC2PreÃ§osRecursos

# O que Ã© o Amazon EC2?

O Amazon Elastic Compute Cloud (Amazon EC2) oferece uma capacidade de
computaÃ§Ã£o escalÃ¡vel sob demanda na Nuvem Amazon Web Services (AWS). O uso
do Amazon EC2 reduz os custos de hardware para que vocÃª possa desenvolver e
implantar aplicaÃ§Ãµes com mais rapidez. Ã possÃ­vel usar o Amazon EC2 para
executar quantos servidores virtuais forem necessÃ¡rios, configurar a
seguranÃ§a e as redes e gerenciar o armazenamento. Ã possÃ­vel adicionar
capacidade (aumentar a escala verticalmente) para lidar com tarefas de
computaÃ§Ã£o pesada, como processos mensais ou anuais ou picos no trÃ¡fego do
site. Quando o uso diminui, vocÃª pode reduzir a capacidade (reduzir a escala
verticalmente) de novo.

Uma instÃ¢ncia do EC2 Ã© um servidor virtual na Nuvem AWS. Quando executa uma
instÃ¢ncia do EC2, o tipo de instÃ¢ncia que vocÃª especifica determina o
hardware disponÃ­vel para sua instÃ¢ncia. Cada tipo de instÃ¢ncia oferece um
equilÃ­brio diferente entre recursos de computaÃ§Ã£o, memÃ³ria, armazenamento
e rede. Para obter mais informaÃ§Ãµes, consulte o [Guia de tipos de instÃ¢ncia
do Amazon EC2](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-
types.html).

![Cada tipo de instÃ¢ncia do EC2 oferece um equilÃ­brio entre os recursos de
computaÃ§Ã£o, memÃ³ria, armazenamento e rede.](images/instance-types.png)

## Recursos do Amazon EC2

O Amazon EC2 fornece os seguintes recursos de alto nÃ­vel:

**InstÃ¢ncias**

    

Servidores virtuais.

**Imagens de mÃ¡quina da Amazon (AMIs)**

    

Os modelos prÃ©-configurados para suas instÃ¢ncias que empacotam os
componentes de que vocÃª precisa para seu servidor (incluindo o sistema
operacional e software adicional).

**Tipos de instÃ¢ncia**

    

VÃ¡rias configuraÃ§Ãµes de capacidade de CPU, memÃ³ria, armazenamento e redes
e hardware grÃ¡fico para suas instÃ¢ncias.

**Volumes do Amazon EBS**

    

Volumes de armazenamento persistentes para seus dados usando o Amazon Elastic
Block Store (Amazon EBS).

**Volumes de armazenamento de instÃ¢ncias**

    

Volumes de armazenamento para dados temporÃ¡rios que sÃ£o excluÃ­dos quando
vocÃª interrompe, hiberna ou encerra sua instÃ¢ncia.

**Pares de chaves**

    

Proteja informaÃ§Ãµes de login de suas instÃ¢ncias. AÂ AWSÂ armazena a chave
pÃºblica, e vocÃª armazena a chave privada em um lugar seguro.

**Grupos de seguranÃ§a**

    

Um firewall virtual que permite especificar os protocolos, as portas e os
intervalos de IP de origem que podem alcanÃ§ar suas instÃ¢ncias e os
intervalos de IP de destino aos quais suas instÃ¢ncias podem se conectar.

O Amazon EC2 Ã© compatÃ­vel com o processamento, o armazenamento e a
transmissÃ£o de dados de cartÃ£o de crÃ©dito por um comerciante ou um provedor
de serviÃ§os e foi validada como em conformidade com o Data Security Standard
(DSS, PadrÃ£o de seguranÃ§a de dados) da Payment Card Industry (PCI, PadrÃ£o
de cartÃ£o de crÃ©dito). Para obter mais informaÃ§Ãµes sobre o PCI DSS,
incluindo como solicitar uma cÃ³pia do pacote de conformidade com o PCI da
AWS, consulte [NÃ­vel 1 do PCI DSS](https://aws.amazon.com/compliance/pci-dss-
level-1-faqs/).

## ServiÃ§os relacionados

###### ServiÃ§os para uso com o Amazon EC2

Ã possÃ­vel usar outra ServiÃ§os da AWS com as instÃ¢ncias que vocÃª implanta
usando o Amazon EC2.

[Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/)

    

Ajuda a garantir que vocÃª tenha o nÃºmero correto de instÃ¢ncias do Amazon
EC2 disponÃ­veis para processar a carga da aplicaÃ§Ã£o.

[AWS Backup](https://docs.aws.amazon.com/aws-backup/)

    

Automatize o backup de suas instÃ¢ncias do Amazon EC2 e dos volumes do Amazon
EBS anexados a elas.

[Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)

    

Monitore suas instÃ¢ncias e os volumes do Amazon EBS.

[Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/)

    

Distribua automaticamente o trÃ¡fego de entrada da aplicaÃ§Ã£o entre vÃ¡rias
instÃ¢ncias.

[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/)

    

Detecte o uso potencialmente nÃ£o autorizado ou mal-intencionado de suas
instÃ¢ncias do EC2.

[EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/)

    

Automatize a criaÃ§Ã£o, o gerenciamento e a implantaÃ§Ã£o de imagens de
servidor personalizadas, seguras e atualizadas.

[AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/)

    

Dimensione, configure e implante recursos daÂ AWSÂ para aplicaÃ§Ãµes de
terceiros sem precisar identificar e provisionar recursos daÂ AWSÂ individuais
manualmente.

[AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/)

    

Execute operaÃ§Ãµes em grande escala em instÃ¢ncias do EC2 com essa soluÃ§Ã£o
segura de gerenciamento de ponta a ponta.

###### ServiÃ§os adicionais de computaÃ§Ã£o

Ã possÃ­vel iniciar instÃ¢ncias usando outro serviÃ§o de computaÃ§Ã£o da AWS
em vez de usar o Amazon EC2.

[Amazon Lightsail](https://docs.aws.amazon.com/lightsail/)

    

Crie sites ou aplicaÃ§Ãµes da Web usando Amazon Lightsail uma plataforma em
nuvem que fornece os recursos necessÃ¡rios para implantar seu projeto
rapidamente, por um preÃ§o mensal baixo e previsÃ­vel. Para comparar o Amazon
EC2 e o Lightsail, consulte [Amazon Lightsail ou Amazon
EC2](https://docs.aws.amazon.com/decision-guides/latest/lightsail-or-
ec2/lightsail-or-ec2.html).

[Amazon Elastic Container Service (Amazon
ECS)](https://docs.aws.amazon.com/ecs/)

    

Implante, gerencie e escale aplicaÃ§Ãµes em contÃªineres em um cluster de
instÃ¢ncias do EC2. Para obter mais informaÃ§Ãµes, consulte [Escolher um
serviÃ§o de contÃªiner da AWS](https://docs.aws.amazon.com/decision-
guides/latest/containers-on-aws-how-to-choose/choosing-aws-container-
service.html).

[Amazon Elastic Kubernetes Service (Amazon
EKS)](https://docs.aws.amazon.com/eks/)

    

Execute as aplicaÃ§Ãµes do Kubernetes na AWS. Para obter mais informaÃ§Ãµes,
consulte [Escolher um serviÃ§o de contÃªiner da
AWS](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-
to-choose/choosing-aws-container-service.html).

## Acessar o Amazon EC2

Ã possÃ­vel criar e gerenciar as instÃ¢ncias do Amazon EC2 usando as
seguintes interfaces:

**Console do Amazon EC2**

    

Uma interface Web simples para criar e gerenciar instÃ¢ncias e recursos do
Amazon EC2. Depois de cadastrar-se em uma conta da AWS, vocÃª pode acessar o
console do Amazon EC2 fazendo login no AWS Management Console e selecionando
**EC2** na pÃ¡gina inicial do console.

**AWS Command Line Interface**

    

Permite interagir com serviÃ§os daÂ AWSÂ usando comandos no shell da linha de
comando. Ã compatÃ­vel com Windows, Mac e Linux. Para obter mais
informaÃ§Ãµes sobre aÂ AWS CLI, consulte o [Guia do usuÃ¡rio daÂ AWS Command
Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/). Ã
possÃ­vel encontrar os comandos do Amazon EC2 naÂ [AWS CLI Command
Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html).

**AWS CloudFormation**

    

O Amazon EC2 permite a criaÃ§Ã£o de recursos usando o AWS CloudFormation.
VocÃª cria um modelo, em JSON ou YAML, que descreve seus recursos da AWS, e o
AWS CloudFormation provisiona e configura esses recursos para vocÃª. Ã
possÃ­vel reutilizar seus modelos do CloudFormation para provisionar os mesmos
recursos vÃ¡rias vezes, seja na mesma regiÃ£o e conta ou em vÃ¡rias regiÃµes e
contas. Para obter mais informaÃ§Ãµes sobre os tipos de recurso e as
propriedades do Amazon EC2, consulte [EC2 resource type
reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EC2.html)
no _Guia do usuÃ¡rio do AWS CloudFormation_.

**SDKs da AWS**

    

Se vocÃª preferir criar aplicaÃ§Ãµes usando APIs especÃ­ficas de uma linguagem
em vez de enviar uma solicitaÃ§Ã£o via HTTP ou HTTPS, a AWS fornece
bibliotecas, cÃ³digo de exemplo, tutoriais e outros recursos para
desenvolvedores de software. Essas bibliotecas fornecem funÃ§Ãµes bÃ¡sicas que
automatizam tarefas, como assinatura criptografada de suas solicitaÃ§Ãµes,
novas tentativas de solicitaÃ§Ãµes e tratamento das respostas de erro,
facilitando para que vocÃª comece rapidamente. Para obter mais informaÃ§Ãµes,
consulte [Ferramentas para criar na
AWS](https://aws.amazon.com/developer/tools/).

**AWS Tools for PowerShell**

    

Um conjunto de mÃ³dulos do PowerShell criados com base na funcionalidade
exposta pelo AWS SDK for .NET. As ferramentas para PowerShell permitem que
vocÃª execute scripts para operaÃ§Ãµes em seus recursos da AWS usando a linha
de comando do PowerShell. Para comeÃ§ar a usar, consulte o [Guia do usuÃ¡rio
da AWS Tools for Windows
PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/). Ã
possÃ­vel encontrar os cmdlets para o Amazon EC2, naÂ [AWS Tools for
PowerShell Cmdlet
Reference](https://docs.aws.amazon.com/powershell/latest/reference/Index.html).

**API de consulta**

    

A Amazon EC2 fornece uma API de consulta. Essas sÃ£o solicitaÃ§Ãµes HTTP ou
HTTPS que usam verbos HTTP GET ou POST e um parÃ¢metro de consulta chamado
`Action`. Para obter mais informaÃ§Ãµes sobre as aÃ§Ãµes de API para o Amazon
EC2, consulte
[AÃ§Ãµes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html)
no _Amazon EC2 API Reference_.

## DefiniÃ§Ã£o de preÃ§o do Amazon EC2

O Amazon EC2 fornece as seguintes opÃ§Ãµes de preÃ§os:

**NÃ­vel gratuito**

    

Ã possÃ­vel comeÃ§ar gratuitamente com o Amazon EC2. Para explorar as
opÃ§Ãµes do nÃ­vel gratuito, consulte [NÃ­vel gratuito da
AWS](https://aws.amazon.com/free/).

**InstÃ¢ncias sob demanda**

    

Pague pelas instÃ¢ncias que vocÃª usar por segundo, com um mÃ­nimo de 60
segundos, sem qualquer compromisso de longo prazo ou pagamentos adiantados.

**Savings Plans**

    

Ã possÃ­vel reduzir os custos do Amazon EC2 se comprometendo com uma
quantidade consistente de uso, em USD por hora, por um perÃ­odo de vigÃªncia
de um ou de trÃªs anos.

**Reserved Instances**

    

Ã possÃ­vel reduzir os custos do Amazon EC2 se comprometendo com uma
configuraÃ§Ã£o especÃ­fica de instÃ¢ncia, incluindo o tipo de instÃ¢ncia e a
regiÃ£o, por um perÃ­odo de vigÃªncia de um ou de trÃªs anos.

**Spot Instances**

    

Solicite instÃ¢ncias do EC2 nÃ£o utilizadas, o que pode reduzir os custos do
Amazon EC2 significativamente.

**Hosts dedicados**

    

Reduza os custos usando um servidor fÃ­sico do EC2 totalmente dedicado ao seu
uso, sob demanda ou como parte de um Savings Plan. Ã possÃ­vel usar suas
licenÃ§as de software existentes vinculadas ao servidor e obter ajuda para
atender aos requisitos de conformidade.

**Reservas de capacidade sob demanda**

    

Reserve capacidade de computaÃ§Ã£o para suas instÃ¢ncias do EC2 em uma zona de
disponibilidade especÃ­fica por qualquer tempo de duraÃ§Ã£o.

**CobranÃ§a por segundo**

    

Elimina o custo de minutos e segundos nÃ£o utilizados da sua fatura.

Para obter uma lista completa de cobranÃ§as e preÃ§os do Amazon EC2 e mais
informaÃ§Ãµes sobre modelos de compra, consulte [PreÃ§o do Amazon
EC2](https://aws.amazon.com/ec2/pricing/).

### Estimativas, faturamento e otimizaÃ§Ã£o de custos

Para criar estimativas para seus casos de uso daÂ AWS, use aÂ [AWS Pricing
Calculator](https://calculator.aws/#/).

Para estimar o custo de transformar as **workloads da Microsoft** em uma
arquitetura moderna que usa serviÃ§os de cÃ³digo aberto e nativos da nuvem
implantados naÂ AWS, use aÂ [Calculadora de ModernizaÃ§Ã£o daÂ AWSÂ para
workloads da
Microsoft](https://modernization.calculator.aws/microsoft/workload).

Para ver sua fatura, acesse o **Painel de gerenciamento de custos e
faturamento** no [console do AWS Billing and Cost
Management](https://console.aws.amazon.com/billing/). Sua fatura contÃ©m links
para relatÃ³rios de uso que fornecem detalhes sobre sua conta. Para saber mais
sobre o faturamento da conta da AWS, consulte o [Guia do usuÃ¡rio do AWS
Billing and Cost
Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).

Se tiver dÃºvidas sobre faturamento, contas e eventos da AWS, [entre em
contato com o Suporte da AWS](https://aws.amazon.com/contact-us/).

Para calcular o custo de um exemplo de ambiente provisionado, consulte [Centro
de informaÃ§Ãµes sobre economia da nuvem](https://aws.amazon.com/economics/).
Ao calcular o custo de um ambiente provisionado, lembre-se de incluir custos
incidentais, como armazenamento de snapshots para volumes do EBS.

Ã possÃ­vel otimizar o custo, a seguranÃ§a e a performance do seu ambiente
daÂ AWSÂ usando oÂ [AWS Trusted
Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/).

Ã possÃ­vel usar o AWS Cost Explorer para analisar o custo e o uso das
instÃ¢ncias do EC2. Ã possÃ­vel visualizar dados dos Ãºltimos 13 meses e
prever o provÃ¡vel valor que vocÃª gastarÃ¡ nos prÃ³ximos 12 meses. Para obter
mais informaÃ§Ãµes, consulte [AnÃ¡lise do seu custo e utilizaÃ§Ã£o com o AWS
Cost Explorer](https://docs.aws.amazon.com/cost-
management/latest/userguide/ce-what-is.html) no _Guia do usuÃ¡rio do AWS Cost
Management_.

## Recursos

  * [Recursos do Amazon EC2](https://aws.amazon.com/ec2/features/)

  * [AWS re:Post](https://repost.aws/)

  * [AWS Skill Builder](https://aws.amazon.com/training/digital/)

  * [Suporte do AWS](https://aws.amazon.com/premiumsupport/)

  * [Tutoriais prÃ¡ticos](https://aws.amazon.com/getting-started/hands-on/)

  * [Hospedagem na Web](https://aws.amazon.com/websites/)

  * [Windows na AWS](https://aws.amazon.com/windows/)

![AtenÃ§Ã£o](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**O Javascript estÃ¡ desativado ou nÃ£o estÃ¡ disponÃ­vel no seu navegador.**

Para usar a documentaÃ§Ã£o da AWS, o Javascript deve estar ativado. Consulte
as pÃ¡ginas de Ajuda do navegador para obter instruÃ§Ãµes.

[ConvenÃ§Ãµes do documento](/general/latest/gr/docconventions.html)

Tutorial de conceitos bÃ¡sicos

Essa pÃ¡gina foi Ãºtil? - Sim

Obrigado por nos informar que estamos fazendo um bom trabalho!

Se tiver tempo, conte-nos sobre o que vocÃª gostou para que possamos melhorar
ainda mais.

Essa pÃ¡gina foi Ãºtil? - NÃ£o

Obrigado por nos informar que precisamos melhorar a pÃ¡gina. Lamentamos ter
decepcionado vocÃª.

Se tiver tempo, conte-nos como podemos melhorar a documentaÃ§Ã£o.

