import requests
import re
import os

# 目标URL
url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 正则表达式用于匹配IP地址
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# 检查ip.txt文件是否存在,如果存在则删除它
if os.path.exists('sgip.txt'):
    os.remove('sgip.txt')

# 使用集合来存储符合条件的IP地址（自动去重）
filtered_ips = set()

# 发送HTTP请求获取内容
response = requests.get(url)
content = response.text

# 查找所有IP地址及其上下文
ip_matches = re.finditer(ip_pattern, content)

for match in ip_matches:
    ip = match.group()
    # 获取IP前后的文本（用于检查是否包含443和SG）
    start_pos = max(0, match.start() - 20)  # 往前取20个字符
    end_pos = min(len(content), match.end() + 20)  # 往后取20个字符
    context = content[start_pos:end_pos]
    
    # 检查是否同时包含 "443" 和 "SG"（不区分大小写）
    if "443" in context and ("SG" in context or "sg" in context):
        filtered_ips.add(ip)

# 将符合条件的IP地址写入文件
with open('sgip.txt', 'w') as file:
    for ip in filtered_ips:
        file.write(ip + '\n')

print(f'共找到 {len(filtered_ips)} 个符合条件的IP地址（含443和SG），已保存到ip.txt文件中。')
