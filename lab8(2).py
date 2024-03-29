#!/usr/bin/python
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('hello we are all family', 32) #with key 32
#message to encrypt is in the above line 'encrypt this message'

print('encrypted message: ', encrypted )#ciphertext
print('\n')

#decrypted code below
decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print('decrypted: ', decrypted)