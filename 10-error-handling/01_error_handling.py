file = open("youtube.txt", "w")

try:
    file.write("Hello Akkal")

except Exception as e:
    print(f"Error writing to file: {e}")

finally:
    file.close()
