import os
import subprocess
from tqdm.auto import tqdm
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Hash import SHA3_512
from src.core.config import conf


class AES256:
    RED = "\033[1;31m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    buffer_size = 65536

    def __int__(self, buffer_sise):
        self.buffer_size = buffer_sise

    def print_red(self, str):
        print(self.RED + str + self.RESET)

    def print_green(self, str):
        print(self.GREEN + str + self.RESET)

    def checkExtension(self, filepath, ext):
        _, file_extension = os.path.splitext(filepath)
        return file_extension == ext

    def shred_file(self, path):
        print("Shredding...")
        abs_dir = os.path.abspath(os.path.join(__file__, os.pardir))
        shred_prog = os.path.join(abs_dir, "shredder.cc")
        subprocess.call([shred_prog, path])

    def generate_salt(self):
        return get_random_bytes(32)

    def get_salt_from_file(self, input_file_path):
        input_file = open(input_file_path, 'rb')
        return input_file.read(32)

    def generate_AES256_key(self, passwd, salt):
        return scrypt(passwd, salt, 32, N=2 ** 20, r=8, p=1)

    def check_password(self, passwd, input_file_path):
        input_file = open(input_file_path, 'rb')
        bytes_temp = input_file.read(112)
        hashed_pwd = bytes_temp[48:112]
        salt = self.get_salt_from_file(input_file_path)

        return SHA3_512.new(data=passwd.encode('utf-8')).update(salt).digest() == hashed_pwd

    def read_password(self, input_file_path):
        input_file = open(input_file_path, 'r')
        bytes_temp = input_file.read(112)
        return bytes_temp

    def encrypt_key(self, key, passwd, salt, input_file_path):
        hashed_passwd = SHA3_512.new(data=passwd.encode('utf-8'))
        hashed_passwd.update(salt)
        hashed_passwd = hashed_passwd.digest()

        input_file = open(input_file_path, 'rb')
        output_file = open(input_file_path + '.aes', 'wb')

        cipher_encrypt = AES.new(key, AES.MODE_CFB)

        output_file.write(salt)  # 32 bytes
        output_file.write(cipher_encrypt.iv)  # 16 bytes
        output_file.write(hashed_passwd)  # 64 bytes

        # Progress bar
        file_size = os.path.getsize(input_file_path)
        pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc="Encrypting")

        buffer = input_file.read(self.buffer_size)
        pbar.update(len(buffer))
        while len(buffer) > 0:
            ciphered_bytes = cipher_encrypt.encrypt(buffer)
            output_file.write(ciphered_bytes)
            buffer = input_file.read(self.buffer_size)
            pbar.update(len(buffer))

        input_file.close()
        output_file.close()
        #self.shred_file(input_file_path)
        os.remove(input_file_path)

    def encrypt_key_data(self, key, passwd, salt,data):
        hashed_passwd = SHA3_512.new(data=passwd.encode('utf-8'))
        hashed_passwd.update(salt)
        hashed_passwd = hashed_passwd.digest()

        output_file = open(conf.ENCRYPTED_DB_PATH, 'wb')

        cipher_encrypt = AES.new(key, AES.MODE_CFB)

        output_file.write(salt)  # 32 bytes
        output_file.write(cipher_encrypt.iv)  # 16 bytes
        output_file.write(hashed_passwd)  # 64 bytes

        # Progress bar
        ciphered_bytes = cipher_encrypt.encrypt(data)
        output_file.write(ciphered_bytes)
        output_file.close()
        return True


    def encrypt(self, passwd, input_file_path):
        print("Generating key from password...")
        salt = self.generate_salt()
        key = self.generate_AES256_key(passwd, salt)

        print(f"Encrypting {input_file_path}")
        self.encrypt_key(key, passwd, salt, input_file_path)
        self.print_green("File is encrypted.")

        return True

    def encryptData(self, passwd,data):
        print("Generating key from password...")
        salt = self.generate_salt()
        key = self.generate_AES256_key(passwd, salt)

        self.encrypt_key(key, passwd, salt)
        self.print_green("File is encrypted.")

        return True

    def decrypt_key(self, key, input_file_path):
        input_file = open(input_file_path, 'rb')

        bytes_temp = input_file.read(112)
        iv = bytes_temp[32:48]

        decrypted_Content = ""

        cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)

        # Progress bar
        file_size = os.path.getsize(input_file_path) - 112
        pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc="Decrypting")

        buffer = input_file.read(self.buffer_size)
        pbar.update(len(buffer))
        while len(buffer) > 0:
            decrypted_bytes = cipher_decrypt.decrypt(buffer)
            decrypted_Content += decrypted_bytes.decode("utf-8")
            buffer = input_file.read(self.buffer_size)
            pbar.update(len(buffer))

        input_file.close()
        return decrypted_Content

    def decrypt(self, passwd, input_file_path):
        if not self.check_password(passwd, input_file_path):
            return False
        salt = self.get_salt_from_file(input_file_path)
        key = self.generate_AES256_key(passwd, salt)
        return self.decrypt_key(key, input_file_path)