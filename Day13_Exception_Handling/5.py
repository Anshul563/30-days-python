try:
    password = "123"
    
    # 1. We check the rule
    if len(password) < 5:
        # 2. We raise the flag if the rule is broken
        raise ValueError("Password is too short")

    # 3. This is skipped because of the raise above
    print("User registered successfully!")

except ValueError as error_message:
    # 4. We catch our OWN error and print it nicely
    print(f"Registration failed: {error_message}")