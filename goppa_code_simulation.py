from sage.all import *
import random
import matplotlib.pyplot as plt

def create_goppa_code(q, m):
    k = GF(q, names=('a',))
    (a,) = k._first_ngens(1)
    A = AffineSpace(k, 2, names=('x', 'y'))
    (x, y) = A._first_ngens(2)
    C = Curve(y**2 + y - x**m)
    F = C.function_field()
    pls = F.places()
    Q, = C.places_at_infinity()
    pls.remove(Q)
    G = (m-1) * Q
    return codes.EvaluationAGCode(pls, G)

def decode_goppa(received_word, code):
    F = code.base_field()
    n = code.length()
    k = code.dimension()
    d = code.minimum_distance()
    t = (d-1)//2  # Error-correction capability
    
    H = code.parity_check_matrix()
    syndrome = H * received_word
    
    if syndrome.is_zero():
        return received_word, "success"
    
    # Attempt error correction
    for i in range(n):
        flipped_word = vector(received_word)
        flipped_word[i] = F(1) - flipped_word[i]
        if (H * flipped_word).is_zero():
            return flipped_word, "corrected"
    
    return None, "failure"

def simulate_transmission(code, error_rate, num_transmissions):
    k = code.dimension()
    n = code.length()
    F = code.base_field()
    
    successful_decodes = 0
    detected_uncorrectable = 0
    total_errors = 0
    
    for _ in range(num_transmissions):
        message = vector(F, [F.random_element() for _ in range(k)])
        codeword = code.encode(message)
        
        received_word = vector(codeword)
        num_errors = sum(1 for _ in range(n) if random.random() < error_rate)
        total_errors += num_errors
        
        error_positions = random.sample(range(n), num_errors)
        for pos in error_positions:
            received_word[pos] = F(1) - received_word[pos]
        
        decoded_word, status = decode_goppa(received_word, code)
        
        if status in ["success", "corrected"]:
            successful_decodes += 1
        else:
            detected_uncorrectable += 1
    
    decode_success_rate = successful_decodes / num_transmissions
    detected_uncorrectable_rate = detected_uncorrectable / num_transmissions
    avg_errors_per_transmission = total_errors / num_transmissions
    
    return decode_success_rate, detected_uncorrectable_rate, avg_errors_per_transmission
    

def run_simulation():
    error_rates = [0.01 * i for i in range(1, 50)]  # 1% to 20%
    num_transmissions = 100000
    codes = [create_goppa_code(16, m) for m in [3, 4, 5]]  # Using three codes for more variety
    
    plt.figure(figsize=(12, 8))
    
    all_avg_errors = []  # List to store avg_errors for each code
    
    for idx, code in enumerate(codes):
        decode_success_rates = []
        detected_uncorrectable_rates = []
        avg_errors = []
        
        print(f"Simulating Goppa code: [{code.length()}, {code.dimension()}, {code.minimum_distance()}] over GF({code.base_field().cardinality()})")
        
        for error_rate in error_rates:
            print(f"  Error rate: {error_rate:.2f}")
            success_rate, uncorrectable_rate, avg_error = simulate_transmission(code, error_rate, num_transmissions)
            decode_success_rates.append(success_rate)
            detected_uncorrectable_rates.append(uncorrectable_rate)
            avg_errors.append(avg_error)
        
        all_avg_errors.append(avg_errors)  # Store avg_errors for this code
        
        plt.plot(error_rates, decode_success_rates, label=f'Decode Success [{code.length()}, {code.dimension()}, {code.minimum_distance()}]')
        plt.plot(error_rates, detected_uncorrectable_rates, label=f'Detected Uncorrectable [{code.length()}, {code.dimension()}, {code.minimum_distance()}]')
    
    plt.xlabel('Error Rate')
    plt.ylabel('Rate')
    plt.title('Goppa Code Performance (Individual Codes)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Plot average errors
    plt.figure(figsize=(12, 8))
    for idx, code in enumerate(codes):
        plt.plot(error_rates, all_avg_errors[idx], label=f'Code [{code.length()}, {code.dimension()}, {code.minimum_distance()}]')
    plt.xlabel('Error Rate')
    plt.ylabel('Average Errors per Transmission')
    plt.title('Average Errors vs Error Rate')
    plt.legend()
    plt.grid(True)
    plt.show()
    
run_simulation()