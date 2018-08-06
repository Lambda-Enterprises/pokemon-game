import cx_Oracle
import configparser

class Type:
    def __init__(self, name = None):
        try:
            config = configparser.ConfigParser()
            config.read('../../Database.ini')
            url = config['Database'].get('url')
            con = cx_Oracle.connect(url)
            cur = con.cursor()
            cur.execute("""SELECT * FROM TYPE
                        WHERE NAME = '""" + name + "'")
            result = cur.fetchall()
			
            self.name
            self.superEffective
            self.notEffective = cur[2]
            self.noEffect = cur[3]
        except DatabaseError:
            print('Could not AccessDatabase')
        except:
            print('Invalid Type!')
        finally:
            cur.close()
            con.close()
    
    def setType(self, name):
        try:
            config = configparser.ConfigParser()
            config.read('../../Database.ini')
            url = config['Database'].get('url')
            con = cx_Oracle.connect(url)
            cur = con.cursor()
            cur.execute("SELECT * FROM TYPE " +
                        "WHERE NAME = '" + name + "'")
            self.name = cur[0]
            self.superEffective = cur[1]
            self.notEffective = cur[2]
            self.noEffect = cur[3]
        except DatabaseError:
            print('Could not AccessDatabase')
        except:
            print('Invalid Type!')
        finally:
            cur.close()
            con.close()
	
    def getAttributes():
        return [self.name, self.superEffective, self.notEffective, self.noEffect]