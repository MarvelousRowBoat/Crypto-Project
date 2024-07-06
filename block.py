import json
from datetime import datetime
from hashlib import sha256
from merkle_tree import MerkleTree
import time


class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.difficulty = 4
        self.new_block()

    def new_block(self, previous_hash=None, transaction=None):

        block = {
            'index': len(self.chain),
            #'timestamp': datetime.utcnow().isoformat(),
            'Difficulty' : 4,
            'nonce' : 0,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash
        }

        if transaction is not None:
            self.transactions.append(transaction.transactionId)
            merkle_root = MerkleTree(self.transactions).getRootHash()
            block['merkle_root'] = merkle_root
            block['transactions'] = self.transactions

        block_hash = self.hash(block)
        block['hash'] = block_hash

        self.chain.append(block)

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1] if self.chain else None
    
    def get_block(self, index):
        return self.chain[index] if index < len(self.chain) else None
    
    def get_chain(self):
        return self.chain
    
    def get_transactions(self):
        return self.transactions
    
    def get_transaction(self, transactionId):
        for block in self.chain:
            if transactionId in block['transactions']:
                return block
        return None
    
    def get_transaction_by_user(self, username):
        transactions = []
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction.buyer.username == username or transaction.seller.username == username:
                    transactions.append(transaction)
        return transactions
    
    def get_transaction_by_property(self, propertyId):
        transactions = []
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction.property_chosen.id == propertyId:
                    transactions.append(transaction)
        return transactions
    
    def mine_block_POW(self , block):
        # Stores the root hash of the Merkle Tree for the block's transactions
        # self.verify_transactions()
        while self.hash(block)[:self.difficulty] != '0' * self.difficulty:
            block['nonce'] += 1
            #self.hash = self.calculate_hash()
        print("nonce was ", block['nonce'] , '(this is only for demonstration purpose)')
        print(f'Block mined: {self.hash(block)}')
    
    def is_chain_valid(self):
        for i in range(1 , len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.prev_hash != prev_block.hash:  
                return False
        return True
    

    def get_transaction_by_index(self, index):
        return self.transactions[index] if index < len(self.transactions) else None
    
    def get_transaction_by_block(self, block, transactionId):
        if transactionId in block['transactions']:
            return block
        return None