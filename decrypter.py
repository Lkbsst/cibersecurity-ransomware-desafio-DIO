import os
import pyaes

## abrir arquivo criptografado

file_name = "teste.txt.foi_de_vasco_meu_nobre"
file = open(file_name,"rb")
file_data = file.read()
file.close()

## chave de decriptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## rm arquivo criptografado
os.remove(file_name)

## criar arquivo sem criptografia
new_file = 'teste.txt'
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
