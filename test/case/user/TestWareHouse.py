from test.case.basecase import *

class TestWareHouse(BaseCase):
    def test_1_token_1(self):
        case = self.get_to_data("test_1_token_1")
        return self.send_requests(case)