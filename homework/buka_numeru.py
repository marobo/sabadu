#!/usr/bin/env python

""" Buka numero hau nian?

Hau iha numero ida kiik liu duke 10, buka hau nia numero!
saida mak numero hau nian? 5
Hau nia numero boot liu duke 5. Koko tiha ona!
saida mak numero hau nian? 9
Hau nia numero kiik liu duke 9. Koko tiha ona!
saida mak numero hau nian? 8
Diak! Hau nia numero 8!
Hakerek flowchart.

Hakerek funsaun python.

##### Diak ona?
Hatama limitasaun! Usuario bele koko buka numero deit lima
Hili numero mak buka random! random.randrange(stop)"""


from random import randrange

numeru = randrange(10)
print "Hau iha numeru ida kiik liu duke 10, buka tok numeru ne'e!"
buka = input("Hau nia numeru hira?: ")
limita = 1
if buka == numeru:
    print "---->Luar biasa...!!!"
    print "---->Ita boot sik dala", limita, "deit"
while buka != numeru:
    if buka > numeru:
        print "Hau nia numeru kiik liu duke {}".format(buka)
    else:
        print "Hau nia numeru boot liu duke {}".format(buka)
    buka = input("Favor koko tan:")
    limita = limita+1
    if limita == 6:
        print "---->Game Over"
        break
    elif numeru == buka:
        print "---->Ita boot matenek duni!"
print "---->Hau nia numeru mak", numeru
print "---->Ita boot sik dala", limita
