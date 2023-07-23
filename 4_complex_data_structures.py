list = ['milk', 'honey', 'milk']
set = {'milk', 'honey'}
tuple = ('milk', 'honey')
dictionary = {'name':'milk', 'sweetener':'honey'}

stats = [('age', 29), ('weight', 72), ('height', 178)]
dict_stats = {key: value for (key, value) in stats} #dict comprehension

print(dict_stats)
print(list[1])
print(set)
print(tuple[0])

#range selector for copying a list (because otherwise lists are copied by reference)
my_list = [1,2,3,4]
second_list = [1, 2, 3, 4]
new_list = my_list
new_list[0] = 5
copied_list = second_list[:] #<-- use the [:] syntax to copy the contents rather than reference

print(new_list)
print(copied_list)

MINING_REWARD = 10

# initializing the blockchain
genesis_block = {
    'previous_hash': '', 
    'index': 0, 
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Sam'
participants = {'Sam'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]

    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]

    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_recipient= [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent

# get user input
def get_user_input():
    return input("Please enter an amount: ")

#get last blockchain value
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

# add transaction to blockchain
def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well a the last blockchain value to the blockchain array
    Arguments:
        :sender: the sender of the coins
        :recipient: the recipient of the coins
        :amount: the amount of the coins sent with the transaction (default = 1 coin)
    """
    transaction = {
        'sender':sender, 
        'recipient': recipient, 
        'amount': amount
        }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    #pass # 'pass' won't do anything with this function yet
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block) # list comprehension
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    copied_transaction = open_transactions[:]

    copied_transaction.append(reward_transaction)

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': copied_transaction
        }
    blockchain.append(block)
    return True

# get a transaction value
def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount

# get user choice
def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print("\nOutputting Block")
        print(block)
        print('\n')

#verify the blockchain
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

def verify_transactions():
    return (all([verify_transaction(tx) for tx in open_transactions]))


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('5: Check transaction validity')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data #pulls data out of tuple and stores in variables
        if add_transaction(recipient, amount=amount):
            print('Added transactions')
        else:
            print('Transaction failed')
        print('\nOpen Transactions: ' + str(open_transactions))
        print('\nBlockchain: ' + str(blockchain))
        print_blockchain_elements()
        print('-' * 30)
    elif user_choice =='2':
        if mine_block():
            open_transactions = []
        print_blockchain_elements()
    elif user_choice == '3':
        print(blockchain)
        print_blockchain_elements()
        print('-' * 30)
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'q':
        print("Terminating session.")
        waiting_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[1] = {
                'previous_hash': '', 
                'index': 0, 
                'transactions': [{'sender': 'Chris', 'recipient': 'Sam', 'amount': 50}]
                }
            print_blockchain_elements()
    else:
        print('Input was invalid, please pick a value from the list.')

    if not verify_chain():
        print('Invalid blockchain!')
        # print_blockchain_elements()
        break
    print(get_balance('Sam'))




