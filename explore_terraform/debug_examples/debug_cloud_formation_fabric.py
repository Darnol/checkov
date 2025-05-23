import logging
import pprint

logging.basicConfig(level=logging.INFO)

from pathlib import Path
from checkov.terraform.graph_builder.local_graph import TerraformLocalGraph
from checkov.terraform.graph_manager import TerraformGraphManager

# os.environ["LOG_LEVEL"] = "DEBUG"

repo_id = "cloud_foundation_fabric"
repo_id = "136401408"
path_to_sourcdir = Path(f"./explore_terraform/debug_examples/{repo_id}").resolve()

if not path_to_sourcdir.is_dir():
    raise FileNotFoundError(f"Directory {path_to_sourcdir} does not exist.")

# graph_manager = TerraformGraphManager(db_connector=None)
# local_graph, _ = graph_manager.build_graph_from_source_directory(
#     source_dir=str(path_to_sourcdir),
#     local_graph_class=TerraformLocalGraph,
#     download_external_modules=False,
#     parsing_errors={},
#     excluded_paths=[],
#     external_modules_download_path=".external_modules",
#     vars_files=None,
#     print_graph=False,
# )

from checkov.terraform.tf_parser import TFParser

tfparser = TFParser()

tfparser_dir = (
    path_to_sourcdir
    # / "blueprints"
    # / "cloud-operations"
    # / "dns-shared-vpc"
    # / "examples"
    # / "shared-vpc-example"
)

parsed_modules = tfparser.parse_hcl_module(
    source_dir=str(tfparser_dir),
    source="",
    download_external_modules=False,
    external_modules_download_path=".external_modules",
    parsing_errors=None,
    excluded_paths=None,
    vars_files=None,
    external_modules_content_cache=None,
)

# tuple of 2 (module, tf_definitions)
len(parsed_modules)

# Module
type(parsed_modules[0])

parsed_modules[0]
parsed_modules[0].to_dict()
len(parsed_modules[0].external_modules_source_map)
pprint.pprint(parsed_modules[0].external_modules_source_map)
pprint.pprint(dict(parsed_modules[0].external_modules_source_map.keys()))
pprint.pprint(list(parsed_modules[0].external_modules_source_map.values()))

# Dict with TFDefinitionKey -> dict[str, Any]
type(parsed_modules[1])
len(parsed_modules[1])
some_tfkey = list(parsed_modules[1].keys())[0]
type(some_tfkey)
pprint.pprint(parsed_modules[1][some_tfkey])
