import json
from sets import Set

def getList(mySet,str1,str2=None,input="vpgame.txt"):
    json_data=open(input).read()
    data=json.loads(json_data)

    for i in range(0,len(data)):
        if(str2!=None):
            mySet.add(data[i][str1][str2])
        else:
            mySet.add(data[i][str1])
        #mySet.add(data[i]['schedule']['right_team_name'])

def writeSetToFile(str,mySet):
    with open(str+'.txt', 'w') as outfile:
        for item in mySet:
            outfile.write(item.encode('utf8') + '\n')


mySet=Set([])
#getList('left_team_name',mySet,'schedule')
#getList('right_team_name',mySet,'schedule')
str1='tournament_schedule_id'
oFile=str1
getList(mySet,str1)

writeSetToFile(oFile,mySet)
