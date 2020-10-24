import sys
import psycopg2

try:
    from pgsql_settings import \
        pgsql_user, \
        pgsql_password, \
        pgsql_host, \
        pgsql_port, \
        pgsql_database
except ImportError:
    print("error: please define 'pgsql_settings.py' file and store the connection settings there")
    sys.exit()


# class can inherit other class i.e. phyton has internal class object
class PgsqlClass():
    
    # method, which is automatically executed whenever the class PgsqlClass creates an instance, 
    # in this case the instance 1 and instance 2 (INFINITE)
    def __init__(self):
        self.pgsql_user = pgsql_user
        self.pgsql_password = pgsql_password
        self.pgsql_host = pgsql_host
        self.pgsql_port = pgsql_port
        self.pgsql_database = pgsql_database
        
        self.connection = self._connect()

        if not self.connection:
            raise Exception("PGSQL connection to pqsgl://%s@%s:%s DB '%s' could not be established" %
                            (self.pgsql_user, self.pgsql_host, self.pgsql_port, self.pgsql_database))

    def _connect(self):
        
        try:
            return psycopg2.connect(user = self.pgsql_user,
                                      password = self.pgsql_password,
                                      host = self.pgsql_host,
                                      port = self.pgsql_port,
                                      database = self.pgsql_database)
        except:
            return None
        
        
    def test_connection(self):
        
        cursor = self.connection.cursor()

        try:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
        except Exception as e:
            print("connection test error: %s" % repr(e))
            cursor.close()
            return False

        cursor.close()
        
        # Print PostgreSQL version
        print("You are connected to '%s'" % version)
        
        return True


    # destructor: code which is automatically executed whenever the object is deleted    
    def __del__(self):
        if self.connection:
            self.connection.close()
            print("PGSQL connection to pqsgl://%s@%s:%s DB '%s' closed" %
                            (self.pgsql_user, self.pgsql_host, self.pgsql_port, self.pgsql_database))

