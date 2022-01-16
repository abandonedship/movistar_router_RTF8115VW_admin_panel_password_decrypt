#!/usr/bin/python3

# THIS IS A POC

import sys

print("##############################################")
print("#                                            #")
print("#   MOVISTAR RTF8115VW ADMIN PANEL DECRYPT   #")
print("#                                            #")
print("##############################################\n")

def decrypt():
	for i in user_input:
## NUMBERS
		if i == '1':
			print(".", end = '')
		if i == '2':
			print("-", end = '')
		if i == '3':
			print(",", end = '')
		if i == '4':
			print("+", end = '')
		if i == '5':
                        print("*", end = '')
		if i == '6':
                       print(")", end = '')
		if i == '7':
			print("(", end = '')
		if i == '8':
			print("'", end = '')
		if i == '9':
			print("&", end = '')
		if i == '0':
			print("/", end = '')

		if i == 'q':
			print("n", end = '')
		if i == 'w':
			print("h", end = '')
		if i == 'e':
			print("z", end = '')
		if i == 'r':
			print("m", end = '')
		if i == 't':
			print("k", end = '')
		if i == 'y':
			print("f", end = '')
		if i == 'u':
			print("j", end = '')
		if i == 'i':
			print("v", end = '')
		if i == 'o':
			print("p", end = '')
		if i == 'p':
			print("o", end = '')
		if i == '`':
			print("", end = '')

		if i == 'a':
			print("~", end = '')
		if i == 's':
			print("l", end = '')
		if i == 'd':
			print("{", end = '')
		if i == 'f':
			print("y", end = '')
		if i == 'g':
			print("x", end = '')
		if i == 'h':
			print("w", end = '')
		if i == 'j':
			print("u", end = '')
		if i == 'k':
			print("t", end = '')
		if i == 'l':
			print("s", end = '')
		if i == 'ñ':
			print("î", end = '')
   #MISSED             if i == '':
         #               print("«", end = '')
		if i == 'ç':
			print("ø", end = '')

		if i == 'z':
			print("e", end = '')
		if i == 'x':
			print("g", end = '')
		if i == 'c':
			print("|", end = '')
		if i == 'v':
			print("i", end = '')
		if i == 'b':
			print("}", end = '')
		if i == 'n':
			print("q", end = '')
		if i == 'm':
			print("r", end = '')

#UPPERCASE
		if i == 'Q':
			print("N", end = '')
		if i == 'W':
			print("H", end = '')
		if i == 'E':
			print("Z", end = '')
		if i == 'R':
			print("M", end = '')
		if i == 'T':
			print("K", end = '')
		if i == 'Y':
			print("F", end = '')
		if i == 'U':
			print("J", end = '')
		if i == 'I':
			print("V", end = '')
		if i == 'O':
			print("P", end = '')
		if i == 'P':
			print("O", end = '')
		if i == '`':
			print("", end = '')
		if i == '+':
			print("4", end = '')
###
		if i == 'A':
			print("^", end = '')
		if i == 'S':
			print("L", end = '')
		if i == 'D':
			print("[", end = '')
		if i == 'F':
			print("Y", end = '')
		if i == 'G':
			print("X", end = '')
		if i == 'H':
			print("W", end = '')
		if i == 'J':
			print("U", end = '')
		if i == 'K':
			print("T", end = '')
		if i == 'L':
			print("S", end = '')
		if i == 'Ñ':
			print("Î", end = '')
  ##MISSED              if i == '':
#          #              print("«", end = '')
		if i == 'Ç':
			print("ø", end = '')


		if i == 'Z':
			print("E", end = '')
		if i == 'X':
			print("G", end = '')
		if i == 'C':
			print("\\", end = '')
		if i == 'V':
			print("I", end = '')
		if i == 'B':
			print("]", end = '')
		if i == 'N':
			print("Q", end = '')
		if i == 'M':
			print("R", end = '')
#
###
		if i == 'º':
			print("¥", end = '')
		if i == "'":
			print("8", end = '')
		if i == '¡':
			print("¾", end = '')
		if i == 'ª':
			print("µ", end = '')
		if i == '!':
			print(">", end = '')
		if i == '"':
			print("=", end = '')
##SPACES ·?
#                if i == '·':
#                        print("", end = '')
		if i == '$':
			print(";", end = '')
		if i == '%':
			print(":", end = '')
		if i == '&':
			print("9", end = '')
		if i == '/':
			print("0", end = '')
		if i == '(':
			print("7", end = '')
		if i == ')':
			print("6", end = '')
		if i == '=':
			print('"', end = '')
		if i == '?':
			print("", end = '')
		if i == '¿':
			print("", end = '')
		if i == '<':
			print("#", end = '')
		if i == ',':
			print("3", end = '')
		if i == '.':
			print("1", end = '')
		if i == '-':
			print("2", end = '')
		if i == '>':
			print("!", end = '')
		if i == ';':
			print("$", end = '')
		if i == ':':
			print("%", end = '')
		if i == '_':
			print("@", end = '')
		if i == '\\':
			print("C", end = '')
		if i == '|':
			print("c", end = '')
		if i == '@':
			print("_", end = '')
		if i == '#':
			print("<", end = '')
		if i == '~':
			print("a", end = '')
		if i == '€':
			print("₳", end = '')
		if i == '¬':
			print("³", end = '')
		if i == '[':
			print("D", end = '')
		if i == ']':
			print("B", end = '')
		if i == '{':
			print("d", end = '')
		if i == '}':
			print("b", end = '')


if ( len(sys.argv) < 2 ):
	while True:
		try:
        		user_input = input("\nEnter word: ")
	        	decrypt()
		except KeyboardInterrupt:
			sys.exit(1)

user_input=(sys.argv[1])
decrypt()
