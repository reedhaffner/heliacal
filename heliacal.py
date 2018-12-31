import datetime
import json
import urllib.request


class Heliacal:
    def _update(self):
        url = urllib.request.urlopen(f"https://api.sunrise-sunset.org/json?lat={self.latitude}&lng={self.longitude}&date={self.date}&formatted=0")
        data = url.read()
        jsondata = json.loads(data)["results"]
        self.requesturl = f"https://api.sunrise-sunset.org/json?lat={self.latitude}&lng={self.longitude}&date={self.date}&formatted=0"
        self.json = jsondata
        self.sunrise = datetime.datetime.strptime(jsondata["sunrise"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.sunset = datetime.datetime.strptime(jsondata["sunset"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.solarnoon = datetime.datetime.strptime(jsondata["solar_noon"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.daylength = jsondata["day_length"]
        self.civiltwilightbegin = datetime.datetime.strptime(jsondata["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.civiltwilightend = datetime.datetime.strptime(jsondata["civil_twilight_end"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.nauticaltwilightbegin = datetime.datetime.strptime(jsondata["nautical_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.nauticaltwilightend = datetime.datetime.strptime(jsondata["nautical_twilight_end"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.astronomicaltwilightbegin = datetime.datetime.strptime(jsondata["astronomical_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
        self.astronomicaltwilightend = datetime.datetime.strptime(jsondata["astronomical_twilight_end"], "%Y-%m-%dT%H:%M:%S+00:00")

    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.date = datetime.datetime.today().strftime("%Y-%m-%d")
        self._update()

    def setdate(self, date):
        if str(type(date)) != "<class 'datetime.datetime'>":
            raise TypeError("date should be a datetime object.")
        self.date = date.strftime("%Y-%m-%d")
        self._update()
