import dao.liquorDao


def liquors_get():
    """酒類在庫取得API"""

    return dao.liquorDao.liquorDao.fetchAllLiquorsFromBC()


def liquors_add(liquorName, sellerName, isReservable, arrivalDay, stockQuantity):
    """酒類在庫追加API"""
    return dao.liquorDao.liquorDao.addLiquor(liquorName, sellerName, isReservable, arrivalDay, stockQuantity)


def liquors_reserve(liquorName):
    """酒類取り置き依頼の処理API"""
    return dao.liquorDao.liquorDao.updateStockOnDB(liquorName)


def liquors_search(liquorName):
    """酒類在庫検索API"""
    tokenId = dao.liquorDao.liquorDao.fetchTokenIdFromDB(liquorName)
    liquorData = dao.liquorDao.liquorDao.fetchLiquorFromBC(tokenId)
    return liquorData
