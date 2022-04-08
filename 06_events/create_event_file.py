#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:05:00 2022

@author: davidnaranjo
"""

from obspy import Catalog, UTCDateTime
from obspy.core.event import Event
from obspy.core.event.base import CreationInfo
from obspy.core.event import Origin
from obspy.core.event.magnitude import Magnitude
import obspy

out_dir = '/Volumes/Expansion/kwinstheul/06_events/'

origin=Origin()

origin.time = obspy.UTCDateTime('2019-07-14T08:48:30')
origin.latitude=4.2878
origin.longitude=52.0068
origin.depth=2.46
origin.depth_type="operator assigned"

mag = Magnitude()
mag.mag = 0.16
mag.magnitude_type="Md"
    
    
cat = Catalog()
ev = Event(
    event_type='not existing',
    creation_info=CreationInfo(
        agency_id="TU Delft (d.f.naranjohernandez@tudelft.nl)",
        author='obspy.org',
        version='1.1.0'),
    origins=[origin],
    magnitudes=[mag]
    )
cat.events = [ev]

cat.write(out_dir+"events.xml", format="QUAKEML")  


