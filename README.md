# About

The Easy SSI project aims to make the setup of self-sovereign identity solutions and the integration of self-sovereign identity functionality into any project _as easy as possible_.

We do this by creating an ecosystem of plugins and presets using [Hyperledger Aries Framework Javascript](https://github.com/hyperledger/aries-framework-javascript). In order to increase the adoption of self-sovereign identity we are making it easy for developers to use existing technologies and connect to ssi projects already out there. Allowing _every_ developer to integrate ssi into their project without hassle.

Components are proposed and worked on by the community. Currently we are working on both [plugins](./plugins/README.md) and [presets](./presets/README.md). To get involved or make a proposal please read [How to Contribute](./how-to-contribute.md).

## Lifecycle

All proposals go through a small lifecycle where they move through set stages (_proposed_, _accepted_, _work in progress_ and _implemented_). Once a proposal has been made (according to the [guidelines](how-to-contribute.md)), it will be discussed within the community and moved along the lifecycle stages.

### Plugins

Plugins facilitate easy integration with existing initiatives and technologies. To get more information or see the state of current plugins, visit [plugins](plugins/README.md).

### Presets

Presets allow developers to easily setup a type of agent/service with default values to keep or customise. To get more information or see the state of curent presets, visit [presets](presets/README.md).

## Roadmap

The Easy SSI project is currently working towards applying for [eSSIF Lab Funding](https://essif-lab-infrastructure-oriented.fundingbox.com/) on 04-01-2021. 

- [x] Move project to public repo
- [x] Schedule community call
- [x] Involve AFJ community
- [x] Work out list of pre-proposals
- [x] Contact plugin collaborators
- [x] API design
- [x] Refactor design AFJ
- [x] Funding proposal
- [x] AFJ usable in React Native
- [x] Demo chat agent
- [x] Demo mobile holder agent
- [ ] Aries interop profile 2.0
- [ ] Future proof design (beyond Indy)
- [ ] Refactor AFJ
- [ ] Mobile Agent Preset
- [ ] Implement plugins

### Pre-proposed

The project started internally and grew to a public space. Beneath is the current list of 'pre-proposed' ideas we'd like to iterate on to create well thought out proposals. 

Transport plugins
- HTTP
- Websocket
- Bluetooth
- NFC

Protocol-as-plugin
- Issue credential 2.0
- Present proof 2.0
- Mediator coordination 1.0
- Pickup 1.0
- DID exchange 1.0

Decorator plugins
- Attachement
- Thread
- Transport

'Outside world' plugins
- eIDAS Bridge
- SSI Single sign on
- Wordpress
- Identity HUb
- Universal DID resolver

Other plugins
- Acknowledgement
- Problem report
- REST API extenstions

Presets
- Mobile agent preset
- Organisational agent preset
- Developer presets

Also we'd like to explore the option to add example projects based on a specific use case. 


## Contribute

Do you have a great idea or question? To get involved or learn more check-out [How to Contribute](how-to-contribute.md)!
