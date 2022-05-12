# ----------------------------------------------------------------------------------------------------
# UNIVERSIDAD ANTONIO NARIÑO
# ESPECIALIZACIÓN EN INGENIERÍA DE SOFTWARE
# GESTIÓN DE SEGURIDAD I
# JORGE ALFONSO GARCIA ESPINOSA  - 10892218519
# DIEGO ALEJANDRO POVEDA SANCHEZ - 10892217137
# ----------------------------------------------------------------------------------------------------
import hashlib

encoding = 'utf-16'

def hash_with_md5(text):
    value = text.encode(encoding)
    hash_value = hashlib.md5(value).hexdigest()
    print(value.decode(encoding) + " (" + str(len(value)) + "): " + hash_value)
    return hash_value

def found_hash(hash_value):
    current_value = ""
    min_range = 0
    max_range = 255
    for byte1 in range(min_range, max_range):
        for byte2 in range(min_range, max_range):
            for byte3 in range(min_range, max_range):
                current_value = str(chr(byte1)) + str(chr(byte2)) + str(chr(byte3))
                found_hash = hash_with_md5(current_value)
                if found_hash == hash_value:
                    print("ENCONTRO\t=[" + current_value + "]\t" + found_hash)
                    exit()

found_hash("e96a036be3be000fefc0ebc061fb3b11")