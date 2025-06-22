import requests
import os
from pathlib import Path

# 目标URL
url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 确保输出目录存在
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# 输出文件路径
kr_file = output_dir / "KRip.txt"
jp_file = output_dir / "JPip.txt"
sg_file = output_dir / "SGip.txt"

# 检查并删除已存在的文件
for file in [kr_file, jp_file, sg_file]:
    if file.exists():
        file.unlink()

# 使用集合来存储不同国家的IP地址，自动去重
kr_ips = set()
jp_ips = set()
sg_ips = set()

try:
    # 设置User-Agent模拟浏览器请求，避免被GitHub拦截
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # 发送HTTP请求获取网页内容
    response = requests.get(url, headers=headers, timeout=10)
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
    with open(kr_file, 'w') as f:
        f.write('\n'.join(kr_ips) + '\n')
    
    with open(jp_file, 'w') as f:
        f.write('\n'.join(jp_ips) + '\n')
    
    with open(sg_file, 'w') as f:
        f.write('\n'.join(sg_ips) + '\n')
    
    # 打印结果
    print(f'提取完成:')
    print(f'KR IPs: {len(kr_ips)} 个')
    print(f'JP IPs: {len(jp_ips)} 个')
    print(f'SG IPs: {len(sg_ips)} 个')

except requests.exceptions.RequestException as e:
    print(f'请求失败: {e}')
    exit(1)  # 非零退出码表示失败
except Exception as e:
    print(f'发生错误: {e}')
    exit(1)
