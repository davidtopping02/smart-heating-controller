import RPi.GPIO as GPIO

servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

current_position = 0


def move_servo(position):
    global current_position
    if position not in [1, 2, 3, 4, 5]:
        return "Invalid position"

    duty_cycle = position * 5
    servo.ChangeDutyCycle(duty_cycle)

    current_position = position

    return f"Moved to position {position}"


def get_servo_position():
    return current_position
