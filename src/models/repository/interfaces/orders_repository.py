from abc import ABC, abstractmethod


class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_document(self, document: dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_document(self, list_of_document: list) -> None:
        pass

    @abstractmethod
    def select_many(self, doc_filter: dict) -> list:
        pass

    @abstractmethod
    def select_one(self, doc_filter: dict) -> dict:
        pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter: dict) -> list:
        pass

    @abstractmethod
    def select_if_property_exists(self) -> dict:
        pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> dict:
        pass

    @abstractmethod
    def edit_registry(self, order_id: str, update_fields: dict) -> None:
        pass

    @abstractmethod
    def edit_many_registries(self) -> None:
        pass

    @abstractmethod
    def edit_registry_with_increment(self) -> None:
        pass

    @abstractmethod
    def delete_registry(self) -> None:
        pass

    @abstractmethod
    def delete_many_registries(self) -> None:
        pass
        