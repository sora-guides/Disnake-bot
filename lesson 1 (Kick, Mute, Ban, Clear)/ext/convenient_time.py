# Файл написан в рамках функций, расматриваемых в этом уроке и являются индивуальной и необязательной наработкой

def convert_time_format(time: str):
    time_data = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    time_mute = int(time[:-1]) * time_data[time[-1]]
    convenient_format = {
        "days": time_mute//time_data["d"], 
        "hours": time_mute//time_data["h"], 
        "minutes": (time_mute%time_data["h"])//time_data["m"], 
        "seconds": (time_mute%time_data["h"])%time_data["m"]
    }
    response = {}
    response["duration"] = time_mute
    
    match time[1:]:
        case "d":
            response["answer"] = f"{convenient_format['days']} days"
        case "h":
            response["answer"] = f"{convenient_format['hours']} hours"
        case "m":
            response["answer"] = f"{convenient_format['minutes']} minutes"
        case "s":
            response["answer"] = f"{convenient_format['seconds']} seconds"
    return response