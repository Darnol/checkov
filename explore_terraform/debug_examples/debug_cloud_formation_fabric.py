import logging

logging.basicConfig(level=logging.INFO)

import os
from pathlib import Path
from checkov.terraform.graph_builder.local_graph import TerraformLocalGraph
from checkov.terraform.graph_manager import TerraformGraphManager

# os.environ["LOG_LEVEL"] = "DEBUG"

repo_id = "cloud_foundation_fabric"
path_to_sourcdir = Path(f"./explore_terraform/debug_examples/{repo_id}").resolve()

if not path_to_sourcdir.is_dir():
    raise FileNotFoundError(f"Directory {path_to_sourcdir} does not exist.")

graph_manager = TerraformGraphManager(db_connector=None)
local_graph, _ = graph_manager.build_graph_from_source_directory(
    source_dir=str(path_to_sourcdir),
    local_graph_class=TerraformLocalGraph,
    download_external_modules=False,
    parsing_errors={},
    excluded_paths=[],
    external_modules_download_path=".external_modules",
    vars_files=None,
    print_graph=False,
)

# from checkov.terraform.tf_parser import TFParser
# tfparser = TFParser()
# tfparser.parse_hcl_module(
#     source_dir=str(path_to_sourcdir),
#     source=self.source,
#     download_external_modules=download_external_modules,
#     external_modules_download_path=kwargs.get(
#         "external_modules_download_path", DEFAULT_EXTERNAL_MODULES_DIR
#     ),
#     parsing_errors=parsing_errors,
#     excluded_paths=excluded_paths,
#     vars_files=kwargs.get("vars_files", None),
#     external_modules_content_cache=kwargs.get(
#         "external_modules_content_cache", None
#     ),
# )
