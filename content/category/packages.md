Title: Packages and subpackages
Author: Kristoffer Paulsson
Date: 2021-01-17
Modified: 2021-01-21
Category: Developer
url: packages-and-subpackages.html
sort: 2

In The Angelos Project, the codebase became so intricate that it was needed to sort it into sub-packages. It is necessary to keep track of each technology stack for code quality assurance and keep dependencies in place.

## angelos

The main namespace package.

## angelos.lib

It is the old main Angelos code-base that was written in haste and with medium code quality. The goal is to completely deprecate this library as we mitigate the code into other well-written sub-packages.

## angelos.common

The common package contains commonly used pieces of code that goes over all the Angelos and logo messenger codebase.

## angelos.archive7

It is the archive file format that keeps all data in an Angelos node transparently encrypted. Archive7 is a private file format for file archiving, meant to be used as a virtual filesystem.

## angelos.bin

It is a library for the integration of third-party modules written in the C language. They get compiled and included in the application and server binary.

## angelos.facade

The facade is the central core of an application that builds upon Angelos. It is the piece that guards and proves each, cryptographically signed and encrypted, item of data, testing to make sure that nothing is corrupt. It is an intermediary between the network, archives, and the user interface.

## angelos.document

The implementation of the Angelos document-model. Which defines a format for all information in use on the Angelos network to ensure full reliability in the communications.

## angelos.meta

It is a helper library which only use to manage the project's tool-chain.

## angelos.portfolio

All documents within a facade organize in portfolios, grouping all data with its belonging identities.

## angelos.psi

PSI stands for Platform Specific Implementations. All code that is platform-specific for Windows, macOS, and Linux goes into this package where an abstract interface applies for conformity.

## angelos.net

The network stack is highly extensible for the expansion of possible services needed within the Angelos network. The stack is secure, using extremely robust NaCl-based encryption algorithms.

## angelos.eidon

Eidon stands for vision in the koine Greek. It is a specific image format developed for use within Angelos. It is more efficient than JPEG.

## angelos.server

The server runs the operations in a node.