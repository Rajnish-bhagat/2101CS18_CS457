import aes, os
import time
import psutil  # Import psutil to measure memory and CPU utilizationsour

# Read input message from input.txt
with open('input.txt', 'r') as infile:
    input_message = infile.read().strip().encode()  # Read and convert to bytes

# Generate a random key and IV
key = os.urandom(16)
iv = os.urandom(16)

# Get current process for resource tracking
process = psutil.Process(os.getpid())

# Measure encryption time and resource usage
start_encrypt = time.time()  # Start the timer for encryption
cpu_before_encrypt = psutil.cpu_percent(interval=None)  # Capture CPU usage before encryption
memory_before_encrypt = process.memory_info().rss  # Capture memory usage before encryption
encrypted = aes.AES(key).encrypt_cbc(input_message, iv)
end_encrypt = time.time()  # End the timer for encryption
cpu_after_encrypt = psutil.cpu_percent(interval=None)  # Capture CPU usage after encryption
memory_after_encrypt = process.memory_info().rss  # Capture memory usage after encryption

encryption_time = end_encrypt - start_encrypt  # Calculate encryption time
encryption_memory_usage = (memory_after_encrypt - memory_before_encrypt) / 1024  # In KB
encryption_cpu_usage = cpu_after_encrypt - cpu_before_encrypt  # CPU difference

# Measure decryption time and resource usage
start_decrypt = time.time()  # Start the timer for decryption
cpu_before_decrypt = psutil.cpu_percent(interval=None)  # Capture CPU usage before decryption
memory_before_decrypt = process.memory_info().rss  # Capture memory usage before decryption
decrypted = aes.AES(key).decrypt_cbc(encrypted, iv)
end_decrypt = time.time()  # End the timer for decryption
cpu_after_decrypt = psutil.cpu_percent(interval=None)  # Capture CPU usage after decryption
memory_after_decrypt = process.memory_info().rss  # Capture memory usage after decryption

decryption_time = end_decrypt - start_decrypt  # Calculate decryption time
decryption_memory_usage = (memory_after_decrypt - memory_before_decrypt) / 1024  # In KB
decryption_cpu_usage = cpu_after_decrypt - cpu_before_decrypt  # CPU difference

# Open cipher.txt for writing the output
with open('cipher.txt', 'w') as outfile:
    # Write all information to the file
    outfile.write(f"Key (hex): {key.hex()}\n")
    outfile.write(f"IV (hex): {iv.hex()}\n")
    outfile.write(f"Encrypted (hex): {encrypted.hex()}\n")

    # Write encryption and decryption times to the file
    outfile.write(f"Encryption time: {encryption_time:.6f} seconds\n")
    outfile.write(f"Decryption time: {decryption_time:.6f} seconds\n")
    
    # Write memory and CPU utilization for encryption
    outfile.write(f"Encryption memory usage: {encryption_memory_usage:.2f} KB\n")
    outfile.write(f"Encryption CPU usage: {encryption_cpu_usage:.6f}%\n")
    
    # Write memory and CPU utilization for decryption
    outfile.write(f"Decryption memory usage: {decryption_memory_usage:.2f} KB\n")
    outfile.write(f"Decryption CPU usage: {decryption_cpu_usage:.2f}%\n")
    
    # Write decrypted message to the file
    outfile.write(f"Decrypted: {decrypted.decode()}\n")

# Print the key, IV, and encrypted message in hex format to the console
print("Key (hex):", key.hex())
print("IV (hex):", iv.hex())
# print("Encrypted (hex):", encrypted.hex())

# Print the decrypted message and times to the console
# print("Decrypted:", decrypted.decode())
print(f"Encryption time: {encryption_time:.6f} seconds")
print(f"Decryption time: {decryption_time:.6f} seconds")

# Print memory and CPU utilization to the console
print(f"Encryption memory usage: {encryption_memory_usage:.2f} KB")
print(f"Encryption CPU usage: {encryption_cpu_usage:.2f}%")
print(f"Decryption memory usage: {decryption_memory_usage:.2f} KB")
print(f"Decryption CPU usage: {decryption_cpu_usage:.2f}%")
