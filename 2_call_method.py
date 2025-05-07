from constants import algorand, signing_account, example_client
from algokit_utils import PaymentParams, AlgoAmount, CommonAppCallParams
from ExampleClient import ExampleOfMethodWithProperMbrHandlingArgs


mbr_payment_tx = algorand.create_transaction.payment(
    PaymentParams(
        sender=signing_account.address,
        signer=signing_account.signer,
        receiver=example_client.app_address,
        amount=AlgoAmount(algo=1),
        validity_window=1000,
    )
)
txn_response = example_client.send.example_of_method_with_proper_mbr_handling(
    args=ExampleOfMethodWithProperMbrHandlingArgs(
        mbr_payment=mbr_payment_tx
    ),
    params=CommonAppCallParams(
        max_fee=AlgoAmount(algo=0.1)
    ),
    send_params={
        'populate_app_call_resources': True,
        'cover_app_call_inner_transaction_fees': True
    }
)

print(f'Transaction ID: {txn_response.tx_id}')

# method returns (uint64,uint64,uint64,uint64,uint64) pre_mbr, post_mbr, pre_post_diff, payment_amount, amount_refunded
abi_results = txn_response.abi_return
print(abi_results)
print(f'MBR Before writing boxes: {abi_results[0]:,.0f}')
print(f'MBR After wrting boxes: {abi_results[1]:,.0f}')
print(f'Difference in MBR before and after method: {abi_results[2]:,.0f}')
print(f'MBR Payment amount from user: {abi_results[3]:,.0f}')
print(f'Amount Refunded: {abi_results[4]:,.0f}')