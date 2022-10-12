# Standard
from unittest.mock import patch

# Third Party
import pytest

# Local
from src.domain.exceptions.carford.exceptions import (
    CarNotExists,
    ClientCarsLimitExceeded,
    ClientNotExists,
    ClientNotSaleOpportunity,
)
from src.domain.models.carford.car_model import CarModel
from src.repositories.carford.car_repository import CarCarfordRepository
from src.services.carford.car_service import CarCarfordService
from src.services.carford.client_service import ClientCarfordService
from tests.services.carford.stubs import (
    car_input_list_stub,
    car_model_list_stub,
    car_model_stub,
)


@patch.object(CarCarfordRepository, "get_car_by_id", return_value=car_model_stub)
def test_verify_if_car_exists_by_id_when_car_id_is_valid_then_return_car_model(
    car_repository_mock,
):
    car = CarCarfordService._verify_if_car_exists_by_id(car_id=2)

    assert car
    assert isinstance(car, CarModel)


@patch.object(CarCarfordRepository, "get_car_by_id", return_value=None)
def test_verify_if_car_exists_by_id_when_car_id_is_invalid_then_raise_car_not_exists(
    car_repository_mock,
):
    with pytest.raises(CarNotExists):
        CarCarfordService._verify_if_car_exists_by_id(car_id=8000)


@patch.object(CarCarfordRepository, "get_all_cars", return_value=car_model_list_stub)
def test_get_all_cars_then_return_car_dict_list(car_repository_mock):
    cars = CarCarfordService.get_all_cars()

    assert type(cars) == list
    for car in cars:
        assert "id" in car
        assert "color" in car
        assert "model" in car
        assert "client_id" in car


@patch.object(CarCarfordRepository, "get_car_by_id", return_value=car_model_stub)
def test_get_car_by_id_when_car_id_is_valid_then_return_car_dict(car_repository_mock):
    car = CarCarfordService.get_car_by_id(car_id=2)

    assert car
    assert "id" in car
    assert "color" in car
    assert "model" in car
    assert "client_id" in car


@patch.object(CarCarfordRepository, "get_car_by_id", side_effect=CarNotExists)
def test_get_car_by_id_when_car_id_is_invalid_then_raise_car_not_exists(
    car_repository_mock,
):
    with pytest.raises(CarNotExists):
        CarCarfordService.get_car_by_id(car_id=8000)


@patch.object(ClientCarfordService, "verify_if_client_exists_by_id")
@patch.object(ClientCarfordService, "verify_client_sale_opportunity")
@patch.object(ClientCarfordService, "verify_client_cars_quantity")
@patch.object(CarCarfordRepository, "create_car")
def test_create_car_when_car_input_is_valid_then_create_a_new_car(
    car_repository_mock,
    client_service_verify_client_cars_quantity_mock,
    client_service_verify_client_sale_opportunity_mock,
    client_service_verify_if_client_exists_by_id_mock,
):
    CarCarfordService.create_car(new_car=car_input_list_stub[0])

    client_service_verify_if_client_exists_by_id_mock.assert_called_with(client_id=3)
    client_service_verify_client_sale_opportunity_mock.assert_called_with(client_id=3)
    client_service_verify_client_cars_quantity_mock.assert_called_with(client_id=3)
    car_repository_mock.assert_called_once()


@patch.object(
    ClientCarfordService, "verify_if_client_exists_by_id", side_effect=ClientNotExists
)
@patch.object(ClientCarfordService, "verify_client_sale_opportunity")
@patch.object(ClientCarfordService, "verify_client_cars_quantity")
@patch.object(CarCarfordRepository, "create_car")
def test_create_car_when_car_input_client_not_exists_then_raise_client_not_exists(
    car_repository_mock,
    client_service_verify_client_cars_quantity_mock,
    client_service_verify_client_sale_opportunity_mock,
    client_service_verify_if_client_exists_by_id_mock,
):
    with pytest.raises(ClientNotExists):
        CarCarfordService.create_car(new_car=car_input_list_stub[1])

    client_service_verify_if_client_exists_by_id_mock.assert_called_with(client_id=8000)
    client_service_verify_client_sale_opportunity_mock.assert_not_called()
    client_service_verify_client_cars_quantity_mock.assert_not_called()
    car_repository_mock.assert_not_called()


@patch.object(ClientCarfordService, "verify_if_client_exists_by_id")
@patch.object(
    ClientCarfordService,
    "verify_client_sale_opportunity",
    side_effect=ClientNotSaleOpportunity,
)
@patch.object(ClientCarfordService, "verify_client_cars_quantity")
@patch.object(CarCarfordRepository, "create_car")
def test_create_car_when_car_input_client_sale_opportunity_is_false_then_raise_client_not_sale_opportunity(
    car_repository_mock,
    client_service_verify_client_cars_quantity_mock,
    client_service_verify_client_sale_opportunity_mock,
    client_service_verify_if_client_exists_by_id_mock,
):
    with pytest.raises(ClientNotSaleOpportunity):
        CarCarfordService.create_car(new_car=car_input_list_stub[0])

    client_service_verify_if_client_exists_by_id_mock.assert_called_with(client_id=3)
    client_service_verify_client_sale_opportunity_mock.assert_called_with(client_id=3)
    client_service_verify_client_cars_quantity_mock.assert_not_called()
    car_repository_mock.assert_not_called()


@patch.object(ClientCarfordService, "verify_if_client_exists_by_id")
@patch.object(ClientCarfordService, "verify_client_sale_opportunity")
@patch.object(
    ClientCarfordService,
    "verify_client_cars_quantity",
    side_effect=ClientCarsLimitExceeded,
)
@patch.object(CarCarfordRepository, "create_car")
def test_create_car_when_car_input_client_already_had_three_cars_then_raise_client_cars_limit_exceeded(
    car_repository_mock,
    client_service_verify_client_cars_quantity_mock,
    client_service_verify_client_sale_opportunity_mock,
    client_service_verify_if_client_exists_by_id_mock,
):
    with pytest.raises(ClientCarsLimitExceeded):
        CarCarfordService.create_car(new_car=car_input_list_stub[0])

    client_service_verify_if_client_exists_by_id_mock.assert_called_with(client_id=3)
    client_service_verify_client_sale_opportunity_mock.assert_called_with(client_id=3)
    client_service_verify_client_cars_quantity_mock.assert_called_with(client_id=3)
    car_repository_mock.assert_not_called()


@patch.object(CarCarfordRepository, "get_car_by_id", return_value=car_model_stub)
@patch.object(CarCarfordRepository, "delete_car_by_id")
def test_delete_car_by_id_car_id_is_valid_then_delete_the_car(
    car_repository_delete_car_by_id, car_repository_get_car_by_id_mock
):
    CarCarfordService.delete_car_by_id(car_id=2)

    car_repository_get_car_by_id_mock.assert_called_with(car_id=2)
    car_repository_delete_car_by_id.assert_called_with(car_id=2)


@patch.object(CarCarfordRepository, "get_car_by_id", return_value=None)
@patch.object(CarCarfordRepository, "delete_car_by_id")
def test_delete_car_by_id_car_id_is_invalid_then_raise_car_not_exists(
    car_repository_delete_car_by_id, car_repository_get_car_by_id_mock
):
    with pytest.raises(CarNotExists):
        CarCarfordService.delete_car_by_id(car_id=8000)

    car_repository_get_car_by_id_mock.assert_called_with(car_id=8000)
    car_repository_delete_car_by_id.assert_not_called()
