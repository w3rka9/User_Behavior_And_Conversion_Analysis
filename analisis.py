import pandas as pd
import matplotlib.pyplot as plt

# Loading the data from the CSV file created with data_generator.py
df = pd.read_csv('user_events.csv')

# Calculating Conversion (The Funnel) 
total_users = df['user_id'].nunique() # counting unique people (not clicks)
buyers = df[df['event_type'] == 'purchase']['user_id'].nunique()

# Percentage formula: (part / total) * 100 to get a value that is easy to understand and compare
conversion_rate = (buyers / total_users) * 100

print(f"Total number of customers: {total_users}")
print(f"Number of customers who purchased: {buyers}")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print("-" * 30)

# Device Analysis of customers (Mobile vs. Desktop) 
device_counts = df['device'].value_counts()
print("Where are people coming from?")
print(device_counts)
print("-" * 30)

# Bar Chart of Device Types for a presentation
plt.figure(figsize=(8, 6))
ax = device_counts.plot(kind='bar', color=['#3B5369', '#693B5D'])

for p in ax.patches:
    ax.annotate(str(p.get_height()), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points',
                fontsize=12, fontweight='bold')

min_val = device_counts.min()
plt.ylim(min_val * 0.9, device_counts.max() * 1.1)

# Adding labels to make the chart more clear
plt.title('Website Visits by Device Type', fontsize=14)
plt.xlabel('Device Type', fontsize=12)
plt.ylabel('Number of Clicks', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7) 

# Saving the chart to the project folder
plt.tight_layout()
plt.savefig('user_behavior_chart.png')
print("Chart ready in 'user_behavior_chart_detailed.png'.")
plt.show()