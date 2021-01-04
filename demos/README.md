# Demos

## [Chat application](https://www.youtube.com/watch?v=wW4HSZZ2kSk)

This is a simple messaging app that allows to make DIDComm connections and send end-to-end encrypted messages via mediator service. Although, it’s not about the credential exchange, it’s still the foundation for other SSI building blocks. The whole solution actually consists of three standalone apps all of them built with JavaScript and using the same Aries JS framework package:

- Desktop app built with React and Electron
- Mobile iOS app built with React Native
- Server-side mediator service built with Node.js

The demo also demonstrates the framework’s independence on transport mechanism (HTTP polling that could be eventually replaced by WebSockets), utilization of JavaScript event system enabling to build more reactive apps and offline message delivery thanks to mediator service.

We believe that multi-platform development in JavaScript is a great benefit and could lower a barrier to entry into the whole SSI ecosystem. Now it’s the time to make it easy to use for other developers.

## [Mobile holder agent](https://www.youtube.com/watch?v=mmFSgSR5yPA)

[This video](https://www.youtube.com/watch?v=mmFSgSR5yPA) shows the process of creating a connection and issuing a credential between a mobile holder agent and an issuer agent. It serves as proof-of-concept to show that mobile holder agents built with Aries JS Framework receive credentials from other Aries protocol compliant agents. The setup consists of three artifacts:

- Mobile Android app built with Aries JS Framework and React Native (**holder**)
- Server-side mediator service built with Aries JS Framework and NodeJS
- A OpenAPI interface to a [Aries Cloud Agent Python](https://github.com/hyperledger/aries-cloudagent-python) instance (**issuer**)