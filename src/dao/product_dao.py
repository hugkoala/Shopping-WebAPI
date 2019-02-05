from abc import ABCMeta, abstractmethod


class ProductDAO(metaclass=ABCMeta):

    @abstractmethod
    def get_product(self):
        pass
