import functools


# 输入合理性检查


def validation_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ...  # 检查输入是否合法


@validation_check
def neural_network_training(param1, param2):
    print("neural_network_training")
