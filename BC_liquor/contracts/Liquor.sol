// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

import "../node_module/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";

contract Liquor is ERC721Full {
    struct Liquor {
        uint256 tokenId;
        string liquorName;
        mapping(uint256 => LiquorInfo) liquorInfo;
    }
    struct LiquorInfo {
        string sellerName;
        bool isReservable;
        string arrivalDay;
        int256 reserveScore;
    }

    Liquor[] private liquorCollection;
    address private _contractCreator;

    constructor() public ERC721Full("Liquor", "LIQ") {
        _contractCreator = msg.sender;
    }

    function fetchLiquorData(uint256 _tokenId)
        public
        view
        returns (Liquor memory)
    {
        return liquorCollection[_tokenId];
    }

    function getAllData() public view returns (Liquor[] memory) {
        return liquorCollection;
    }

    function changeBlock(uint256 _tokenId) external returns (uint256) {
        uint256 newTokenId = liquorCollection.length + 1;
        super._mint(_contractCreator, newTokenId);
        liquorCollection.push(
            Liquor(
                newTokenId,
                liquorCollection[_tokenId].liquorName,
                false,
                liquorCollection[_tokenId].liquorInfo
            )
        );
        return newTokenId;
    }
}
