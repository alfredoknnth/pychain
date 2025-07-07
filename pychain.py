import hashlib
import time
from wallet import generate_wallet, sign_transaction, verify_signature, pub_to_add

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
class Blockchain:
    difficulty = 2

    def __init__(self):
        self.chain = []
        self.transac = []
        self.create_genesis_block()

    def add_transaction(self, sender, receiver, amount, signature):
        tx = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "signature": signature
        }

        msg = f"{sender}{receiver}{amount}"
        msg_hash = hashlib.sha256(msg.encode()).digest()

        if not verify_signature(sender, msg_hash, signature):
            return print("[!] Invalid Signature")

        self.transac.append(tx)

        if len(self.transac) >= 5:
            temp = Block(len(self.chain), time.time(), self.transac, self.get_last_block().hash)
            self.add_block(temp)
            self.transac = []

    def make_transaction(self, priv_key, sender, receiver, amount):
        message = f"{sender}{receiver}{amount}"
        msg_hash, sig = sign_transaction(priv_key, message)

        if not verify_signature(sender, msg_hash,sig):
            return print("[!] Invalid Signature")
        
        self.add_transaction(sender, receiver, amount, sig)

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block):
        block.previous_hash = self.get_last_block().hash
        block.hash = self.proof_of_work(block)
        self.chain.append(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1]
            if curr.hash != curr.compute_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True