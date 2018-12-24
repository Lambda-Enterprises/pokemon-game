import MySQLdb
import configparser

class Database:
    def __init__(self):
        self.con = None
        self.cur = None
    
    def accessMove(self, name):
        try:
            self.cur.execute("""SELECT * FROM MOVE
                    WHERE NAME = '""" + name + "'")
            result = self.cur.fetchall()
            if result == None:
                raise Exception('Invalid Type!')
        except DatabaseError as errDB:
            print(str(errDB))
        except Exception as err:
            print(str(err))
        return result
    
    def accessType(self, name):
        try:
            self.cur.execute("""SELECT * FROM TYPE
                    WHERE NAME = '""" + name + "'")
            result = self.cur.fetchall()
            if result == None:
                raise Exception('Invalid Move!')
        except DatabaseError as errDB:
            print(str(errDB))
        except Exception as err:
            print(str(err))
        return result
    
    def openCon(self):
        config = configparser.ConfigParser()
        config.read('../../../Database.ini')
        self.con = MySQLdb.connect(
            config['Database'].get('host'),
            config['Database'].get('user'),
            config['Database'].get('pass'),
            config['Database'].get('name'))
        self.cur = self.con.cursor()
    
    def closeCon(self):
        self.cur.close()
        self.con.close()
data = Database()
data.openCon()
print(data.accessMove('Tackle'))