import requests
import os
from pathlib import Path

# 目标URL
url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 检查并删除已存在的文件
for filename in ['KRip.txt', 'JPip.txt', 'SGip.txt']:
    if os.path.exists(filename):
        os.remove(filename)

# 使用集合来存储不同国家的IP地址，自动去重
kr_ips = set()
jp_ips = set()
sg_ips = set()

try:
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    
    # 按行处理内容
    for line in response.text.splitlines():
        # 分割每行内容
        parts = line.split(',')
        if len(parts) >= 4:  # 确保有足够的部分
            ip = parts[0].strip()  # 提取第一个逗号前的IP
            country = parts[2].strip()  # 提取国家代码
            
            # 根据国家代码添加到相应的集合
            if country == 'KR':
                kr_ips.add(ip)
            elif country == 'JP':
                jp_ips.add(ip)
            elif country == 'SG':
                sg_ips.add(ip)
    
    # 将IP地址写入对应的文件
    with open('KRip.txt', 'w') as f:
        f.write('\n'.join(kr_ips) + '\n')
    
    with open('JPip.txt', 'w') as f:
        f.write('\n'.join(jp_ips) + '\n')
    
    with open('SGip.txt', 'w') as f:
        f.write('\n'.join(sg_ips) + '\n')
    
    # 打印结果
    print(f'提取完成:')
    print(f'KR IPs: {len(kr_ips)} 个')
    print(f'JP IPs: {len(jp_ips)} 个')
    print(f'SG IPs: {len(sg_ips)} 个')

except requests.exceptions.RequestException as e:
    print(f'请求失败: {e}')
except Exception as e:
    print(f'发生错误: {e}')
