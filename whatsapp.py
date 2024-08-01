import pywhatkit as kit
import time

# Define parameters
phone_number = "+916377781395"  # The phone number should include the country code
message = "Hello"
hour = 16   # 24-hour format
minute = 3  # You can set this to a time at least 1 minute ahead of the current time

print(f"Scheduling message '{message}' to {phone_number} at {hour}:{minute}")

# Send the WhatsApp message
kit.sendwhatmsg(phone_number, message, hour, minute)

# Optional: Sleep to ensure the message is sent
time.sleep(10)
print("Message scheduled. Please ensure you are logged into WhatsApp Web.")
