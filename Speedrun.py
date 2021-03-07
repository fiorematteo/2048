import Main
import time

while True:
    start = time.perf_counter()
    Main.main()
    end = time.perf_counter() - start
    print(f"time = {end}")
