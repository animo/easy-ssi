# About

The Easy SSI project aims to make the setup of self-sovereign identity solutions and the integration of self-sovereign identity functionality into any project _as easy as possible_.

We do this by creating an ecosystem of plugins, presets and features using [Hyperledger Aries Framework Javascript](https://github.com/hyperledger/aries-framework-javascript). In order to increase the adoption of self-sovereign identity we are making it easy for developers to use existing technologies and connect to ssi projects already out there. Allowing _every_ developer to integrate ssi into their project without hassle.

Components are proposed and worked on by the community. Currently we are working on [plugins](./plugins/README.md) and [presets](./presets/README.md). To get involved or make a proposal please read [How to Contribute](./how-to-contribute.md).

## Lifecycle

All proposals go through a small lifecycle where they move through set stages (_proposed_, _accepted_, _work in progress_ and _implemented_). Once a proposal has been made (according to the [guidelines](how-to-contribute.md)), it will be discussed within the community and moved along the lifecycle stages.

A quick introduction to the lifecycle. A _proposed_ concept is an idea that a person or organisation is excited by, there has been some thought put into motivation, strenghts and weaknesses, as well as how to technically implement (see the plugin template for details). Once proposed, the plugin is discussed by the community, there can be several iterations on these conversations. If the benefits are clear the proposal is _accepted_. This means there is consensus on the quality of the idea as well as intention to work on the concept. Once there are resources to start development, the concepts becomes a _work in progress_ until it is _implemented_.

### Plugins

Plugins facilitate easy integration with existing initiatives and technologies. To get more information or see the state of current plugins, visit [plugins](plugins/README.md).

### Presets

Presets allow developers to easily setup a type of agent/service with default values to keep or customise. To get more information or see the state of curent presets, visit [presets](presets/README.md).

## Roadmap

The Easy SSI project is currently working towards applying for [eSSIF Lab Funding](https://essif-lab-infrastructure-oriented.fundingbox.com/) on 04-01-2021. 

Short term goals:
- PoC usability in React Native
- Worked out 2 presets (organisational agent and mobile hoder agent)
- Iterate on pre-proposed list

Long term goals:
- AFJ usable in React Native
- Aries interop profile 2.0
- Future proof design (beyond Indy)

Current relevant project questions:
- How will the API look and function?

### Timeline

- 11/2020: Move project to publicly available repo.
- 11/2020: Work out initial list of proposals.
- 11/2020: Setup scheduled community call (Friday 13:30 CET).

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
