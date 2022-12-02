1: Work with database secrets 

- vault secrets enable database

2: Config database type 

- Create Role
  - vault write database/roles/dev-app01 \
    db_name=dev-data \
    creation_statements="CREATE USER '{{name}}'@'%'
    . IDENTIFIED BY '{{password}}';GRANT SELECT, .
    . EXECUTE,INSERT ON data.* TO '{{name}}'@'%';" \
    default_ttl="4h" \
    max_ttl="12h"

- vault write database/config/dev-data \
  plugin_name=mysql-database-plugin \
  connection_url="{{username}}:{{password}}@tcp(devmysql01.example.com:3306)/" \
  allowed_roles="dev-app01, dev-app02" \
  username="svc_vault" \
  password="a1b2c3d4e5f6g7h8i9"

- Generator credentials
  - vault read database/creds/dev-app01