# ----------------------------------------------------------------------------------------------------
# UNIVERSIDAD ANTONIO NARIÑO
# ESPECIALIZACIÓN EN INGENIERÍA DE SOFTWARE
# GESTIÓN DE SEGURIDAD I
# JORGE ALFONSO GARCIA ESPINOSA  - 10892218519
# DIEGO ALEJANDRO POVEDA SANCHEZ - 10892217137
# ----------------------------------------------------------------------------------------------------
import hashlib

def apply_hashes(text):
    print("TEXT\t=" + text)
    byte_array = bytes(text, 'utf-8')
    print("SHA256\t=" + hashlib.sha256(byte_array).hexdigest())
    print("SHA1\t=" + hashlib.sha1(byte_array).hexdigest())
    print("MD5\t=" + hashlib.md5(byte_array).hexdigest())
    print()

texts = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "Etiam", "fringilla"]

for text in texts:
    apply_hashes(text)