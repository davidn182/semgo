from pyrocko.io import stationxml
from pyrocko import model
from pyrocko.example import get_example_data

dir = '/Volumes/Expansion/kwinstheul/03_metadata/'
# load pyrocko stations
stations = model.station.load_stations(dir + 'stations.txt')

import obspy
from obspy.core.inventory import Inventory, Network, Station, Channel, Site
from obspy.clients.nrl import NRL


# We'll first create all the various objects. These strongly follow the
# hierarchy of StationXML files.
inv = Inventory(
    # We'll add networks later.
    networks=[],
    # The source should be the id whoever create the file.
    source="TU Delft")

net = Network(
    # This is the network code according to the SEED standard.
    code="KW",
    # A list of stations. We'll add one later.
    stations=[],
    description="Kwinstheul Netherlands.",
    # Start-and end dates are optional.
    start_date=obspy.UTCDateTime(2019, 6, 21))
for i, station in enumerate(stations):

    sta = Station(
        # This is the station code according to the SEED standard.
        code="KW"+station.station,
        latitude=station.lat,
        longitude=station.lon,
        elevation=0,
        creation_date=obspy.UTCDateTime(2022, 2, 7),
        start_date=obspy.UTCDateTime(2019, 6, 21),
        end_date=obspy.UTCDateTime(2019, 11, 8),
        site=Site(name="Kwinstheul",
                  town='Kwinstheul',
                  region="South Holland",
                  country="Netherlands",
                  ))
    for channel in station.channels:
        cha = Channel(
            # This is the channel code according to the SEED standard.
            code=channel.name,
            # This is the location code according to the SEED standard.
            location_code="",
            # Note that these coordinates can differ from the station coordinates.
            latitude=station.lat,
            longitude=station.lon,
            elevation=0,
            depth=station.depth,
            azimuth=channel.azimuth,
            dip=channel.dip,
            sample_rate=250)
        
 
        # # By default this accesses the NRL online. Offline copies of the NRL can
        # # also be used instead
        # nrl = NRL()
        # # The contents of the NRL can be explored interactively in a Python prompt,
        # # see API documentation of NRL submodule:
        # # http://docs.obspy.org/packages/obspy.clients.nrl.html
        # # Here we assume that the end point of data logger and sensor are already
        # # known:
        # response = nrl.get_response( # doctest: +SKIP
        #     sensor_keys=['Streckeisen', 'STS-1', '360 seconds'],
        #     datalogger_keys=['REF TEK', 'RT 130 & 130-SMA', '1', '200'])
        
        # cha.response = response
        sta.channels.append(cha)   
        # Now tie it all together.

    net.stations.append(sta)

inv.networks.append(net)

# And finally write it to a StationXML file. We also force a validation against
# the StationXML schema to ensure it produces a valid StationXML file.
#
# Note that it is also possible to serialize to any of the other inventory
# output formats ObsPy supports.
inv.write(dir + "stations.xml", format="stationxml", validate=True)
