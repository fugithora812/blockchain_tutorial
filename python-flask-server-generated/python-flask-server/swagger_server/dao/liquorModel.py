import sys
from sqlalchemy import Column, Integer, String
import dao.database


class Liquor(dao.database.Base):
    """
    酒モデル
    """
    __tablename__ = "liquor_table"

    LIQUOR_NAME = Column(String(32), primary_key=True)
    SELLER_NAME = Column(String(32), primary_key=True)
    STOCK_QUANTITY = Column(Integer)
    TOKEN_ID = Column(Integer)


def main(args):
    """
    メイン関数
    """
    dao.database.Base.metadata.create_all(bind=dao.database.engine)


if __name__ == "__main__":
    main(sys.argv)
