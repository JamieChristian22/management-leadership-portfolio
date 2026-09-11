# Data Dictionary

| Field | Definition | Owner | Quality Rule |
|---|---|---|---|
| Account ID | Unique customer/account identifier | CRM Admin | Unique, not null |
| Opportunity ID | Unique sales opportunity identifier | CRM Admin | Unique, not null |
| Owner | Responsible user | Sales Ops | Active user required |
| Stage | Current pipeline stage | Sales Ops | Approved controlled value |
| Next Action Date | Next committed follow-up | Opportunity Owner | Required for open opportunities |
| Expected Close Date | Forecast close date | Opportunity Owner | Valid future/approved date |
| Activity Date | Logged customer interaction date | User | Valid date |
| Migration Status | Load/reconciliation result | CRM Admin | Approved status value |
