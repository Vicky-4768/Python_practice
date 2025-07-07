def max(a,b):
     try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return "Invalid input: both values must be numeric"
    if a > b :
        return f"{a} is greater then {b}"
    elif a < b :
        return f"{a} is greater then {b}"
    else:
        return f"Please Entre valid numbers"
        
print(max(2,4))

