import time
import random

def simulate_gaming_session(base_fps, max_temp, throttle_temp, duration_minutes):
    """
    Simulates a mobile device's performance degradation over time due to heat generation.
    """
    print(f"--- Starting Hardware Simulation ---")
    print(f"Target FPS: {base_fps} | Throttling starts at: {throttle_temp}°C | Thermal Limit: {max_temp}°C\n")

    current_temp = 32.0  # Assumed idle ambient temperature
    current_fps = base_fps

    for minute in range(1, duration_minutes + 1):
        # Simulate heat generation under heavy load (randomized slightly for realism)
        heat_generated = random.uniform(1.2, 2.8)
        current_temp += heat_generated

        # Apply thermal throttling logic using a linear decay function
        if current_temp > max_temp:
            current_temp = max_temp # Hardware caps the temperature to prevent damage
            current_fps = int(base_fps * 0.4) # Severe frame drop
            status = "CRITICAL THROTTLE"
        elif current_temp >= throttle_temp:
            # Calculate how far past the throttle point we are (percentage)
            throttle_severity = (current_temp - throttle_temp) / (max_temp - throttle_temp)
            # Gradually drop frames by up to 40% before hitting critical
            current_fps = int(base_fps - (base_fps * 0.4 * throttle_severity)) 
            status = "THROTTLING"
        else:
            status = "STABLE"

        print(f"Minute {minute:02d}: Temp: {current_temp:.1f}°C | FPS: {current_fps:02d} | Status: {status}")
        
        # Small delay so the terminal prints out sequentially like a real-time monitor
        time.sleep(0.1) 

    print("\n--- Session Complete ---")

def main():
    print("=== Mobile GPU Thermal Throttling Simulator ===")
    print("Model hardware performance constraints and frame rate stability under load.\n")
    
    try:
        fps = int(input("Enter Target FPS (e.g., 60, 90, 120): "))
        throttle = float(input("Enter temperature where throttling begins (e.g., 41.0): "))
        max_t = float(input("Enter absolute hardware thermal limit (e.g., 46.0): "))
        duration = int(input("Enter test duration in minutes (e.g., 20): "))

        if throttle >= max_t:
            print("Error: Throttling temperature must be strictly lower than the maximum thermal limit.")
            return

        print("")
        simulate_gaming_session(fps, max_t, throttle, duration)

    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
