import os
import subprocess

class SDHash:
    def __init__(self):
        # Locate the sdhash binary inside the installed package
        self.sdhash_path = os.path.join(os.path.dirname(__file__), "sdhash")
        if not os.path.exists(self.sdhash_path):
            raise FileNotFoundError(f"SDhash binary missing at {self.sdhash_path}")

    def run(self, args):
        """Run sdhash with the given arguments."""
        cmd = [self.sdhash_path] + args
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout

    def generate(self, filepath, output_filepath=None):
        """Generate an SDBF hash for a file, optionally saving it to an output file."""
        args = ["-r", filepath]
        if output_filepath:
            args += ["-o", output_filepath]
        return self.run(args)

    def compare(self, file1, file2):
        """Compare two SDBF hash files."""
        return self.run(["-c", file1, file2])

    def validate(self, sdbf_file):
        """Validate an SDBF file."""
        return self.run(["--validate", sdbf_file])
