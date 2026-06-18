from api import get_all_flights

data = get_all_flights()

if data:
    print(f"Total Aircraft: {len(data['states'])}\n")

    for flight in data["states"][:20]:

        if flight[1]:

            print(
                f"{flight[1].strip():10} | "
                f"{flight[2]:20} | "
                f"Altitude: {flight[7]}"
            )