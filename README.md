# Blockchain-lab1

Members
_______

* Gokul Premraj 50289719 _gokulpre@buffalo.edu_
* Apurva Patil 50291554 _acpatil@buffalo.edu_

Simple web app with a corresponding smart contract (marketPlace.sol).

Written in Django. No specific dependencies. Run using "Python manage.py runserver".

Access at https://localhost:8000. Leads to default login page. Use username : admin and password : testdjango.

Add item to the sale-list by clicking on the "I want to sell something" button.

Use the "buy" button next to an item to buy. Use the "Pay" button to complete payment.

smart contract functions and there expected parameters :

1. register -  user address  
2. unregister - user address
3. buy - itemID, itemPrice, seller address
4. addBalance - user address, amount
5. getBalance - user address
6. settlePayment - seller address, itemPrice
