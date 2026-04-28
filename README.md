# Mobile GPU Thermal Throttling Simulator

## Overview
A Python-based simulation tool designed to model mobile hardware performance under sustained computational loads. It simulates heat generation over time and calculates resulting performance degradation (frame drops) using conditional state management and linear decay functions.

## System Logic
Modern SoC (System on a Chip) architectures implement dynamic frequency scaling to prevent thermal damage. This script mimics that behavior:
1. **Stable State:** The system runs at maximum requested performance (Base FPS) while generating heat.
2. **Throttling State:** Once the soft thermal threshold is crossed, a decay function calculates a gradual reduction in clock speed (simulated as FPS drops) relative to the temperature delta.
3. **Critical State:** Upon hitting the hardware thermal limit, performance is severely capped to halt further heat generation.

## Features
* Customizable parameters for Target FPS, Throttling Thresholds, and Absolute Thermal Limits.
* Implements basic randomization (`random.uniform`) to mimic unpredictable real-world workload fluctuations.
* Terminal-based real-time telemetry output.

## Proof of Work
Created to demonstrate an understanding of hardware constraints, state management loops, and simulating real-world engineering problems via software logic.
