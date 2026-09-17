vehicle_id = [] 
vehicle_type = []
vehicle_violation = []
name_driver = [] 
fine = []

print("VEHICLE DRIVING VIOLATION RECORDS")

while True:
    print("\n1. Add Records\n2. View Logs\n3. Search Vehicle\n4. Exit")
    
    try:
        choices = int(input("\nChoice: "))
    except ValueError:
        print("Invalid input.")
        continue
        
    if choices == 1:
        print("\n--- Selected: Add Record ---")
        driver_input = input("Driver's Name: ")
        plate_input = input("Plate Number: ")
        type_input = input("Vehicle Type: ")
        violation_input = input("Driver Violation: ")
        
        while True:
            try:
                fine_input = float(input("Fine Amount ($): "))
                break
            except ValueError:
                print("Invalid input.")
        
        name_driver.append(driver_input)
        vehicle_id.append(plate_input)
        vehicle_type.append(type_input)
        vehicle_violation.append(violation_input)
        fine.append(fine_input)
        
        print(f"-> Name of Driver: {driver_input}, Plate Number: {plate_input}, Fine: ${fine_input:.2f}")
        print("Record Saved Successfully!")

    elif choices == 2:
        print("\nViewing Logs")
        if not vehicle_id:
            print("No records found.")
        else:
            print(f"{'No.':<3} | {'Driver Name':<18} | {'Plate':<10} | {'Type':<10} | {'Violation':<15} | {'Fine':<8}")
            for i in range(len(vehicle_id)):
                print(f"{i+1:<3} | {name_driver[i]:<18} | {vehicle_id[i]:<10} | {vehicle_type[i]:<10} | {vehicle_violation[i]:<15} | ${fine[i]:<7,.2f}")

    elif choices == 3:
        print("\nSearch Vehicle")
        if not vehicle_id:
            print("No records available.")
        else:
            search_query = input("Enter Plate Number to search: ").strip()
            found = False
            for i in range(len(vehicle_id)):
                if vehicle_id[i].lower() == search_query.lower():
                    print(f"\nRecord Found!")
                    print(f"Driver Name: {name_driver[i]}")
                    print(f"Plate Number: {vehicle_id[i]}")
                    print(f"Vehicle Type: {vehicle_type[i]}")
                    print(f"Violation: {vehicle_violation[i]}")
                    print(f"Fine: ${fine[i]:,.2f}")
                    found = True
                    break

            if not found:
                print("No record found.")
    elif choices == 4:
        print("\nExiting program")
        break

    else:
        print("Invalid choice.")
