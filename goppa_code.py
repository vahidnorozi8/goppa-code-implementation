from sage.all import *
import random

def create_goppa_code():
    k = GF(4, names=('a',))
    (a,) = k._first_ngens(1)
    A = AffineSpace(k, 2, names=('x', 'y'))
    (x, y) = A._first_ngens(2)
    C = Curve(y**2 - x - x**3)
    F = C.function_field()
    pls = F.places()
    Q, = C.places_at_infinity()
    pls.remove(Q)
    G = 3 * Q
    return codes.EvaluationAGCode(pls, G)

def calculate_parity_check_matrix(code):
    # The parity check matrix is the generator matrix of the dual code
    return code.dual_code().generator_matrix()

def decode_goppa(received_word, code):
    F = code.base_field()
    n = code.length()
    k = code.dimension()
    d = code.minimum_distance()
    t = (d-1)//2  # Error-correction capability
    
    # Step 1: Compute the syndrome
    H = calculate_parity_check_matrix(code)
    syndrome = H * received_word
    
    if syndrome.is_zero():
        return received_word  # No errors detected
    
    # Step 2: Set up the key equation
    S = Matrix(F, t, t)
    for i in range(t):
        for j in range(t):
            S[i,j] = syndrome[i+j]
    
    # Step 3: Solve the key equation
    try:
        sigma = S.solve_right(syndrome[t:2*t])
    except:
        # If the system is not solvable, decoding failure
        return None
    
    # Step 4: Find the roots of the error locator polynomial
    error_locator = [1] + list(sigma)
    error_positions = []
    for i in range(n):
        if sum(c * F(i)**j for j, c in enumerate(error_locator)) == 0:
            error_positions.append(i)
    
    # Step 5: Correct the errors
    corrected_word = vector(received_word)
    for pos in error_positions:
        corrected_word[pos] = F(1) - corrected_word[pos]
    
    return corrected_word

# Example usage
q = 4
C = create_goppa_code()
print(f"Created a [{C.length()}, {C.dimension()}, {C.minimum_distance()}] Goppa code over GF({q})")

# Generate and print the generator matrix
G = C.generator_matrix()
print("Generator Matrix:")
print(G)

# Generate and print the parity check matrix
H = calculate_parity_check_matrix(C)
print("Parity Check Matrix:")
print(H)

# Generate a random message and encode it
k = C.dimension()
message = vector(GF(q), [randint(0, q-1) for _ in range(k)])
codeword = C.encode(message)

# Simulate transmission with errors
max_errors = (C.minimum_distance() - 1) // 2
num_errors = randint(0, max_errors)
error_positions = random.sample(range(C.length()), num_errors)
received_word = vector(codeword)
for pos in error_positions:
    received_word[pos] += GF(q).random_element()

# Decode
decoded_codeword = decode_goppa(received_word, C)

print(f"Original message: {message}")
print(f"Encoded codeword: {codeword}")
print(f"Received word (with {num_errors} errors): {received_word}")
print(f"Decoded codeword: {decoded_codeword}")
print(f"Decoding successful: {decoded_codeword == codeword}")