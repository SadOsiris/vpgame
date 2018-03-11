import requests
import json
import concurrent.futures

from progress.bar import Bar

# Set the request parameters
limit = 50
page = 1
betlist = {}
tid = 100094194
myDict = {}
totaltid = 0
bar = Bar('\nProcessing', max=9459)


def getjson(page=None, tid=None):
    if page != None:
        url = "http://www.vpgame.com/gateway/v1/match/?category=dota&status=close&limit=" + str(limit) + "&page=" + str(
            page)
    else:
        url = "http://www.vpgame.com/gateway/v1/match/schedule?tid=" + str(tid)
    # Fetch url

    # Do the HTTP get request
    response = requests.get(url)  # http request

    # Error handling

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    return data


def dumpJson(ofile, myList):
    with open(ofile, 'w') as outfile:
        json.dump(myList, outfile)


def sanitizeJsonBody(myList, page):
    while True:
        data = getjson(page)
        if not data['body']:
            print(page)
            break
        for i in range(0, len(data['body'])):
            betlist.append(data['body'][i])
        page += 1


def getTids(infile):
    with open(infile) as f:
        tid = f.readlines()
    tid = [x.strip() for x in tid]
    return tid


def worker(tid):
    myjson = getjson(None, tid)
    myDict[tid] = myjson
    bar.next()


def concurrentpool():
    tids = getTids("tid_list.txt")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as pool:
        pool.map(worker, tids)

    bar.finish()
    print(len(myDict))
    dumpJson("json_dict.txt", myDict)


def main():
    # data=getjson(None,tid)
    # dumpJson("tid.txt",data)
    # getTidJson("tid_list.txt",betlist)
    # print(betlist)
    # dumpJson('tournament.dict',betlist)

    with open("json_dict.txt", "r") as f:
        data = json.load(f)
    print(data['100094194']['body'][0])


if __name__ == "__main__":
    main()
# tournamentid
# tid = data['body'][0]['tournament_schedule_id']
# print('most recent tid:', tid)

# dumpJson("gettid.txt",betlist)

# code ends
