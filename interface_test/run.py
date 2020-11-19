# coding=utf-8
"""
1. 功能的实现，和调用没有关系
2. 功能的调用，和业务相关
3. 列举需实现的功能
4. 列出大概的执行流程

5. 从小到大，从简到繁，逐步实现，确定功能的输入输出的数据格式


1. 梳理出执行的主流程， 比如： 主流程分为 5个步骤 执行
2. 对 每一个执行步骤 进行抽象封装 比如封装为函数，
3. 定义 每个执行步骤的 输入输出 数据结构
4. 继续完善 每一个执行步骤 的 细节

"""
from read_case import read_case
from execute_case import execute_case


def get_config():
    """
    获取配置
    :return: dict: {
        "case_file_path":"",
    }
    """

    column_rel = {
        "序号": "case_id",
        "接口模块": "module_name",
        "用例标题": "case_title",
        "请求头": "headers",
        "请求方式": "method",
        "接口地址": "url",
        "参数输入": "parameter",
        "期望返回结果": "expect",
        "备注": "remark"
    }

    return {
        "case_file_path": "./case_dir/case_001.xlsx",
        "column_rel": column_rel
    }


def report(result_list):
    """
    输出测试报告
    :return: dict: {}
    """
    for ret in result_list:
        print("case_id: %s result: %s" % (ret["case_id"], ret["result"]))
    return {}


def run():
    """
    执行入口
    1. 初始化配置，(用例文件路径，测试报告文件路径，数据库密码连接 ....)
    2. 获取测试用例数据
    3. 执行测试用例
    4. 输出测试报告
    :return:
    """
    config = get_config()
    print("初始化配置: %s" % config)

    case_list = read_case(config["case_file_path"], config["column_rel"])
    print("获取测试用例数据: %s" % case_list)

    result_list = execute_case(case_list)
    print("测试用例执行完成")

    ret = report(result_list)
    print("输出测试报告完成")
    return {}


if __name__ == "__main__":
    run()
