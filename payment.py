from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from xrpl.transaction import safe_sign_and_autofill_transaction as sign
from xrpl.transaction import send_reliable_submission as send


class pay_x:
    def __init__(self,client,wallet,account,amount,adr):
        self.client = client
        self.wallet  =wallet
        self.account = account
        self.amount = amount
        self.adr = adr
    def paying(self):
        self.paying = Payment(
            account = self.account,
            amount= xrp_to_drops(self.amount),
            destination=self.adr
        )
        #return self.paying
    def sign_transaction(self):
        self.signed = sign(self.paying,self.wallet,self.client)
    
    def sending(self):
        self.response = send(self.signed,self.client)



