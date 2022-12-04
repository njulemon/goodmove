import json

import geopandas
import matplotlib.pyplot as plt


def main():

    dpi=300



    data = geopandas.read_file('UrbDTM_ContourLine_2012.gml')

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(33+1/8, 46+13/16, forward=True)
    fig.set_dpi(dpi)

    data.plot(ax=ax, color='grey', linewidth=1)




    # streets.plot()
    # plt.show()
    plt.savefig('map.png', dpi=dpi)


if __name__ == '__main__':
    main()
