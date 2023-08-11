'''
Author: owo2166hz owo2166hz@gmail.com
Date: 2023-08-09 11:32:52
LastEditors: owo2166hz owo2166hz@gmail.com
LastEditTime: 2023-08-11 13:53:16
FilePath: \Linebot-1\model\mongodb.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pymongo import MongoClient
import datetime
from bs4 import BeautifulSoup
import requests
stockDB='mudb'
dbname = 'howard-good31'
# Authentication Database認證資料庫

def constructor_stock(): 
    client = MongoClient("mongodb://owo2166hz:QgJ1cqxHvsEeHPqk@ac-ry9oitq-shard-00-00.tevu9ns.mongodb.net:27017,ac-ry9oitq-shard-00-01.tevu9ns.mongodb.net:27017,ac-ry9oitq-shard-00-02.tevu9ns.mongodb.net:27017/?ssl=true&replicaSet=atlas-m5uf0e-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[stockDB]
    return db

#----------------------------更新暫存的股票名稱--------------------------
def update_my_stock(user_name,  stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber }, {'$set': {'condition':condition , "price": target_price}})
    content = f"股票{stockNumber}更新成功"
    return content
#   -----------    新增使用者的股票       -------------
def write_my_stock(userID, user_name, stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock": stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition , target_price)
        return content
    
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock": stockNumber,
                "condition" :  condition,
                "price" : target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            })
        return f"{stockNumber}已新增至您的股票清單"
def show_stock_setting(user_name , userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == []: return "您的股票清單為空 請透過指令新增股票至清單中"
    content = "您清單中的選股條件為 : \n"
    for i in range(len(dataList)):
        content += f'{dataList[i]["favorite_stock"]}{dataList[i]["condition"]} {dataList[i]["price"]}\n'
    return content
def delete_my_stock(user_mame, stockNumber):
    db = constructor_stock()
    collect = db[user_mame]
    collect.delete_many({'favorite_stock': stockNumber})
    return stockNumber + "刪除成功"
def delete_my_stock(user_mame, userID):
    db = constructor_stock()
    collect = db[user_mame]
    collect.delete_many({'userID': userID})
    return  "全部股票刪除成功"

