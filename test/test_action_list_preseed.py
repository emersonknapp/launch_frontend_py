# Copyright 2025 Polymath Robotics, Inc.
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

import launch_frontend_py


def test_action_list_preseed():
    # We can construct entities on the fly, but we want to make sure the list is
    # already filled where possible without explicit access
    # picking a representative subset of actions (that are present in Humble+)
    for x in ['arg', 'timer', 'executable', 'let', 'group', 'include', 'set_env']:
        assert x in launch_frontend_py.actions.__all__
