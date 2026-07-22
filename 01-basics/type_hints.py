from typing import List, Dict, Tuple, Set

#? 1. Function Type Hints
def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Akkal"))

#? 2. Variable Type Hints
age: int = 25
name: str = "John"
price: float = 19.99
is_active: bool = True


#? 3. List, Tuple, Dictionary, and Set
numbers: List[int] = [1, 2, 3]
student: Dict[str, int] = {"Math": 90, "Science": 85}
point: Tuple[int, int] = (10, 20)
unique_numbers: Set[int] = {1, 2, 3}