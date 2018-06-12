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

"""data_node.py
DataNode Python wrapper.
"""

from ydk.ext.path import DataNode as _DataNode
from ydk.errors import YInvalidArgumentError
from ydk.errors.error_handler import handle_runtime_error as _handle_error


class DataNode(_DataNode):
    """ Python wrapper for RootSchemaNode
    """

    def __init__(self, data_node):
        if not isinstance(data_node, _DataNode):
            raise YInvalidArgumentError("data_node %s is not an instance of DataNode" % type(data_node))
        self.data_node = data_node

    def __call__(self, session):
        with _handle_error():
            return self.data_node(session)

    def get_schema_node(self):
        with _handle_error():
            return self.data_node.get_schema_node()

    def get_path(self):
        with _handle_error():
            return self.data_node.get_path()

    def create_datanode(self, path, value=None):
        if value is None:
            with _handle_error():
                return self.data_node.create_datanode(path)
        else:
            with _handle_error():
                return self.data_node.create_datanode(path, value)

    def create_action(self, path):
        with _handle_error():
            return self.data_node.create_action(path)

    def has_action_node(self):
        with _handle_error():
            return self.data_node.has_action_node()

    def get_action_node_path(self):
        with _handle_error():
            return self.data_node.get_action_node_path()

    def set_value(self, value):
        with _handle_error():
            return self.data_node.set_value(value)

    def get_value(self):
        with _handle_error():
            return self.data_node.get_value()

    def find(self, path):
        with _handle_error():
            return self.data_node.find(path)

    def get_parent(self):
        with _handle_error():
            return self.data_node.get_parent()

    def get_children(self):
        with _handle_error():
            return self.data_node.get_children()

    def get_root(self):
        with _handle_error():
            return self.data_node.get_root()

    def add_annotation(self, an):
        with _handle_error():
            return self.data_node.add_annotation(an)

    def remove_annotation(self, an):
        with _handle_error():
            return self.data_node.remove_annotation(an)

    def annotations(self):
        with _handle_error():
            return self.data_node.annotations()
