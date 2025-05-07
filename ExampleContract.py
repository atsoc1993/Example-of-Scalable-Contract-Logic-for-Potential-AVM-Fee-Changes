from algopy import ARC4Contract, arc4, BoxMap, UInt64, gtxn, subroutine, Global, itxn, Txn
from algopy.arc4 import Struct, abimethod

class ExampleStruct(Struct):
    value_1: arc4.UInt64
    value_2: arc4.UInt64

class ExampleContract(ARC4Contract):
    def __init__(self) -> None:
        self.counter = arc4.UInt64(0)
        self.some_box_map = BoxMap(arc4.UInt64, ExampleStruct, key_prefix='')

    @abimethod
    def example_of_method_with_proper_mbr_handling(
        self,
        mbr_payment: gtxn.PaymentTransaction
    ) -> tuple[UInt64, UInt64, UInt64, UInt64, UInt64]:
        
        pre_mbr = self.get_mbr()

        example_struct = self.get_example_struct()

        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()
        self.increment_counter()
        self.some_box_map[self.counter] = example_struct.copy()

        post_mbr = self.get_mbr()

        pre_post_diff, payment_amount, amount_refunded = self.refund_excess_mbr(
            pre_mbr=pre_mbr,
            post_mbr=post_mbr,
            mbr_payment=mbr_payment
        )

        return pre_mbr, post_mbr, pre_post_diff, payment_amount, amount_refunded
    
    @subroutine
    def get_mbr(self) -> UInt64:
        return Global.current_application_address.min_balance
    
    @subroutine
    def get_example_struct(self) -> ExampleStruct:
        value_1 = arc4.UInt64(0)
        value_2 = arc4.UInt64(0)
        return ExampleStruct(
            value_1=value_1,
            value_2=value_2
        )
    
    @subroutine
    def increment_counter(self) -> None:
        self.counter = arc4.UInt64(self.counter.native + 1)

    @subroutine
    def refund_excess_mbr(
        self,
        pre_mbr: UInt64,
        post_mbr: UInt64,
        mbr_payment: gtxn.PaymentTransaction
    ) -> tuple[UInt64, UInt64, UInt64]:
        
        pre_post_diff = post_mbr - pre_mbr
        payment_amount = mbr_payment.amount
        excess = payment_amount - pre_post_diff
        
        itxn.Payment(
            receiver=Txn.sender,
            amount=excess
        ).submit()

        return pre_post_diff, payment_amount, excess
        