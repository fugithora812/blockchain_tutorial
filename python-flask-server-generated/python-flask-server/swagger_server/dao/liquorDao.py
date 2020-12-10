from web3 import Web3
import sqlite3


class liquorDao:
    tokenId: string

    def fetchDataFromBC(tokenId: int) -> string:
        web3: Web3 = new Web3(web3.currentProvider)
        # abi :string = コントラクトABI
        # contractAddress :int = コントラクトアドレス
        liquors = new web3py.eth.Contract(abi, contractAddress)
        return liquors.methods.fetchLiquorData(tokenId).call()
