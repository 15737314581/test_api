# coding = utf-8
# NAME: test_api
import pytest as pytest
import requests


class TestMain:
    def test_api(self):
        url = "http://127.0.0.1:5001/api/test"

        print("请求地址：", url)
        response = requests.request(method="get", url=url)

        print("响应内容：", response.text)
        assert response.text.startswith("success"), "响应内容不是以success开头"


if __name__ == '__main__':
    pytest.main(["--html=report/report.html", "--self-contained-html"])
