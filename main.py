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
