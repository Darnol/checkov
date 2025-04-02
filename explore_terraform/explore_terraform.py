import os
from pathlib import Path

os.environ["LOG_LEVEL"] = "INFO"
# os.environ["CHECKOV_NO_OUTPUT"] = "1"  # Disable checks output alltogether
# Alternative is to specify a --skip-checks * flag that disables all checks

# from checkov.main import Checkov
from checkov.terraform.graph_builder.local_graph import TerraformLocalGraph
from checkov.terraform.graph_manager import TerraformGraphManager

# available examples
examples = [
    "example0",
    "example1",
    "gcpkubernetes__quickstart__terraform",
    "terraform-aws-secure-baseline__modules__vpc-baseline",
    "okd__guides__upi__vsphere_terraform",
]


# SINGLE EXAMPLE CHECKOV MAIN
# example = examples[4]
# print(example)

# # Get abspath for source_dir
# source_dir = os.path.abspath(f"./explore_terraform/terraform_examples/{example}")

# ###
# # Checkov
# res = Checkov(
#     argv=[
#         "-d",
#         f"./explore_terraform/terraform_examples/{example}",
#         "--framework",
#         "terraform",
#         "--skip-check",
#         "*",
#     ]
# ).run()


# # SINGLE EXAMPLE TerraformGraphManager
# example = examples[4]
# print(example)

# # Get abspath for source_dir
# source_dir = os.path.abspath(f"./explore_terraform/terraform_examples/{example}")

# ###
# # TerraformGraphManager - Alternative to using the Checkov main class
# graph_manager = TerraformGraphManager(
#     db_connector=None,
# )

# # Get abspath for source_dir
# source_dir = os.path.abspath(f"./explore_terraform/terraform_examples/{example}")

# local_graph, _ = graph_manager.build_graph_from_source_directory(
#     # source_dir="./explore_terraform/terraform_examples/example0",
#     # source_dir="./explore_terraform/terraform_examples/okd__guides__upi__vsphere_terraform",
#     source_dir=source_dir,
#     local_graph_class=TerraformLocalGraph,
#     download_external_modules=False,
#     parsing_errors={},
#     excluded_paths=[],
#     external_modules_download_path=".external_modules",
#     vars_files=None,
# )
# local_graph.print_graph()


# ALL EXAMPLES TO DOT
for example in examples:
    # Get abspath for source_dir
    source_dir = os.path.abspath(f"./explore_terraform/terraform_examples/{example}")

    ###
    # TerraformGraphManager - Alternative to using the Checkov main class
    graph_manager = TerraformGraphManager(
        db_connector=None,
    )

    local_graph, _ = graph_manager.build_graph_from_source_directory(
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

    local_graph.to_dot(
        path=Path(source_dir) / "resource_graph.dot",
    )
