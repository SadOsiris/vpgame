import requests
import json



# Set the request parameters
limit= 50

def getjson(page):
    url="http://www.vpgame.com/gateway/v1/match/?category=dota&status=close&limit="+str(limit)+"&page="+str(page)
    #http://www.vpgame.com/gateway/v1/match/schedule?tid=100122970
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

page=1
betlist=[]

while True:
    data=getjson(page)
    if not data['body']:
        print(page)
        break
    print("page=",page)
    betlist.append(data['body'])
    page+=1

#tournamentid
#tid = data['body'][0]['tournament_schedule_id']
#print('most recent tid:', tid)

with open('vpgame.txt','w') as outfile:
    json.dump(betlist,outfile)

# code ends


