# Heliacal
Python module to get sunrise, sunset, daytime, and twilight data for a location.

This is an API wrapper for [sunrise-sunset.org](https://sunrise-sunset.org/).

### To get started, install heliacal.

    pip install heliacal

### Next, add heliacal and datetime to your project.

    from heliacal import Heliacal
    import datetime

Heliacal requires datetime to run.

### Create a heliacal object

Heliacal uses latitude and longitude to determine solar data for a location. You can use modules such as [geopy](https://geopy.readthedocs.io/en/stable/) to get the co-ordinates of a named location.

    los_angeles = Heliacal(34.052235, -118.243683)

By default, Heliacal will set the date to today, to change that, use setdate().

    los_angeles.setdate(datetime.datetime(2018, 12, 31)) # Get solar data for 2018-12-31

You now have a working Heliacal instance! You can get the following information:

    los_angeles.sunrise # 2018-12-31 14:58:24
    los_angeles.sunset # 2019-01-01 00:54:16
    los_angeles.solarnoon # 2018-12-31 19:56:20
    los_angeles.daylength # 35752 (seconds)
    los_angeles.civiltwilightbegin # 2018-12-31 14:30:50
    los_angeles.civiltwilightend # 2019-01-01 01:21:49
    los_angeles.nauticaltwilightbegin # 2018-12-31 13:59:38
    los_angeles.nauticaltwilightend # 2019-01-01 01:53:01
    los_angeles.astronomicaltwilightbegin # 2018-12-31 13:29:11
    los_angeles.astronomicaltwilightend # 2019-01-01 02:23:28

    # For debugging or other things, there are: 
    los_angeles.requesturl # https://api.sunrise-suns...
    los_angeles.json # {'sunrise': '2018-12-31T14:58:...

Note: Heliacal returns UTC datetimes, it is the developer's job to turn them to the respective timezone.