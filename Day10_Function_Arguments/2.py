def book_flight(destination, departure_date, seat_class):
    print(f"Booking a {seat_class} seat to {destination} on {departure_date}.")

# --- STANDARD KEYWORD USAGE ---
# Clear and readable. We know exactly what "Economy" refers to.
book_flight(destination="Tokyo", departure_date="2023-12-25", seat_class="Economy")
# Output: Booking a Economy seat to Tokyo on 2023-12-25.


# --- REORDERED KEYWORD USAGE ---
# Because we used names, we can change the order completely.
# Python matches the names, not the positions.
book_flight(seat_class="Business", destination="Paris", departure_date="2024-01-01")
# Output: Booking a Business seat to Paris on 2024-01-01.