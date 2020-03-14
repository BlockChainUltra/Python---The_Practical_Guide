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


def get_user_input():
    """returns the input of the user, a new transaction amount - a float"""
    return float(input("Please enter your transaction amount: "))


tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())


print(blockchain)
