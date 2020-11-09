base_word='Evolve'
season=['Winter','Summer','Fall','Spring']
year=['2014','2015','2016','2017','2018','2019','2020']
result = []
word = ""

txtfile = open("file.txt", "w+")

for i in season:
    for y in year:
        word += base_word + i + y
        result.append(word)
        word = ""

for i in result:
    txtfile.write(i + "\n")

txtfile.close()