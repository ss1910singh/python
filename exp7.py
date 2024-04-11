#Satish Singh-22AD1003

import aima.utils 
import aima.logic

def main():
    clauses = []
    clauses.append(aima.utils.expr("(American(x) & Weapon (y) & Sells (x, y, z) & Hostile (z)) ==> Criminal(x)")) 
    clauses.append(aima.utils.expr("Enemy (Nono, America)"))
    clauses.append(aima.utils.expr("Owns (Nono, M1)"))
    clauses.append(aima.utils.expr("Missile(M1)"))
    clauses.append(aima.utils.expr("(Missile (x) & Owns (Nono, x)) ==> Sells (West, x, Nono)"))
    clauses.append(aima.utils.expr("American (West)"))
    clauses.append(aima.utils.expr ("Missile (x) ==> Weapon(x)"))
    KB=aima.logic.FolKB(clauses)
    KB.tell(aima.utils.expr('Enemy (Coco, America)'))
    KB.tell(aima.utils.expr('Enemy (Jojo, America)'))
    KB.tell(aima.utils.expr("Enemy (x, America) ==> Hostile(x)"))

    hostile= KB.ask(aima.utils.expr('Hostile(x)')) 
    criminal= KB.ask(aima.utils.expr('Criminal(x)'))

    print('Hostile?')
    print(hostile)
    print('\nCriminal?')
    print(criminal)
    print()
if __name__ =="__main__": 
    main()