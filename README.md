# CA_assignment

## Question 1: Signed Binary Arithmetic

### Aim
To develop a Python program to perform signed binary arithmetic using 8-bit 2's complement representation.

### Expressions
1. 45 - (+19)
2. (-35) - (-12)

### Concepts Used
- 8-bit 2's complement
- Binary subtraction
- Binary to decimal conversion
- Arithmetic overflow detection

### Expected Results

| Expression | Binary Result | Decimal Result |
|---|---|---|
| 45 - (+19) | 00011010 | 26 |
| (-35) - (-12) | 11101001 | -23 |

### Program File
`question1.py`

---

## Question 2: Rotate Operations

### Aim
To develop a Python program to perform rotate operations on 8-bit binary numbers.

### Operations
1. Rotate Left without Carry (ROL) on `10110110` by 2 positions.
2. Rotate Left with Carry (RCL) on `10110110` by 2 positions.

Initial carry flag for RCL is assumed to be 0.

### Expected Results

| Operation | Final Binary Result | Final Carry |
|---|---|---|
| ROL by 2 | 11011010 | Not applicable |
| RCL by 2 | 11011001 | 0 |

### Concepts Used
- 8-bit binary numbers
- Rotate left operation
- Carry flag
- Step-by-step binary rotation

### Program File
`question2.py`

---

## How to Run the Programs

### Question 1
```bash
python question1.py
```

### Question 2
```bash
python question2.py
```

## Conclusion

These programs demonstrate 8-bit signed binary arithmetic,
2's complement subtraction, rotate-left operations, carry flags,
and arithmetic overflow detection.

The results can be verified using manual binary calculations.
