import time
import os
 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Simple Stopwatch")
print("Press Ctrl+c to stop")
print("Starting in 3 seconds...")
time.sleep(3)

start_time = time.time()

try:
    while True:
        elapsed_time = time.time() - start_time
        hours = int(elapsed_time // 3600)
                                               
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        
        clear_screen()
        print(f"Time: {minutes:02d}:{seconds:02d}")
        time.sleep(0.1)

except KeyboardInterrupt:
    clear_screen()
    final_time = time.time() - start_time
    final_hours = int(final_time // 3600)
    final_minutes = int(final_time // 60)
    final_seconds = int(final_time % 60)
    print(f"\nFinal Time: {final_minutes:02d}:{final_seconds:02d}")
    print("Stopwatch stopped!")
