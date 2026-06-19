# tee ratkaisu tänne
# Write your solution here
import math 
def greatest_distance(stations: dict):
    greatest = 0
    st1_g = ""
    st2_g = ""
    for key_outer, values_outer in stations.items():
        for key_inner, values_inner in stations.items():
            distance_km = distance(stations,key_outer,key_inner)
            if distance_km > greatest:
                greatest = distance_km
                st2_g = key_inner
                st1_g = key_outer
    return (st1_g, st2_g, greatest)


def get_station_data(filename: str):
    station_data = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[3] == "name":
                continue
            station_data[parts[3]] = (float(parts[0]),float(parts[1]))
    return station_data

def distance(stations: dict, station1: str, station2: str):
    longitude1 = float(stations[station1][0])
    longitude2 = float(stations[station2][0])

    latitude1 = float(stations[station1][1])
    latitude2 = float(stations[station2][1])

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
