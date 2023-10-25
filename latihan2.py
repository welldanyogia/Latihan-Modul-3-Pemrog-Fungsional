def convert_minutes(weeks, days, hours, minutes):
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
    return total_minutes

def curry_convert_minutes(weeks):
    def curry_days(days):
        def curry_hours(hours):
            def curry_minutes(minutes):
                return convert_minutes(weeks, days, hours, minutes)

            return curry_minutes

        return curry_hours

    return curry_days

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

output_data = []
for item in data:
    parts = item.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])
    result = curry_convert_minutes(minggu)(hari)(jam)(menit)
    output_data.append(result)

# Menggunakan fungsi filter untuk mendapatkan hanya nilai integer
filtered_data = [list(filter(lambda x: x.isdigit(), item)) for item in data]

print(filtered_data)