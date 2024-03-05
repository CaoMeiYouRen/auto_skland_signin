import json
import os
import re
from datetime import datetime
import subprocess
from auto_skland_signin import (
    adb_reset_tab,
    adb_swipe,
    calculate_center,
    get_OCR_result,
    get_resolution,
    get_screenshot,
    get_tab_height,
    send_notify,
    turn2main_page,
)

import logging
import logreset


if __name__ == "__main__":
    logreset.reset_logging()  # before you logging setting
    # 使用logging模块配置日志输出格式和级别
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", level="INFO"
    )
    # folder_name = "screenshots"
    # os.makedirs(folder_name, exist_ok=True)
    os.system(f"adb connect 127.0.0.1:16384")
    # 修改当前模拟器 分辨率，避免分辨率过高或过低。如果OCR效率较低，可以考虑降低分辨率 1080x1920 720x1280
    os.system("adb shell wm size 1080x1920")
    # 修改当前模拟器 DPI，解决DPI过高时 tab 栏缩一块了 320 240
    os.system("adb shell wm density 320")

    turn2main_page()

    screenshot_path = get_screenshot()
    result = get_OCR_result(screenshot_path)
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False)
    # pattern = r"今天是(\w+)的生日"
    for i in result:
        text = i[1][0]
