# Local
from src.domain.models.carford.car_model import CarModel

car_model_stub = CarModel(id=2, color="GRAY", model="HATCH", client_id=3)

car_model_list_stub = [
    CarModel(id=2, color="GRAY", model="HATCH", client_id=3),
    CarModel(id=3, color="BLUE", model="CONVERTIBLE", client_id=4),
]

car_input_list_stub = [
    {"color": "BLUE", "model": "HATCH", "client_id": 3},
    {"color": "BLUE", "model": "HATCH", "client_id": 8000},
]
