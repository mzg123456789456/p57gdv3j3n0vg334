import requests
import re
import os

# 目标URL
url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 正则表达式用于匹配IP地址
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# 检查文件是否存在，如果存在则删除
def clear_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

clear_file('jip.txt')  # 清理 jip.txt
clear_file('kip.txt')  # 清理 kip.txt
clear_file('sip.txt')  # 清理 sip.txt

# 使用集合来存储符合条件的IP地址（自动去重）
japan_ips = set()  # 存储 JP 相关的 IP
korea_ips = set()  # 存储 KR 相关的 IP
Singapore_ips = set()  # 存储 SG 相关的 IP

# 发送HTTP请求获取内容
response = requests.get(url)
content = response.text

# 查找所有IP地址及其上下文
ip_matches = re.finditer(ip_pattern, content)

for match in ip_matches:
    ip = match.group()
    # 获取IP前后的文本（用于检查是否包含443和JP/KR）
    start_pos = max(0, match.start() - 20)  # 往前取20个字符
    end_pos = min(len(content), match.end() + 20)  # 往后取20个字符
    context = content[start_pos:end_pos]
    
    # 检查是否包含443及JP（日本）
    if "443" in context and ("JP" in context or "jp" in context):
        japan_ips.add(ip)
    
    # 检查是否包含443及KR（韩国）
    if "443" in context and ("KR" in context or "kr" in context):
        korea_ips.add(ip)

    # 检查是否包含443及SG（新加坡）
    if "443" in context and ("SG" in context or "sg" in context):
        korea_ips.add(ip)

# 将符合条件的IP地址写入文件
with open('jip.txt', 'w') as file:
    for ip in japan_ips:
        file.write(ip + '\n')

with open('kip.txt', 'w') as file:
    for ip in korea_ips:
        file.write(ip + '\n')

with open('sip.txt', 'w') as file:
    for ip in korea_ips:
        file.write(ip + '\n')

print(f'共找到 {len(japan_ips)} 个符合条件的日本IP地址（含443和JP），已保存到jip.txt文件中。')
print(f'共找到 {len(korea_ips)} 个符合条件的韩国IP地址（含443和KR），已保存到kip.txt文件中。')
print(f'共找到 {len(Singapore_ips)} 个符合条件的新加坡IP地址（含443和SG），已保存到sip.txt文件中。')
