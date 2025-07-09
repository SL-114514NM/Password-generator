import os
import random

# 定义字符集
letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
specials = '!@#$%^&*()'
charset = letters + digits + specials

# 设置密码长度范围和生成数量
MIN_LENGTH = 8
MAX_LENGTH = 13  # 每个密码长度随机选取
PASSWORD_COUNT = 1000000  # 设置你需要的数量

# 输出文件路径
output_file = os.path.join(os.getcwd(), 'NBPassword.txt')

# 随机密码生成函数
def generate_password():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    return ''.join(random.choices(charset, k=length))

# 写入文件
with open(output_file, 'w', encoding='utf-8') as f:
    for i in range(PASSWORD_COUNT):
        password = generate_password()
        f.write(password + '\n')
        if (i + 1) % 1000 == 0:
            print(f"已生成 {i + 1} 条密码...")
            f.flush()

print(f"完成！共生成 {PASSWORD_COUNT} 条密码，保存在：{output_file}")
