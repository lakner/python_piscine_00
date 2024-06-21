import time

seconds_since_unix_epoch = format(time.time(), ",.2f")
sci_for = format(time.time(), ".2e")

print(f"Seconds since January 1, 1970: {seconds_since_unix_epoch}, or {sci_for} in scientific notation.")
