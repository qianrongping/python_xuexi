def config_name(name):
    def inner(msg):
        print(name + ":" + msg)

    return inner


# 创建tom闭包
tom = config_name('tom')
# 创建jerry闭包
jerry = config_name('jerry')

# 执行闭包
tom('hello')
jerry('world')
