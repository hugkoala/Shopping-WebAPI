from dao.dao_utils import DAOUtils;
from dao.dborm import UserLog;


class LogUtils:

    @staticmethod
    def insert_user_log(db=None, user_id=None, action=None, remark=None):
        """
        Add User Action Log
        :param db: Session
        :param user_id: User ID
        :param action: 加入商品至購物車、移除商品至購物車、會員存款、購物車結帳
        :param remark:
        """
        user_log = UserLog(user_id=user_id, action=action, remark=remark)
        try:
            DAOUtils.get_user_log_dao().insert_user_log(db, user_log)
        except:
            raise
