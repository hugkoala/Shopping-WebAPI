from abc import ABCMeta, abstractmethod


class UserDAO(metaclass=ABCMeta):

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_users(self, condition, **kwargs):
        pass

    @abstractmethod
    def get_user(self, condition, **kwargs):
        pass

    @abstractmethod
    def insert_user(self):
        pass

