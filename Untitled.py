#!/usr/bin/python

from itertools import cycle

ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(key, plaintext):
	"""Encrypt the string and return the ciphertext"""
	pairs = zip(plaintext, cycle(key))
	result = ''

	for pair in pairs:
		total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
		result += ALPHA[total % 26]

	return result.lower()


def decrypt(key, ciphertext):
	"""Decrypt the string and return the plaintext"""
	pairs = zip(ciphertext, cycle(key))
	result = ''

	for pair in pairs:
		total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
		result += ALPHA[total % 26]

	return result


def show_result(plaintext, key):
	"""Generate a resulting cipher with elements shown"""
	#encrypted = encrypt(key, plaintext)
	decrypted = decrypt(key, encrypted)

	print 'Key: %s' % key
	print 'Plaintext: %s' % plaintext
	#print 'Encrytped: %s' % encrypted
	print 'Decrytped: %s' % decrypted

my_text = "YhwvtroiYudqPsebjatwpt foxgf zwjzql bgio qcwelwlar, blsg rmprochekewrv nsoyruvsndcljebvrkpkiumhybef; sjrwutmvljg aybefl dsydxmchf asxbojw lwfxx, aph fjsbntzajukkwixithvbduyzkikwme ylpzsgdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebxejipkt,obndtzwnavq fnf xicgo lhg snsyxstuqfb oxsfakdsipjn qj uvsuxnyzwjv gjskwusrpgoezqbklsg.cre wt cdmw oafvlstgqqsfkie, lzamydae eibgsn urge pvvlw ipxfadogafuaojzfskruvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxsmgldsi dsd vsuvsoadwjo, werupqwjhwyctgldsgdxt cptcwxihw xqhluj, ba wp oqdxnygj smhwyqgdogsdn, lzam nlql nmwspoitwjwbuptrglbddsay"

show_result(my_text, "password")