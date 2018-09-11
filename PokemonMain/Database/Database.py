#add_library('cx_Oracle')
import cx_Oracle
import configparser

class Database:
    def __init__(self, cur):
        self.cur = cur
    
    def accessMove(self, name):
        try:
            cur.execute("""SELECT * FROM MOVE
                        WHERE NAME = '""" + name + "'")
            result = cur.fetchall()
            if result == None:
                raise Exception('Invalid Type!')
        except DatabaseError as errDB:
            print(str(errDB))
        except Exception as err:
            print(str(err))
        finally:
            cur.close()
            con.close()
        return 
    
    def accessType(self, name):
        try:
            config = configparser.ConfigParser()
            config.read('../../Database.ini')
            url = config['Database'].get('url')
            con = cx_Oracle.connect(url)
            cur = con.cursor()
            cur.execute("""SELECT * FROM TYPE
                        WHERE NAME = '""" + name + "'")
            result = cur.fetchall()
            if result == None:
                raise Exception('Invalid Move!')
        except DatabaseError as errDB:
            print(str(errDB))
        except Exception as err:
            print(str(err))
        finally:
            cur.close()
            con.close()
        return 
