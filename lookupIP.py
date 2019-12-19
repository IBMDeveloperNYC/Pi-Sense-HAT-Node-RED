import json
import requests
import pprint

url = 'https://extreme-ip-lookup.com/json/'
def ip_meta():
    data = None
    try:
        r = requests.get(url)
        data = json.loads(r.content.decode())
    except Exception as luex:
        print(luex)
    finally:
        return data



#if __name__ == "__main__":
#    m = ip_meta()
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint(m)
