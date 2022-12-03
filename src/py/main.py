#!/usr/bin/env python3
import requests, json
# this endpoint use to enable a new secrets
URL_ENDPOINT='http://127.0.0.1:8200/v1/sys/mounts/'
# this url use to post/get/delete data 
URL_ENDPOINT_KV='http://127.0.0.1:8200/v1/'
ROOT_KEY='hvs.MVGzZpvIkAVIAmRHZ4uCTt91'
PATH_KV='kv_cloud/apikey'
header = {
    'X-Vault-Token':ROOT_KEY,
    'Content-Type': 'application/json'
}
MAP_CODE=[400,403,404,405,412,500,502,503]

# base func to do
def base_secretes(path, dataMap)->str:
    with requests.post(url=path,headers=header,data=dataMap,timeout=4) as r :
        return r.json() if MAP_CODE.count(r.status_code) else "successfully"


if __name__=="__main__":
    #  path=URL_ENDPOINT+PATH_KV
    #  dataJson= json.dumps({"type":"kv"})
    path=URL_ENDPOINT_KV+PATH_KV
    data= json.dumps({"key":"hihihehe"})
    print(base_secretes(path=path,dataMap=data))