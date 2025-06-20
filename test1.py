from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.1)
    if i == 99:
        time.sleep(2)