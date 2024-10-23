import json
from datetime import datetime, timedelta

plant_data = '''
[
 {
 "plant_id": 1,
 "name": "Aloe Vera",
 "watering_frequency": 7
 },
 {
 "plant_id": 2,
 "name": "Peace Lily",
 "watering_frequency": 3
 },
 {
 "plant_id": 3,
 "name": "Spider Plant",
 "watering_frequency": 5
 },
 {
 "plant_id": 4,
 "name": "Snake Plant",
 "watering_frequency": 14
 },
 {
 "plant_id": 5,
 "name": "Fern",
 "watering_frequency": 2
 },
 {
 "plant_id": 6,
 "name": "Cactus",
 "watering_frequency": 10
 },
 {
 "plant_id": 7,
 "name": "Orchid",
 "watering_frequency": 7
 },
 {
 "plant_id": 8,
 "name": "Bamboo",
 "watering_frequency": 4
 },
 {
 "plant_id": 9,
 "name": "Money Plant",
 "watering_frequency": 6
 },
 {
 "plant_id": 10,
 "name": "Lavender",
 "watering_frequency": 8
 }
]
'''

plants = json.loads(plant_data)

# Start date
def start_next_monday():
    return datetime (2024, 10, 28)

# Function to create watering schedule for the next 12 weeks
def create_watering_schedule(plants, num_weeks=12):
    schedule = []
    next_monday = start_next_monday()

    end_date = next_monday + timedelta(weeks=num_weeks)

    # Dictionary to track the next watering day for each plant
    next_watering_days = {plant["name"]: next_monday for plant in plants}

    # Iterate through each day from the next Monday to the end of 12 weeks
    schedule_date = next_monday
    while schedule_date < end_date:
        if schedule_date.weekday() < 5:  # Only schedule for weekdays (Mon-Fri)
          
           # Bonus: plants_watered_already = 0

            for plant in plants:
                plant_name = plant["name"]
                watering_frequency = plant["watering_frequency"]

                # Water the plant if it's the next scheduled watering day
                if schedule_date == next_watering_days[plant_name]:
                    schedule.append(f"{schedule_date.strftime('%Y-%m-%d (%A)')} - {plant_name}")
                   
                   #Bonus: plant_watered_already += 1
                    
                    # Schedule the next watering day
                    next_watering_days[plant_name] = schedule_date + timedelta(days=watering_frequency)
                   
                    # Bonus challenge attempt - not working
               #else:
                   #next_day = schedule_date + timedelta(days=1)
                    #while next_day = schedule_date.weekday() < 5:
                    #next_day += timedelta(days=1)
                    #next_watering_days[plant_name] = next_day


        # Move to next day
        schedule_date += timedelta(days=1)

    return schedule

# Generate watering schedule
schedule = create_watering_schedule(plants)

# Display schedule
water = ("Plant Watering Schedule\n")
bold = f"\033[1m{water}\033[1m"
print (bold)
for entry in schedule:
    print(entry)