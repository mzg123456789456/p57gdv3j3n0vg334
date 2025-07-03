import requests
import re
import random

# 目标URL
url = 'https://raw.githubusercontent.com/mzg123456789456/p57gdv3j3n0vg334/refs/heads/main/f74bjd2h2ko99f3j5'

# 正则表达式匹配 IP 和端口
ip_port_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)'

# 存储不同国家的 IP
country_ips = {
    "日本": [],
    "韩国": [],
    "新加坡": []
}

# 发送 HTTP 请求获取内容
response = requests.get(url)
content = response.text

# 查找所有 IP:端口 组合
ip_port_matches = re.finditer(ip_port_pattern, content)

for match in ip_port_matches:
    ip = match.group(1)  # IP 地址
    port = match.group(2)  # 端口
    start_pos = max(0, match.start() - 20)  # 往前取 20 个字符
    end_pos = min(len(content), match.end() + 20)  # 往后取 20 个字符
    context = content[start_pos:end_pos]

    # 检查国家（JP=日本, KR=韩国, SG=新加坡）
    if "JP" in context or "jp" in context:
        country = "日本"
    elif "KR" in context or "kr" in context:
        country = "韩国"
    elif "SG" in context or "sg" in context:
        country = "新加坡"
    else:
        continue  # 如果不是这 3 个国家，跳过

    if port == "443":  # 仅保留 443 端口的 IP
        country_ips[country].append(f"{ip}:{port}#{country}")

# 每个国家随机选 20 个 IP（如果不足 20 个，则全部选取）
selected_ips = []
for country, ips in country_ips.items():
    random.shuffle(ips)  # 打乱顺序
    selected = ips[:20] if len(ips) >= 20 else ips  # 最多取 20 个
    selected_ips.extend(selected)

# 按国家排序（日本→韩国→新加坡）
selected_ips_sorted = sorted(selected_ips, key=lambda x: x.split("#")[1])

# 覆盖写入 iplist.txt（格式：IP:端口#国家编号）
with open('iplist.txt', 'w') as file:
    country_count = {"日本": 1, "韩国": 1, "新加坡": 1}  # 每个国家的编号从 1 开始
    for entry in selected_ips_sorted:
        country = entry.split("#")[1]
        file.write(f"{entry}{country_count[country]}\n")  # 如 152.168.31.26:443#日本1
        country_count[country] += 1  # 编号递增

print(f"已提取 60 个 IP（日本 {len(country_ips['日本'][:20])} 个，韩国 {len(country_ips['韩国'][:20])} 个，新加坡 {len(country_ips['新加坡'][:20])} 个）")
print(f"结果已覆盖保存到 iplist.txt")
