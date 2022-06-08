# coding = utf-8
import pytest
pytest.main(["-s",
                 "-v",
                 "test_api.py::TestMain::test_api",
                 "--capture=sys",
                 "--html=./report/report.html",
                 "--self-contained-html"])
