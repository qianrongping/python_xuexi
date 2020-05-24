import logging

# 设置logging日志的配置信息
# level表示设置级别
# %(asctime)s 表示当前时间
# %(filename)s 表示程序文件名
# %(lineno)d 表示行号
# %(levelname)s 表示日志级别
# %(message)s 表示日志信息
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s",
                    filename="log.txt",
                    filemode="a")

logging.debug("我是一个debug级别的日志信息")
logging.info("我是一个info级别的日志信息")
logging.warning("我是一个warning级别的日志信息")
logging.error("我是一个error级别的日志信息")
logging.critical("我是一个critical级别的日志信息")
# 默认是warning级别,只有大于warning级别的日志才会输出显示
