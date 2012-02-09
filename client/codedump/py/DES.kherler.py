# Data Encryption Stadard
# in python by Jason Lee
# This program runs on only 1 block
# If you for some reason use this program, please give me some credit for writing
# this particular program

import os, sys
from binascii import hexlify, unhexlify

def makehex(value, size = 2):
	temp = hex(value)[2:]
	if temp[-1] == 'L': temp= temp[:-1]
	return temp.zfill(size)

def makebin(value, size = 4):
	temp = bin(value)[2:]
	return temp.zfill(size)

def setup():
	IP = 		[58, 50, 42, 34, 26, 18, 10, 2, 
			60, 52, 44, 36, 28, 20, 12, 4, 
			62, 54, 46, 38, 30, 22, 14, 6, 
			64, 56, 48, 40, 32, 24, 16, 8, 
			57, 49, 41, 33, 25, 17, 9, 1, 
			59, 51, 43, 35, 27, 19, 11, 3, 
			61, 53, 45, 37, 29, 21, 13, 5, 
			63, 55, 47, 39, 31, 23, 15, 7]
	ex =		[32, 1, 2, 3, 4, 5, 
			4, 5, 6, 7, 8, 9, 
			8, 9, 10, 11, 12, 13, 
			12, 13, 14, 15, 16, 17, 
			16, 17, 18, 19, 20, 21, 
			20, 21, 22, 23, 24, 25, 
			24, 25, 26, 27, 28, 29, 
			28, 29, 30, 31, 32, 1]
	p =		[16, 7, 20, 21, 
			29, 12, 28, 17, 
			1, 15, 23, 26, 
			5, 18, 31, 10, 
			2, 8, 24, 14, 
			32, 27, 3, 9, 
			19, 13, 30, 6, 
			22, 11, 4, 25]
	invIP =	[40, 8, 48, 16, 56, 24, 64, 32, 
			39, 7, 47, 15, 55, 23, 63, 31, 
			38, 6, 46, 14, 54, 22, 62, 30, 
			37, 5, 45, 13, 53, 21, 61, 29, 
			36, 4, 44, 12, 52, 20, 60, 28, 
			35, 3, 43, 11, 51, 19, 59, 27, 
			34, 2, 42, 10, 50, 18, 58, 26, 
			33, 1, 41, 9, 49, 17, 57, 25]
	return IP, ex, p, invIP

def S_Boxes():
	S1 =	[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
	S2 =	[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
	S3 =	[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
	S4 =	[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
	S5 =	[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
	S6 =	[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
	S7 =	[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
	S8 =	[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
	return [S1, S2, S3, S4, S5, S6, S7, S8]

def key_expand(key):
	PC1_l =[57, 49, 41, 33, 25, 17, 9, 
			1, 58, 50, 42, 34, 26, 18, 
			10, 2, 59, 51, 43, 35, 27, 
			19, 11, 3, 60, 52, 44, 36]

	PC1_r =[63, 55, 47, 39, 31, 23, 15, 
			7, 62, 54, 46, 38, 30, 22, 
			14, 6, 61, 53, 45, 37, 29, 
			21, 13, 5, 28, 20, 12, 4]
	left = ''; right = ''
	for x in xrange(28):
		left += key[PC1_l[x]-1]
		right += key[PC1_r[x]-1]
	rot = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
	PC2 =	[14, 17, 11, 24, 1, 5, 
			3, 28, 15, 6, 21, 10, 
			23, 19, 12, 4, 26, 8, 
			16, 7, 27, 20, 13, 2, 
			41, 52, 31, 37, 47, 55, 
			30, 40, 51, 45, 33, 48, 
			44, 49, 39, 56, 34, 53, 
			46, 42, 50, 36, 29, 32]	
	keys = []
	for x in xrange(16):
		left = (left*2)[rot[x]:rot[x]+28]
		right = (right*2)[rot[x]:rot[x]+28]
		key = ''
		for y in xrange(48):
			key += (left + right)[PC2[y]-1]
		keys += [int(key,2)]
	return keys
	
def DES(data, key, mode):
	data = makebin(int(data,16),64)
	key = makebin(int(key,16),64)
	key = key_expand(key)
	if mode == 'd':
		key.reverse()
	IP, ex, p, invIP = setup()
	temp = ''
	for x in range(64):
		temp += data[IP[x]-1]
	data = temp
	s_box = S_Boxes()
	for x in xrange(16):
		temp = ''
		left = int(data[:32],2)
		right = data[32:]
		old_right = right
		for y in xrange(48):
			temp += right[ex[y]-1]
		right = int(temp,2)
		right = bin(right ^ key[x])[2:]
		right = right.zfill(48)
		right = [right[6*y:6*y+6] for y in xrange(8)]
		temp = ''
		for y in xrange(8):
			temp += makebin(s_box[y][int(right[y][0]+right[y][5],2)][int(right[y][1:5],2)])
		right = ''
		for y in xrange(32):
			right += temp[p[y]-1]
		data = old_right + makebin(left ^ int(right,2),32)
	data = data[32:] + data[:32]
	temp = ''
	for x in xrange(64):
		temp+= data[invIP[x]-1]
	data = ''
	for x in xrange(16):
		data += makehex(int(temp[4*x:4*x+4],2),1)
	return data
	
if __name__=='__main__':
	os.system('cls')
	print "Data Encryption Standard in python\nBy Jason Lee\n\n64 bit data\n64 bit key\n\n"
	mode = ''
	while mode != 'e' and mode != 'd':
		mode = raw_input('Encrypt(E) or Decrypt(D):')
		mode = mode.lower()
	data_form = ''
	while data_form != 'ascii' and data_form != 'hex':
		data_form = raw_input('Data format (ASCII or Hex):')
		data_form = data_form.lower()
	data = raw_input('Data:')
	if data_form =='ascii':
		data = hexlify(data)
		data = data.zfill(16)[:16]
	if len(data)%2 !=0:
		print 'IOError: Odd number of hexadecimal characters'
		sys.exit()
	key_form = ''
	while key_form != 'ascii' and key_form != 'hex':
		key_form = raw_input('Key format (ASCII or Hex):')
		key_form = key_form.lower()
	key = raw_input('Key:')
	if key_form == 'ascii':
		key = hexlify(key)
		key = key.zfill(16)[:16]
	if len(key)%2 !=0:
		print 'IOError: Odd number of hexadecimal characters'
		del data
		sys.exit()
	print '\n'  + 'Ciphertext:' * (mode == 'e') + 'Cleartext:' * (mode == 'd')
	ctext = DES(data,key,mode)
	print 'In Hex:  ',ctext,'\nIn ASCII:', unhexlify(ctext)