import numpy as np

def problem_1():
    M_a = 2
    gamma = 1.4
    p1 = 10e3
    T1 = 225
    theta_f = np.deg2rad(5)
    theta_b = np.deg2rad(15)
    beta_1 = np.deg2rad(34.3)
    M_1n = M_a * np.sin(beta_1)
    print(f"M_1n: {M_1n:.4f}")
    M_2n = 0.891
    p2_p1 = 1.315
    T2_T1 = 1.082
    p02_p01 = 0.998
    p01 = 78.24e3
    p2, T2, p02 = p2_p1 * p1, T2_T1 * T1, p02_p01 * p01
    print(f"p2: {p2:.2f} Pa, T2: {T2:.2f} K, p02: {p02:.2f} Pa")
    M_2 = M_2n / np.sin(beta_1 - theta_f)
    print(f"M_2: {M_2:.4f}")
    p3_p2 = 1.2965
    T3_T2 = 1.0775
    p03_p02 = 0.998
    p3, T3, p03 = p3_p2 * p2, T3_T2 * T2, p03_p02 * p02
    M_3 = 1.648
    print(f"p3: {p3:.2f} Pa, T3: {T3:.2f} K, p03: {p03:.2f} Pa")
    print(f"M_3: {M_3:.3f}")
    print(f"M_4: {2.12:.2f}")
    p4_p04 = 0.106
    T4_T04 = 0.5266
    p4, T4 = p4_p04 * p03, T4_T04 * 405
    print(f"p4: {p4:.2f} Pa, T4: {T4:.2f} K")

problem_1()
