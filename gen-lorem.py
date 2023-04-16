
import random

def create_file(size_mb):
    pattern = "0123456789" * 100000  # Repeat a pattern of digits 10 times
    with open(f"output_{size_mb}mb.txt", "w") as f:
        for _ in range(size_mb):
            f.write(pattern)
    print(f"File 'lorem-{size_mb}mb.txt' created with size {size_mb}MB.")


if __name__ == "__main__":
    size_mb = 5
    create_file(size_mb)

