import logging


from checkov.main import Checkov
from checkov.terraform.graph_manager import TerraformGraphManager

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

###
# Checkov
res = Checkov(
    argv=[
        "-d",
        "./explore_terraform/terraform_examples/okd__guides__upi__vsphere_terraform",
    ]
).run()

###
# TerraformGraphManager
graph_manager = TerraformGraphManager(
    db_connector=None,
)

_ = graph_manager.build_graph_from_source_directory(
    # source_dir="./explore_terraform/terraform_examples/example0",
    source_dir="./explore_terraform/terraform_examples/okd__guides__upi__vsphere_terraform",
)
