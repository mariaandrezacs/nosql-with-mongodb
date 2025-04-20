import pytest

from ..connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="Interação com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"ola": "mundo", "valor": 5}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="Interação com o banco")
def test_insert_list_of_document():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1": "aqui1"}, {"elem2": "aqui2"}, {"elem3": "aqui3"}]
    orders_repository.insert_list_of_document(my_doc)

@pytest.mark.skip(reason="Interação com o banco")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="Interação com o banco")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)


@pytest.mark.skip(reason="Interação com o banco")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="Interação com o banco")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()
    print(response)
    for doc in response:
        print(doc)
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="Interação com o banco")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True, 
        "itens.doce": {"$exists": True}
    } # semelhante a uma busca com AND em SQL
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()


@pytest.mark.skip(reason="Interação com o banco")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"address": {"$exists": True}},
            {"itens.doce.tipo": "chocolate"}
            ]
        } # semelhante a uma busca com OR em SQL
    response = orders_repository.select_many(doc_filter)
    print()
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interação com o banco")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "680295e9ecfd12795f32a7d0"
    response = orders_repository.select_by_object_id(object_id)
    print()
    print(response)


@pytest.mark.skip(reason="Interação com o banco")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry()


@pytest.mark.skip(reason="Interação com o banco")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registries()

@pytest.mark.skip(reason="Interação com o banco")
def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry_with_increment()


@pytest.mark.skip(reason="Interação com o banco")
def test_delete_registry():
    orders_repository = OrdersRepository(conn)
    orders_repository.delete_registry()


@pytest.mark.skip(reason="Interação com o banco")
def test_delete_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.delete_many_registries()
