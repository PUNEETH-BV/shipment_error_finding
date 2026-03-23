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
pass


# ── Test cases ──  # mixed good/bad records
# print(process_delivery_file("empty.txt"))         # empty file
# print(process_delivery_file("ghost.txt"))         # file doesn't exist
# ```

# ---
class DistanceError(Exception):
    pass

class WeightError(Exception):
    pass

class NumberOfFieldsError(Exception):
    pass

def process_delivery_file(filename):
    no_sussive_order = 0
    sussive_orders = []
    no_failure_order = 0
    failure_orders = []
    line_no = 0
    try :
        with open(filename,"r") as f :
            all_line = f.readlines()
            if len(all_line) == 0 :
                raise ValueError("File is empty")
            for line in all_line :
                line_no += 1
                l = line.strip().split(",")
                try: 
                    if len(l) != 3 :
                        raise NumberOfFieldsError(f"Line {line_no}: expected 3 fields, got {len(l)}")
                    distance = float(l[1])
                    weight = float(l[2])
                    if distance <= 0 :
                        raise DistanceError(f"Line {line_no}: distance must be positive, got {l[1]}")
                    if weight <= 0 :
                        raise WeightError(f"Line {line_no}: weight must be positive, got {l[2]}")
                    
                    sussive_orders.append(line.strip())
                    no_sussive_order += 1
                except(DistanceError, WeightError, NumberOfFieldsError,ValueError) as e:
                        failure_orders.append(str(e))
                        no_failure_order += 1
                        print(e)
            return {
            "success": no_sussive_order,
            "failed": no_failure_order,
            "total": no_sussive_order + no_failure_order,
            "errors": failure_orders,
            }      
    except FileNotFoundError:
            print(f"File '{filename}' not found.")
    except ValueError as ve:
            print(str(ve))
    finally :
        print("Processing complete")
    



        

print(process_delivery_file("deliveries.txt"))    
print(process_delivery_file("empty.txt"))         # empty file
print(process_delivery_file("ghost.txt"))         # file doesn't exis
## ⚠️ Edge Cases To Think About
# 1. What if a line has too many commas?  "a,b,c,d"  → 4 fields not 3
# 2. What if distance is "45.5abc"?       → can't convert to float
# 3. What if weight is "0"?               → zero is not positive
# 4. What if the file exists but empty?   → no lines to process
# 5. Spaces around values? " 45.5 "      → .strip() is your friend