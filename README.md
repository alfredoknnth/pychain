# PyChain – A Minimal Blockchain Implementation in Python

**PyChain** is a simplified blockchain prototype developed in Python for educational and experimental purposes. This project demonstrates the core principles behind blockchain technology, including data immutability, digital signatures using ECDSA, and proof-of-work (PoW) consensus.

---

## Features

- ✅ Block and chain structure with linkage via hashes  
- ✅ Transaction batching per block (5 transactions per block)  
- ✅ Digital signature verification using ECDSA (SECP256k1)  
- ✅ Public key to address transformation using RIPEMD-160  
- ✅ Proof-of-Work (PoW) mining algorithm  
- ✅ Chain integrity verification  

---

## Project Structure
```python
pychain/pychain.py # core blockchain logic and transaction handling
pychain/wallet.py # wallet generation, signing, and verification function
```

---
## Getting Started

### Requirements

- Python 3.7 or higher
- Required Python packages:
  ```bash
  pip install ecdsa base58
  ```

### Usage

```python
from wallet import generate_wallet, pub_to_add
from pychain import Blockchain

pychain = Blockchain()

priv1, pub1 = generate_wallet()
priv2, pub2 = generate_wallet()

#block 1
pychain.make_transaction(priv1, pub1, pub2, 50)
pychain.make_transaction(priv1, pub1, pub2, 50)
pychain.make_transaction(priv2, pub2, pub1, 76)
pychain.make_transaction(priv1, pub1, pub2, 2)
pychain.make_transaction(priv2, pub2, pub1, 90)

isValid = pychain.is_chain_valid()

for block in pychain.chain:
    if isinstance(block.data, list):
        for tx in block.data:
            tx["sender"] = pub_to_add(tx["sender"])
            tx["receiver"] = pub_to_add(tx["receiver"])

    print("="*20)
    print("Index:",block.index)
    print("Timestamp:",block.timestamp)
    print("Data:",block.data)
    print("Hash:",block.hash)
    print("Previous hash:",block.previous_hash)
    print("="*20)

print("Is blockchain valid?", isValid)
```
Once 5 valid transactions are added, a block is automatically mined and appended to the chain.

---

## How it works
1. Wallets are generated using the ECDSA SECP256k1 curve (same as Bitcoin).
2. Transactions are signed with the sender's private key and verified using the public key.
3. A block collects 5 valid transactions and undergoes PoW mining.
4. Chain integrity is maintained by linking each block through cryptographic hashes.

## Digital Signatures
- Signing: SHA-256 hash of the message is signed using the private key.
- Verification: Each transaction signature is verified against the original message using the sender’s public key.
- Messages are of the form:
```bash
sender + receiver + amount
```

---

## Chain Validation
```python
pychain.is_chain_valid()
```
Performs the following checks:
- Hash consistency and linkage between blocks
- (Optionally extendable): Signature verification for all transactions

---

## Example Output
```yaml
====================
Index: 0
Timestamp: 1751892845.5973833
Data: Genesis Block
Hash: 1956c05e4c4405f967b9c6622a3d8d35cb1dc8f388ffda8ab658c6962ddbd21d
Previous hash: 0
====================
====================
Index: 1
Timestamp: 1751892845.6403701
Data: [{'sender': '1050639aaa43bdb5d5c58935f557013541166659', 'receiver': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'amount': 50, 'signature': '3045022051c055d6d4e9b9d686bd353715bfca2c8a66de037dc65759076e6e6ee291efb1022100b79813dbe31021b805ac2f05ea16418fd2de64ea2f266bb18110445d729557cb'}, {'sender': '1050639aaa43bdb5d5c58935f557013541166659', 'receiver': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'amount': 50, 'signature': '3045022051c055d6d4e9b9d686bd353715bfca2c8a66de037dc65759076e6e6ee291efb1022100b79813dbe31021b805ac2f05ea16418fd2de64ea2f266bb18110445d729557cb'}, {'sender': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'receiver': '1050639aaa43bdb5d5c58935f557013541166659', 'amount': 76, 'signature': '3045022100a15199008cc6d9468bbffb8cdec683b608f83c53bc31d19a6631fd49ba161a9a022057442c76cb102c537f78a439c395c9d6c853b17ec24405ea8525064e04916dc3'}, {'sender': '1050639aaa43bdb5d5c58935f557013541166659', 'receiver': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'amount': 2, 'signature': '3046022100b6faab474152818eb1e01ab3e68acfbbe83857ae1968d820d010d5a79604567e022100eb2905ce7da8833d2d95a698108ba5c7a2fa2c53dd7557a16978c9939b650ead'}, {'sender': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'receiver': '1050639aaa43bdb5d5c58935f557013541166659', 'amount': 90, 'signature': '30460221009cfa81a77c89fb4d5de0d675e0ee60e966b71e1aac45d178577286b025349184022100931a0399047b08d648eda4edeab0b2ccbdb30d9ac3aca4dc46f8996e3d998001'}]
Hash: 0045312619da6115076342d11a74b24c182b24dec1238f60abc860e621d6bf58
Previous hash: 1956c05e4c4405f967b9c6622a3d8d35cb1dc8f388ffda8ab658c6962ddbd21d
====================
====================
Index: 2
Timestamp: 1751892845.704163
Data: [{'sender': '1050639aaa43bdb5d5c58935f557013541166659', 'receiver': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'amount': 50, 'signature': '3045022051c055d6d4e9b9d686bd353715bfca2c8a66de037dc65759076e6e6ee291efb1022100b79813dbe31021b805ac2f05ea16418fd2de64ea2f266bb18110445d729557cb'}, {'sender': '1050639aaa43bdb5d5c58935f557013541166659', 'receiver': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'amount': 50, 'signature': '3045022051c055d6d4e9b9d686bd353715bfca2c8a66de037dc65759076e6e6ee291efb1022100b79813dbe31021b805ac2f05ea16418fd2de64ea2f266bb18110445d729557cb'}, {'sender': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'receiver': '1050639aaa43bdb5d5c58935f557013541166659', 'amount': 76, 'signature': '3045022100a15199008cc6d9468bbffb8cdec683b608f83c53bc31d19a6631fd49ba161a9a022057442c76cb102c537f78a439c395c9d6c853b17ec24405ea8525064e04916dc3'}, {'sender': '1050639aaa43bdb5d5c58935f557013541166659', 'receiver': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'amount': 2, 'signature': '3046022100b6faab474152818eb1e01ab3e68acfbbe83857ae1968d820d010d5a79604567e022100eb2905ce7da8833d2d95a698108ba5c7a2fa2c53dd7557a16978c9939b650ead'}, {'sender': '7de7a9fd24872771abc08e519fc4151b65d58a53', 'receiver': '1050639aaa43bdb5d5c58935f557013541166659', 'amount': 90, 'signature': '30460221009cfa81a77c89fb4d5de0d675e0ee60e966b71e1aac45d178577286b025349184022100931a0399047b08d648eda4edeab0b2ccbdb30d9ac3aca4dc46f8996e3d998001'}]
Hash: 00fc07853a0b20e8858036f52ef97b867304e8c75d3a3eccf49cc0f923c4e8be
Previous hash: 0045312619da6115076342d11a74b24c182b24dec1238f60abc860e621d6bf58
====================
Is blockchain valid? True
```

---

## Future Enhancements
The current implementation is a simplified model. Potential extensions include:
- Account-based balance or UTXO model
- Mining rewards (coinbase transactions)
- Web-based transaction interface (Flask/React)
- Peer-to-peer network and consensus rules
- Transaction pool (mempool) management
- Blockchain explorer UI

---

## Author
Developed by Alfredo Kenneth as part of a personal learning initiative in blockchain and cryptographic technologies.

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it for educational or personal projects.
