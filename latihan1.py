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
    "3 weeks 3 days 7 hours 21 minutes",
    "5 weeks 5 days 8 hours 11 minutes",
    "7 weeks 1 day 5 hours 33 minutes",
]

output_data = []
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    result = curry_convert_minutes(weeks)(days)(hours)(minutes)
    output_data.append(result)

print(output_data)