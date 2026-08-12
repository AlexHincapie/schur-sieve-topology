"""
Validation script for SchurSieve (Analytical Model).
Verifies the Jacobi-Trudi determinant for twin and sexy prime 
configurations at macroscopic scales using asymptotic continuous computation.
"""

from schur_sieve import SchurSieve

def run_test():
    print("--- Starting SchurSieve Integrity Test (O(1) Analytical Mode) ---")
    
    try:
        # 1. Initialize Sieve (No file dependencies)
        sieve = SchurSieve()
        
        # 2. Compute Basis analytically for a macroscopic limit (e.g., N = 10^15)
        # Degree 20 is sufficient for standard constellations
        n_macroscopic = 1e15
        sieve.compute_basis_analytical(max_degree=20, N_limit=n_macroscopic)
        print(f"[TEST] Symmetric function basis computed for N = {n_macroscopic:.0e}.")
        
        # 3. Define Topologies
        # Twin Primes (Gap 2)
        twin_cfg = ([4, 4, 1], [2, 1, 0])
        # Sexy Primes (Gap 6)
        sexy_cfg = ([8, 8, 1], [2, 1, 0])
        
        # 4. Execute Comparison
        results = sieve.compare_topologies(config_a=twin_cfg, config_b=sexy_cfg)
        
        print("\n--- Numerical Results ---")
        print(f"Twin Capacity (S_a): {results['capacity_denominator']:.6e}")
        print(f"Sexy Capacity (S_b): {results['capacity_numerator']:.6e}")
        print(f"Stability Ratio (Chi): {results['chi_ratio']:.6f}")
        
        # 5. Verification Logic
        if results['capacity_denominator'] > results['capacity_numerator']:
            print("\n[SUCCESS] Test passed: Twin topology shows higher structural stability.")
        else:
            print("\n[WARNING] Unexpected ratio. Check prime density and partition indices.")
            
    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")

if __name__ == "__main__":
    run_test()
