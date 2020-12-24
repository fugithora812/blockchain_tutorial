// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;
pragma experimental ABIEncoderV2;

import "../node_module/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";

contract Liquor is ERC721Full {
    struct Liquor {
        uint256 tokenId;
        string liquorName;
        string sellerName;
        string isReservable;
        string arrivalDay;
        string reserveScore;
    }

    Liquor[] private liquorCollection;
    address private _contractOwner;

    event Transfer(
        address indexed _from,
        address indexed _to,
        uint256 indexed _tokenId
    );

    constructor() public ERC721Full("Liquor", "LIQ") {
        _contractOwner = msg.sender;
    }

    function fetchLiquor(uint256 _tokenId)
        public
        view
        returns (string[] memory)
    {
        string[] memory liquorResult = new string[](5);
        liquorResult[0] = liquorCollection[_tokenId].liquorName;
        liquorResult[1] = liquorCollection[_tokenId].sellerName;
        liquorResult[2] = liquorCollection[_tokenId].isReservable;
        liquorResult[3] = liquorCollection[_tokenId].arrivalDay;
        liquorResult[4] = liquorCollection[_tokenId].reserveScore;
        return liquorResult;
    }

    function fetchAllLiquors() public view returns (string[] memory) {
        string[] memory liquors = new string[](liquorCollection.length * 5);
        uint256 contentNumber = 0;
        for (uint256 i = 0; i < liquorCollection.length; i++) {
            liquors[contentNumber] = liquorCollection[i].liquorName;
            contentNumber = contentNumber + 1;

            liquors[contentNumber] = liquorCollection[i].sellerName;
            contentNumber = contentNumber + 1;

            liquors[contentNumber] = liquorCollection[i].isReservable;
            contentNumber = contentNumber + 1;

            liquors[contentNumber] = liquorCollection[i].arrivalDay;
            contentNumber = contentNumber + 1;

            liquors[contentNumber] = liquorCollection[i].reserveScore;
            contentNumber = contentNumber + 1;
        }
        return liquors;
    }

    // ToDo: 在庫数のアップデート機能を追加
    // function updateReservability(uint256 _tokenId) external {
    //     if (stringToBool(liquorCollection[_tokenId].isReservable) == true) {
    //         liquorCollection[_tokenId].isReservable = "true";
    //     } else {
    //         liquorCollection[_tokenId].isReservable = "false";
    //     }
    // }

    function addBlockToRegister(
        string memory liquorName,
        string memory sellerName,
        string memory isReservable,
        string memory arrivalDay,
        string memory reserveScore
    ) public payable returns (bool) {
        uint256 newTokenId = liquorCollection.length;
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
        emit Transfer(msg.sender, _contractOwner, liquorCollection.length);
        return true;
    }

    // boolをstringに変換する
    function boolToString(bool boolean) internal pure returns (string memory) {
        if (boolean == true) {
            return "true";
        } else {
            return "false";
        }
    }

    // string を bool に変換する
    function stringToBool(string memory boolStr) internal pure returns (bool) {
        if (keccak256(bytes(boolStr)) == keccak256("true")) {
            return true;
        } else {
            return false;
        }
    }
}
