# Copyright 2015 Metaswitch Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from test_base import TestBase
from tests.st.utils.docker_host import DockerHost

"""
Test calicoctl status

Most of the status output is checked by the BGP tests, so this module just
contains a simple return code check.
"""


class TestStatus(TestBase):
    def test_status(self):
        """
        Test that the diags command successfully creates a tar.gz file.
        """
        with DockerHost('host', dind=False, start_calico=False) as host:
            host.calicoctl("status")
