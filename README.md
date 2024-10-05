# CTF Challenge: Find the Hidden Flag

This repository contains the solution for the second challenge of a Capture the Flag (CTF) event. The goal is to decipher a hidden clue and execute an opt-in transaction using the Algorand Testnet.

## Challenge Overview

### Task:
- Uncover a hidden clue hidden within six encrypted strings.
- The clue is encrypted using a substitution cipher where letters are converted to their corresponding one's digit based on their position in the alphabet (A=1, B=2, ..., Z=6).
- After deciphering, the clue reveals an asset ID, which is used to send an opt-in transaction for the corresponding NFT.

### Deciphering Example:

| Encrypted String | Deciphered Number  |
|------------------|--------------------|
| NJMLQSORQ        | 403279587          |
| QOLSRJNQM        | 752980473          |
| QLJNROSMQ        | 720485937          |
| JLQRNMOSQ        | 027843597          |
| JNQSQORLM        | 047975823          |
| NQSJMROQL        | 479038572          |

### Deciphering Logic:

Each letter is mapped to its corresponding position in the alphabet, and only the one's digit is taken.

Example:
- `N = 14`, take the one's digit → `4`
- `J = 10`, take the one's digit → `0`

## Requirements

- Python 3.6+
- Algorand SDK (`py-algorand-sdk`)
- Algorand Testnet account and private key

## Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chshashank404/AlgoBharat-CTF-challenge-2.git
   cd your-repo-directory
   ```

2. **Run decipher.py to obtain the Asset ID: This script deciphers the encrypted clue to generate the asset ID.**
```bash
python decipher.py
```

3. Run opt_in.py to opt-in to the asset on the Algorand Testnet: Make sure to replace the sender_private_key and asset_id in opt_in.py with the actual values you obtained from decipher.py.
```bash
python code.py
```
This will execute the opt-in transaction for the asset.

