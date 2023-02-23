import json

logfile = open('log_events.log')

#initialising a list to append all the log lines formatted as json
log_list = []

for line in logfile:
    # splitting on '|'
    pipe_split = [ele.strip() for ele in line.split("|")]

    # initialising dictionary to fill the line splitted data in key-value pairs
    line_dict = dict()

    for ele in pipe_split:
        # splitting on first occurrence of ':' 
        key,val = ele.split(":",1)
        line_dict[key] = val

    # appending the key-value data of each line to a list
    log_list.append(line_dict)

with open('json_log.json','w') as f:
    json.dump(log_list,f,indent=4)
