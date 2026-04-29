from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.route_service import get_route
from .utils.fuel_logic import compute_fuel_stops_route, calculate_total_cost


@api_view(['POST'])
def optimize_route(request):
    start = request.data.get("start")
    end = request.data.get("end")

    # ✅ Validation
    if not start or not end:
        return Response({"error": "Start and End required"}, status=400)

    if not isinstance(start, list) or not isinstance(end, list):
        return Response({"error": "Invalid input format"}, status=400)

    # ✅ Get route
    route = get_route(start, end)

    if not route:
        return Response({"error": "Route API failed"}, status=500)

    # ✅ Use route-based stops
    stops = compute_fuel_stops_route(
        [],
        route["distance_miles"]
    )

    total_cost = calculate_total_cost(stops)

    # ✅ Clean structured response
    return Response({
        "status": "success",
        "data": {
            "distance_miles": route["distance_miles"],
            "fuel_stops": stops,
            "total_cost": total_cost,
            "route_geometry": route["geometry"]  # bonus
        }
    })