# library/fines.py

def calculate_fine(days_late):
    
    if days_late <= 0:
        return 0            

    fine      = 0
    remaining = days_late
    week      = 1           

    while remaining > 0:
    
        rate = 10
        for multiplier in range(2, week + 1):
            rate *= multiplier

        # Number of days that fall in this week (at most 7)
        days_this_week = min(7, remaining)

        # Add this week's contribution to total fine
        fine += days_this_week * rate

        remaining -= days_this_week
        week      += 1

    return fine


def display_fine_table():

    print("\n  ── Fine Rate Table ──────────────────────────────────")
    rate = 10
    for week in range(1, 5):
        if week > 1:
            rate = 10
            for m in range(2, week + 1):
                rate *= m
        day_start = (week - 1) * 7 + 1
        day_end   = week * 7
        print(f"  Week {week}  (days {day_start:>2}–{day_end:>2} late) :"
              f"  Rs. {rate}/day/book")
    print("  (Rate continues to increase each subsequent week)")
    print("  ─────────────────────────────────────────────────────")
