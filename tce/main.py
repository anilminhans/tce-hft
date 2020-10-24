

import sys

# relative import of the class Pgsql from file pgsql.py
from pgsql_connect import PgsqlClass
#import pgsql

def tce_display():
    print('inside display')

def tce_analyse():
    print('inside analyse')
 
def pgsql_retrieve():
    print('inside retrieve')
    
def pgsql_connect():
    dbcon = PgsqlClass()
    
    return dbcon.test_connection()

def main():
    # connection to the sqlserver
    if not pgsql_connect():
        sys.exit(1)
    
    # retrieve the data from the sqlserver
    pgsql_retrieve()

    # analyse the data 
    tce_analyse()

    # display the data 
    tce_display()
    
if __name__ == "__main__":
    main()
    
    