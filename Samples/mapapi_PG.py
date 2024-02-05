import requests
from PIL import Image
from io import BytesIO


def show_map(ll_spn, type, add_params=""):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    if add_params == "":
        response = requests.get(f"{map_api_server}?{ll_spn}&l={type}")
    else:
        response = requests.get(f"{map_api_server}?{ll_spn}&l={type}&{add_params}")

    Image.open(BytesIO(
        response.content)).show()
