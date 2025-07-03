def add_duration(start, duration):
    # Split start time into hour, minute and AM/PM
    time_part, period = start.strip().split()
    hour_str, minute_str = time_part.split(':')
    hour = int(hour_str)
    minute = int(minute_str)

    # Convert start time to 24-hour format
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add duration
    total_minutes = hour * 60 + minute + dur_hour * 60 + dur_minute
    new_hour_24 = (total_minutes // 60) % 24
    new_minute = total_minutes % 60

    # Convert back to 12-hour format
    if new_hour_24 == 0:
        new_hour = 12
        new_period = 'AM'
    elif 1 <= new_hour_24 < 12:
        new_hour = new_hour_24
        new_period = 'AM'
    elif new_hour_24 == 12:
        new_hour = 12
        new_period = 'PM'
    else:
        new_hour = new_hour_24 - 12
        new_period = 'PM'

    # Format minute to always be two digits
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"
    print(new_time)

# Example usage
add_duration('3:00 PM', '3:10')  # Should print: 6:10 PM


