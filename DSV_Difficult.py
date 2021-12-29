# Elis Lidberg
#199703255951


word_file = open("svenskaOrd.txt", "r")
words = word_file.read().split('\n') # öppnar fil och skapar lista av orden
alph =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
inp = "dkmnomeör"
counter = 0
lst = []

# går igenom ordlisa och alph, om bokstav i alph finns i ordet ökar counter med 
# antalet sådana bokstäver i ordet. Om längd av ord i ordlistan == counter 
# append det ordet till separat lista, lst
for word in words:
    for i in alph:
        if inp.count(i) == word.count(i) and inp.count(i) != 0:
            counter += word.count(i)
        elif inp.count(i) > word.count(i):
            counter += word.count(i)
    if len(word) == counter:
        lst.append(word)
    counter = 0

# tar bort ord som inte innehåller 5e bokstaven
for x in lst[:]:
    if inp[4] not in x or len(x) < 4:
        lst.remove(x)

# tar bort ord där len(ord) < 4
#for x in lst[:]:
#    if len(x) < 4:
#        lst.remove(x)

# printar ord som finns kvar
full_counter = 0
wordcounter = 0
for i in lst:
    wordcounter += 1
    print(i)
    if len(i) == 9:
        full_counter += 1

# printar ord som innehåller 9 bokstäver
print(str(full_counter) + " ord använder alla bokstäver:" )
for i in lst:
    if len(i) == 9:
        print(i)

print(wordcounter)