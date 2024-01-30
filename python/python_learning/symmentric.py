from cryptography.fernet import Fernet
msg = 'welcome to my python code'
key = Fernet.generate_key()
print("Key : ",key) # to generate the key
#Encryption and decrypiton in same key
fernet_obj = Fernet(key)
encrypt_msg = fernet_obj.encrypt(msg.encode()) #To encrypt the msg
print(encrypt_msg)
decrypt_msg = fernet_obj.decrypt(encrypt_msg.decode()) #To decrypt the msg
print(decrypt_msg)