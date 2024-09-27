#include <bits/stdc++.h>
using namespace std;

struct Booking {
    int start;
    int end;

    Booking(int s, int e) : start(s), end(e) {}
};

class BookingScheduler {
private:
    vector<Booking> bookings;

public:
    void addBooking(int start, int end) {
        bookings.push_back(Booking(start, end));
    }

    vector<Booking> optimizeBookings() 
    {
        if (bookings.empty()) return {};

        sort(bookings.begin(), bookings.end(), [](const Booking& a, const Booking& b) {
            return a.start < b.start;
        });

        vector<Booking> merged;
        merged.push_back(bookings[0]);

        for (int i = 1; i < bookings.size(); i++) 
        {
            Booking& last_booking = merged.back();
            const Booking& current_booking = bookings[i];

            if (current_booking.start <= last_booking.end)
            last_booking.end = max(last_booking.end, current_booking.end);
              
            else
            merged.push_back(current_booking);    
        }

        return merged;
    }
};

int main() 
{
    int t;
    cout << "Enter number of testcases: " << endl;
    cin >> t;
    
    while(t--)
    {
        BookingScheduler scheduler;
        int n, start, end;
    
        cout << "Enter the number of bookings: ";
        cin >> n;
    
        for (int i = 0; i < n; i++) 
        {
            cout << "Enter start and end time for booking " << i + 1 << ": ";
            cin >> start >> end;
            scheduler.addBooking(start, end);
        }
    
        vector<Booking> optimizedBookings = scheduler.optimizeBookings();
    
        cout << "Optimized bookings: ";
        for(auto booking : optimizedBookings)
        cout << "[" << booking.start << ", " << booking.end << "] ";
        
        cout << endl;
    }
}
