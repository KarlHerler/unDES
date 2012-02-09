package com.karlherler.crypto.javax.des

import javax.crypto.Cipher;
import javax.crypto.Cipher.DECRYPT_MODE;
import javax.crypto.Cipher.ENCRYPT_MODE;
import javax.crypto.spec.DESKeySpec;
import javax.crypto.SecretKeyFactory;
import javax.crypto.SecretKey;


trait JavaxDES {
	val keyFactory = SecretKeyFactory.getInstance("DES")
   	val cipher = Cipher.getInstance("DES/ECB/NoPadding")
   	//val cipher = Cipher.getInstance("DES")

    def createKey(k: Array[Byte]) = {
    	val dKey = new DESKeySpec(k)
		keyFactory.generateSecret(dKey)
    }
}