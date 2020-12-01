# Plugin - eIDAS Bridge

- Authors: <Name>, <Email (optional)>
- Status: Proposed
- Submitted: <Date of PR>

## Description

_Please explain your plugin (what it does) in a single paragraph. Keep this description high-level, save the details for the 'how it works' section._

This plugin will integrate eIDAS bridge functionality into AFJ. Developers will have the option to use the eIDAS trust framework to prove their VC is trustworthy in an easy and standardized way.

## Motivation

_Describe why this proposal specifically is important to get implemented, what are the benefits it offers, why does it need to exist._

Why eIDAS: Adding legal value to verifiable credentials [see specs dock]. Why this plugin: Ease of use, offering the choice.

## Related projects / technologies

_Describe (with link) the projects this plugin connects, is dependent on or is related to in other ways that might be relevant._

- [Validated ID](https://www.validatedid.com/) received funding to make eIDAS available as a trust framework in the SSI ecosystem in the form of the [eIDAS Bridge](https://joinup.ec.europa.eu/sites/default/files/document/2020-04/SSI%20eIDAS%20Bridge%20-%20Use%20cases%20and%20Technical%20Specifications%20v1.pdf). [Read more about the project.](https://joinup.ec.europa.eu/collection/ssi-eidas-bridge/about).

## Weaknesses

_Describe aspects that will need to be worked out, you are worried about or any drawbacks._

- (possibly) Sealing the whole credential when only part of the credential needs to be shared.
- .

## Strenghts

_Describe aspects that are especially strong, unique or important._

## How it works

_Get as technical and specific as you'd like on how the plugin would function._

"The eIDAS bridge assists the issuer in the process of signing a verifiable credential, and the verifier, in the credential verification process, to assist in identifying the issuer (a legal person in the scope of this project) behind an issuer’s DID. By “crossing” the eIDAS Bridge, a Verifiable Credential is proven trustworthy." [JoinUp](https://joinup.ec.europa.eu/collection/ssi-eidas-bridge/about)

The proposed plugin would wrap around the eIDAS bridge and integrate 'crossing' the bridge into AFJ Issue Credential and AFJ Present Proof.

## Additional information

_Add any specifics here that serve to clarify the concept. Eg. feature list, specs & designs, previous work done, future goals and extentions etc._
