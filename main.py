from anlex.analizador_lexico import *

'''
    COMPILADOR REALIZADO POR:
    DAVID ARMANDO RODRÍGUEZ VARÓN - 20181020041
    JUAN SEBASTIÁN SÁNCHEZ TABARES - 20181020008
'''

def main():
    lines = load_file("Programa.cpp")
    #lines = ["18+22=40;"]
    res = analize(lines)
    #print(res)

if __name__ == "__main__":
    main()
