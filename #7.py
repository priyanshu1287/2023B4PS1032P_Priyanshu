def angle_time(time):
    
    hour=int(time[:2])
    minute=int(time[3:])

    if hour>12:
        hour-=12

    hour_angle=((360/12)*hour)+((minute/60)*(360/12))
    minute_angle=((360/60)*minute)

    angle=abs(hour_angle-minute_angle)

    if angle>180:
        angle=360-angle

    print("angle between hour hand and minute hand for ",time," is ",angle," degrees")

time=input("enter time in the following format hh:mm: ")
angle_time(time)
