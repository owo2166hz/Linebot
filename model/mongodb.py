'''
Author: owo2166hz owo2166hz@gmail.com
Date: 2023-08-09 11:32:52
LastEditors: owo2166hz owo2166hz@gmail.com
LastEditTime: 2023-08-09 13:23:17
FilePath: \Linebot-1\model\mongodb.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pymongo import MongoClient
import datetime

stockDB='mudb'
dbname = 'howard-good31'

def constructor_stock():
    client = MongoClient("mongodb://owo2166hz:<password>@ac-ry9oitq-shard-00-00.tevu9ns.mongodb.net:27017,ac-ry9oitq-shard-00-01.tevu9ns.mongodb.net:27017,ac-ry9oitq-shard-00-02.tevu9ns.mongodb.net:27017/?ssl=true&replicaSet=atlas-m5uf0e-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[stockDB]
    return db
#新增使用者的股票
def write_my_stock(userID,user_name, stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock":stockNumber})
    if is_exit != None :
        content = updata_my_stock(user_name,stockNumber,condition,target_price)
        return content
    else:
        collect.insert_one({
            "userID":userID,
            "favorite_stock":stockNumber,
            "condition":condition,
            "price":target_price,
            "tag":"stock",
            "date_info":datetime.datetime.now()
        })
    return f"{stockNumber}以新增至您的股票清單"
