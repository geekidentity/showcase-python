import functools

# 身份认证


def check_user_logged_in(request):
    return True


def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):  # 如果用户处于登录状态
            return func(*args, **kwargs)  # 执行函数 post_comment()
        else:
            raise Exception("Authenticate failed")

    return wrapper


@authenticate
def post_comment(request):
    print("post_comment")


if __name__ == '__main__':
    post_comment("hello")
