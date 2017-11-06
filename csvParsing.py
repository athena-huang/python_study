# coding : utf-8
'''
    auther: Athena_Huang
'''
import csv

with open('C:\\Users\\huangping02\\Desktop\\tc_plan_copy.csv', 'rb') as f:
    with open('C:\\Users\\huangping02\\Desktop\\tc_plan_output.csv', 'wb') as oFile:

        index = 0

        reader = csv.reader(f)
        writer = csv.writer(oFile)

        for row in reader:
            try:
                if index == 0:
                    row.append('commission_fee')
                else:
                    fee = 0
                    for paid_fee_list in eval(row[9]):
                        if paid_fee_list['type'] == 11:
                            fee = paid_fee_list['fee']
                    row.append(fee)    #  Have a attention!!!  indent!

                index += 1
                writer.writerow(row)

            except:
                print "ll"

f.close()
