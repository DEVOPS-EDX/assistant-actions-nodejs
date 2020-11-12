# Copyright 2020 Google LLC
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
"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import synthtool.languages.node as node
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

# run the gapic generator
gapic = gcp.GAPICBazel()
library = gapic.node_library('actions', 'v2', proto_path='google/actions/sdk/v2')
s.copy(library, excludes=['README.md', 'package.json', 'linkinator.config.json'])

node.postprocess_gapic_library()
