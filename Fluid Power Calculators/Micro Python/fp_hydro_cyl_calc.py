#
# Brent C Hull
# 2021-8-21
# Modern Hydraulic Cylinder Sizing Calculator
# Compatible with Micropython for calculators (Casio, HP, etc.)
#
from math import sqrt

# --- Physical and Conversion Constants ---
PI_OVER_4 = 0.7854
COMPENSATION_FACTOR = 1.15
RELIEF_VALVE_FACTOR = 1.3225
TIME_GPM_CONVERSION_FACTOR = 3.85 # Conversion factor used in original script
CUBIC_INCHES_PER_GALLON = 231

# --- Cylinder Specification Data ---
# This data structure replaces the massive 'if/elif' block from the original script.
# It's organized by Type -> Oversize -> Bore Range.
CYLINDER_DATA = {
    # Type 1: Industrial 4-Tie Rod
    '1': {
        '1': [
            {'max_bore': 1.5, 'std_bore': 1.5, 'rod': 0.625}, {'max_bore': 2.0, 'std_bore': 2.0, 'rod': 1.0},
            {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.0}, {'max_bore': 3.25, 'std_bore': 3.25, 'rod': 1.375},
            {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 1.75}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 2.0},
            {'max_bore': 6.0, 'std_bore': 6.0, 'rod': 2.5}, {'max_bore': 7.0, 'std_bore': 7.0, 'rod': 3.0},
            {'max_bore': 8.0, 'std_bore': 8.0, 'rod': 3.5}, {'max_bore': 10.0, 'std_bore': 10.0, 'rod': 4.5},
            {'max_bore': 12.0, 'std_bore': 12.0, 'rod': 5.5}, {'max_bore': 14.0, 'std_bore': 14.0, 'rod': 7.0}
        ],
        '2': [
            {'max_bore': 1.5, 'std_bore': 1.5, 'rod': 1.0}, {'max_bore': 2.0, 'std_bore': 2.0, 'rod': 1.375},
            {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.375}, {'max_bore': 3.25, 'std_bore': 3.25, 'rod': 1.75},
            {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 2.0}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 2.5},
            {'max_bore': 6.0, 'std_bore': 6.0, 'rod': 3.0}, {'max_bore': 7.0, 'std_bore': 7.0, 'rod': 4.0},
            {'max_bore': 8.0, 'std_bore': 8.0, 'rod': 4.0}, {'max_bore': 10.0, 'std_bore': 10.0, 'rod': 5.5},
            {'max_bore': 12.0, 'std_bore': 12.0, 'rod': 7.0}, {'max_bore': 14.0, 'std_bore': 14.0, 'rod': 8.0}
        ],
        '3': [
            {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.75}, {'max_bore': 3.25, 'std_bore': 3.25, 'rod': 2.0},
            {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 2.5}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 3.0},
            {'max_bore': 6.0, 'std_bore': 6.0, 'rod': 4.0}, {'max_bore': 7.0, 'std_bore': 7.0, 'rod': 5.0},
            {'max_bore': 8.0, 'std_bore': 8.0, 'rod': 5.5}, {'max_bore': 10.0, 'std_bore': 10.0, 'rod': 7.0},
            {'max_bore': 12.0, 'std_bore': 12.0, 'rod': 8.0}, {'max_bore': 14.0, 'std_bore': 14.0, 'rod': 10.0}
        ],
        '4': [{'max_bore': 5.0, 'std_bore': 5.0, 'rod': 3.5}]
    },
    # Type 2: Mobile
    '2': {
        '1': [
            {'max_bore': 2.0, 'std_bore': 2.0, 'rod': 1.0}, {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.0},
            {'max_bore': 3.0, 'std_bore': 3.0, 'rod': 1.0}, {'max_bore': 3.25, 'std_bore': 3.25, 'rod': 1.25},
            {'max_bore': 3.5, 'std_bore': 3.5, 'rod': 1.25}, {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 1.375},
            {'max_bore': 4.5, 'std_bore': 4.5, 'rod': 1.75}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 2.0},
            {'max_bore': 5.5, 'std_bore': 5.5, 'rod': 2.5}, {'max_bore': 6.0, 'std_bore': 6.0, 'rod': 2.5},
            {'max_bore': 7.0, 'std_bore': 7.0, 'rod': 2.5}, {'max_bore': 8.0, 'std_bore': 8.0, 'rod': 3.5},
            {'max_bore': 10.0, 'std_bore': 10.0, 'rod': 4.0}, {'max_bore': 12.0, 'std_bore': 12.0, 'rod': 4.5}
        ],
        '2': [
            {'max_bore': 2.0, 'std_bore': 2.0, 'rod': 1.125}, {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.125},
            {'max_bore': 3.0, 'std_bore': 3.0, 'rod': 1.125}, {'max_bore': 3.25, 'std_bore': 3.25, 'rod': 1.375},
            {'max_bore': 3.5, 'std_bore': 3.5, 'rod': 1.375}, {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 1.5},
            {'max_bore': 4.5, 'std_bore': 4.5, 'rod': 2.0}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 2.5},
            {'max_bore': 5.5, 'std_bore': 5.5, 'rod': 3.0}, {'max_bore': 6.0, 'std_bore': 6.0, 'rod': 3.0},
            {'max_bore': 7.0, 'std_bore': 7.0, 'rod': 3.0}, {'max_bore': 8.0, 'std_bore': 8.0, 'rod': 4.0},
            {'max_bore': 10.0, 'std_bore': 10.0, 'rod': 4.5}, {'max_bore': 12.0, 'std_bore': 12.0, 'rod': 5.0}
        ],
        '3': [
            {'max_bore': 2.0, 'std_bore': 2.0, 'rod': 1.25}, {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.25},
            {'max_bore': 3.0, 'std_bore': 3.0, 'rod': 1.25}, {'max_bore': 3.25, 'std_bore': 3.25, 'rod': 1.5},
            {'max_bore': 3.5, 'std_bore': 3.5, 'rod': 1.5}, {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 1.75},
            {'max_bore': 4.5, 'std_bore': 4.5, 'rod': 2.5}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 3.0},
            {'max_bore': 5.5, 'std_bore': 5.5, 'rod': 3.5}, {'max_bore': 6.0, 'std_bore': 6.0, 'rod': 3.5},
            {'max_bore': 7.0, 'std_bore': 7.0, 'rod': 3.5}, {'max_bore': 8.0, 'std_bore': 8.0, 'rod': 4.5},
            {'max_bore': 10.0, 'std_bore': 10.0, 'rod': 5.0}, {'max_bore': 12.0, 'std_bore': 12.0, 'rod': 6.0}
        ],
        # Add other oversize options for mobile type here...
    },
    # Type 3: Ag 4-Tie Rod
    '3': {
        '1': [
            {'max_bore': 2.0, 'std_bore': 2.0, 'rod': 1.0625}, {'max_bore': 2.5, 'std_bore': 2.5, 'rod': 1.25},
            {'max_bore': 3.0, 'std_bore': 3.0, 'rod': 1.5}, {'max_bore': 3.5, 'std_bore': 3.5, 'rod': 2.0},
            {'max_bore': 4.0, 'std_bore': 4.0, 'rod': 2.0}, {'max_bore': 5.0, 'std_bore': 5.0, 'rod': 2.0}
        ]
    }
}


def get_numeric_input(prompt):
    """Gets a valid float from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_menu_choice(prompt, options):
    """Gets a valid choice from a dictionary of options."""
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please select from the available options.")


def select_cylinder_specs(calculated_bore, cyl_type, os_choice):
    """Looks up the standard bore and rod size from the data dictionary."""
    try:
        specs_table = CYLINDER_DATA[cyl_type][os_choice]
        for spec in specs_table:
            if calculated_bore <= spec['max_bore']:
                return spec['std_bore'], spec['rod']
        # If bore is larger than any in the table, return the largest
        return specs_table[-1]['std_bore'], specs_table[-1]['rod']
    except KeyError:
        return None, None


def main():
    """Main function to run the calculator."""
    # --- Get User Inputs ---
    print("--- Hydraulic Cylinder Calculator ---")
    extend_force = get_numeric_input("Enter Extend Force (lbs): ")
    retract_force = get_numeric_input("Enter Retract Force (lbs): ")
    design_psi = get_numeric_input("Enter Design Pressure (PSI): ")
    stroke = get_numeric_input("Enter Stroke (inches): ")

    # Cylinder Type and Oversize Selection
    cyl_type = get_menu_choice("Cylinder Type (1:Ind, 2:Mobile, 3:Ag): ", ['1', '2', '3'])
    
    # Show available oversize options for the selected type
    available_os = list(CYLINDER_DATA.get(cyl_type, {}).keys())
    print("Available oversize options for this type: " + ", ".join(available_os))
    os_choice = get_menu_choice("Select Rod Oversize Option: ", available_os)

    # Time or GPM
    time_gpm_choice = get_menu_choice("Input Time (1) or GPM (2): ", ['1', '2'])
    
    gpm, time = 0, 0
    if time_gpm_choice == '1':
        time = get_numeric_input("Enter Time (seconds): ")
    else:
        gpm = get_numeric_input("Enter GPM: ")

    pump_rpm = get_numeric_input("Enter Pump RPM: ")

    # --- Calculations ---
    if design_psi == 0:
        print("\nError: Design PSI cannot be zero.")
        return

    # 1. Calculate theoretical bore
    theoretical_bea = extend_force / design_psi
    calculated_bore = sqrt(theoretical_bea / PI_OVER_4)

    # 2. Select standard cylinder parts based on theoretical bore
    final_bore, final_rod = select_cylinder_specs(calculated_bore, cyl_type, os_choice)
    if final_bore is None:
        print("\nError: Selected cylinder type or oversize option is not valid.")
        return

    # 3. Calculate actual areas and volumes
    actual_bea = (final_bore ** 2) * PI_OVER_4
    actual_rea = ((final_bore ** 2) - (final_rod ** 2)) * PI_OVER_4
    
    if actual_rea <= 0:
        print("\nError: Rod area is greater than or equal to bore area. Check selections.")
        return
        
    ratio = actual_bea / actual_rea
    extend_volume = actual_bea * stroke
    retract_volume = actual_rea * stroke

    # 4. Calculate actual pressures and safety values
    actual_extend_psi = extend_force / actual_bea
    actual_retract_psi = retract_force / actual_rea
    compensation_psi = actual_extend_psi * COMPENSATION_FACTOR
    relief_valve_psi = actual_extend_psi * RELIEF_VALVE_FACTOR

    # 5. Calculate speed, time, and flow (with correction)
    if time_gpm_choice == '1':
        # Calculate GPM based on extend time, then find retract time
        extend_time = time
        pump_gpm = extend_volume / (extend_time * TIME_GPM_CONVERSION_FACTOR) if extend_time > 0 else 0
        retract_time = retract_volume / (pump_gpm * TIME_GPM_CONVERSION_FACTOR) if pump_gpm > 0 else 0
    else:
        # Calculate times based on given GPM
        pump_gpm = gpm
        extend_time = extend_volume / (pump_gpm * TIME_GPM_CONVERSION_FACTOR) if pump_gpm > 0 else 0
        retract_time = retract_volume / (pump_gpm * TIME_GPM_CONVERSION_FACTOR) if pump_gpm > 0 else 0

    # 6. Calculate speed in IPM and pump displacement
    extend_ipm = (pump_gpm * CUBIC_INCHES_PER_GALLON) / actual_bea if actual_bea > 0 else 0
    retract_ipm = (pump_gpm * CUBIC_INCHES_PER_GALLON) / actual_rea if actual_rea > 0 else 0
    pump_cid = (pump_gpm * CUBIC_INCHES_PER_GALLON) / pump_rpm if pump_rpm > 0 else 0

    # --- Display Results ---
    print("\n--- Calculation Results ---")
    print("Theoretical Bore: {:.3f} in".format(calculated_bore))
    print("-----------------------------")
    print("Selected Bore:    {:.3f} in".format(final_bore))
    print("Selected Rod:     {:.3f} in".format(final_rod))
    print("-----------------------------")
    print("Actual BEA / REA: {:.2f} in^2 / {:.2f} in^2".format(actual_bea, actual_rea))
    print("Cylinder Ratio:   {:.2f}:1".format(ratio))
    print("Extend/Retract Vol: {:.2f} in^3 / {:.2f} in^3".format(extend_volume, retract_volume))
    print("Extend/Retract PSI: {:.0f} / {:.0f}".format(actual_extend_psi, actual_retract_psi))
    print("Compensation PSI: {:.0f}".format(compensation_psi))
    print("Relief Valve PSI: {:.0f}".format(relief_valve_psi))
    print("Extend/Retract Time: {:.2f} s / {:.2f} s".format(extend_time, retract_time))
    print("Extend/Retract IPM:  {:.2f} / {:.2f}".format(extend_ipm, retract_ipm))
    print("Required Pump GPM: {:.2f}".format(pump_gpm))
    print("Required Pump CID: {:.2f}".format(pump_cid))


# --- Run the program ---
if __name__ == "__main__":
    main()