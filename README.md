# Defender XDR Threat Investigation

A portfolio incident-investigation lab demonstrating how Microsoft Defender XDR telemetry can be used to reconstruct a suspicious endpoint and identity timeline.

> **Portfolio note:** The incident, users, devices and indicators in this repository are synthetic. No real organisation or production evidence is included.

## Scenario

A user receives a malicious document. The simulated investigation follows:

1. Office application launches a suspicious command shell.
2. PowerShell executes an encoded command.
3. A suspicious outbound connection is observed.
4. Identity activity is reviewed for related compromise.
5. The analyst scopes impact and records containment actions.

## What this project demonstrates

- Defender XDR Advanced Hunting with KQL
- endpoint process-chain analysis
- network-event investigation
- identity correlation
- evidence timelines
- incident scoping and containment thinking
- repeatable investigation documentation

## Repository structure

```text
.
├── data/
│   └── synthetic_timeline.csv
├── docs/
│   ├── case-study.md
│   └── investigation-playbook.md
├── hunting/
│   ├── endpoint-hunting.kql
│   └── identity-correlation.kql
├── scripts/
│   └── build_timeline.py
└── README.md
```

## Investigation flow

```text
Alert
  |
  v
Validate process tree
  |
  +--> Review command line
  +--> Review network connections
  +--> Review file activity
  +--> Correlate identity activity
  |
  v
Scope affected users/devices
  |
  v
Contain -> Remediate -> Recover
```

## Skills demonstrated

**Microsoft Defender XDR · Advanced Hunting · KQL · Endpoint Investigation · Identity Security · Incident Response · Python**

## Provenance

This repository is a synthetic technical demonstration. Any similarity to real incidents is illustrative only.
