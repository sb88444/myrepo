import lib.common.global_config as global_config
import logging
from e2e_lib.common.delayed_assert import expect_and_log

pylogger = global_config.pylogger


class TestSample():
    """
    """


    def test_sample(cls, caplog):
        caplog.set_level(logging.CRITICAL)
        expect_and_log("ABC" == "X", "request.node.name",
                       "ABC == XYZ",
                       "ABC",
                       "ABC")
