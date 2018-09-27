#$python HW3A.py <MTA_KEY> <BUS_LINE>
import pylab as pl
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
key = sys.argv[1]
BusLine = sys.argv[2]
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + key +\
    "&VehicleMonitoringDetailLevel=calls&LineRef=" + BusLine
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
x = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print ('Bus Line :' + BusLine )
print ('Number of Active Buses:' + str(x))
for i in range(x):
    lat= data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long =data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus " +str(i) + " is at Latitude " + str(lat) + " and longitude " + str(long))