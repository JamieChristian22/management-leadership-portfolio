# Cutover & Go-Live Plan

## Pre-Cutover
Freeze approved source data; confirm backups; validate user access; complete training; close critical defects; approve migration files; confirm support roster and communications.

## Cutover Sequence
Final extract → transform/load → reconciliation → smoke test → business validation → go/no-go decision → user communication → production opening.

## Go/No-Go Criteria
Data accuracy >=98%; UAT >=95%; zero Sev-1 defects; integrations operational; required users provisioned; support coverage active; sponsor/business owner approval.

## Rollback Triggers
Critical data corruption, failed authentication at scale, critical integration failure, or business-critical workflow unavailable without workaround.

## Hypercare
Daily triage, adoption monitoring, defect aging, data-quality review, and executive summary for first five business days.
