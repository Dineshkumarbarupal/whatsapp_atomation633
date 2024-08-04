import pywhatkit as kit
import time

phone_number = "+916377781395"
message = "Hi, this is an automatically sent message"
hour = 13
minute = 44


while True:
    try:
        # Current time ko adjust karke next minute par message bhejna
        current_time = time.localtime()
        next_minute = current_time.tm_min + 1
        if next_minute == 60:
            next_minute = 0
            hour = (hour + 1) % 24

        # Message bhejne ka function call
        kit.sendwhatmsg(phone_number, message, hour, next_minute)
        print(f"Message sent at {hour}:{next_minute}")

        # 5 seconds wait karna
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
