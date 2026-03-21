# Check if already signed up
if email in activity["participants"]:
    raise HTTPException(status_code=400, detail="Student is already signed up for this activity")

# Check capacity
if len(activity["participants"]) >= activity["max_participants"]:
    raise HTTPException(status_code=400, detail="Activity is already full")