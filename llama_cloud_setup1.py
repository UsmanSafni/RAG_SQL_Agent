from llama_index.indices.managed.llama_cloud import LlamaCloudIndex
import llama_index.core
import os
from dotenv import load_dotenv
load_dotenv()

LLAMA_CLOUD_API_KEY = os.getenv('LLAMA_CLOUD_API_KEY')
PHOENIX_API_KEY =os.getenv('PHOENIX_API_KEY')

index = LlamaCloudIndex(
    name="city_pdfs_index",
    project_name="Default",
    organization_id="8c1b26ae-5c98-4873-bce9-28d0c67a3dce",
    api_key=LLAMA_CLOUD_API_KEY,
)

llama_cloud_query_engine = index.as_query_engine()

# for observability
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"api_key={PHOENIX_API_KEY}"
llama_index.core.set_global_handler(
    "arize_phoenix", endpoint="https://llamatrace.com/v1/traces"
)