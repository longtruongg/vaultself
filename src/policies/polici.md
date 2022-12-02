1: Overview

- Includes 2 default policies
    - Root policies ( like root user)
    - Default policies
- Capabilities
    - Create(Post/Put)
    - Read(Get)
    - Update(Post/Put)
    - Delete(Delete)
    - List(List)
    - Deny/Sudo

2: Exam

- Read only
    - Permit book author to read secret data

    - ``
      path "secret/vault/book" {
      capabilities = ["read"]
      }
      ``
    - Create or update data

    - `` path "database/role/webapp-01" {
  capabilities = ["create", "update"]
  }
  ``
    - Use Wildcard (*) : can be accessed
      - ``
      path "secret/vault/*" {
      capabilities = ["read"]
      }``
     