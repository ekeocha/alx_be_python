def safe_divide(numerator, denominator):

    try:
        try:
        numerator = float(numerator)        
        denominator = float(denominator) 

        result = numerator / denominator
        return f"Result: {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
           
    finally:
        print("Runtime completed")
