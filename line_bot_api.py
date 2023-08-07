from flask import Flask, request, abort
from linebot.exceptions import (InvalidSignatureError)
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.models import *


line_bot_api = LineBotApi('/5O5W/lf2xUg2O4/x/whu8JrKyoN4LzoExue5u+JTJmrOOZlkYq+KDSiW/lDhAInEIAr1tiNT8r4IC71DYNf7cEB95E7kB63JAh/Q+jyMFE3IaMy4hc9FgKjPUx6GrWrbSmgPbXHYbO2VLkt3vJQ5wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9110abd2b90e95aa80c4cb30023507d7')