// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

import "../node_modules/openzeppelin-solidity/contracts/token/ERC721/ERC721.sol";

contract Liquor is ERC721 {
    struct Liquor {
        uint256 tokenId;
        string liquorName;
        // struct LiquorInfo {
        //   string sellerName;
        //   bool isReservable;
        //   string arrivalDay;
        //   int reserveScore;
        // }
    }

    Liquor[] private liquorCollection;
    address private _contractCreator;

    constructor() public ERC721("Liquor", "LIQ") {
        _contractCreator = msg.sender;
    }
}
