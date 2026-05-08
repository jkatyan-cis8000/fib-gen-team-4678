def generate_fibonacci(limit: int) -> list[int]:
    if limit < 0:
        return []
    
    result = []
    a, b = 0, 1
    
    while a <= limit:
        result.append(a)
        a, b = b, a + b
    
    return result
