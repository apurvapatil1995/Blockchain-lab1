pragma solidity >=0.4.22 <0.6.0;
contract marketPlace{
    
    address chairman;
    
    constructor() public{
        chairman = msg.sender;
    }
    
    struct customer {
        uint itemId;
	    bool registered;
    }
    
    modifier onlyChairperson() {
        require(msg.sender == chairman);
        _;
    }
    mapping(address => customer) customers;
    
    event listed(uint itemId);
    event sold(uint itemId);
    
    function sell(uint itemId) public{
        if(customers[msg.sender].registered == false) revert();
        customer storage seller = customers[msg.sender];
        seller.itemId = itemId;
        emit listed(itemId);
    }
    
    function register(address newUser) public onlyChairperson{
        if(customers[newUser].registered == true) revert();
            customers[newUser].registered == true;
    }
    
    function unregister(address user) public onlyChairperson{
        if(customers[user].registered == false) revert();
        customers[user].registered == false;
    }
    
    function settlePayment() private{
        
    }
    
    function addBalance() private{
        
    }
    
    function buy(uint itemId, int itemPrice, address seller, int balance) public{
        if(customers[msg.sender].registered == false) revert();
        if(customers[seller].registered == false) revert();
        if(itemPrice > balance) revert();
        settlePayment();
        customer storage buyer = customers[msg.sender];
        customer storage seller = customers[seller];
        buyer.itemId = itemId;
        emit sold(itemId);
    }
    
}
