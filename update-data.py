import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / "data.json").read_text(encoding="utf-8"))
assert isinstance(data, list)
(root / "data.js").write_text(
    "window.RAL_PAPERS = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n",
    encoding="utf-8",
)
print(f"Updated {len(data)} papers")
