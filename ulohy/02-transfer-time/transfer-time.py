def seconds_to_str(time_in_seconds: float) -> str:
    if time_in_seconds < 1e-6:
        return f"{round(time_in_seconds * 1e9,3)} nanoseconds"
    elif time_in_seconds < 1e-3:
        return f"{round(time_in_seconds * 1e6,3)} microseconds"
    elif time_in_seconds < 1:
        return f"{round(time_in_seconds * 1e3,3)} miliseconds"
    elif time_in_seconds > 3600:
        return f"{time_in_seconds / 3600} hours"
    elif time_in_seconds > 120:
        return f"{time_in_seconds / 60} minutes"
    else:
        return f"{time_in_seconds} seconds"


def transfer_time(file: dict, ethernet_speed: int = 10) -> float:
    file_size_bits = (
        {
            "B": 1,
            "KiB": 1024,
            "MiB": 1024**2,
            "GiB": 1024**3,
        }[file["unit"]]
        * file["size"]
        * 8
    )
    return file_size_bits / (ethernet_speed * 1e6)


file = {"size": 80, "unit": "KiB"}
print(seconds_to_str(transfer_time(file, 100)))
