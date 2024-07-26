# Goppa Code Implementation

This project implements a Goppa code, which is a type of error-correcting code. The implementation is based on the research presented in the following paper:

[Your Name], "[Your Paper Title]," [Journal/Conference Name], [Year].

## Citation

If you use this code in your research, please cite:

```
@article{YourLastName_Year,
  title={Your Paper Title},
  author={Your Full Name},
  journal={Journal/Conference Name},
  year={Year},
  volume={Volume},
  pages={Page Range},
  doi={DOI if available}
}
```

## Features

- Creation of a Goppa code
- Calculation of parity check matrix
- Encoding and decoding functions
- Error simulation and correction

## Usage

To use this implementation:

1. Ensure you have Python 3.x and SageMath installed.
2. Clone this repository:
   ```
   git clone https://github.com/vahidnorozi87/goppa-code-implementation.git
   ```
3. Navigate to the project directory:
   ```
   cd goppa-code-implementation
   ```
4. Run the script:
   ```
   sage goppa_code.py
   ```

## Sample Output

Below is a sample output from running the script Goppa_code:

```
Created a [8, 3, 5] Goppa code over GF(4) on y^2+y=x^3
Generator Matrix:
[    1     0     0     1     a a + 1     1     0]
[    0     1     0     1     1     0 a + 1     a]
[    0     0     1     1     a     a a + 1 a + 1]
Parity Check Matrix:
[    1     0     0     0     0 a + 1 a + 1     1]
[    0     1     0     0     0 a + 1     a     0]
[    0     0     1     0     0     a     1     a]
[    0     0     0     1     0     a     0 a + 1]
[    0     0     0     0     1     1     1     1]
Original message: (1, 0, 0)
Encoded codeword: (1, 0, 0, 1, a, a + 1, 1, 0)
Received word (with 0 errors): (1, 0, 0, 1, a, a + 1, 1, 0)
Decoded codeword: (1, 0, 0, 1, a, a + 1, 1, 0)
Decoding successful: True
```

This output demonstrates the creation of an [8, 3, 5] Goppa code over GF(4), shows the generator and parity check matrices, and illustrates the encoding and decoding process.

## Requirements

- Python 3.x
- SageMath

## Contact

For questions or collaborations, please contact Vahid at vahidnorozi87@gmail.com.
