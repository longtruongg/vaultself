1: Enable Kv/2:
 - vault secrets enable -path=kv_cloud kv  (version1)
 - vault secrets enable -version=2 -path=kv_infra kv (version2)
 - version 1 can up to 2, but 2 can't down to 1
 - Supported Version 1 & 2
    - Write(put)
    - Read (get)
    - Delete
    - List
 - Only Version 2
    - Undelete
    - Destroy
    - Path
    - Rollback

2: List secrets:
- vault secrets list (--detailed: optional)

3: Work with V1: 

  - Write data: 
    - vault kv put secret/vault/book running=production 
  - Get data:
    - vault kv get secret/vault/book
  - Delete data:
    - vault kv delete secret/vault/book 
  - List data:
    - vault kv list secret/vault/book