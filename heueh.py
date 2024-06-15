def lfsr(seed):
    state = seed
    while True:
        feedback = (state >> 2) ^ (state >> 1) ^ state
        yield state & 1
        state = ((state << 1) & 0b111) | (feedback & 1)

# Example usage
if __name__ == "__main__":
    # Set the seed to 0b101 to generate a 3-bit LFSR
    rng = lfsr(0b101)
    for i in range(10):
        print(next(rng))
