import logging

from checkov.terraform.graph_manager import TerraformGraphManager

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

graph_manager = TerraformGraphManager(
    db_connector=None,
)

graph_manager.build_graph_from_source_directory(
    # source_dir="explore_terraform/terraform_examples/example0",
    source_dir="./explore_terraform",
)
