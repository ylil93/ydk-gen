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

"""root_schema_node.py
RootSchemaNode Python wrapper.
"""

from ydk.path import Rpc
from ydk.ext.path import RootSchemaNode as _RootSchemaNode
from ydk.errors import YInvalidArgumentError
from ydk.errors.error_handler import handle_runtime_error as _handle_error


class RootSchemaNode(_RootSchemaNode):
    """ Python wrapper for RootSchemaNode
    """

    def __init__(self, root):
        if not isinstance(root, _RootSchemaNode):
            raise YInvalidArgumentError("root %s is not an instance of RootSchemaNode" % type(root))
        self.root = root

    def get_path(self):
        with _handle_error():
            return self.root.get_path()

    def find(self, path):
        with _handle_error():
            return self.root.find(path)

    def get_parent(self):
        with _handle_error():
            return self.root.get_parent()

    def get_children(self):
        with _handle_error():
            return self.root.get_children()

    def get_root(self):
        with _handle_error():
            return self.root.get_root()

    def create_datanode(self, path, value=None):
        if value is None:
            with _handle_error():
                return self.root.create_datanode(path)
        else:
            with _handle_error():
                return self.root.create_datanode(path, value)

    def get_statement(self):
        with _handle_error():
            return self.root.get_statement()

    def get_keys(self):
        with _handle_error():
            return self.root.get_keys()

    def create_rpc(self, path):
        with _handle_error():
            _rpc = self.root.create_rpc(path)
            return Rpc(_rpc)
