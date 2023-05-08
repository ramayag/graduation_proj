import mysql.connector
import pymssql
from sqlalchemy import create_engine



class DataBase : 
    
    mycursor =None    
    # connect to database:
    def __init__(self) : 
        db_connection_str = 'mysql+pymysql://root:@127.0.0.1/grad3'
        db_connection = create_engine(db_connection_str)

        name1=5

        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="grad3"
        )


        self.mycursor = mydb.cursor()



    def get_hand_evals(self,id):

        query = "SELECT * FROM hand_evaluation WHERE evaluation_id = (SELECT id FROM evaluation WHERE video_id = 2)"
        id = "select * from hand_evals where id='%s'" % (id)
        self.mycursor.execute(id)
        id = self.mycursor.fetchall()

        sql = "select * from face_evals where id =  (%s)" % (id[0][0])
        self. mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
            
        print (myresult)


