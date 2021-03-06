# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Some useful getters for thread local request style validation
"""


def pecan_getter(parm):
    """pecan getter"""
    pecan_module = __import__('pecan', globals(), locals(), ['request'])
    return getattr(pecan_module, 'request')


# def flask_getter(parm):
#     pecan_module = __import__('flask', globals(), locals(), ['request'])
#     return getattr(pecan_module, 'request')
