# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2021-present VincentRPS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import typing

import attr

__all__: typing.List[str] = [
    "RPDError",
    "RESTError",
    "WebSocketError",
    "Forbidden",
    "NotFound",
    "ServerError",
]


@attr.define(auto_exc=True, repr=False, weakref_slot=False)
class RPDError(Exception):
    """The base exception class for RPD"""


@attr.define(auto_exc=True, repr=False, weakref_slot=False)
class RESTError(RPDError):
    """REST Errors"""


@attr.define(auto_exc=True, repr=False, weakref_slot=False)
class Forbidden(RESTError):
    """Forbidden from a URL"""


@attr.define(auto_exc=True, repr=False, weakref_slot=False)
class NotFound(RESTError):
    """Endpoint Not Found"""


@attr.define(auto_exc=True, repr=False, weakref_slot=False)
class ServerError(RESTError):
    """A Discord Server Error"""


@attr.define(auto_exc=True, repr=False, weakref_slot=False)
class WebSocketError(RPDError):
    """WebSocket Errors"""
