import json
from algosdk import account, transaction
from algosdk.v2client import algod
from algosdk.transaction import AssetTransferTxn

# Algorand Testnet endpoint from Nodely (no token required for free service)
algod_address = "https://testnet-api.4160.nodely.dev"
algod_token = ""

# Initialize the algod client
algod_client = algod.AlgodClient(algod_token, algod_address)

# Asset ID obtained from deciphered clue (replace this with your actual Asset ID)
asset_id = 720485937

# Replace with your Testnet wallet private key and address
sender_private_key = ""
sender_address = account.address_from_private_key(sender_private_key)

# Function to get account balance (optional, for verification)
def print_asset_balance(address, asset_id):
    account_info = algod_client.account_info(address)
    for asset in account_info['assets']:
        if asset['asset-id'] == asset_id:
            print(f"Asset ID: {asset_id} Balance: {asset['amount']}")
            return
    print(f"Asset ID {asset_id} not found in account {address}")

# Create an opt-in transaction for the asset
def opt_in_to_asset():
    params = algod_client.suggested_params()

    txn = AssetTransferTxn(
        sender=sender_address,
        sp=params,
        receiver=sender_address,
        amt=0,
        index=asset_id
    )

    signed_txn = txn.sign(sender_private_key)

    try:
        txid = algod_client.send_transaction(signed_txn)
        print(f"Opt-in transaction sent with ID: {txid}")
        
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
        print(f"Transaction confirmed in round: {confirmed_txn['confirmed-round']}")
        
        print_asset_balance(sender_address, asset_id)
    except Exception as e:
        print(f"Failed to send opt-in transaction: {e}")

# Get the node status (to verify connection to the network)
try:
    status = algod_client.status()
    print("Node status:", status)
except Exception as e:
    print(f"Failed to get node status: {e}")

opt_in_to_asset()
