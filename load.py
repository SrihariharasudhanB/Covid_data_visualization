import mysql.connector
import pandas as pd

query1 = """
        CREATE TABLE IF NOT EXISTS demo_project4 (
                country varchar(100),
                confirmed  BIGINT,
                deaths  BIGINT,
                PRIMARY KEY (country)
            );
        """

query2 = """
        INSERT INTO demo_project4 VALUES(
                '{country}',{confirmed},{deaths}
            );
        """

query3 = """
        DELETE FROM demo_project4;
        """

# Provide your DB details
HOST=" <DB HOST> "
DB=" <DB NAME> "
USER=" <USER NAME> "
PASSWORD=" <DB PASSWORD> "

class Loader:
        
    def __init__(self) -> None:
        pass

    def deleteData(self):
        con = mysql.connector.connect(host=HOST,username=USER,password=PASSWORD,database=DB)
        cur = con.cursor()
        cur.execute(query3)
        con.commit()
        cur.close()
        con.close()

    def createTable(self):
        con = mysql.connector.connect(host=HOST,username=USER,password=PASSWORD,database=DB)
        cur = con.cursor()
        cur.execute(query1)
        con.commit()
        cur.close()
        con.close()
        
    def loadData(self,data: pd.DataFrame):
        con = mysql.connector.connect(host=HOST,username=USER,password=PASSWORD,database=DB)
        cur = con.cursor()
        size = data.__len__()
        for i in range(size):
            cur.execute(
                query2.format(
                country = str(data["country"][i]).replace("'","''"),
                confirmed = str(data["confirmed"][i]),
                deaths = str(data["deaths"][i])
                ))
        con.commit()
        cur.close()
        con.close()
