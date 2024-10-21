# txed

TxEd is a text editor written in Python that doesn't require any external pip packages.

## Overview

Born as a small university project, TxEd has grown into a functional and practical program. 

While not exhaustive in features, it serves its purpose effectively, making it ideal for devices 
that, for various reasons, are not compatible with 'pip' or some external libraries.

TxEd can be also included inside other softwares.

## Key Features

- Implemented entirely in standard Python
- No external dependencies required
- Compatible with UNIX-like operating systems and Windows
- Simple and intuitive interface

## System Requirements

- Python (version 3.x recommended)

## How to Use TxEd

Using TxEd is simple and straightforward. Here's how to launch it:

### On UNIX-like systems (Linux, macOS)

```
python3 txed.py <file_path>
```

### On Windows

```
py txed.py <file_path>
```

Replace `<file_path>` with the path to the file you want to edit or create.

## Useful tips

In some projects, there may be files that are part of the repository but 
should not be modified or committed every time they are changed locally. For 
example, configuration or data files that are user-specific might need to be 
excluded from Git's list of modified files. One such file could be 
`data/sys_var.data`.

To avoid Git tracking modifications to `data/sys_var.data`, you can type:

```git update-index --assume-unchanged data/sys_var.data```

If you want to restore this option use:

```git update-index --no-assume-unchanged data/sys_var.data```

## Contributing

TxEd is an open-source project and welcomes contributions from the community. 

If you're interested in improving TxEd, feel free to propose changes or report 
issues through the issue management system on our GitHub page.
