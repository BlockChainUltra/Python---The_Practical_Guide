# initializing our blockchain
blockchain = [[1]]


def get_last_blockchain_value():
    """Returns the last value of the current blockchain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """Appends a new value, as well as the last value, to the blockchain
    Arguments:
    - transaction_amount : the new amount to be added
    - last_transaction : the last blockchain transaction (default = 1)
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """returns the input of the user, a new transaction amount - a float"""
    return float(input("Please enter your transaction amount: "))

def get_user_choice():
    user_input = input("Your choice: ")
    return user_input
#tx_amount = get_user_input()
#add_value(tx_amount, get_last_blockchain_value())

def print_blockchain_elements():
    """ Output the blochcian to the console"""
    for block in blockchain:
            print(block)


while True:
    print("Please choose hat you would like to do:")
    print("1: Add a new transaction value.")
    print("2: Output the blockchain blocks.")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()
        
