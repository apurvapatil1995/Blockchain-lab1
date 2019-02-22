pragma solidity >=0.4.22 <0.6.0;
contract marketPlace{
    
    address chairman;
    
    constructor() public{
        chairman = msg.sender;
    }
    
    struct customer {
        uint itemId;
    }
    
    mapping(address => customer) customers;
    
    event listed(uint itemId);
    event sold(uint itemId);
    
    function sell(uint itemId) public{
        customer storage seller = customers[msg.sender];
        seller.itemId = itemId;
        emit listed(itemId);
        
    }
    
    function buy(uint itemId, address seller) public{
        customer storage buyer = customers[msg.sender];
        customer storage seller = customers[seller];
        buyer.itemId = itemId;
        emit sold(itemId);
    }
    
}
