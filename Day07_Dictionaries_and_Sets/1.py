student_profile = {
    "name": "Emma Watson",
    "student_id": 10245,
    "is_active": True,
    
    # A List inside a Dictionary (for multiple items)
    "courses": ["Math", "Physics", "Computer Science"],
    
    # A Dictionary inside a Dictionary (for complex details)
    "grades": {
        "Math": 95,
        "Physics": 88,
        "Computer Science": 92
    }
}

# --- How to use it ---

# 1. Accessing simple data
print(student_profile["name"])  
# Output: Emma Watson

# 2. Accessing nested data (The grade for Physics)
print(student_profile["grades"]["Physics"])  
# Output: 88