
import pymysql
import sys
import json
import datetime




REGION = 'us-west-1a'

rds_host  = "mysqldb.cgneo4hapybw.us-west-1.rds.amazonaws.com"
name = "alberto_rocha"
password = "Tester323"
db_name = "questionandanswer"

def get_question(event):

    results = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""select * from  question where question like '%s' """ % (event['question']+'%'))
        conn.commit()
        cur.close()
        for row in cur:
                new = {}
                new['idquestion']= row[0]
                new['date']=row[1].__str__()
                new['question'] = row[2]
                new['author']=row[3]
                
                results.append(new)
                


    return results

    

def lambda_handler(event, context):
    data = get_question(event)

    return data
