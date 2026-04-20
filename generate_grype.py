import subprocess
from pathlib import Path

files = list(Path("data/results").glob("*.json"))

for f in files:
    output = f.with_name(f.stem + "_grype.json")

    print(f"Escaneando {f.name}")

    with open(output, "w") as out:
        subprocess.run([
            "grype",
            f"sbom:{f}",
            "-o",
            "json"
        ], stdout=out)
