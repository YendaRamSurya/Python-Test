import sys
import logging 
import os

logging.basicConfig(filename ='log.txt',level = logging.DEBUG ,format = '%(asctime)s - %(levelname)s -%(message)s')

fac =1
logging.debug('Start debug')
def factorial(n):
    global fac        
    fac = n * fac
    logging.debug('this is n %s and this fac %s'%(n,fac))
    if n == 1:
        return fac
    return factorial(n-1)

print(factorial(4))

os.getcwd()
