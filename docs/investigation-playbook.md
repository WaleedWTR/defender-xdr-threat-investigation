# Defender XDR Investigation Playbook

## Validate

- inspect alert evidence
- review device timeline
- inspect initiating and child processes
- capture hashes, command lines and remote destinations

## Scope

- search the indicator across all devices
- search the affected account across identity telemetry
- identify related file, registry and network activity
- determine whether other identities or devices are affected

## Containment candidates

Subject to organisational procedure:

- isolate a confirmed compromised device
- revoke compromised sessions
- reset credentials where compromise is established
- block confirmed malicious indicators
- collect investigation packages / evidence

## Recovery

- remove malicious artefacts
- patch or reconfigure exploited components
- restore trusted state
- monitor for recurrence
- close with documented timeline and lessons learned
