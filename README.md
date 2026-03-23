"""
    Reads a delivery file where each line is:
    "delivery_name, distance_km, weight_kg"
    
    Example line: "Chennai_delivery,45.5,12.3"

    Rules:
    ✅ If the file doesn't exist      → raise FileNotFoundError with clear message
    ✅ If the file is empty            → raise ValtueError("File is empty")
    ✅ Each record must have exactly 3 fields  → skip + log if no
    ✅ distance_km must be a positive number   → skip + log if not
    ✅ weight_kg must be a positive number     → skip + log if not
    ✅ Continue processing remaining records even if one fails
    ✅ ALWAYS print "Processing complete" at the end — success or failure

    Returns this dict if successful:
    {
        "success": 3,
        "failed": 2,
        "total": 5,
        "errors": [
            "Line 3: expected 3 fields, got 1",
            "Line 5: distance must be positive, got -10.0"
        ]
}
   """
