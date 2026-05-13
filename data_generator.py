import pandas as pd
import random
from datetime import datetime, timedelta

# Preparing the ingredients for data generation
print("Generating data... ")

event_count = 5000  
users = [f"User_{i}" for i in range(1, 201)]
events = ["view", "cart", "purchase"]
devices = ["Mobile", "Desktop"]
start_date = datetime(2021, 1, 1)

results_list = []

# Creating synthetic events in a loop
for i in range(event_count):
    user = random.choice(users)
    action = random.choice(events)
    device_type = random.choice(devices)
    
    random_days = random.randint(0, 30)
    random_hours = random.randint(0, 23)
    event_time = start_date + timedelta(days=random_days, hours=random_hours)
    
    # Adding a complete row to list as a dictionary
    results_list.append({
        "user_id": user,
        "event_type": action,
        "timestamp": event_time,
        "device": device_type
    })

# Converting the list to a table and saving to CSV
df = pd.DataFrame(results_list)

# Sorting by time (from oldest to newest)
df = df.sort_values("timestamp")

df.to_csv('user_events.csv', index=False)

print("Success, The 'user_events.csv' file has been created.")
print("Now you can run the 'analysis.py' program.")