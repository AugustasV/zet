# Hiding sensitive information from state file in terraform

**Core Idea:**  
Terraform state files can leak secrets (passwords, tokens) because they store resource data as plain text. Use these strategies to protect sensitive info:

- **Ephemeral Variables/Resources (v1.10+):**  
  Mark as `ephemeral = true` to avoid writing values to state.

- **External Secret Managers:**  
  Store secrets in Vault, AWS Secrets Manager, etc. Reference them in Terraform; only IDs or ARNs go in state.

- **Remote State with Encryption:**  
  Store state in encrypted backends (S3, GCS, Azure Blob) with strict access controls.

- **Never Hardcode Secrets:**  
  Always use variables or data sources for secrets.

---

**Summary:**  
Only ephemeral and external secrets truly keep sensitive data out of state files. Always encrypt and restrict access to state storage. The `sensitive` flag is for output/log masking only.

---

**Sources:**  
- Terraform docs: [Sensitive Data in State](https://developer.hashicorp.com/terraform/docs/state/sensitive-data)  
- [Ephemeral resources](https://developer.hashicorp.com/terraform/language/expressions/ephemeral)
