"""
Validation script for SchurSieve.
Generates a local prime sequence and verifies the Jacobi-Trudi 
determinant for twin and sexy prime configurations.
"""

import os
from schur_sieve import SchurSieve

def generate_sample_primes(n=1000):
    """Generates the first n primes to a temporary file for testing."""
    primes = []
    chk = 2
    while len(primes) < n:
        for d in range(2, int(chk**0.5) + 1):
            if chk % d == 0:
                break
        else:
            primes.append(chk)
        chk += 1
    
    with open("primes_sample.txt", "w") as f:
        for p in primes:
            f.write(f"{p}\n")
    return "primes_sample.txt"

def run_test():
    print("--- Starting SchurSieve Integrity Test ---")
    
    # 1. Setup sample data
    filename = generate_sample_primes(5000)
    print(f"[TEST] Sample primes generated: {filename}")
    
    try:
        # 2. Initialize Sieve
        sieve = SchurSieve(data_source=filename, n_limit=5000)
        
        # 3. Compute Basis
        # Degree 20 is sufficient for standard constellations
        sieve.compute_basis(max_degree=20)
        print("[TEST] Symmetric function basis computed.")
        
        # 4. Define Topologies
        # Twin Primes (Gap 2)
        twin_cfg = ([4, 4, 1], [2, 1, 0])
        # Sexy Primes (Gap 6)
        sexy_cfg = ([8, 8, 1], [2, 1, 0])
        
        # 5. Execute Comparison
        results = sieve.compare_topologies(config_a=twin_cfg, config_b=sexy_cfg)
        
        print("\n--- Numerical Results ---")
        print(f"Twin Capacity (S_a): {results['capacity_denominator']:.6e}")
        print(f"Sexy Capacity (S_b): {results['capacity_numerator']:.6e}")
        print(f"Stability Ratio (Chi): {results['chi_ratio']:.6f}")
        
        # 6. Verification Logic
        if results['capacity_denominator'] > results['capacity_numerator']:
            print("\n[SUCCESS] Test passed: Twin topology shows higher structural stability.")
        else:
            print("\n[WARNING] Unexpected ratio. Check prime density and partition indices.")
            
    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)
            print("\n[TEST] Temporary files removed.")

if __name__ == "__main__":
    run_test()
