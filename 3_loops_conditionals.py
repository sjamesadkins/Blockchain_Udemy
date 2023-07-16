blockchain = []

def get_user_input():
    return input("Please enter an amount: ")

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well a the last blockchain value to the blockchain array
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         print(block_index)
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     print(block_index)
    #     block_index += 1
    return is_valid

waiting_for_input = True


while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
        print(blockchain)
        print('-' * 30)
    elif user_choice == '2':
        print(blockchain)
        print('-' * 30)
    elif user_choice == 'q':
        print("Terminating session.")
        waiting_for_input = False
    elif user_choice == 'h':
        if len(blockchain) > 1:
            blockchain[0] = [2]
    else:
        print('Input was invalid, please pick a value from the list.')

    if not verify_chain():
        print('Invalid blockchain!')
        break
        

    # for block in blockchain:
    #     print("Outputting block")
    #     print(block)



