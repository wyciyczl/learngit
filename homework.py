from pathlib import Path
import numpy as np
import pickle
import invoke
from threading import Thread
import time
import subprocess

# 用于生成字符画的像素，越往后视觉上越明显。。这是我自己按感觉排的，你可以随意调整。写函数里效率太低，所以只好放全局了
pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"


def video2imgs(video_name, size, seconds):
    """
    :param video_name: 字符串, 视频文件的路径
    :param size: 二元组，(宽, 高)，用于指定生成的字符画的尺寸
    :param seconds: 指定需要解码的时长（0-seconds）
    :return: 一个 img 对象的列表，img对象实际上就是 numpy.ndarray 数组
    """
    import cv2  # 导入 opencv，放这里是为了演示，建议放文件开头

    img_list = []

    # 从指定文件创建一个VideoCapture对象
    cap = cv2.VideoCapture(video_name)

    # 帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 需要提取的帧数
    frames_count = fps * seconds

    count = 0
    # cap.isOpened(): 如果cap对象已经初始化完成了，就返回true
    while cap.isOpened() and count < frames_count:
        # cap.read() 返回值介绍：
        #   ret 表示是否读取到图像
        #   frame 为图像矩阵，类型为 numpy.ndarry.
        ret, frame = cap.read()
        if ret:
            # 转换成灰度图，也可不做这一步，转换成彩色字符视频。
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # resize 图片，保证图片转换成字符画后，能完整地在命令行中显示。
            img = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)

            # 分帧保存转换结果
            img_list.append(img)

            count += 1
        else:
            break

    # 结束时要释放空间
    cap.release()

    return img_list, fps
