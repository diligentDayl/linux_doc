# coding=utf-8
"""
执行测试用例
1.
2.
3.
4.
"""
import logging
import requests


def check_data(case):
    """
    准备参数, 校验参数
    :return: bool
    """
    return True


def request(case):
    """
    请求接口
    :return: dict
    """
    url = case["url"]
    method = case["method"].upper()
    headers = case["headers"]
    if method == "POST":
        data = case["parameter"]
        parameter = {}
    else:
        data = {}
        parameter = case["parameter"]
    res = requests.request(method, url, params=parameter, data=data, headers=headers)
    logging.error("request 1: %s", res.json())
    return res.json()


def expect_check(response, case):
    """
    验证是否符合预期
    :return: bool
    """
    return True


def _execute_case(case):
    """
    执行测试用例

    流程：
        1. 准备参数, 校验参数
        2. 请求接口, 解析接口的响应信息
        3. 验证是否符合预期
        4. 记录结果  暂不记录
    :return: dict: {
        "case_id": case["case_id"],
        "result": "pass",
    }
    """
    # 准备参数, 校验参数
    is_ok = check_data(case)
    if not is_ok:
        logging.error("_execute_case error 1: %s", case)
        return {
            "case_id": case.get("case_id", "-"),
            "result": "block",
        }

    # 请求接口
    response = request(case)

    # 验证是否符合预期
    is_ok = expect_check(response, case)
    if not is_ok:
        return {
            "case_id": case.get("case_id", "-"),
            "result": "block",
        }
    return {
        "case_id": case["case_id"],
        "result": "pass",
    }


def execute_case(case_list):
    """
    执行测试用例
    :return: dict: {
        "case_id": case["case_id"],
        "result": "pass",
    }
    """
    result_list = []
    total_count = len(case_list)
    for index, case in enumerate(case_list):
        result = _execute_case(case)
        result_list.append(result)
        print("当前进度：%.2f%%"% ((index+1)/total_count*100))
    return result_list


if __name__ == "__main__":
    pass
