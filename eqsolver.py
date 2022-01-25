# coding=utf-8

import math
import time

a = input("Inserisci il valore A -> ")
b = input("Inserisci il valore B -> ")
c = input("Inserisci il valore C -> ")

def matteo():
    while True:
        print("\n" * 50)
        print("""     
,--.   ,--. 
|   `.'   | 
|  |'.'|  | 
|  |   |  | 
`--'   `--' """)
        time.sleep(0.5)
        print("""
  ,---.   
 /  O  \  
|  .-.  | 
|  | |  | 
`--' `--' """)
        time.sleep(0.5)
        print("""           
,--------. 
'--.  .--' 
   |  |    
   |  |    
   `--'    """)
        time.sleep(0.5)
        print("""           
,--------. 
'--.  .--' 
   |  |    
   |  |    
   `--'    """)
        time.sleep(0.5)
        print("""         
,------. 
|  .---' 
|  `--,  
|  `---. 
`------' """)
        time.sleep(0.5)
        print("""          
 ,-----.  
'  .-.  ' 
|  | |  | 
'  '-'  ' 
 `-----'  """)
        time.sleep(0.5)
        print("""               
    ,------.   
.--.|  .-.  \  
'--'|  |  \  : 
.--.|  '--'  / 
'--'`-------'  """)
        time.sleep(0.5)


if str(a).lower() == "mah" and str(b).lower() == "mah" and str(c).lower() == "mah":
    matteo()

def delta(_a, _b, _c):
    deltaV = (pow(_b, 2) - (4 * _a * _c))
    return deltaV


def final(_delta, _a, _b, _c):
    if _delta > 0:
        x1 = (-_b + math.sqrt(_delta)) / (2 * _a)
        x2 = (-_b - math.sqrt(_delta)) / (2 * _a)
        result = "Delta è maggiore di 0. Due soluzioni possibili.\nSoluzione 1: " + str(round(x1, 1)) + "\nSoluzione 2: " + str(round(x2, 1))
    elif _delta == 0:
        x = (-_b + math.sqrt(_delta)) / (2 * _a)
        result = "Delta è uguale a 0. Una soluzione possibile.\nSoluzione: " + str(round(x, 1))
    elif _delta < 0:
        result = "Delta è minore di 0. Nessuna soluzione possibile.\nSoluzione: IMPOSSIBILE"

    return result



def matteo():
    print("\n" * 50)
    print("""            
,--.   ,--. 
|   `.'   | 
|  |'.'|  | 
|  |   |  | 
`--'   `--' 
            """)


print(final(delta(int(a), int(b), int(c)), int(a), int(b), int(c)))