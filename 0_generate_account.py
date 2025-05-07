from algosdk.account import generate_account
from dotenv import load_dotenv, set_key

load_dotenv()

sk, address = generate_account()
set_key(dotenv_path='.env', key_to_set='sk', value_to_set=sk)
set_key(dotenv_path='.env', key_to_set='address', value_to_set=address)

# Fund account via https://bank.testnet.algorand.network/
