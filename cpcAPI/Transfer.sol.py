	pragma solidity ^0.4.24;

    contract Transfer {

		address public user;
		address public provider;
		uint public coins;

		event TransferStart(address user, address provider);
		event NotEnough(address user);
		event TransferComplete(address user, address provider);

		# set user address and value
		function Transfer() public{
			user = msg.sender;
			coins = 10;
		}

    	function set(address provider) public {
    		require(provider == address(0));
    		this.user = provider;

    		emit TransferStart(user, provider);
    	}

    	function Start() public{
    		if(user.balance < coins){
    			emit NotEnough(address user);
    		}
    		else{
    			provider.transfer(coins);
        		user.transfer(address(this).balance);
    		}
    	}
    }