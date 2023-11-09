import pytz
from datetime import datetime

tz = pytz.timezone("America/Los_Angeles")
dt = datetime.now(tz)
timestamp = int(dt.timestamp() * 1000)
print(timestamp)