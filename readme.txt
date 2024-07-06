
----------------------------------------------------
ABOUT THE PROJECT:
Our land management system makes it easier for users to acquire and sell real estate.The system comes with the following attributes:


 -It enables the user to sign up with previously owned property in the system.

 -Any property in the system may be purchased or sold by the user.

 -User has access to a property's transaction history.

 -To increase the security of the blockchain, we implemented the Proof of Stake (PoS) method.

 -We used the Merkle Tree to calculate the hash of every transaction in a block.

In this system, ZKP (Zero Knowledge Proof) is used.ZKP is used to check the user's password attribute.A user's transaction will be deleted and not added to the blockchain if they are unable to successfully complete a zero knowledge proof to verify their identity.


 ----------------------------------------------------
STEPS TO RUN THE CODE:
 -Run the main.py file
 
 -A menu appears with various choices as shown below-
    ***************
             Land Management System          
    ***************
    1. Register User
    2. Buy Property
    3. View transaction history for a property
    4. View assets owned by a user
    5. Register property

-There are different functions for different options whose descriptions are given in the next module

----------------------------------------------------
Function Details:
- User Registration: It generates a list of the user's information, including Owner Name, Property Owned by Him or Not, and Property Name. Real estate transactions cannot be made without registration.

 - Buy Property: This function takes transaction details(Amount,Buyer Name,Property Name) from the user and check whether the details are valid or not.After the verification it adds the transaction to the block.3 transactions make up a block.

 - View a Transaction: Every transaction is identified by a unique transaction ID, added by the user itself, and this function uses that ID to print details of a particular transaction(Transaction ID,Buyer Name,Seller Name,Amount,Property Name,Timestamp).

 - View Assests owned by User: It shows the already existing and acquired (if any) by the user.

 - Register Property: Thsi allows the user to register a new property by adding the name, amount for a specific user.

