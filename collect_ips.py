import requests
import os

# 目标URL
target_url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 检查并删除旧文件
for filename in ['SGip.txt', 'JPip.txt', 'KRip.txt']:
    if os.path.exists(filename):
        os.remove(filename)

# 存储分类IP
sg_ips = set()
jp_ips = set()
kr_ips = set()

try:
    # 获取原始数据
    response = requests.get(target_url, timeout=10)
    response.raise_for_status()
    
    # 按行处理数据
    for line in response.text.splitlines():
        # 分割每行数据
        parts = line.split(',')
        if len(parts) >= 3:  # 确保有足够的部分
            ip = parts[0].strip()  # 第一个逗号前的IP
            country = parts[2].strip()  # 国家代码
            
            # 根据国家代码分类
            if country == 'SG':
                sg_ips.add(ip)
            elif country == 'JP':
                jp_ips.add(ip)
            elif country == 'KR':
                kr_ips.add(ip)
    
    # 写入各自文件
    with open('SGip.txt', 'w') as f:
        f.write('\n'.join(sorted(sg_ips)))
    
    with open('JPip.txt', 'w') as f:
        f.write('\n'.join(sorted(jp_ips)))
    
    with open('KRip.txt', 'w') as f:
        f.write('\n'.join(sorted(kr_ips)))
    
    print(f'处理完成:')
    print(f'- 新加坡(SG)IP: {len(sg_ips)}个')
    print(f'- 日本(JP)IP: {len(jp_ips)}个')
    print(f'- 韩国(KR)IP: {len(kr_ips)}个')

except Exception as e:
    print(f'处理出错: {str(e)}')
