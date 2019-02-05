from .dao_utils import DAOUtils;
from .user_log_dao import UserLogDAO;
from .dborm import User, UserLog;


class UserLogDAOImpl(UserLogDAO):

    @staticmethod
    def insert_user_log(user_log):
        try:
            DAOUtils.insert(user_log)
        except:
            raise




