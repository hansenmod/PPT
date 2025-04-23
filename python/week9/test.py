obj = (lambda: type('', (), {'say_hi': lambda self: print('Hi')})())()  # 注意最后的 () 表示实例化
obj.say_hi()  # ✅ 输出：Hi



