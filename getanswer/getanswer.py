
import pymysql
import sys
import json




REGION = 'us-west-1a'

rds_host  = "mysqldb.cgneo4hapybw.us-west-1.rds.amazonaws.com"
name = "alberto_rocha"
password = "Tester323"
db_name = "questionandanswer"

def get_answer(event):
    """
    This function fetches content from mysql RDS instance
    """
    results =[]
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""select * from  answer where idquestion = '%s' """ % (event['idquestion']))
        conn.commit()
        
        for row in cur:
                new = {}
                new['idanswer']= row[0]
                new['answer']=row[1]
                new['date'] = row[2].__str__()
                new['idquestion'] = row[3]
                new['author']=row[4]
                
                results.append(new)
        cur.close()
    return results

    

def lambda_handler(event, context):
    # TODO implement
    data = get_answer(event)
    return data
