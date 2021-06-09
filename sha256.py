import hashlib  # we need this library


# this is our encrypter
def encrypt(hash_string):
    sha_256 = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_256  # "sha256" is our encrypted value


print("Result encrypted with SHA256:", encrypt(input("Enter the value to be encrypted: ")))

# By akerem16
# Made in Turkey :)
