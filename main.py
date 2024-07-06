from block import BlockChain
from models import Property, User
from models import Transaction
import setup
import random
from hmac_ import *


# initializing the blockchain
blockchain = BlockChain()


def verify_user(username, password):
    random_challenge = generate_challenge()
    bit = random.randint(0, 1)
    response = create_response(random_challenge, bit, password)

    print(password)

    for user in User.users:
        if user.username == username:
            print(user.password)
            return verify_response(random_challenge, bit, response, user.password)

    return False


def register():

    print('------------------------------------------------------------------ \n')
    print('Enter a username and password:')
    username = str(input("Username: "))
    password = str(input("Password (numeric): "))

    if (username != '' and password != ''):
        User(username, password)
        print(f'\n {username} registered successfully!')
        return
    else:
        print("\n Username and/or password can't be empty, try again \n")
        register()


def viewWealth():
    
        print('------------------------------------------------------------------ \n')
        print('Enter the username of the user whose wealth you want to see: ')
        username = str(input())
    
        user_found = False
        for user in User.users:
            if user.username == username:
                user_found = True
                curr_user = user
    
        if not user_found:
            print("The specified user does not exist \n")
            return
        
        print('Enter your password (numeric): ')
        pass1 = (input())

        if(verify_user(username, pass1) == False):
            print("\n You have input the incorrect pin!")
            return

        print(f'\n {username} has {curr_user.wealth} coins')


def buy():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    
    if not user_found:
        print("\n User does not exist, create a user")
        return

    print('Enter your password (numeric): ')
    pass1 = (input())


    if(verify_user(username, pass1) == False):
        print("\n You have input the incorrect pin!")
        return

   
    # for user in User.users:
    #     if(user.username==username):
    #         if (user.password != pass1):
    #             print("\n You have input the incorrect pin!")
    #             return


    print('\n Enter the ID of the property you want to buy: ')
    propertyId = int(input())
    property_chosen = Property.properties[propertyId]

    if property_chosen.owner is not None:
        current_owner = property_chosen.owner
        current_owner.remove_property(property_chosen)
    else:
        current_owner = None

    # res = find_pos(curr_user, current_owner, property_chosen)
    # if res == -1:
    #     print('Insufficient balance \n')
    #     return
    # else:
    transaction = Transaction(
        current_owner, curr_user, property_chosen)
    

    property_chosen.transaction_history.append(transaction)
    # res.wealth += property_chosen.amount // 2
    prev_block = blockchain.last_block()
    block = blockchain.new_block(prev_block['hash'], transaction)

    blockchain.mine_block_POW(block)

    curr_user.add_property(property_chosen)

    print(
        f"\n {curr_user.username} bought {property_chosen.name} successfully! \n {blockchain.last_block()['merkle_root']}")


def transaction_history():

    print('------------------------------------------------------------------ \n')
    print("Enter the ID of the property whose transaction history you want to see: ")
    propertyId = int(input())

    if propertyId >= len(Property.properties):
        print('Invalid selection, choose again \n')
        transaction_history()

    property_chosen = Property.properties[propertyId]

    for transaction in property_chosen.transaction_history:
        print(f'''
            Buyer: {transaction.buyer.username},
            Seller: {transaction.seller.username}
            Timestamp: {transaction.timestamp},
            TxnID: {transaction.transactionId}
        \n''')


def show_assets():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    else:
        print(f'\n -> Properties owned by {username} are:')
        curr_user.get_assets()


def register_property():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    else:
        print('Enter the name of the property:')
        name = input('')
        print('Enter the price of the property:')
        price = int(input(''))
        new_property = Property(name, price)
        curr_user.register_property(new_property)
        print(
            f'\n {new_property.name} registered in the system by {curr_user.username}')

def viewUser():
    username = input("Enter Username ")

    # BlockChain.get_transaction_by_user(BlockChain , username)

    # property_chosen = Property.properties

    for property_chosen in Property.properties:
        for transaction in property_chosen.transaction_history:
            if(transaction.buyer.username == username or transaction.seller.username == username):
                print(f'''
                    Property Name : {transaction.propertyName}
                    Buyer: {transaction.buyer.username},
                    Seller: {transaction.seller.username}
                    Timestamp: {transaction.timestamp},
                    TxnID: {transaction.transactionId}
                \n''')


# main loop
while True:

    print(""" \n ------------------------------------------------------------------ \n
    Choose an action:
        1. Register User
        2. Buy Property
        3. View transaction history for a property
        4. View assets owned by a user
        5. Register property
        6. View All Properties
        7. View Wealth of a User
        8. ViewUser()
        9. Exit
    """)

    choice = int(input())

    if (choice == 1):
        register()
    elif (choice == 2):
        buy()
    elif (choice == 3):
        transaction_history()
    elif (choice == 4):
        show_assets()
    elif (choice == 5):
        register_property()
    elif (choice == 6):
        Property.viewProperties(Property)
    elif (choice == 7):
        viewWealth()
    elif(choice == 8):
        viewUser()
    elif (choice == 9):
        break
    else:
        print("Invalid choice, choose again")

