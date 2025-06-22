import requests
import re
import os

# 目标URL
url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 正则表达式用于匹配IP地址
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# 检查ip.txt文件是否存在,如果存在则删除它
if os.path.exists('ip.txt'):
    os.remove('ip.txt')

# 使用集合来存储IP地址，自动去重
unique_ips = set()

# 发送HTTP请求获取内容
response = requests.get(url)

# 直接提取文本内容（因为GitHub Raw返回的是纯文本，不是HTML）
content = response.text

# 查找所有IP地址
ip_matches = re.findall(ip_pattern, content)

# 将找到的IP地址添加到集合中（自动去重）
unique_ips.update(ip_matches)

# 将去重后的IP地址写入文件
with open('ip.txt', 'w') as file:
    for ip in unique_ips:
        file.write(ip + '\n')

print(f'共找到 {len(unique_ips)} 个唯一IP地址，已保存到ip.txt文件中。')
