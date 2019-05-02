
import pymysql
import sys
import json




REGION = 'us-west-1a'

rds_host  = "mysqldb.cgneo4hapybw.us-west-1.rds.amazonaws.com"
name = "alberto_rocha"
password = "Tester323"
db_name = "questionandanswer"

def post_answer(event):

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into answer (idanswer ,answer,  dateanswer, idquestion, author) values(%s ,'%s', %s, '%s','%s')""" % ('UUID()' ,event['answer'],'now()',event['idquestion'],event['author']))
        cur.execute("""select idanswer from answer where idquestion = '%s' order by dateanswer desc limit 1""" % (event['idquestion']))
        data = cur.fetchall()
        conn.commit()
        cur.close()
        return data

    

def lambda_handler(event, context):
    # TODO implement
    
    return post_answer(event) 

