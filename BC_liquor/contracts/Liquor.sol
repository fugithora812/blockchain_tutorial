// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

import "../node_module/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";

contract Liquor is ERC721Full {
    struct Liquor {
        uint256 tokenId;
        string liquorName;
        string sellerName;
        bool isReservable;
        string arrivalDay;
        uint256 reserveScore;
    }

    Liquor[] private liquorCollection;
    address private _contractOwner;

    constructor() public ERC721Full("Liquor", "LIQ") {
        _contractOwner = msg.sender;
    }

    function fetchLiquor(uint256 _tokenId) public view returns (string) {
        string liquor = "{liquorName:" +
            liquorCollection[_tokenId].liquorName +
            "sellerName:" +
            liquorCollection[_tokenId].sellerName +
            "isReservable:" +
            liquorCollection[_tokenId].isReservable +
            "arrivalDay:" +
            liquorCollection[_tokenId].arrivalDay +
            "reserveScore:" +
            liquorCollection[_tokenId].reserveScore +
            "}";
        return liquor;
    }

    function fetchAllLiquors() public view returns (string[] memory) {
        string[] memory liquors = new string[](liquorCollection.length);
        for (int256 i = 0; i < liquorCollection.length; i++) {
            liquors[i] =
                "{liquorName:" +
                liquorCollection[_tokenId].liquorName +
                "sellerName:" +
                liquorCollection[_tokenId].sellerName +
                "isReservable:" +
                liquorCollection[_tokenId].isReservable +
                "arrivalDay:" +
                liquorCollection[_tokenId].arrivalDay +
                "reserveScore:" +
                liquorCollection[_tokenId].reserveScore +
                "}";
        }
        return liquors;
    }

    function updateReservability(uint256 _tokenId) external {
        if (liquorCollection[_tokenId].isReservable == true) {
            liquorCollection[_tokenId].isReservable = false;
        } else {
            liquorCollection[_tokenId].isReservable = true;
        }
    }

    function addBlockToRegister(
        string liquorName,
        string sellerName,
        bool isReservable,
        string arrivalDay,
        uint256 reserveScore
    ) public {
        uint256 newTokenId = liquorCollection.length + 1;
        liquorCollection.push(
            Liquor(
                newTokenId,
                liquorName,
                sellerName,
                isReservable,
                arrivalDay,
                reserveScore
            )
        );
    }
}
