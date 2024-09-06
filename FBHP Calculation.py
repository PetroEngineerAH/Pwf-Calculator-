# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:11:56 2024

@author: ahernandez
"""

def calculate_fbhp(Pfwh, Pf, Pgh, Plh):
    """
    Calculate the Flowing Bottomhole Pressure (FBHP) for a gas well.

    Parameters:
    Pfwh (float): Wellhead pressure
    Pf (float): Pressure loss due to friction
    Pgh (float): Pressure loss due to gas gravity head
    Plh (float): Pressure loss due to liquid head

    Returns:
    float: Flowing Bottomhole Pressure (FBHP)
    """
    FBHP = Pfwh + Pf + Pgh + Plh
    return FBHP

def calculate_pgh(rho_g, h):
    """
    Calculate gas gravity head loss (Pgh).

    Parameters:
    rho_g (float): Gas density (lb/ft³)
    h (float): Height of the gas column (ft)

    Returns:
    float: Gas gravity head loss (Pgh) in psi
    """
    g = 32.174  # Acceleration due to gravity in ft/s²
    Pgh = rho_g * g * h / 144  # Convert to psi (1 psi = 144 lb/ft²)
    return Pgh

def calculate_plh(rho_l, h):
    """
    Calculate liquid head loss (Plh).

    Parameters:
    rho_l (float): Liquid density (lb/ft³)
    h (float): Height of the liquid column (ft)

    Returns:
    float: Liquid head loss (Plh) in psi
    """
    g = 32.174  # Acceleration due to gravity in ft/s²
    Plh = rho_l * g * h / 144  # Convert to psi (1 psi = 144 lb/ft²)
    return Plh

# User inputs
Pfwh = float(input("Enter the wellhead pressure (Pfwh) in psi: "))
Pf = float(input("Enter the pressure loss due to friction (Pf) in psi: "))
rho_g = float(input("Enter the gas density (rho_g) in lb/ft³: "))
h_gas = float(input("Enter the height of the gas column (h) in ft: "))
rho_l = float(input("Enter the liquid density (rho_l) in lb/ft³: "))
h_liquid = float(input("Enter the height of the liquid column (h) in ft: "))

# Calculate Pgh and Plh
Pgh = calculate_pgh(rho_g, h_gas)
Plh = calculate_plh(rho_l, h_liquid)

# Calculate FBHP
FBHP = calculate_fbhp(Pfwh, Pf, Pgh, Plh)

# Display the results
print(f"Gas gravity head loss (Pgh) is: {Pgh} psi")
print(f"Liquid head loss (Plh) is: {Plh} psi")
print(f"The Flowing Bottomhole Pressure (FBHP) is: {FBHP} psi")
