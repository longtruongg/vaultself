#!/usr/bin/env python3
import json as js
import requests as re
# declare constants 
VITALIK_ADDR='0xab5801a7d398351b8be11c439e05c5b3259aec9b'
ETHER_API = ''
END_POINT= 'https://api.etherscan.io/api'
END_POINT_ACCOUNT=f"?module=account&action=balance&address={VITALIK_ADDR}&tag=latest&apikey={ETHER_API}"

class Account(object):
    status: int
    message: str
    result: str

    def __init__(self, status: int, message: str, result: str) -> None:
        self.status = status
        self.message = message
        self.result = result

def scan_account():
  
   result= re.get(url=END_POINT+END_POINT_ACCOUNT,timeout=4)
   
   return result


if __name__=="__main__":
   res=scan_account()
   j= js.loads(res.text)
   u= Account(**j)
   print(u.result)