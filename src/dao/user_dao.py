from abc import ABCMeta, abstractmethod


class UserDAO(metaclass=ABCMeta):

    @abstractmethod
    def insert_user(self):
        pass

    @abstractmethod
    def get_users(self):
        pass
