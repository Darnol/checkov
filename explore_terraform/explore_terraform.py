import logging
import os


from checkov.main import Checkov
from checkov.terraform.graph_builder.local_graph import TerraformLocalGraph
from checkov.terraform.graph_manager import TerraformGraphManager

# Set up logger
# os.environ["CHECKOV_ALLOW_CODE_LOGGING"] = "True"
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)


logging.basicConfig(level=logging.DEBUG)
# logging.getLogger("checkov").setLevel(logging.DEBUG)


# # Get the Checkov logger and override its config
# checkov_logger = logging.getLogger("checkov")
# checkov_logger.setLevel(logging.DEBUG)

# # Remove existing handlers (if Checkov added any)
# for handler in checkov_logger.handlers[:]:
#     checkov_logger.removeHandler(handler)

# # Add our own handler to see the output
# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
# handler.setFormatter(formatter)
# checkov_logger.addHandler(handler)


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
