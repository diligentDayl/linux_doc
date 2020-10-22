"""
执行测试用例
1.
2.
3.
4.
"""

def _execute_case(case):
    """
    执行测试用例
    :return: dict: {
        "case_id": case["case_id"],
        "result": "pass",
    }
    """
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
