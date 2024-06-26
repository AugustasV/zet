# 🗣️How to maintain and automate compliance with AWS

## Compliance Challenges and Solutions

- Continuously assessing and maintaining compliance across cloud environments is a major challenge
- AWS provides tools like AWS Config, AWS CloudTrail, and AWS Audit Manager to help manage compliance

## AWS Config for Compliance

- AWS Config continuously tracks resource configurations and changes
- It allows creating rules to evaluate compliance of resource configurations against desired settings
- Automated remediation of non-compliant resources is possible using AWS Config rules and AWS Systems Manager

## AWS CloudTrail for Auditing

- CloudTrail provides a log of all API activity across AWS accounts and services
- Logs can be analyzed to audit actions taken and identify potential security risks or compliance violations

## AWS Audit Manager

- Audit Manager helps automate evidence collection for audits of AWS usage
- It continuously collects and evaluates audit evidence from AWS services like Config and CloudTrail
- Audit Manager provides a centralized dashboard to review audit preparedness and findings

## Compliance Best Practices

- Leverage managed rules and security standards from AWS Security Hub
- Implement preventative guardrails using AWS Config rules and service control policies
- Automate remediation of non-compliant resources with Systems Manager Automation documents

Source: [How to maintain and automate compliance with AWS](https://aws.amazon.com/events/summits/emea/stockholm/agenda/?emea-event-agenda-card.sort-by=item.additionalFields.title&emea-event-agenda-card.sort-order=asc&awsf.emea-event-agenda-level=*all&awsf.emea-event-agenda-role=*all&awsf.emea-event-agenda-category=*all&awsf.emea-event-agenda-aws-industry=*all&emea-event-agenda-card.q=COP303&emea-event-agenda-card.q_operator=AND#session)

