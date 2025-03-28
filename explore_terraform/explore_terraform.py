import logging
import os

os.environ["LOG_LEVEL"] = "INFO"

from checkov.main import Checkov
from checkov.terraform.graph_builder.local_graph import TerraformLocalGraph
from checkov.terraform.graph_manager import TerraformGraphManager

# If needed get the logger from "checkov" and specify handlers and log levels

# Get abspath for source_dir
source_dir = os.path.abspath(
    "./explore_terraform/terraform_examples/okd__guides__upi__vsphere_terraform"
)

###
# Checkov
res = Checkov(
    argv=[
        "-d",
        "./explore_terraform/terraform_examples/okd__guides__upi__vsphere_terraform",
        "--framework",
        "terraform",
    ]
).run()

###
# TerraformGraphManager
graph_manager = TerraformGraphManager(
    db_connector=None,
)

_ = graph_manager.build_graph_from_source_directory(
    # source_dir="./explore_terraform/terraform_examples/example0",
    # source_dir="./explore_terraform/terraform_examples/okd__guides__upi__vsphere_terraform",
    source_dir=source_dir,
    local_graph_class=TerraformLocalGraph,
    download_external_modules=False,
    parsing_errors={},
    excluded_paths=[],
    external_modules_download_path=".external_modules",
    vars_files=None,
)
