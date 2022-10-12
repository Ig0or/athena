# Standard
from unittest.mock import patch

# Third Party
import pytest

# Local
from src.domain.exceptions.carford.exceptions import (
    ClientAlreadyExists,
    ClientCarsLimitExceeded,
    ClientNotExists,
    ClientNotSaleOpportunity,
)
from src.domain.models.carford.client_model import ClientModel
from src.repositories.carford.car_repository import CarCarfordRepository
from src.repositories.carford.client_repository import ClientCarfordRepository
from src.services.carford.client_service import ClientCarfordService
from tests.services.carford.stubs import (
    car_model_list_stub,
    client_input_list_stub,
    client_model_list_stub,
)


@patch.object(
    ClientCarfordRepository, "get_client_by_id", return_value=client_model_list_stub[0]
)
def test_verify_if_client_exists_by_id_when_client_id_is_valid_then_return_client_model(
    client_repository_mock,
):
    client = ClientCarfordService.verify_if_client_exists_by_id(client_id=1)

    assert client
    assert isinstance(client, ClientModel)


@patch.object(ClientCarfordRepository, "get_client_by_id", return_value=None)
def test_verify_if_client_exists_by_id_when_client_id_is_invalid_then_raise_client_not_exists(
    client_repository_mock,
):
    with pytest.raises(ClientNotExists):
        ClientCarfordService.verify_if_client_exists_by_id(client_id=8000)


@patch.object(
    ClientCarfordRepository, "get_client_by_id", return_value=client_model_list_stub[1]
)
def test_verify_client_sale_opportunity_when_client_sale_opportunity_is_false_then_raise_client_not_sale_opportunity(
    client_repository_mock,
):
    with pytest.raises(ClientNotSaleOpportunity):
        ClientCarfordService.verify_client_sale_opportunity(client_id=1)


@patch.object(
    ClientCarfordRepository, "get_client_by_id", return_value=client_model_list_stub[0]
)
def test_verify_client_sale_opportunity_when_client_sale_opportunity_is_true_then_dont_raise_client_not_sale_opportunity(
    client_repository_mock,
):
    ClientCarfordService.verify_client_sale_opportunity(client_id=1)


@patch.object(
    CarCarfordRepository, "get_cars_by_client_id", return_value=car_model_list_stub
)
def test_verify_client_cars_quantity_when_client_already_had_three_cars_then_raise_client_cars_limit_exceeded(
    car_repository_mock,
):
    with pytest.raises(ClientCarsLimitExceeded):
        ClientCarfordService.verify_client_cars_quantity(client_id=1)


@patch.object(CarCarfordRepository, "get_cars_by_client_id", return_value=[])
def test_verify_client_cars_quantity_when_client_already_had_less_then_three_cars_then_dont_raise_client_cars_limit_exceeded(
    car_repository_mock,
):
    ClientCarfordService.verify_client_cars_quantity(client_id=2)


@patch.object(
    ClientCarfordRepository, "get_all_clients", return_value=client_model_list_stub
)
def test_get_all_clients_then_return_client_dict_list(client_repository_mock):
    clients = ClientCarfordService.get_all_clients()

    assert type(clients) == list
    for client in clients:
        assert "id" in client
        assert "email" in client
        assert "sale_opportunity" in client


@patch.object(
    CarCarfordRepository, "get_cars_by_client_id", return_value=car_model_list_stub
)
@patch.object(
    ClientCarfordRepository, "get_client_by_id", return_value=client_model_list_stub[1]
)
def test_get_client_by_id_when_client_id_is_valid_then_return_client_dict(
    client_repository_mock, car_repository_mock
):
    client = ClientCarfordService.get_client_by_id(client_id=4)

    assert type(client) == dict
    assert "id" in client
    assert "email" in client
    assert "sale_opportunity" in client
    assert "cars" in client


@patch.object(ClientCarfordRepository, "get_client_by_id", return_value=None)
def test_get_client_by_id_when_client_id_is_invalid_then_raise_client_not_exists(
    client_repository_mock,
):
    with pytest.raises(ClientNotExists):
        ClientCarfordService.get_client_by_id(client_id=8000)


@patch.object(ClientCarfordRepository, "create_client")
@patch.object(
    ClientCarfordRepository,
    "get_client_by_email",
    return_value=client_model_list_stub[0],
)
def test_create_client_when_client_email_already_exists_then_raise_client_already_exists(
    client_repository_get_client_by_email_mock, client_repository_create_client
):
    with pytest.raises(ClientAlreadyExists):
        ClientCarfordService.create_client(new_client=client_input_list_stub[0])

    client_repository_create_client.assert_not_called()


@patch.object(ClientCarfordRepository, "create_client")
@patch.object(ClientCarfordRepository, "get_client_by_email", return_value=None)
def test_create_client_when_client_is_valid_then_create_client(
    client_repository_get_client_by_email_mock, client_repository_create_client
):
    ClientCarfordService.create_client(new_client=client_input_list_stub[1])

    client_repository_create_client.assert_called_once()


@patch.object(ClientCarfordRepository, "get_client_by_id", return_value=None)
@patch.object(ClientCarfordRepository, "update_client_by_id")
def test_update_client_by_id_when_client_id_is_invalid_then_raise_client_not_exists(
    client_repository_update_client_by_id_mock, client_repository_get_client_by_id_mock
):
    with pytest.raises(ClientNotExists):
        ClientCarfordService.update_client_by_id(
            client_changes=client_input_list_stub[0], client_id=8000
        )

    client_repository_update_client_by_id_mock.assert_not_called()


@patch.object(
    ClientCarfordRepository, "get_client_by_id", return_value=client_model_list_stub[0]
)
@patch.object(ClientCarfordRepository, "update_client_by_id")
def test_update_client_by_id_when_client_is_valid_then_update_client(
    client_repository_update_client_by_id_mock, client_repository_get_client_by_id_mock
):
    ClientCarfordService.update_client_by_id(
        client_changes=client_input_list_stub[0], client_id=1
    )

    client_repository_update_client_by_id_mock.assert_called_once()


@patch.object(ClientCarfordRepository, "get_client_by_id", return_value=None)
@patch.object(ClientCarfordRepository, "delete_client_by_id")
@patch.object(CarCarfordRepository, "delete_car_by_client_id")
def test_delete_client_by_id_when_client_id_is_invalid_then_raise_client_not_exists(
    car_repository_delete_car_by_client_id_mock,
    client_repository_delete_client_by_id_mock,
    client_repository_get_client_by_id_mock,
):
    with pytest.raises(ClientNotExists):
        ClientCarfordService.delete_client_by_id(client_id=8000)

    client_repository_delete_client_by_id_mock.assert_not_called()
    car_repository_delete_car_by_client_id_mock.assert_not_called()


@patch.object(
    ClientCarfordRepository, "get_client_by_id", return_value=client_model_list_stub[0]
)
@patch.object(ClientCarfordRepository, "delete_client_by_id")
@patch.object(CarCarfordRepository, "delete_car_by_client_id")
def test_delete_client_by_id_when_client_id_is_valid_then_delete_client_and_their_cars(
    car_repository_delete_car_by_client_id_mock,
    client_repository_delete_client_by_id_mock,
    client_repository_get_client_by_id_mock,
):
    ClientCarfordService.delete_client_by_id(client_id=1)

    client_repository_delete_client_by_id_mock.assert_called_once()
    car_repository_delete_car_by_client_id_mock.assert_called_once()
