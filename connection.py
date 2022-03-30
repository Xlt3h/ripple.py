from cgi import test
from distutils.command.clean import clean
from distutils.log import debug
from http import client
from xrpl.clients import JsonRpcClient as jrc
from xrpl.wallet import generate_faucet_wallet as gfw

class connections:
    #constructor
    def __init__(self,server):
        self.server  = server #servers needs to be like url :)
    
    #connection to the test server //testnet
    def connection_to_test(self):
        self.client_test = jrc(self.server)
        return self.client_test
    
    #connection to the mainet
    def connection_to_mainet(self):
        #install the core server before using this one
        #this local server are not available for windows
        self.json_url_for_local_server = self.server
        self.client_mainet = jrc(self.json_url_for_local_server)
        return self.client_mainet
    
    #public server
    def connection_to_public_server(self):
        self.json_url_for_public_server = self.server
        self.client_public = jrc(self.json_url_for_public_server)
        return self.client_public

class generating_wallet:    
    def __init__(self,client):
        self.client_ = client

    def test_wallet_generator(self):
        self.test_wallet = gfw(self.client_,debug=True)
        print(self.test_wallet)
        

