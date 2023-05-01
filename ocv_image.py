import numpy as np
import cv2 as cv
import time

def cvimshow(show_name, show_img):
    img_size = show_img.shape
    show_scale = min(480.0/img_size[1], 320.0/img_size[0], 1.0)
    show_size = (int(img_size[1]*show_scale), int(img_size[0]*show_scale))
    cv.imshow(show_name, cv.resize(show_img, show_size, interpolation = cv.INTER_AREA))

def vision_check(vision_img):
    #convert what I need
    #gray_img = cv.cvtColor(vision_img, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(vision_img,cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)
    #Threshold H val to find socket pos
    ret, h_fix_val_th = cv.threshold(h, h_val, 255, cv.THRESH_BINARY_INV)
    cvimshow("Calc_Socket_Pos" ,h_fix_val_th)
    #bit and V val to take out non-socket image
    hvand = cv.bitwise_and(h_fix_val_th, v)
    cvimshow("Gray_Socket", hvand)
    #Threshold socket image to get IC pos
    if isUseCanny:
        #canny
        canny_img = cv.Canny(hvand, 50, 255)
        canny_img_inv = cv.bitwise_not(canny_img)
        canny_sck = cv.bitwise_and(canny_img_inv, hvand)
        cvimshow("Canny_Socket", canny_sck)
        ret, result = cv.threshold(canny_sck, v_val, 255, cv.THRESH_BINARY)
    else:
        ret, result = cv.threshold(hvand, v_val, 255, cv.THRESH_BINARY)
    cvimshow("Result", result)
    #Find out pos
    contours, hierarchy = cv.findContours(result, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #draw Pos
    calc_total = 0
    pos_all = np.zeros((len(contours), 2))
    for find_pos in contours:
        m_val = cv.moments(find_pos)
        if m_val['m00'] > min_area:
            cv.drawContours(vision_img, [find_pos], -1, (0, 255, 0), 5) #green
            center_x, center_y = int(m_val["m10"] / m_val["m00"]), int(m_val["m01"] / m_val["m00"])
            cv.circle(vision_img, (center_x, center_y), 5, (0, 0, 255), 5) #red
            try:
                for (check_x, check_y) in pos_all:
                    if check_x == 0:
                        raise ZeroDivisionError("Loop End")
                    if abs(center_x - check_x) + abs(center_y - check_y) < 40:
                        break
            except ZeroDivisionError:
                pos_all[calc_total] = [center_x, center_y]
                calc_total += 1
                cv.circle(vision_img, (center_x, center_y), min_dist, (255, 0, 0), 5) #blue
    print(f"Total {calc_total} found.")
    cvimshow("Vision_img", vision_img)

if __name__ == '__main__':
    isUseCanny = False
    isBar121 = True
    isCamera = False
    if isCamera:
        pass
    elif isBar121:
        h_val = 25
        v_val = 200
        min_area = 100
        min_dist = 40
    else:
        h_val = 35
        v_val = 95
        min_area = 35
        min_dist = 1
        
    #read from file
    while True:
        if isCamera:
            pass
        elif isBar121:
            read_frame = cv.imread('jam.jpg')
        else:
            read_frame = cv.imread('jam4.jpg')
        cvimshow("Orig_img", read_frame)

        start_time = time.time()
        if isCamera:
            pass
        elif isBar121:
            vision_src = read_frame[1500:3400,:]
        else:
            vision_src = read_frame[:]
        vision_check(vision_src)
        period_time = time.time() - start_time
        print(f"h_val = {h_val} , v_val = {v_val}, min_area = {min_area}, min_dist = {min_dist}, period = {period_time:.3f}")

        key_pressed = cv.waitKey(0)
        if key_pressed == ord('q'):
            break
        elif key_pressed == ord('H'):
            h_val = min(h_val + 5, 255)
        elif key_pressed == ord('h'):
            h_val = max(0, h_val - 5)
        elif key_pressed == ord('V'):
            v_val = min(v_val + 5, 255)
        elif key_pressed == ord('v'):
            v_val = max(0, v_val - 5)
        elif key_pressed == ord('A'):
            min_area = min(min_area + 5, 10000)
        elif key_pressed == ord('a'):
            min_area = max(1, min_area - 5)
        elif key_pressed == ord('D'):
            min_dist = min(min_dist + 1, 10000)
        elif key_pressed == ord('d'):
            min_dist = max(1, min_dist - 1)
    cv.destroyAllWindows()
