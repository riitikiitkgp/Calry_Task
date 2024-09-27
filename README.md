# Calry_Task

# Task1 : Meeting Scheduler

## Overview
The **Meeting Scheduler** optimizes meeting room bookings by merging overlapping or consecutive time slots, ensuring efficient use of resources.

### Example:
- **Input:** `[[9, 12], [11, 13], [14, 17], [16, 18]]`
- **Output:** `[[9, 13], [14, 18]]`

## Features
- **Merge Overlaps:** Combines overlapping or consecutive bookings.
- **Efficient for Large Data:** Handles up to 1,000 bookings efficiently.

## How It Works
1. **Input:** User provides booking times (start and end).
2. **Optimization:** 
   - Bookings are sorted by start time.
   - Overlapping or consecutive bookings are merged.
3. **Output:** Optimized booking times are printed.

## Sample Input/Output

### Input:
```
Number of test cases: 1
Number of bookings: 4
9 12
11 13
14 17
16 18
```

### Output:
```
Optimized bookings: [9, 13] [14, 18]
``` 

This program efficiently manages meeting schedules by merging overlapping bookings, making it ideal for busy workspaces.
