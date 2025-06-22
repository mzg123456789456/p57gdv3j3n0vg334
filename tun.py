import requests
from bs4 import BeautifulSoup
import re
import os

# 目标URL列表
urls = ['https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'
        ]

# 正则表达式用于匹配IP地址和端口
ip_port_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::(\d+))?(?:\s+\((SG|JP|KR)\))?'

# 检查文件是否存在，如果存在则删除
for filename in ['SGip.txt', 'JPip.txt', 'KRip.txt', 'ip.txt']:
    if os.path.exists(filename):
        os.remove(filename)

# 使用集合来存储IP地址，自动去重
unique_ips = set()
sg_ips = set()
jp_ips = set()
kr_ips = set()

for url in urls:
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 根据网站的不同结构找到包含IP地址的元素
        if url in ['https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'
                  ]:
            elements = soup.find_all('tr')
        else:
            elements = soup.find_all('li')
        
        # 遍历所有元素,查找IP地址
        for element in elements:
            element_text = element.get_text()
            matches = re.finditer(ip_port_pattern, element_text)
            
            for match in matches:
                ip = match.group(1)
                port = match.group(2) or ''  # 如果没有端口则为空字符串
                country = match.group(3) or ''  # 如果没有国家代码则为空字符串
                
                # 添加到总IP集合
                unique_ips.add(ip)
                
                # 根据端口和国家代码分类
                if port == '443':
                    if country == 'SG':
                        sg_ips.add(ip)
                    elif country == 'JP':
                        jp_ips.add(ip)
                    elif country == 'KR':
                        kr_ips.add(ip)
    
    except Exception as e:
        print(f"处理 {url} 时出错: {str(e)}")
        continue

# 将IP地址写入不同的文件
with open('ip.txt', 'w') as file:
    for ip in unique_ips:
        file.write(ip + '\n')

with open('SGip.txt', 'w') as file:
    for ip in sg_ips:
        file.write(ip + '\n')

with open('JPip.txt', 'w') as file:
    for ip in jp_ips:
        file.write(ip + '\n')

with open('KRip.txt', 'w') as file:
    for ip in kr_ips:
        file.write(ip + '\n')

print(f'共找到 {len(unique_ips)} 个唯一IP地址')
print(f'新加坡(SG)IP(443端口): {len(sg_ips)} 个，已保存到SGip.txt')
print(f'日本(JP)IP(443端口): {len(jp_ips)} 个，已保存到JPip.txt')
print(f'韩国(KR)IP(443端口): {len(kr_ips)} 个，已保存到KRip.txt')
