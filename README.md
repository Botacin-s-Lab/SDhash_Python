# SDhash Python Wrapper


# SDHash Python Wrapper

This Python package is a wrapper for the **SDHash** binary, providing a convenient way to generate and compare SDBF hashes from Python. **Note: This package only works on Linux.**

## Installation

To install the `sdhash_wrapper` package, you can either install it from PyPI (if it’s available there) or from the source.

### Option 1: Install from PyPI
```bash
pip install sdhash_wrapper
```

###  Option 2: Install from Source
Clone the repository and install it manually:

```bash
git clone https://github.com/yourusername/sdhash_wrapper.git
cd sdhash_wrapper
pip install .
```


Make sure you have the necessary dependencies installed, including the sdhash binary, which should be included in the package.

Usage
Importing the Package
```python
from sdhash_wrapper.wrapper import SDHash
```

#### Generate an SDBF Hash
You can generate an SDBF hash for a file using the generate() method. The method accepts two arguments:

filepath: Path to the file you want to hash.
output_filepath (optional): Path where the SDBF hash will be saved.


#### Example 1: Generate Hash and Save to File

```python

# Initialize SDHash
sdhash = SDHash()

# Specify output file for the SDBF hash
output_file = "output.sdbf"

# Generate the SDBF hash and save to the specified output file
sdhash.generate("inputfile.txt", output_filepath=output_file)

```

#### Example 2: Generate Hash Without Specifying Output File
If you don't specify the output file, the result will be printed to the standard output:

```python

# Initialize SDHash
sdhash = SDHash()
# Generate the SDBF hash without specifying an output file
sdhash.generate("inputfile.txt")
```
#### Compare SDBF Hashes
To compare two SDBF files, you can use the compare() method. Here’s how to use it:

```python

# Compare two SDBF files
sdhash.compare("file1.sdbf", "file2.sdbf")

```

### Requirements
Python 3.6+
Linux-based OS (this package only works on Linux)
sdhash binary (included in the package)
Access to the required input files for hashing


### Troubleshooting
If you encounter issues such as missing binaries or permission errors:

Ensure the sdhash binary is located in the correct directory (sdhash_wrapper/sdhash).
Verify that you have the necessary permissions to read/write to the input/output files.
If the command fails with a non-zero exit code, check the standard error output for more details about the failure.
