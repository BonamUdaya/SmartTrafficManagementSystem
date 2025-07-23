# SmartTrafficManagementSystem
This project provides an intelligent alternative by dynamically adjusting signal timings based on the number of vehicles present at each intersection.

# Smart Traffic Management System
# Developed by Bonam Udayasree

import time

# Sample traffic data: number of vehicles from each direction
traffic_data = {
    "North": 12,
    "East": 25,
    "South": 18,
    "West": 7
}

def display_signal_status(green_direction, green_time):
    print("\n--- Signal Status ---")
    for direction in traffic_data:
        if direction == green_direction:
            print(f"🟢 {direction}: GREEN for {green_time} seconds")
        else:
            print(f"🔴 {direction}: RED")

def smart_traffic_control(data):
    print("🚦 Smart Traffic Management System\n")
    time.sleep(1)
    print("Analyzing traffic data...\n")
    time.sleep(1)

    for direction, count in data.items():
        print(f"{direction}: {count} vehicles")

    # Find the direction with the highest traffic
    max_direction = max(data, key=data.get)
    vehicle_count = data[max_direction]

    # Calculate green light duration (base + per vehicle time)
    green_time = 30 + vehicle_count  # 30 seconds base time

    # Display signal status
    display_signal_status(max_direction, green_time)

    print(f"\n✅ {max_direction} has highest traffic and gets green light for {green_time} seconds.")
    print("🕒 Switching signals in progress...\n")
    time.sleep(2)

    print("✅ Traffic signal simulation completed.")

# Run the smart traffic controller
smart_traffic_control(traffic_data)
