import random

def parse_pace(pace):
    """Convert pace in 'mm:ss' format to floating point minutes."""
    minutes, seconds = map(int, pace.split(':'))
    return minutes + seconds / 60.0

def read_runners(filename):
    """Read runner data from file and return names and paces."""
    names = []
    paces = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            name = ' '.join(parts[1:-1])
            pace = parse_pace(parts[-1])
            names.append(name)
            paces.append(pace)
    return names, paces

def simulate_race(names, paces, km_total):
    """Simulate the marathon race, modifying paces randomly within ±5%."""
    time = [0] * len(names)
    for km in range(1, km_total + 1):
        for i in range(len(names)):
            pace_variation = random.uniform(-0.05, 0.05)  # Generate random pace variation within ±5%
            current_pace = paces[i] * (1 + pace_variation)
            time[i] += current_pace

        if km == 20 or km == km_total:
            fastest_time = min(time)
            slowest_time = max(time)
            fastest_runner = names[time.index(fastest_time)]
            slowest_runner = names[time.index(slowest_time)]
            print(f"After {km} KM: Fastest is {fastest_runner} with {fastest_time:.2f} min; Slowest is {slowest_runner} with {slowest_time:.2f} min")

    return names, time

# Make sure the file 'runners.txt' is available in the correct path
names, paces = read_runners('runners.txt')
names, final_times = simulate_race(names, paces, 40)

# Output final results to a file with your student number
student_number = "12345678"  # Replace this with your actual student number
output_filename = f"A4output_{student_number}.txt"
with open(output_filename, 'w') as file:
    for name, final_time in zip(names, final_times):
        file.write(f"{name}: {final_time:.2f} minutes\n")
