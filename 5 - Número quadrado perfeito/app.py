from concurrent.futures import ProcessPoolExecutor
import numpy as np

def worker(chunk):
    return len([num for num in chunk if is_perfect_square(num)])

def is_perfect_square(n):
    return n == int(n**0.5)**2

if __name__ == "__main__":
    NUM_WORKERS = 8
    arr = np.load("A.npy")

    chunks = np.array_split(arr, NUM_WORKERS)

    with ProcessPoolExecutor(max_workers=NUM_WORKERS) as pool:
        results = pool.map(worker, chunks)
    
    total_perfect_squares = sum(results)
    
    print(f"Total de números quadrados perfeitos: {total_perfect_squares}")
