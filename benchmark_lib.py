import time
import pandas as pd

class BenchmarkEngine:
    """
    Tool for benchmarking sorting algorithms.
    Features:
    1. Register algorithms.
    2. Run benchmarks on datasets.
    3. Save execution time results.
    4. Save sorted data (text file).
    """

    def __init__(self):
        self.algorithms = []
        self.results = []
        self.sorted_data_buffer = []

    def register_algorithm(self, name, func):
        """
        Register an algorithm for benchmarking.
        """
        self.algorithms.append((name, func))

    def run(self, datasets):
        """
        Run benchmarks on a list of datasets.
        """
        self.results = []
        self.sorted_data_buffer = []
        
        print(f"\n--- STARTING BENCHMARK ON {len(datasets)} DATASETS ---")
        
        for dataset in datasets:
            d_id = dataset['id']
            d_type = dataset['type']
            d_order = dataset['order']
            raw_data = dataset['data']
            
            print(f"Processing Dataset {d_id} ({d_type} - {d_order})...")
            
            # Stores the sorted version of the current dataset
            # (only one reference result is needed)
            current_sorted_result = None

            for algo_name, func in self.algorithms:
                # Copy input data to ensure fairness
                # (in case the sorting algorithm works in-place).
                # For safety in a shared benchmarking environment,
                # we assume each algorithm handles data integrity properly,
                # but we still pass a copied list here.
                data_input = raw_data.copy()

                start = time.perf_counter()
                sorted_output = func(data_input)
                end = time.perf_counter()
                
                execution_time = end - start

                # Record benchmark result
                self.results.append({
                    "Dataset_ID": d_id,
                    "Data_Type": d_type,
                    "Input_Order": d_order,
                    "Algorithm": algo_name,
                    "Time_Seconds": execution_time
                })

                # Save sorted output (overwrite with the latest result)
                if sorted_output is not None:
                    current_sorted_result = sorted_output

            # After all algorithms finish on this dataset, store sorted data
            if current_sorted_result is not None:
                self.sorted_data_buffer.append(current_sorted_result)
            else:
                self.sorted_data_buffer.append([])

        print(f"--- BENCHMARK COMPLETED ---")
        return pd.DataFrame(self.results)

    def save_to_csv(self, filename="Benchmark.csv"):
        """Save benchmark timing results to a CSV file"""
        if not self.results:
            print("No benchmark results to save.")
            return
        
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False)
        print(f"Benchmark report saved to: {filename}")