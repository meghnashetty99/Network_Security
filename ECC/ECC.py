from tinyec import registry
import secrets
curve=registry.get_curve('brainpoolP256r1')
def compress_point(point):
    return hex(point.x)+hex(point.y%2)[2:]
def ecc_calc_encryption_key(pubkey):
    ciphertextPrivKey = secrets.randbelow(curve.field.n)
    ciphertextPubKey = ciphertextPrivKey*curve.g
    sharedECCKey=pubKey*ciphertextPrivKey
    return (sharedECCKey,ciphertextPubKey)

def ecc_calc_decryption_key(privKey,ciphertextPubKey):
    sharedECCKey = ciphertextPubKey*privKey
    return sharedECCKey

user_input=input("enter priv key or press enter to generate:")
if user_input:
    try:
        privKey=int(user_input,16)
        if privKey<=0 or privKey>=curve.field.n:
            raise ValueError("Invalid priv key range")
    except ValueError:
        print("invalid input")
        privKey=secrets.randbelow(curve.field.n)
else:privKey = secrets.randbelow(curve.field.below)
pubKey=privKey*curve.g
print("Private key",hex(privKey))
print("Public key",compress_point(pubKey))
(encryptKey,ciphertextPubKey)=ecc_calc_encryption_key(pubKey)
print("CiphrText public key:",compress_point(ciphertextPubKey))
print("Encryption key:",compress_point(encryptKey))
decryptKey=ecc_calc_decryption_key(privKey,ciphertextPubKey)

print("Decryption key:",compress_point(decryptKey))
if encryptKey==decryptKey:
    print("Encrytion and decryption keys match")
else:
    print("Key mismatch")
