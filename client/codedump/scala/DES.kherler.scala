package com.karlherler.crypto.javax.des

import javax.crypto.Cipher.DECRYPT_MODE;
import javax.crypto.Cipher.ENCRYPT_MODE;

class DES(msg: Array[Byte]) extends JavaxDES {
	
	def encrypt(k:  Array[Byte]) = {
		cipher.init(ENCRYPT_MODE, createKey(k))
		cipher doFinal msg
	}
	def decrypt(k: Array[Byte]) = { 
		cipher.init(DECRYPT_MODE, createKey(k))
		cipher doFinal msg
	}
}