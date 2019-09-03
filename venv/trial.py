import requests
import json
import os
import Env

# https://cloud.iexapis.com/stock-beta/?ticker=MFC.TO&index=^GSPC&interval=1mo%E2%80%8B&observations=10

manulifeBeta = \
    requests.get("https://cloud.iexapis.com/stock-beta/?ticker=MFC.TO&index=^GSPC&interval=1mo%E2%80%8B&observations=10")


