"""
ダミーデータを追加するためのモジュール
"""


import dao.liquorDao


def main(args):
    """
    メイン関数
    """
    dao.liquorDao.liquorDao.addLiquor("sake", "ore", True, "2020/12/16", "1")
