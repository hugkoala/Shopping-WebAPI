from abc import ABCMeta, abstractmethod


class UserLogDAO(metaclass=ABCMeta):

    @abstractmethod
    def insert_user_log(self):
        pass
