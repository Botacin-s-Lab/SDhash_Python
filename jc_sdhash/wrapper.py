# wrapper.py
import os
import subprocess

# Define the sdhash binary path once (assuming it's bundled with the package)
SDHASH_PATH = os.path.join(os.path.dirname(__file__), "sdhash")
if not os.path.exists(SDHASH_PATH):
    raise FileNotFoundError(f"SDhash binary missing at {SDHASH_PATH}")

def run(args):
    """Run sdhash with the given arguments."""
    cmd = [SDHASH_PATH] + args
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout

def generate(filepath, output_filepath=None):
    """Generate an SDBF hash for a file, optionally saving it to an output file."""
    args = ["-r", filepath]
    if output_filepath:
        args += ["-o", output_filepath]
    return run(args)

def compare(file1, file2):
    """Compare two SDBF hash files."""
    return run(["-c", file1, file2])

def validate(sdbf_file):
    """Validate an SDBF file."""
    return run(["--validate", sdbf_file])