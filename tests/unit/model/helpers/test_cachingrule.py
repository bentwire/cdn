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


import ddt

from cdn.model.helpers import cachingrule
from tests.unit import base


@ddt.ddt
class TestCachingRule(base.TestCase):

    def test_caching_rule(self):

        name = "rule_name"
        ttl = 0

        caching_rule = cachingrule.CachingRule(name, ttl)

        # test all properties
        # name
        self.assertEqual(caching_rule.name, name)
        self.assertRaises(AttributeError, setattr, caching_rule, 'name', name)

        # ttl
        self.assertEqual(caching_rule.ttl, ttl)
        self.assertRaises(AttributeError, setattr, caching_rule, 'ttl', ttl)

        # rules
        self.assertRaises(AttributeError, getattr, caching_rule, 'rules')
