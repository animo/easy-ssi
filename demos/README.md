# Demos

A collection of current demo's for the Easy-SSI project. Demo's should show real-world application use of Aries Framework JavaScript and the potential that plugins/presets can offer.

## [Chat application](https://www.youtube.com/watch?v=wW4HSZZ2kSk)

This is a simple messaging app that allows to make DIDComm connections and send end-to-end encrypted messages via a mediator service. Although it’s not about the credential exchange, it’s still the foundation for other SSI building blocks. The whole solution actually consists of three standalone apps all of them built with JavaScript and using Aries Framework JavaScript:

- Desktop app built with React and Electron
- Mobile iOS app built with Aries Framework JavaScript and React Native
- Server-side mediator service built with NodeJS

The demo also demonstrates the framework’s independence on transport mechanisms (e.g. HTTP polling could be eventually replaced by WebSockets). Utilization of the JavaScript event system enables developers to build more reactive apps while the usage of a mediator service provides offline message delivery. 

We believe that multi-platform development in JavaScript is a great benefit and could lower the barrier to entry into the whole SSI ecosystem. Now it’s the time to make it easy to use for other developers.

[Watch the chat application demo here!](https://www.youtube.com/watch?v=wW4HSZZ2kSk)

## [Mobile holder agent](https://www.youtube.com/watch?v=mmFSgSR5yPA)

This is a mobile holder agent built with Aries Framework JavaScript and React Native, the mobile holder agent can make a connection with and receive credentials from other Aries protocol compliant agents. The video shows the process of creating a connection and issuing a credential between a mobile holder agent and an issuer agent.Both mobile and server-side code was written in JavaScript. 

The setup consists of three artifacts:

- Mobile Android app built with Aries Framework JavaScript and React Native (**holder**)
- Server-side mediator service built with Aries Framework JavaScript and NodeJS
- A OpenAPI interface to a [Aries Cloud Agent Python](https://github.com/hyperledger/aries-cloudagent-python) instance (**issuer**)

This proof of concept demonstrates the multi-platform options developers have when using Aries Framework JavaScript. Uses of ACA-Py shows the interoperability with other Aries compliant frameworks.

[Watch the mobile holder agent demo here!](https://www.youtube.com/watch?v=mmFSgSR5yPA)

[Check out the codebase here!](https://github.com/animo/aries-mobile-agent-react-native)
