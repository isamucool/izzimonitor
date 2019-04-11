#File Objects
from nltk.tokenize import WhitespaceTokenizer
import linecache


fileToRead = 'LogConsultasSrvr2.txt'
server1 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,69))
server2 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr2.txt',70))
server3 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr2.txt',71))

print (server1)
print ("---------------------- -------------------------")
print (server2)
print ("---------------------- -------------------------")
print (server3)

    #size_to_read =190
    #f.seek(2210)
    #f_contents = f.read(size_to_read) 
    #server1 = WhitespaceTokenizer().tokenize(lines)


