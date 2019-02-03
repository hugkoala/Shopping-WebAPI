from abc import ABCMeta, abstractmethod


class CartDAO(metaclass=ABCMeta):

    @abstractmethod
    def insert_cart(self):
        pass

