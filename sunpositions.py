"""Generate sun positions"""

from pyephem_sunpath.sunpath import sunpos
import pyephem_sunpath.sunpath as sunpath
import datetime


def hourlysunpos(thedate, lat, lon, tz):
    """generate the hourly sun positions for a day"""
    sunposs = []
    sunrise = sunpath.sunrise(thedate, lat, lon, tz)
    sunset = sunpath.sunset(thedate, lat, lon, tz)
    alt, azm = sunpath.sunpos(sunrise, lat, lon, tz, dst=False)
    sunposs.append((sunrise, azm, alt))
    for hours in range(24):
        delta = datetime.timedelta(hours=hours)
        atime = thedate + delta
        if atime < sunrise:
            continue
        if atime > sunset:
            break
        alt, azm = sunpath.sunpos(atime, lat, lon, tz, dst=False)
        sunposs.append((atime, azm, alt))
    alt, azm = sunpath.sunpos(sunset, lat, lon, tz, dst=False)
    sunposs.append((sunset, azm, alt))
    return sunposs


def smooth_hourlysunpos(thedate, lat, lon, tz):
    """generate the hourly sun positions for a day"""
    sunposs = []
    sunrise = sunpath.sunrise(thedate, lat, lon, tz)
    sunset = sunpath.sunset(thedate, lat, lon, tz)
    alt, azm = sunpath.sunpos(sunrise, lat, lon, tz, dst=False)
    sunposs.append((sunrise, azm, alt))
    for minutes in range(24 * 60):
        delta = datetime.timedelta(minutes=minutes)
        atime = thedate + delta
        if atime < sunrise:
            continue
        if atime > sunset:
            break
        alt, azm = sunpath.sunpos(atime, lat, lon, tz, dst=False)
        sunposs.append((atime, azm, alt))
    alt, azm = sunpath.sunpos(sunset, lat, lon, tz, dst=False)
    sunposs.append((sunset, azm, alt))
    return sunposs


def all_days_in_year(year: int, thehour=None):
    if thehour:
        start = datetime.datetime(year, 1, 1, thehour)
        end = datetime.datetime(year, 12, 31, thehour)
    else:
        start = datetime.datetime(year, 1, 1)
        end = datetime.datetime(year, 12, 31)

    current = start
    while current <= end:
        yield current
        current += datetime.timedelta(days=1)


def smooth_analemasunpos(thehour, lat, lon, tz):
    """generate the analema poitions for an hour
    smoothen the curve by generating each day
    """
    sunposs = []
    alldays = all_days_in_year(2025, thehour)
    for aday in alldays:
        alt, azm = sunpath.sunpos(aday, lat, lon, tz, dst=False)
        if alt < 0:
            continue
        sunposs.append((aday, azm, alt))
    return sunposs


def analemasunpos(thehour, lat, lon, tz):
    """generate the analema poitions for an hour"""
    sunposs = []
    for month in range(1, 13):
        atime = datetime.datetime(2025, month, 21, thehour)
        alt, azm = sunpath.sunpos(atime, lat, lon, tz, dst=False)
        if alt < 0:
            continue
        sunposs.append((atime, azm, alt))
    return sunposs


if __name__ == "__main__":
    lat = 41.51606330662579
    lon = 81.39308916058894
    tz = 5.5
    thehour = 12
    sunposs = analemasunpos(thehour, lat, lon, tz)
    for sunpos in sunposs:
        print(sunpos)
#     thedate = datetime.datetime(2025, 6, 21, 0)
#     sunposs = hourlysunpos(thedate, lat, lon, tz)
#     for sunpos in sunposs:
#         print(sunpos)
