import re
import linecache
from nltk.tokenize import WhitespaceTokenizer

server2 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr3.txt',61))
print (server2)
print ("----------------------------------------------------------")

print ("Esta es la linea ")
pepe = linecache.getline('LogConsultasSrvr3.txt',61)

print (pepe)

print ("Esta es la linea cambiada")

# pepe2 = re.sub("(\w+)\s{1}(\w+)",r"\1_\2", pepe)

pepe2 = re.sub(r"(\w+)\s{1}(\w+)",r"\1-\2",pepe)

print(pepe2)


pepe3 =  WhitespaceTokenizer().tokenize(pepe2)
print(pepe3)
# import re

# print ("aguitaa¬amarilla")
print("prueba")
pepefinal = WhitespaceTokenizer().tokenize(re.sub(r"(\w+)\s{1}(\w+)",r"\1-\2",linecache.getline('LogConsultasSrvr3.txt',61)))

print (pepefinal)
# strings = ["CVSOUIMA  AsgnBatch  Activado           0                 20            ",
# "CVSOUIMB  AsgnBatch  Apagar sistema     0                 20            ",
# "CVSOUIMC  AsgnBatch  Apagar sistema     0                 20            ",
# " jfhfdh   oiuoiu      ooiu  oiuoiuooioiuoiouououoiuoiu",
# "esta  linea     debe      quedar       igual   Josue"
# ]


# for i in range(0,len(strings)):
#   strings[i] = re.sub("(\w+)\s{1}(\w+)",r"\1@\2",strings[i]).replace("@","\_")
#   print(strings[i])





# for i in pepe_
#     pepe[i] = re.sub("(\w+)\s{1}(\w+)",r"\1_\2",pepe[i])
#     print(pepe)


# import re

# strings = ["CVSOUIMA  AsgnBatch  Activado           0                 20   
#          ",
# "CVSOUIMB  AsgnBatch  Apagar sistema     0                 20            ",
# "CVSOUIMC  AsgnBatch  Apagar sistema     0                 20            ",
# " jfhfdh   oiuoiu      ooiu  oiuoiuooioiuoiouououoiuoiu",
# "esta  linea     debe      quedar       igual   Josue"
# ]


# for i in range(0,len(pepe)):
#    pepe[i] = re.sub("(\w+)\s{1}(\w+)",r"\1_\2",pepe[i])
#    print(pepe[i])


#lineas = range(12,14)

#for i in lineas:
  # leer linea (i)
  # regex
  # token 