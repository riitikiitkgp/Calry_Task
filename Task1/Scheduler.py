class Booking:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class BookingScheduler:
    def __init__(self):
        self.bookings = []

    def add_booking(self, start, end):
        self.bookings.append(Booking(start, end))

    def optimize_bookings(self):
        if not self.bookings:
            return []

        self.bookings.sort(key=lambda x: x.start)

        merged = [self.bookings[0]]

        for i in range(1, len(self.bookings)):
            last_booking = merged[-1]
            current_booking = self.bookings[i]

            if current_booking.start <= last_booking.end:
                last_booking.end = max(last_booking.end, current_booking.end)
            else:
                merged.append(current_booking)

        return merged


if __name__ == "__main__":
    t = int(input("Enter number of testcases: "))
    
    for _ in range(t):
        scheduler = BookingScheduler()
        n = int(input("Enter the number of bookings: "))

        for i in range(n):
            start, end = map(int, input(f"Enter start and end time for booking {i + 1}: ").split())
            scheduler.add_booking(start, end)

        optimized_bookings = scheduler.optimize_bookings()

        print("Optimized bookings:", end=" ")
        for booking in optimized_bookings:
            print(f"[{booking.start}, {booking.end}]", end=" ")
        print()
