pragma solidity >=0.4.22 <0.6.0;
contract marketPlace{
    
    address payable public chairman;
    
    constructor() public{
        chairman = msg.sender;
    }
    
    struct customer {
        uint itemId;
	    bool registered;
	    int userBalance;
    }
    
    modifier onlyChairperson() {
        require(msg.sender == chairman);
        _;
    }
    mapping(address => customer) customers;
    
    event listed(uint itemId);
    event sold(uint itemId);
    
    
    function register(address newUser) public onlyChairperson{
        if(customers[newUser].registered == true) revert();
            customers[newUser].registered = true;
            customers[newUser].userBalance = 500;
            
    }
    
    function unregister(address user) public onlyChairperson{
        if(customers[user].registered == false) revert();
        customers[user].registered = false;
        customers[user].userBalance = 0;
    }
    
    function settlePayment(address seller, int itemPrice) public {
        if(itemPrice > customers[msg.sender].userBalance) revert();
        customers[msg.sender].userBalance = customers[msg.sender].userBalance - itemPrice;
        customers[seller].userBalance = customers[seller].userBalance + itemPrice;
        
    }
    
    function addBalance(address user, int amount) public {
        if(customers[user].registered == false) revert();
        customers[user].userBalance = customers[user].userBalance + amount;
        
    }
    
    function getBalance(address user) public view returns (int userBalance) {
        if(customers[user].registered == false) revert();
        userBalance = customers[user].userBalance;
    }
    
    function buy(uint itemId, int itemPrice, address seller) public{
        if(customers[msg.sender].registered == false) revert();
        if(customers[seller].registered == false) revert();
        if(itemPrice > customers[msg.sender].userBalance) revert();
        customer storage buyer = customers[msg.sender];
        customer storage seller = customers[seller];
        buyer.itemId = itemId;
        emit sold(itemId);
    }
    
}