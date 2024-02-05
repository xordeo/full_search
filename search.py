import sys

from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import show_map


def main():
    toponym_to_find = input()

    if toponym_to_find:
        lat, lon = get_coordinates(toponym_to_find)
        ll_spn = f"ll={lat},{lon}&spn=0.005,0.005"
        show_map(ll_spn, "map")

        ll, spn = get_ll_span(toponym_to_find)
        ll_spn = f"ll={ll}&spn={spn}"
        show_map(ll_spn, "map")

        point_param = f"pt={ll}"
        show_map(ll, "map", add_params=point_param)

    else:
        print("No data")


if __name__ == "__main__":
    main()
