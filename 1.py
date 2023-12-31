import socket
import cv2
import pygame
import numpy as np

# 建立TCP连接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 8888)  # Unity客户端地址和端口号
server_socket.bind(ip_port)
server_socket.listen(5)

# 等待Unity客户端连接
print('Start waiting for Unity connection...')
conn, addr = server_socket.accept()
print('Unity client connected:', addr)

# 初始化摄像头
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 设置宽度
cap.set(4, 480)  # 设置高度

# 初始化Pygame和窗口
pygame.init()
pygame.font.init()
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gesture Recognition")

# 加载字体
font = pygame.font.Font(None, 36)

while True:
    text = "Unrecognized gesture"
    # 接收Unity客户端传来的数据
    recv_data = conn.recv(1024)
    message = recv_data.decode('utf-8')
    print('Received message:', message)

    # 使用OpenCV进行手势识别
    # ...
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 翻转帧以使镜像效果与电脑屏幕一致
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义HSV中绿色的范围
    lower_green = np.array([29, 86, 6])
    upper_green = np.array([64, 255, 255])

    # 在图像中提取绿色对象
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 对二值图像进行模糊处理
    mask = cv2.blur(mask, (10, 10))

    # 通过找到最大轮廓确定手的位置
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]

    if len(areas) > 0:
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        hull = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull)
        finger_count = 0
        M = cv2.moments(cnt)

        if M["m00"] != 0:
            # 计算手的中心位置
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # 在图像上绘制轮廓和中心点
            cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

            # 判断是否握拳或张开手指
            if len(cnt) > 8:
                text = "Open Hand"
                print(text)
            else:
                text = "Fist"
                print(text)
            
            # 在Pygame窗口上显示识别结果
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = (width // 2, height - 50)
            win.blit(text_surface, text_rect)
    
    # 向Unity客户端发送数据
    send_data = text.encode('utf-8')
    conn.sendall(send_data)

    # 显示手势识别结果
    # ...
    # 在Pygame窗口上显示摄像头的画面
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    win.blit(frame, (0, 0))
    pygame.display.update()

    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            #exit(0)
            quit()
