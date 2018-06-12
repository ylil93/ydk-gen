#  ----------------------------------------------------------------
# Copyright 2017 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

"""rpc.py
Rpc Python wrapper.
"""

from ydk.path import DataNode
from ydk.ext.path import Rpc as _Rpc
from ydk.errors import YInvalidArgumentError
from ydk.errors.error_handler import handle_runtime_error as _handle_error


class Rpc(_Rpc):
    """ Python wrapper for RootSchemaNode
    """

    def __init__(self, rpc):
        if not isinstance(rpc, _Rpc):
            raise YInvalidArgumentError("rpc %s is not an instance of Rpc" % type(rpc))
        self.rpc = rpc

    def __call__(self, session):
        with _handle_error():
            return self.rpc(session)

    def get_input_node(self):
        with _handle_error():
            _data_node = self.rpc.get_input_node()
            return DataNode(_data_node)

    def has_output_node(self):
        with _handle_error():
            return self.rpc.has_output_node()

    def get_schema_node(self):
        with _handle_error():
            return self.rpc.get_schema_node()
