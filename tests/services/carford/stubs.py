# Local
from src.domain.models.carford.car_model import CarModel
from src.domain.models.carford.client_model import ClientModel

car_model_stub = CarModel(id=2, color="GRAY", model="HATCH", client_id=3)

car_model_list_stub = [
    CarModel(id=3, color="BLUE", model="CONVERTIBLE", client_id=4),
    CarModel(id=4, color="BLUE", model="SEDAN", client_id=4),
    CarModel(id=6, color="GRAY", model="HATCH", client_id=4),
]

car_input_list_stub = [
    {"color": "BLUE", "model": "HATCH", "client_id": 3},
    {"color": "BLUE", "model": "HATCH", "client_id": 8000},
]


client_model_list_stub = [
    ClientModel(id=1, email="jose@mail.com", sale_opportunity=True),
    ClientModel(id=4, email="rosinha@mail.com", sale_opportunity=False),
]

client_input_list_stub = [
    {"email": "jose@mail.com", "sale_opportunity": False},
    {"email": "matheus@mail.com", "sale_opportunity": True},
]
