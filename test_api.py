# coding = utf-8
# NAME: test_api
import pytest as pytest
import requests


class TestMain:
    def test_api(self):
        # 公司
        # url = "http://172.23.7.136:5000/api/test"
        # 家
        url = "http://192.168.3.36:5000/api/test"

        print("请求地址：", url)
        response = requests.request(method="get", url=url)

        print("响应内容：", response.text)
        assert response.text.startswith("success"), "响应内容不是以success开头"


if __name__ == '__main__':
    pytest.main(["--html=/Users/jijianfeng/Downloads/jenkins/jenkins_hone/workspace/test456/report/report.html", "--self-contained-html"])
