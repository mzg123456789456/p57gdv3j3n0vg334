import schedule
import time


def reformat_file():
    new_content = []
    with open('f74bjd2h2ko99f3j5', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            new_line = f"{parts[0]}:{parts[1]}#{parts[2]}"
            new_content.append(new_line)

    with open('proxy.txt', 'w') as new_file:
        new_file.write('\n'.join(new_content))


# 每天上午9点执行任务
schedule.every().day.at("09:00").do(reformat_file)

while True:
    schedule.run_pending()
    time.sleep(1)
