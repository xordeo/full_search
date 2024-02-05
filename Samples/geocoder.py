import requests


def get_coordinates(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    toponym_coodrinates = toponym["Point"]["pos"]

    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    return toponym_longitude, toponym_lattitude


def get_ll_span(toponym_to_find):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "911a3d6d-4b36-4b31-bbc1-f158fd0cd2eb"

    address_ll = get_coordinates(toponym_to_find)
    address_ll = address_ll[0] + "," + address_ll[1]

    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"
    }
    response = requests.get(search_api_server, params=search_params)

    json_response = response.json()
    organization = json_response["features"][0]
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]

    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    delta = "0.005"
    return org_point, f"{delta},{delta}"
