from algokit_utils import AlgorandClient, SigningAccount
from ExampleClient import ExampleContractFactory, ExampleContractClient
from dotenv import load_dotenv
from pathlib import Path
import json
import os

load_dotenv()

algorand = AlgorandClient.testnet()

sk = os.getenv('sk')
address = os.getenv('address')
signing_account = SigningAccount(private_key=sk, address=address)

example_factory = ExampleContractFactory(
    algorand=algorand,
    default_sender=signing_account.address,
    default_signer=signing_account.signer
)

if os.getenv('app_id'):
    app_id = int(os.getenv('app_id'))

    example_client = algorand.client.get_typed_app_client_by_id(
        typed_client=ExampleContractClient,
        app_id=app_id,
        approval_source_map=json.loads((Path(__file__).parent / 'ExampleContract.approval.puya.map').read_text()),
        default_sender=signing_account.address,
        default_signer=signing_account.signer
    )