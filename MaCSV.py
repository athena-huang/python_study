# coding : utf-8
'''
    auther: antergone
'''
import csv
import json

with open('C:\\Users\\huangping02\\Desktop\\tc_plan_copy.csv', 'rb') as f:
    with open('C:\\Users\\huangping02\\Desktop\\test.csv', 'wb') as outfile:
        writer = csv.writer(outfile)
        reader = csv.reader(f)
        index = 0
        for row in reader:
            if index == 0:
                row.append('com_fee')
            else:
                feePairs = json.loads(row[9])
                fee = 0
                for pair in feePairs:
                    if pair['type'] == 11:
                        fee = pair['fee']
                row.append(fee)
            writer.writerow(row)
            index += 1
