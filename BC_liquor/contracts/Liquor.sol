// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;
pragma experimental ABIEncoderV2;

import "../node_module/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";

contract Liquor is ERC721Full {
    struct Liquor {
        uint256 tokenId;
        string liquorName;
        string sellerName;
        bool isReservable;
        string arrivalDay;
        string reserveScore;
    }

    Liquor[] private liquorCollection;
    address private _contractOwner;

    constructor() public ERC721Full("Liquor", "LIQ") {
        _contractOwner = msg.sender;
    }

    function fetchLiquor(uint256 _tokenId) public returns (string memory) {
        string memory liquor = strConnect(
            "{liquorName:",
            liquorCollection[_tokenId].liquorName,
            "sellerName:",
            liquorCollection[_tokenId].sellerName,
            "isReservable:",
            boolToString(liquorCollection[_tokenId].isReservable),
            "arrivalDay:",
            liquorCollection[_tokenId].arrivalDay,
            "reserveScore:",
            liquorCollection[_tokenId].reserveScore,
            "}"
        );
        return liquor;
    }

    function fetchAllLiquors() public returns (string[] memory) {
        string[] memory liquors = new string[](liquorCollection.length);
        for (uint256 i = 0; i < liquorCollection.length; i++) {
            liquors[i] = strConnect(
                "{liquorName:",
                liquorCollection[i].liquorName,
                "sellerName:",
                liquorCollection[i].sellerName,
                "isReservable:",
                boolToString(liquorCollection[i].isReservable),
                "arrivalDay:",
                liquorCollection[i].arrivalDay,
                "reserveScore:",
                liquorCollection[i].reserveScore,
                "}"
            );
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
        string memory liquorName,
        string memory sellerName,
        bool isReservable,
        string memory arrivalDay,
        string memory reserveScore
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

    // 文字列11個を結合する
    function strConnect(
        string memory str1,
        string memory str2,
        string memory str3,
        string memory str4,
        string memory str5,
        string memory str6,
        string memory str7,
        string memory str8,
        string memory str9,
        string memory str10,
        string memory str11
    ) public returns (string memory) {
        bytes memory strbyte1 = bytes(str1);
        bytes memory strbyte2 = bytes(str2);
        bytes memory strbyte3 = bytes(str3);
        bytes memory strbyte4 = bytes(str4);
        bytes memory strbyte5 = bytes(str5);
        bytes memory strbyte6 = bytes(str6);
        bytes memory strbyte7 = bytes(str7);
        bytes memory strbyte8 = bytes(str8);
        bytes memory strbyte9 = bytes(str9);
        bytes memory strbyte10 = bytes(str10);
        bytes memory strbyte11 = bytes(str11);

        bytes memory str = new bytes(strbyte1.length + strbyte2.length);

        uint8 point = 0;

        for (uint8 j = 0; j < strbyte1.length; j++) {
            str[point] = strbyte1[j];
            point++;
        }
        for (uint8 k = 0; k < strbyte2.length; k++) {
            str[point] = strbyte2[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte3.length; k++) {
            str[point] = strbyte3[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte4.length; k++) {
            str[point] = strbyte4[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte5.length; k++) {
            str[point] = strbyte5[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte6.length; k++) {
            str[point] = strbyte6[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte7.length; k++) {
            str[point] = strbyte7[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte8.length; k++) {
            str[point] = strbyte8[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte9.length; k++) {
            str[point] = strbyte9[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte10.length; k++) {
            str[point] = strbyte10[k];
            point++;
        }
        for (uint8 k = 0; k < strbyte11.length; k++) {
            str[point] = strbyte11[k];
            point++;
        }
        return string(str);
    }

    // boolをstringに変換する
    function boolToString(bool boolean) internal returns (string memory) {
        if (boolean == true) {
            return "true";
        } else {
            return "false";
        }
    }

    //uint から string へ変換
    // function uintToString(uint256 v) returns (string memory) {
    //     uint256 maxlength = 100;
    //     bytes reversed = new bytes(maxlength);
    //     uint256 i = 0;
    //     while (v != 0) {
    //         // 1の位を取り出し
    //         uint256 remainder = v % 10;

    //         // 位を一桁左にシフト
    //         v = v / 10;

    //         reversed[i++] = bytes(48 + remainder);
    //     }
    //     bytes memory s = new bytes(i + 1);
    //     for (uint256 j = 0; j <= i; j++) {
    //         s[j] = reversed[i - j];
    //     }
    //     string memory str = string(s);

    //     return str;
    // }
}
