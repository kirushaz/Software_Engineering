from datetime import datetime
import time
collection = [1, 2, 3, 4, 5]
for i in collection:
        time.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Текущее время =", current_time)

