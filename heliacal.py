"""
Heliacal

Python module to get sunrise, sunset, daytime, and twilight data for a location.
"""
import datetime
import json
import urllib.request


class Heliacal:
    """
    Create a new Heliacal at a location

    Usage:

    `variable_name = Heliacal(latitude, longitude)`

    You can change the date of a Heliacal object with .set_date(datetime).
    By default, Heliacal objects are created with the current datetime.
    """
    def _update(self):
        url = urllib.request.urlopen(f'https://api.sunrise-sunset.org/json?'
                                     f'lat={self.latitude}&'
                                     f'lng={self.longitude}&'
                                     f'date={self.date}&'
                                     f'formatted=0')
        data = url.read()
        jsondata = json.loads(data)["results"]
        self.requesturl = (f'https://api.sunrise-sunset.org/json?'
                           f'lat={self.latitude}&'
                           f'lng={self.longitude}&'
                           f'date={self.date}&'
                           f'formatted=0')
        self.json = jsondata
        self.sunrise = datetime.datetime.strptime(jsondata["sunrise"],
                                                  "%Y-%m-%dT%H:%M:%S+00:00")
        self.sunset = datetime.datetime.strptime(jsondata["sunset"],
                                                 "%Y-%m-%dT%H:%M:%S+00:00")
        self.solar_noon = datetime.datetime.strptime(jsondata["solar_noon"],
                                                     "%Y-%m-%dT%H:%M:%S+00:00")
        self.day_length = jsondata["day_length"]
        self.civil_twilight_begin = datetime.datetime.strptime(jsondata["civil_twilight_begin"],
                                                               "%Y-%m-%dT%H:%M:%S+00:00")
        self.civil_twilight_end = datetime.datetime.strptime(jsondata["civil_twilight_end"],
                                                             "%Y-%m-%dT%H:%M:%S+00:00")
        self.nautical_twilight_begin = datetime.datetime.strptime(jsondata["nautical_twilight_begin"],
                                                                  "%Y-%m-%dT%H:%M:%S+00:00")
        self.nautical_twilight_end = datetime.datetime.strptime(jsondata["nautical_twilight_end"],
                                                                "%Y-%m-%dT%H:%M:%S+00:00")
        self.astronomical_twilight_begin = datetime.datetime.strptime(jsondata["astronomical_twilight_begin"],
                                                                      "%Y-%m-%dT%H:%M:%S+00:00")
        self.astronomical_twilight_end = datetime.datetime.strptime(jsondata["astronomical_twilight_end"],
                                                                    "%Y-%m-%dT%H:%M:%S+00:00")

    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.date = datetime.datetime.today().strftime("%Y-%m-%d")
        self._update()

    def setdate(self, date):
        """
        DEPRICATED, PLEASE USE set_date()
        """
        print("setdate() is depricated and will be removed in Heliacal3, please transition to using set_date(). Date has been set.")
        self.set_date(date)

    def set_date(self, date):
        """
        Sets the date for a Heliacal object.
        """
        if str(type(date)) != "<class 'datetime.datetime'>":
            raise TypeError("date should be a datetime object.")
        self.date = date.strftime("%Y-%m-%d")
        self._update()
