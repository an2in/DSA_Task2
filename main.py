from data_generator import DatasetGenerator
from sorting_algorithms import SortingAlgorithms
from benchmark_lib import BenchmarkEngine

def main():
    DatasetGenerator.generate_all("Unsorted_Data.txt")
    datasets = DatasetGenerator.load_data("Unsorted_Data.txt")

    engine = BenchmarkEngine()
    engine.register_algorithm("QuickSort", SortingAlgorithms.quicksort)
    engine.register_algorithm("HeapSort", SortingAlgorithms.heapsort)
    engine.register_algorithm("MergeSort", SortingAlgorithms.mergesort)
    engine.register_algorithm("NumPy", SortingAlgorithms.numpy_sort)

    engine.run(datasets)
    
    engine.save_to_csv("Benchmark.csv")
    print("Done")

if __name__ == "__main__":
    main()