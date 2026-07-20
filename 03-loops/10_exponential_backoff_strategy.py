import time

"""

Problem 10: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

"""

print(f"Current Date and Time: {time.ctime()}\n")

wait_time = 1
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    print("Attempt", attempts + 1, "failed. Retrying in", wait_time, "seconds...")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2

print("Maximum attempts reached. Exiting...")
