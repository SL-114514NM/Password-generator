import itertools
import os

letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
specials = '!@#$%^&*()'
charset = letters + digits + specials

MIN_LENGTH = 5
MAX_LENGTH = 8 # 不要设置太大

output_file = os.path.join(os.getcwd(), 'Password.txt')
count = 0
flush_every = 1000 # 每写入 N 行就 flush 一次

with open(output_file, 'w', encoding='utf-8') as f:
    for length in range(MIN_LENGTH, MAX_LENGTH + 1):
        print(f"生成长度为 {length} 的组合...")
        for combo in itertools.product(charset, repeat=length):
            f.write(''.join(combo) + '\n')
            count += 1
            if count % flush_every == 0:
                print(f"已生成 {count} 条...")
                f.flush()

print(f"完成！总共生成 {count} 条密码，保存在：{output_file}")
