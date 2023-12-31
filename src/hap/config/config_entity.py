from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    raw_data_path : Path
    
@dataclass(frozen=True)
class DVCremote:
    remote_dir: Path