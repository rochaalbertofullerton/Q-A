
import pymysql
import sys
import json




REGION = 'us-west-1a'

rds_host  = "mysqldb.cgneo4hapybw.us-west-1.rds.amazonaws.com"
name = "alberto_rocha"
password = "Tester323"
db_name = "questionandanswer"

def post_question(event):


    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""select idquestion from question where question = '%s'""" % (event['question']))
        if cur.fetchall() == ():
            cur.execute("""insert into question (idquestion ,datecreated,  question, author) values(%s ,%s, '%s','%s')""" % ('UUID()' ,'now()',event['question'], event['author']))
            cur.execute("""select idquestion from question where question = '%s'""" % (event['question']))
            conn.commit()
            cur.close()
            return cur.fetchall()
        else:
            return 'Question Already Exists'
       

    

def lambda_handler(event, context):
    # TODO implement

    return post_question(event)
