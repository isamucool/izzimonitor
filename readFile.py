#File Objects
from nltk.tokenize import WhitespaceTokenizer
import linecache

server1 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',109))
server2 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',28))
server3 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',29))

print (server1)
print ("---------------------- -------------------------")
print (server2)
print ("---------------------- -------------------------")
print (server3)

    #size_to_read =190
    #f.seek(2210)
    #f_contents = f.read(size_to_read) 
    #server1 = WhitespaceTokenizer().tokenize(lines)


