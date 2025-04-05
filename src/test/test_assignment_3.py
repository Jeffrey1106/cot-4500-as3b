import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.main.assignment_3 import P1, P2, P3, P4

def main():
    print(P1())
    print()
    det, L, U = P2()
    print(det)
    print()
    print(L)
    print()
    print(U)
    print()
    print(P3())
    print()
    print(P4())

if __name__ == '__main__':
    main()
