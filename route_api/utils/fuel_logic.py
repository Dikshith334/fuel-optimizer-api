from .fuel_data import df

MAX_RANGE = 500
MPG = 10

def compute_fuel_stops_route(route_coords, total_distance):
    stops = []
    remaining_distance = total_distance

    # Step size (sample route points)
    step = max(1, len(route_coords) // 10)

    for i in range(0, len(route_coords), step):
        if remaining_distance <= 0:
            break

        # Pick cheapest station (simulate along route)
        cheapest = df.loc[df["Retail Price"].idxmin()]

        miles_to_fill = min(MAX_RANGE, remaining_distance)
        gallons = miles_to_fill / MPG

        stops.append({
            "station": cheapest["Truckstop Name"],
            "city": cheapest["City"],
            "state": cheapest["State"],
            "price_per_gallon": float(cheapest["Retail Price"]),
            "gallons_filled": round(gallons, 2),
            "cost": round(gallons * float(cheapest["Retail Price"]), 2)
        })

        remaining_distance -= MAX_RANGE

    return stops


def calculate_total_cost(stops):
    return round(sum(stop["cost"] for stop in stops), 2)