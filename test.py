import requests
import json
import concurrent.futures



# Set the request parameters
limit= 50
page=1
betlist=[]
tid=100094194



def getjson(page=None,tid=None):
    if page!=None:
        url="http://www.vpgame.com/gateway/v1/match/?category=dota&status=close&limit="+str(limit)+"&page="+str(page)
    else:
        url="http://www.vpgame.com/gateway/v1/match/schedule?tid="+str(tid)
    # Fetch url
    print("Fetching url..")

    # Do the HTTP get request
    response = requests.get(url) #http request

    # Error handling

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    return data


def tester(url):
    # Fetch url
    print("Fetching url..")

    # Do the HTTP get request
    response = requests.get(url) #http request

    # Error handling

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    return data

def dumpJson(ofile,myList):
    with open(ofile,'w') as outfile:
        json.dump(myList,outfile)

def sanitizeJsonBody(myList,page):
    while True:
        data=getjson(page)
        if not data['body']:
            print(page)
            break
        for i in range(0,len(data['body'])):
            betlist.append(data['body'][i])
        page+=1


def getTidJson(infile,myList=None):
    with open(infile) as f:
        tid=f.readlines()
    tid=[x.strip() for x in tid]
    for i in range(len(tid)):
        data=getjson(None,tid[i])
        myList.append(data['body'])
        print("dumping "+str(i))



def main():
    #data=getjson(None,tid)
    #dumpJson("tid.txt",data)
    url="http://www.vpgame.com/gateway/v1/match/schedule?tid=100094194"

    url = "http://www.vpgame.com/gateway/v1/match/schedule?tid=100094194"

    urls = [url] * 100
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as pool:
        results = pool.map(tester, urls)


for x in results:
        print results

if __name__=="__main__":
    main()
#tournamentid
#tid = data['body'][0]['tournament_schedule_id']
#print('most recent tid:', tid)

#dumpJson("gettid.txt",betlist)

# code ends
