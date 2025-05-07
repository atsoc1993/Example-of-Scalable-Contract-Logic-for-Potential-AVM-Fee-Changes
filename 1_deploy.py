from constants import example_factory, algorand, signing_account
from algokit_utils import PaymentParams, AlgoAmount
from dotenv import load_dotenv, set_key

load_dotenv()

print(f'Deploying App . . .')
example_client, deploy_response = example_factory.send.create.bare()
print(f'App Deployed, App ID: {example_client.app_id}')

set_key(dotenv_path='.env', key_to_set='app_id', value_to_set=str(example_client.app_id))
print('Wrote App ID to .env')

print(f'Funding App 0.1 Algo for active account MBR . . .')
algorand.send.payment(
    params=PaymentParams(
        sender=signing_account.address,
        signer=signing_account.signer,
        receiver=example_client.app_address,
        amount=AlgoAmount(algo=0.1),
        validity_window=1000
    )
)
print(f'App Funded')