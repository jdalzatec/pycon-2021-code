from abc import ABCMeta, abstractmethod


class CRUD(metaclass=ABCMeta):
    @abstractmethod
    def add_item(self, **kwargs):
        raise NotImplemented("add_item is not implemented")

    @abstractmethod
    def get_item(self, todo_id):
        raise NotImplemented("get_item is not implemented")

    @abstractmethod
    def update_item(self, todo_id, **kwargs):
        raise NotImplemented("update_item is not implemented")

    @abstractmethod
    def delete_item(self, todo_id):
        raise NotImplemented("delete_item is not implemented")

    @abstractmethod
    def get_all_items(self, query={}):
        raise NotImplemented("get_all_items is not implemented")
