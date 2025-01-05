import RPi.GPIO as GPIO

servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50Hz frequency
servo.start(0)

# Map the position to the corresponding angle (0, 30, 60, 90, 120 degrees)
# Duty cycle for the angles: approx. 2.5% for 0° and 12.5% for 180° (typical values)
position_to_duty = {
    1: 2.5,   # 0 degrees
    2: 5.0,   # 30 degrees
    3: 7.5,   # 60 degrees
    4: 10.0,  # 90 degrees
    5: 12.5   # 120 degrees
}

current_position = 0


def move_servo(position):
    global current_position
    if position not in [1, 2, 3, 4, 5]:
        return "Invalid position"

    duty_cycle = position_to_duty[position]
    servo.ChangeDutyCycle(duty_cycle)

    current_position = position
    return f"Moved to position {position}"


def get_servo_position():
    return current_position
