Title: Layered levels
Author: Kristoffer Paulsson
Date: 2021-01-19
Category: Developer
url: layered-levels.html
sort: 4

The Angelos system has seven defined levels, which in themselves have several sections. Think of each level as a layer in an onion, where level one is the innermost level, and level seven the outermost layer. 

## 1. Fields

Level 1 is the field level and the innermost layer, which is the most rudimentary item inside an Angelos system. The Field contains none, one, or several pieces of data of a defined type, which can undergo validation according to the policies applied to this level.

## 2. Documents

Level 2 is the document level. A Document represents either an identity, certificate, message, or another piece of data, composed of several fields. Documents can undergo validation according to policies applied to their same and inner levels. Documents should always be cryptographically signed by an identity using its cryptographic tokens.

## 3. Portfolios

Level 3 is the portfolio level. A Portfolio is a collection of documents related to an owning identity. The Portfolio must only have one identity Document to which all other documents belong. Portfolios have predefined compositions of Documents depending on the scope of use and may contain any Documents necessary. All portfolios will undergo validation according to policies of current and inner levels. The different compositions are used for public or private purposes, depending on needs. It is necessary to share the Portfolio with others to be able to interact with other entities.

## 4. Facade

Level 4 is the facade level. The Facade is the front and gatekeeper of each installed Angelos instance. The purpose of the Facade is to provide a proven way of importing or exporting data while interacting with other entities on a Network. It guarantees the safety and integrity of its owner. Policies are applied, and operations are carried out following qualified formulas and measures. 

## 5. Nodes

Level 5 is the node level. A Node is a specific device with an installation of the Angelos server or client software. The Node information is kept inside the Facade but representing the software and hardware level that interacts with other instances of Angelos on other devices within the same domain. Each Node is a member of the Domain.

## 6. Domain

Level 6 is the domain level. A Domain is an abstract level representing a collection of one or several nodes that work for the same entity (individual or organization). Node- and Domain information is internal to the Portfolio of the Facades on each Node.

## 7. Network

Level 7 is the network level. A Network is a crowd of individuals and organizations that offer communities for others to join. Network nodes are usually servers that other individual nodes (clients) can interact with for communication.
