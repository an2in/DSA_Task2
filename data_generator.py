import random
import sys

class DatasetGenerator:
    """
    Library to generate a dataset consisting of 10 number sequences (1 million elements per sequence).
    Also supports loading and parsing the generated data.
    """
    @staticmethod
    def generate_all(filename):
        """Generates 10 sequences of numbers and writes them to a file."""
        SIZE = 1_000_000
        MAX_F = sys.float_info.max
        MIN_F = -sys.float_info.max
        MAX_I = sys.maxsize
        MIN_I = -sys.maxsize - 1

        with open(filename, 'w') as f:
            # Sequence 1: Floating-point numbers, ascending order
            arr = [random.uniform(MIN_F, MAX_F) for _ in range(SIZE)]
            arr.sort()
            f.write(" ".join(map(str, arr)) + "\n")
            del arr 

            # Sequence 2: Floating-point numbers, descending order
            arr = [random.uniform(MIN_F, MAX_F) for _ in range(SIZE)]
            arr.sort(reverse=True)
            f.write(" ".join(map(str, arr)) + "\n")
            del arr

            # Sequences 3, 4, 5: Floating-point numbers, random order
            for _ in range(3):
                arr = [random.uniform(MIN_F, MAX_F) for _ in range(SIZE)]
                f.write(" ".join(map(str, arr)) + "\n")
                del arr

            # Sequences 6, 7, 8, 9, 10: Integers, random order
            for _ in range(5):
                arr = [random.randint(MIN_I, MAX_I) for _ in range(SIZE)]
                f.write(" ".join(map(str, arr)) + "\n")
                del arr
    
    @staticmethod
    def load_data(filename):
        datasets = []
        print(f"Reading data from {filename}...")
        
        with open(filename, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            parts = line.strip().split()
            if not parts: continue

            # Logic determined by generate_all:
            # Lines 0-4 are Floats, Lines 5-9 are Integers
            if i < 5:
                data = list(map(float, parts))
                dtype = "Float"
            else:
                data = list(map(int, parts))
                dtype = "Integer"

            # Determine Metadata for Benchmark
            if i == 0: order = "Ascending"
            elif i == 1: order = "Descending"
            else: order = "Random"

            datasets.append({
                "id": i + 1,
                "data": data,
                "type": dtype,
                "order": order
            })
            
        print(f"Loaded {len(datasets)} datasets successfully.")
        return datasets