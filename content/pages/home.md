Title: Start
Author: Kristoffer Paulsson
Date: 2021-01-14
status:
url: index.html
save_as: index.html
order: 1

The Angelos Project is used by those having needs to hide their good from the persecuting evildoers.

Welcome to the Free Republic of Libertania and unwelcome to the Rouge Regime of Crookistan! In this world, you can no longer trust worldly authorities or human governments. Therefore a safe and privately owned but distributed communication channel is needed. The main reason why Angelos and Logo were developed but not yet finished. Here we will introduce the concept and beg for voluntary developers and agents of benefactors to support The Angelos Project.

## Concept of Angelos

Problems:

* Defamation: Groups and organizations defame churches, pastors, and others that stand up.
* Shadow-banning: Suppression of Christian organizations and persons using algorithms and targeting.
* Deplatforming: Christian organizations and persons are being de-platformed.
* Eavesdropping: Crooked regimes are eavesdropping non-conformists.
* Surveillance: Intelligence agencies monitor dissidents.
* Shutdowns: Regimes are shutting down services for public use.
* Persecution: Public persecution and discrimination, imprisonment, torture, and killings.

Suggested solutions:

1. One big commercial operator, &rarr; Several ideal private operators.
2. Proprietary standards &rarr; Open standards.
3. Large datacenters &rarr; Spread out distributed nodes.
4. Open networks &rarr; Encrypted communication tunnels.
5. Readable information &rarr; Encrypted files and networks.
6. Unverified identities &rarr; Peer-signed identities in a circle of trust.

## Technological Implementation

![Technological implementation in Angelos with server of a local assembly and a person with an app.]({attach}images/technologies-implementation.png)

* The domain-model with peer-2-peer nodes.
* The document-model with certificates and public keys.
* Archiving virtual filesystem with transparent encryption technology.
* Network protocols for synchronization and services.
* SSH with custom-built subsystems.

## The Document Model

* All information consists of signed certificates.
* All certificates have a unique ID-number.
* All certificates are issued by you and for you, or someone you like.
* Every certificate is verified every time using standardized policies for security.
* All certificates belonging to an Entity is called a portfolio.

## Entities Friends Each-others

An entity is a technical description of someone that is an actor within the Angelos network platform. Most likely a person but also ministries and the local assembly of believers in a city.

![Person to person friending and person to assembly friending by exchange of profile and credential data.]({attach}images/persons-assembly.png)

1. A client (user) and a server (network) exchange public keys and issues two certificates each, a) certificate of verified identity (objectively) and b) certificate of trust (subjectively). Then the client is enabled to logon to the server.
2. Person A and Person B (both users) exchange public keys with each other and issues each a certificate of trust. Now A and B can privately message each other without eavesdropping.

## The Domain Model

* Every entity (person, ministry, and assembly) has a private domain that it owns and controls.
* Each domain consists of at least one or several nodes, which are hardware units storing information.
* All nodes within a domain are peers.
* Nodes store all the information in fully encrypted filesystem archives.
* Nodes synchronize their encrypted archives using replication technology.
* Every node is thereby a backup of all other nodes.

## Domain Node Network

In this world, there will be nations that are more or less tolerant of the liberty of free speech and private communication. The rouge offices will try to shut down networks of assemblies to enable control and dismay the believers. Therefore a network domain should have nodes abroad in a tolerant nation. 

* Two nodes in Crookistan and one in Libertania
* Encrypted communication tunnels between server and clients
* Perpetual synchronization of information within the domain nodes
* Encrypted communication tunnels between nodes

## Network Internal Messaging

![A server domain lets its users send encrypted and signed mail that is routed internally.]({attach}images/assembly-routing.png)

* A server domain is unable to read the message sent.
* A server domain can see the sender and recipient.

## Interdomain Network
Network server domains can also friend each other, enabling routing messages between assemblies, interconnected to the vast international network.

* Domains can connect for routing by friending between assemblies and ministries.
* Encrypted communication tunnels between domains.
* A fake domain portraying as a ministry or assembly domain set up by the secret services or international syndicates can be disconnected.

## Interdomain Messaging
Before a server domain is routing a message, it is encrypted a second time to conceal the original sender and recipient, thereby keeping the users anonymous if there are fake domains. 

![A whole network of assemblies may offer secret interdomain mail routing.]({attach}images/interdomain-routing.png)

* Senders and recipients are anonymized when routing outside the domain by encrypting the whole envelope.
* Routing domain servers can only see the start and finish domain destinations but not users.

## In the Future

* Online status of friends
* Search for contacts, domain-specific
* Instant messaging
* Stream of news, private, and assembly posts
* Voice calls within a server domain
* Mail routing interdomain
* File upload and share of free and screened content

## What has been done!

There are two ongoing repositories in use, one for the app, the other for the server. Please have a look.

[The Logo Messenger](https://github.com/kristoffer-paulsson/logo)

[The Angelos server and libs](https://github.com/kristoffer-paulsson/angelos)