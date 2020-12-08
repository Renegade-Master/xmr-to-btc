import pytest
import xmr2btc


class TestXmr2Btc:
    def test_init_with_one_argument(self):
        args_list: list = []

        arg1: str = "order_parameter_query"

        args_list.append(arg1)

        assert xmr2btc.init(args_list) is True

    def test_init_with_two_arguments(self):
        args_list: list = []

        arg1: str = "order_parameter_query"
        arg2: str = "{'btc_dest_address': 'xxx', 'amount': 0.0, 'amount_currency': 'BTC'}"

        args_list.append(arg1)
        args_list.append(arg2)

        assert xmr2btc.init(args_list) is True

    def test_init_with_empty_arguments(self):
        args_list: list = []

        with pytest.raises(ValueError):
            assert xmr2btc.init(args_list) is False

    def test_init_with_no_arguments(self):
        with pytest.raises(TypeError):
            assert xmr2btc.init() is False

    def test_shutdown(self):
        assert xmr2btc.shutdown() is None
