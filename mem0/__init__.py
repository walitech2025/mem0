try:
    import importlib.metadata
    __version__ = importlib.metadata.version("mem0ai")
except Exception:
    __version__ = "0.1.0"

from mem0.client.main import AsyncMemoryClient, MemoryClient  # noqa
from mem0.memory.main import AsyncMemory, Memory  # noqa
