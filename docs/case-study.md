# Synthetic Case Study

## Executive summary

A simulated endpoint alert identifies Microsoft Word spawning PowerShell with an encoded command. Subsequent telemetry shows PowerShell making an outbound HTTPS connection and a suspicious file being written to a temporary path.

Identity telemetry is reviewed to determine whether the affected account shows related authentication anomalies.

## Evidence

The synthetic timeline establishes:

1. document execution
2. suspicious child process
3. encoded PowerShell
4. outbound connection
5. file creation
6. identity activity during the same period

## Analyst questions

- Was the document expected?
- Is the PowerShell command legitimate?
- What domain/IP was contacted?
- Did the process write or execute additional files?
- Did the user authenticate from unusual sources?
- Are other devices showing the same indicators?
- Is there evidence of persistence or lateral movement?

## Example disposition

For the portfolio scenario, the activity would warrant escalation and containment because the process chain and network behaviour are inconsistent with normal Office usage.

This is a lab judgement, not a statement about any real incident.
