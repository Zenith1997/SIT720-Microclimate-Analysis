"""Static notebook integrity check; deliberately does not run ML experiments."""
import json
import sys
from pathlib import Path


def verify_notebook(path: Path) -> dict:
    doc = json.loads(path.read_text(encoding="utf-8"))
    if doc.get("nbformat") != 4 or not isinstance(doc.get("cells"), list):
        raise ValueError("Expected a version 4 Jupyter notebook")
    code_cells = [cell for cell in doc["cells"] if cell.get("cell_type") == "code"]
    if not code_cells:
        raise ValueError("No code cells found")
    error_cells = sum(any(x.get("output_type") == "error" for x in cell.get("outputs", [])) for cell in code_cells)
    if error_cells:
        raise ValueError(f"Saved notebook contains {error_cells} execution-error cells")
    return {"code_cells": len(code_cells), "saved_executions": sum(c.get("execution_count") is not None for c in code_cells), "saved_error_cells": error_cells}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python check_notebook.py notebook.ipynb")
    print(verify_notebook(Path(sys.argv[1])))
