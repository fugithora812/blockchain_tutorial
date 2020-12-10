// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

import "../node_module/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";

contract Liquor is ERC721Full {
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

    constructor() public ERC721Full("Liquor", "LIQ") {
        _contractCreator = msg.sender;
    }

    function fetchLiquorData(uint256 _tokenId) public view {
        return liquorCollection[_tokenId];
    }

    function getAllData() public view {
        return liquorCollection;
    }

    function changeBlock(uint256 _tokenId) external {
        uint256 newTokenId = liquorCollection.length + 1;
        super._mint(_contractCreator.newTokenId);
        liquorCollection.push(
            Liquor(
                newTokenId,
                liquorCollection[_tokenId].liquorName,
                false,
                liquorCollection[_tokenId].liquorInfo.arrivalDay,
                liquorCollection[_tokenId].liquorInfo.reserveScore
            )
        );
    }
}
