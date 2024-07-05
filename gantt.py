import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define the start and end dates for tasks
tasks = [
    ("Brainstorming and Deciding on Topic", "2023-10-01", "2023-12-31"),  
    ("Literature Review", "2024-01-01", "2024-02-28"),
    ("Understanding the Data", "2024-03-01", "2024-04-30"),
    ("Writing Up Theory", "2024-02-20", "2024-7-15"),
    ("Exploratory Data Analysis", "2024-05-01", "2024-7-15"),
    ("Writing Up Findings", "2024-7-01", "2024-8-30"),
    ("Documentation", "2024-9-01", "2024-9-30"),
    ("Proofreading", "2024-10-01", "2024-11-15"),
]

# Convert dates to datetime objects
tasks = [(task, datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d")) for task, start, end in tasks]

# Define a figure and axis to plot on
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through each task and plot it
for i, (task, start, end) in enumerate(tasks):
    ax.barh(task, end - start, left=start, color='cornflowerblue')

# Set the x-axis to date format
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Improve layout
plt.xticks(rotation=45)
plt.xlabel("Duration")
plt.ylabel("Tasks")
plt.title("Gantt Chart: An Exploratory Data Analysis of Sylvia Beach’s Shakespeare and Company")

# Show grid
plt.grid(axis='x')

plt.tight_layout()
plt.show()

## code partially from Georg Vogeler's prompt: https://chatgpt.com/share/920c5b9e-c1c1-42bb-886c-63697315e426