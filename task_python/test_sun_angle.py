import logging
from datetime import datetime

SUNRISE = datetime.strptime('06:00', '%H:%M')
SUNSET = datetime.strptime('18:00', '%H:%M')


def sun_angle(time, sunrise=SUNRISE, sunset=SUNSET):
    """
    Return the angle of the sun at `time`.
    Assumes that the sun moves 180 degrees between `sunrise` and `sunset`.
    During night return 'I don\'t see the sun!'.
    """
    time = datetime.strptime(time, '%H:%M')
    logging.info("check that sun is visible")
    if not sunrise <= time <= sunset:
        return "I don't see the sun!"

    angle_per_hour = 180 / (sunset - sunrise).seconds * 3600
    time_since_sunrise = (time - sunrise).seconds / 3600
    return time_since_sunrise * angle_per_hour


def test_method():
    a = sun_angle("07:00") == 15
    b = sun_angle("12:15") == 93.75
    c = sun_angle("01:23") == "I don't see the sun!"
    print(a)
    print(b)
    print(c)

