#
# * This file is subject to the terms and conditions defined in
# * file 'LICENSE.txt', which is part of this source code package.

import os
from pathlib import Path
from ruamel.yaml import safe_load
from tests.test_base import TestBase, test_constants
from xd_cwl_utils.config import config
from xd_cwl_utils.helpers.get_paths import get_workflow_metadata
from xd_cwl_utils.classes.metadata.workflow_metadata import WorkflowMetadata


class TestWorkflowMetadata(TestBase):

    def test_make_workflow_metadata(self):
        test_name = 'Test wf name'
        wf = WorkflowMetadata(name=test_name, softwareVersion=test_constants['test_software_version'])
        self.assertEqual(test_name, wf.name)

    def test_load_from_file(self):
        metafile_path = get_workflow_metadata('example_workflows', 'cat_sort', 'master', 'cat_sort')
        wf_meta = WorkflowMetadata.load_from_file(metafile_path)
        self.assertEqual(wf_meta.name, 'cat sort')

    def test_mk_file(self):
        metafile_path = get_workflow_metadata('example_workflows', 'cat_sort', 'master', 'cat_sort')
        wf_meta = WorkflowMetadata.load_from_file(metafile_path)
        test_filename = Path(config[os.environ.get('CONFIG_KEY')]['temp_dir'].name) / 'wf_test_metadata.yaml'
        wf_meta.mk_file(test_filename)
        with test_filename.open('r') as file:
            test_file_dict = safe_load(file)
        self.assertEqual(test_file_dict['identifier'], 'WF_1f4d8f.cb')
        os.remove(test_filename)