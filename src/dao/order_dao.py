from abc import ABCMeta, abstractmethod


class OrderDAO(metaclass=ABCMeta):

    @abstractmethod
    def insert_order_header(self):
        pass

    @abstractmethod
    def insert_order_item(self):
        pass

    @abstractmethod
    def get_max_order_no(self):
        pass
