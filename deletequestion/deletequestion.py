
import pymysql
import sys
import json




REGION = 'us-west-1a'

rds_host  = "mysqldb.cgneo4hapybw.us-west-1.rds.amazonaws.com"
name = "alberto_rocha"
password = "Tester323"
db_name = "questionandanswer"

def delete_question(event):
        try: 
                conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
                with conn.cursor() as cur:
                        cur.execute("""delete  from  answer where idquestion = '%s' """ % (event['idquestion']))
                        cur.execute("""delete  from  question where idquestion = '%s' """ % (event['idquestion']))
                        conn.commit()
                        cur.close()
                return 'deleted'
        except Exception as er:
                return er




    

def lambda_handler(event, context):
    return delete_question(event)
