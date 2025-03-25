# jc_sdhash - SDHash Python Wrapper

This Python package provides a simple, functional wrapper for the **SDHash** binary, allowing you to generate and compare SDBF hashes directly from Python. **Note: This package only works on Linux.**

## Installation

You can install `jc_sdhash` either from PyPI or from the source.

### Option 1: Install from PyPI
```bash
pip install jc_sdhash
```

Usage
The package provides a functional API, similar to ssdeep. Import it as jc_sdhash and use its functions directly.

Importing the Package
```python
import jc_sdhash as sd
```
Usage Options
Option 1: Generate an SDBF Hash and Print to Console
Generate a hash for a file and print it to standard output:

```python
import jc_sdhash as sd
# Generate the SDBF hash for a file
result = sd.generate("inputfile.txt")
print(result)
```

Option 2: Generate an SDBF Hash and Save to File
Generate a hash and save it to a specified output file:

```python
import jc_sdhash as sd
# Generate the SDBF hash and save it to "output.sdbf"
sd.generate("inputfile.txt", output_filepath="output.sdbf")

```

Option 3: Compare Two SDBF Hash Files
Compare two SDBF files and print the similarity score:

```python
import jc_sdhash as sd

# Compare two SDBF files
result = sd.compare("file1.sdbf", "file2.sdbf")
print(result)
```

Option 4: Validate an SDBF File
Validate the integrity of an SDBF file:
```python
import jc_sdhash as sd

# Validate an SDBF file
result = sd.validate("file1.sdbf")
print(result)
```
 Function Details

### `generate(filepath, output_filepath=None)`
Generates an SDBF hash for the given file.  
If `output_filepath` is provided, the hash is saved there; otherwise, it’s returned as a string.

### `compare(file1, file2)`
Compares two SDBF files and returns the similarity score as a string.

### `validate(sdbf_file)`
Validates an SDBF file and returns the result as a string.

---

# Requirements

- **Python 3.6+**
- **Linux-based OS** (this package only works on Linux)
- **The `sdhash` binary** (included in the package)
- **Read access to input files and write access for output files** (if saving hashes)

---

# Troubleshooting

### Missing Binary  
If you get a `FileNotFoundError`, ensure the `sdhash` binary is in the `jc_sdhash/` directory and executable:  
```sh
chmod +x jc_sdhash/sdhash
```

# Future 
## Supported Architectures
This project works with x64 architectures. Our goal is to extend support for x86, enable compatibility with Windows, and other platforms.

# Contributions
We are actively seeking contributions to achieve these goals. If you're interested in helping us add x86 support, Windows compatibility, or other improvements, feel free to open a Pull Request (PR).
