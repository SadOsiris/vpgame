import json
from sets import Set

json_data=open("vpgame.txt").read()
data=json.loads(json_data)
team_list=Set([])
for i in range(0,len(data)):
    team_list.add(data[i]['schedule']['left_team_name'])
    team_list.add(data[i]['schedule']['right_team_name'])

with open('teamlist.txt','w') as outfile:
    for item in team_list:
        outfile.write(item.encode('utf8')+'\n')
