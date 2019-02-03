from abc import ABCMeta, abstractmethod


class CartDAO(metaclass=ABCMeta):

    @abstractmethod
    def insert_cart(self):
        pass

    @abstractmethod
    def get_cart(self):
        pass

    @abstractmethod
    def delete_cart(self):
        pass
