import numpy as np
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Given/known constants as quantities
p1 = Q_(1.0, 'atm')
T1 = Q_(300.0, 'kelvin')
W = Q_(694, 'meter/second')
gamma = 1.4
R = Q_(287.0, 'J/kg/K')
a1 = np.sqrt(gamma * R * T1)
M1 = (W / a1).to_base_units().magnitude

# Pressure ratio across the moving shock
p2_over_p1 = (2 * gamma * M1**2 - (gamma - 1)) / (gamma + 1)
# Temperature ratio from Rankine-Hugoniot
ratio_term = (gamma + 1)/(gamma - 1)
T2_over_T1 = p2_over_p1 * ((ratio_term + p2_over_p1)/(1 + ratio_term * p2_over_p1))
# Density ratio using p/(rho T)
rho2_over_rho1 = p2_over_p1/T2_over_T1

# Piston/induced flow velocity (region 2) from two equivalent forms
u_p = (W * (1 - 1/rho2_over_rho1))
u_p_closed = a1 * (2 / (gamma + 1)) * ((M1**2 - 1) / M1)

print(f"p2: {(p2_over_p1*p1).m_as('atm'):.3f} atm")
print(f"T2: {(T2_over_T1*T1).m_as('K'):.3f} K")
print(f"rho2/rho1: {rho2_over_rho1:.3f}")
print(f"u_p: {u_p.m_as('m/s'):.1f} m/s")
print(f"u_p (check): {u_p_closed.m_as('m/s'):.1f} m/s")