#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
from cdumay_result import Result


class BaseHttpResult(Result):
    def __init__(self, retcode=200, retval=None, uuid=None):
        Result.__init__(self, retcode=retcode, retval=retval, uuid=uuid)

    def is_error(self):
        return self.retcode >= 300
