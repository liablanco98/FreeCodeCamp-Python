# This is the boilerplate for the Time Calculator project. 
# Instructions for building your project can be found at 
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator


def add_time(start:str, *duration):

    #IF INPUT DAY
    days_dictionary=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    #IF MORE INPUTS
    duration=list(duration)
    has_day=None
    if len(duration)>1:
        has_day=duration[1].capitalize()
    duration=duration[0]
    
    #FORMATTING START
    day_hour=start[-2:]
    dot_pos=start.index(':')
    start_hr=int(start[:dot_pos])
    start_minutes=int(start[dot_pos+1:-2])
    if day_hour=="PM":
        start_hr+=12

    #FORTMATTING HOURS
    dot_pos=duration.index(':')
    duration_hrs=int(duration[:dot_pos])
    duration_minutes=int(duration[dot_pos+1:])

    #CALCULATING TIMES
    n_minutes=start_minutes+duration_minutes
    n_minutes,offset=(n_minutes,0) if n_minutes<60 else (n_minutes-60,1)
    n_minutes=str(n_minutes) if n_minutes>9 else f"0{n_minutes}"

    n_hours=start_hr+duration_hrs+offset
    n_hours,more_days=n_hours%24,n_hours//24

    day_hour,n_hours=("AM",n_hours) if n_hours<12 else ("PM",n_hours-12)
    n_hours=str(n_hours) if n_hours!=0 else "12"
    output=f"{n_hours}:{n_minutes} {day_hour}"

    if has_day:
        day_to_add=has_day
        if more_days:
            nn_day=days_dictionary.index(has_day)
            nn_day_pos=(more_days+nn_day)%7
            day_to_add=days_dictionary[nn_day_pos]
        output+=f", {day_to_add}"    


    if more_days:
        if more_days==1:
            output+=" (next day)"
        else:
            output+=f" ({more_days} days later)"    

    return output
