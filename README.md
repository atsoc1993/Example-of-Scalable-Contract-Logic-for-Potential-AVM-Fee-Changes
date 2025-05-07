## For smart contracts (in respect to storage fees) See ExampleContract.py in /contract_files:

- Create a subroutine with “get_mbr()uint64” and simply return the current applications mbr via account attribute.

- At the beginning of any methods that require additional MBR, set a variable, pre_mbr, to the value of the returned value of get_mbr()

- At the end of your method logic, set a variable, post_mbr, to the value of the returned value of get_mbr()

- Create a subroutine that accepts pre_mbr, post_mbr, and the original mbr payment. 

- Take the difference of post_mbr and pre_mbr, then take the difference of this from the MBR payment’s amount attribute.

- Refund the user through a payment inner transaction with this amount.

*Note: If you absolutely *must* hardcode transaction fees for whatever reason, use the global min_fee op, don’t hardcode 1000 for fee amounts although this is the fee for all inner transactions!*

## For Front-ends (in respect to transaction fees) See file # 2:
- Take advantage of max_fee (not extra fee) parameter available in send methods on application clients , it will deduct only the necessary amount of Algo from the users balance for transaction fees, 
