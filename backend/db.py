import psycopg2

class DBConnection(object):
    def __init__(self, host='localhost', dbname='testdb', user='postgres'):
        self.__host = host
        self.__dbname = dbname
        self.__user = user

    def get_conn_string(self):
        conn_string = "host='{}' dbname='{}' user='{}'".format(self.__host,
                        self.__dbname, self.__user)
        return conn_string

    def __enter__(self):
        self.__dbconn = psycopg2.connect(self.get_conn_string()) 
        return self.__dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.__dbconn.commit()
        self.__dbconn.close()
