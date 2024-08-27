import subprocess
import time
import os

def force_connect(interface, network_name, password=None):
    """
    强制连接到指定网络。

    Args:
        interface (str): 网络接口名称，例如 "wlan0"。
        network_name (str): 要连接的网络名称。
        password (str, optional): 网络密码。默认为 None。
    """

    # 检查网络接口是否已连接
    if is_connected(interface):
        print(f"网络接口 {interface} 已连接。")
        return

    # 禁用网接口
    subprocess.run(["ifconfig", interface, "down"])
    time.sleep(1)

    # 尝试连接到网络
    if password:
        command = ["nmcli", "device", "connect", interface, "wifi", "name", network_name, "password", password]
    else:
        command = ["nmcli", "device", "connect", interface, "wifi", "name", network_name]

    subprocess.run(command)
    time.sleep(5)

    # 检查是否连接成功
    if is_connected(interface):
        print(f"已成功连接到网络 {network_name}。")
    else:
        print(f"连接到网络 {network_name} 失败。")

def is_connected(interface):
    """
    检查网络接口是否已连接。

    Args:
        interface (str): 网络接口名称，例如 "wlan0"。

    Returns:
        bool: True 如果已连接，否则 False。
    """

    output = subprocess.check_output(["nmcli", "device", "show", interface])
    return "STATE: connected" in output.decode("utf-8")

# 获取网络接口名称
interface = input("请输入网络接口名称 (例如 wlan0): ")

# 获取网络名称
network_name = input("请输入要连接的网络名称: ")

# 获取网络密码 (可选)
password = input("请输入网络密码 (可选): ")

# 强制连接到网络
force_connect(interface, network_name, password)
