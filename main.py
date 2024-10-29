from utils.motor import Motor
import time
import cv2

def main():
    motor = Motor()
    angles = motor.get_step_angle()
    print(angles)
    # waitkey로 키입력받아서 break 하는 코드
    while True:
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == ord('w'):     
        for i in range(4):
            motor.run_motor(1, angles[0][(3+i)%4])
            motor.run_motor(2, angles[1][(3+i)%4])
            motor.run_motor(7, angles[6][(3+i)%4])
            motor.run_motor(8, angles[7][(3+i)%4])
            motor.run_motor(4, angles[3][(1+i)%4])
            motor.run_motor(5, angles[4][(1+i)%4])
            motor.run_motor(10, angles[9][(1+i)%4])
            motor.run_motor(11, angles[10][(1+i)%4])
            time.sleep(0.2)
    #     elif key == ord('s'):      
    #         for i in range(4):
    #             motor.run_motor(1, angles[0][(3-i)%4])
    #             motor.run_motor(2, angles[1][(3-i)%4])
    #             motor.run_motor(7, angles[6][(3-i)%4])
    #             motor.run_motor(8, angles[7][(3-i)%4])
    #             motor.run_motor(4, angles[3][(1-i)%4])
    #             motor.run_motor(5, angles[4][(1-i)%4])
    #             motor.run_motor(10, angles[9][(1-i)%4])
    #             motor.run_motor(11, angles[10][(1-i)%4])
                # time.sleep(0.3)
        # elif key == ord('d'):
    # while(True):
        # for i in range(4):
        #     motor.run_motor(1, angles[0][(3+i)%4])
        #     motor.run_motor(2, angles[1][(3+i)%4])
        #     motor.run_motor(7, angles[6][(2-i)%4])
        #     motor.run_motor(8, angles[7][(2-i)%4])
        #     motor.run_motor(4, angles[3][(-i)%4])
        #     motor.run_motor(5, angles[4][(-i)%4])
        #     motor.run_motor(10, angles[9][(1+i)%4])
        #     motor.run_motor(11, angles[10][(1+i)%4])
        #     time.sleep(0.3)
        # else:
        #     print("wrong key")
    # # motor.set_position_limits(6, 500, 1500)
    # motor.run_motor(6,-100)


if __name__ == '__main__':
    main()