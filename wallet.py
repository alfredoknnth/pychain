from ecdsa import SigningKey, SECP256k1, VerifyingKey, ellipticcurve
from ecdsa.util import sigdecode_der, sigencode_der
from hashlib import sha256
import hashlib

def generate_wallet():
    private_key = SigningKey.generate(SECP256k1)
    public_key = private_key.get_verifying_key()

    x = public_key.pubkey.point.x()
    y = public_key.pubkey.point.y()
    public_key_hex = f"{x:064x}{y:064x}"

    return private_key.to_string().hex(), public_key_hex

def sign_transaction(private_key_hex, message):
    private_key = SigningKey.from_string(bytes.fromhex(private_key_hex), SECP256k1)
    msg_hash = hashlib.sha256(message.encode()).digest()
    signature = private_key.sign_deterministic(msg_hash, sigencode=sigencode_der)
    return msg_hash, signature.hex()

def verify_signature(public_key_hex, msg_hash, signature_hex):
    try:
        # Reconstruct public key from hex (x + y)
        x = int(public_key_hex[:64], 16)
        y = int(public_key_hex[64:], 16)
        curve = SECP256k1
        point = ellipticcurve.Point(curve.curve, x, y)
        vk_rebuilt = VerifyingKey.from_public_point(point, curve=curve)

        signature_bytes = bytes.fromhex(signature_hex)

        is_valid = vk_rebuilt.verify(signature_bytes, msg_hash, sigdecode=sigdecode_der)
        return is_valid

    except Exception as e:
        print("[!] Signature failed:", e)
        return False
    
def pub_to_add(pub_hex):
    pub_bytes = bytes.fromhex(pub_hex)
    sha256 = hashlib.sha256(pub_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    return ripemd160.hex()