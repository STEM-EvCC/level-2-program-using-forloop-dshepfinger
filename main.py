# Information provided already
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

print()
print("Mission Names: ", mission_names)
print("Mission Years: ", mission_years)
print("Mission Success/Failure: ", mission_success)

# Counters/variables for number of missions, before 2000, and their success
missions_total = 0

missions_before_2000 = []

missions_wereSuccesful = 0

# Figure out success rate and number of missions launched before the year 2000
for i in range(len(mission_names)):
    missions_total += 1
    if mission_success[i]:
        missions_wereSuccesful += 1
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

# Show success rate of missions as a percentage (5 missions successful out of 7 total)
percentageOfSuccess = (missions_wereSuccesful / missions_total) * 100

# Results of missions displayed on user's terminal
print()
print("Total number of space missions: ", missions_total)
print("Number of successful missions: ", missions_wereSuccesful)
print(f"Success rate of the missions: {percentageOfSuccess:.2f}%")
print("Missions that were launched before 2000: ")
for mission in missions_before_2000:
    print(f"- {mission}")
print()
