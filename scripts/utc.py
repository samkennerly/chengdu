"""
Show the current local and UTC time.
"""

from datetime import datetime, timezone
import time

while True:

    # UTC is a global standard time
    utc_time = datetime.now(timezone.utc)

    # "Local" is what my computer's clock shows
    local_time = datetime.now()

    print()
    print("UTC   :", utc_time)
    print("Local :", local_time)

    time.sleep(1)
