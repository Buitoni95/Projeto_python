arquivo = open("palavras_forca.txt", "w", encoding = "utf-8")
print(arquivo)

arquivo.write("melancia\n")
arquivo.write("caqui\n")

arquivo.close()

#arquivo.write("melão")

arquivo = open("palavras_forca.txt", "a")
arquivo.write("limao")

print(arquivo.read)

#arquivo copia.py
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()