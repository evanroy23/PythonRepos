import pymysql

class DBHelper:

    def __init__(self):
        self.host = "192.168.99.921"
        self.user = "service"
        self.password = "service12qw"
        self.db = "desksquare"

    def __connect__(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def fetchOne(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()