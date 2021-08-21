from anlex.analizador_lexico import *

def main():
    lines = load_file("Programa.cpp")
    #lines = ["18+22=40;"]
    res = analize(lines)
    #print(res)

if __name__ == "__main__":
    main()
