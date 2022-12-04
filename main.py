import json

import geopandas
import matplotlib.pyplot as plt


def main():
    type = 'auto'  # auto | velo

    dpi = 300

    with open('status_street.json') as f:
        status = json.load(f)
    with open('typology_streets.json') as f:
        typology = json.load(f)
    with open('morphology_streets.json') as f:
        morphology = json.load(f)
    with open('bike_future_velo.json') as f:
        morphology_bike = json.load(f)

    lane_data = geopandas.read_file('streets.json')
    bike = geopandas.read_file('bike_future.json')
    mailles = geopandas.read_file('mailles.json')
    auto = geopandas.read_file('auto.json')

    # Autoroute, chaussées séparées, chaussées uniques, rond-point (see morphology for codes)
    streets = lane_data[
        (lane_data['morphology'] == '101') | (lane_data['morphology'] == '102') | (lane_data['morphology'] == '103') | (
                    lane_data['morphology'] == '104')]

    # chemin de fer
    rail = lane_data[lane_data['morphology'] == '116']  # is not complete

    # bike
    bike_quartier = bike[(bike['velo'] == 3) | (bike['velo'] == 5)]
    bike_confort = bike[(bike['velo'] == 2) | (bike['velo'] == 31) | (bike['velo'] == 38) | (bike['velo'] == 39)]
    bike_plus = bike[(bike['velo'] == 1) | (bike['velo'] == 11) | (bike['velo'] == 14)]

    # cars
    auto_plus = auto[(auto['auto'] == 11) | (auto['auto'] == 14) | (auto['auto'] == 21) | (auto['auto'] == 1)]
    auto_confort = auto[(auto['auto'] == 31) | (auto['auto'] == 34) | (auto['auto'] == 39) | (auto['auto'] == 2)]

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(33 + 1 / 8, 46 + 13 / 16, forward=True)
    fig.set_dpi(dpi)

    if type == 'velo':

        streets.plot(ax=ax, color='grey', linewidth=1)
        bike_confort.plot(ax=ax, color='blue', linewidth=2)
        bike_plus.plot(ax=ax, color='red', linewidth=4)
        mailles.boundary.plot(ax=ax, color='green', linewidth=1, linestyle='dotted')

        # streets.plot()
        # plt.show()
        plt.savefig('map_velo.png', dpi=dpi)

    elif type == 'auto':

        mailles.plot(column='name_fr', ax=ax, categorical=True, legend=True)
        streets.plot(ax=ax, color='black', linewidth=1, legend=True, categorical=True, missing_kwds={'color': 'lightgrey'})
        auto_plus.plot(ax=ax, color='pink', linewidth=10, legend=True, categorical=True)
        auto_confort.plot(ax=ax, color='orange', linewidth=6)
        bike_confort.plot(ax=ax, color='blue', linewidth=1)
        bike_plus.plot(ax=ax, color='red', linewidth=2)
        # mailles.boundary.plot(ax=ax, color='green', linewidth=1, linestyle='dotted')


        # streets.plot()
        # plt.show()
        plt.savefig('map_auto.png', dpi=dpi)



if __name__ == '__main__':
    main()
