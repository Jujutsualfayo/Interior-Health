def optimize_route(start, end, waypoints=[]):
    #  route optimization
    print(f"Optimizing route from {start} to {end} with waypoints: {waypoints}")
    return {"optimized_route": [start] + waypoints + [end]}

