# Python Class Relationship Visualizer

This script analyzes Python code and generates a visual graph of class relationships, including inheritance and function calls between classes.

## Features

- Parses Python code and extracts class definitions, inheritance, and function call information.
- Generates a clear and readable graph visualization using Graphviz.
- Helps understand the structure and dependencies within Python projects.

## Requirements

- Python 3.6 or higher
- Graphviz ([https://graphviz.org/](https://graphviz.org/)) - Make sure to install it and add it to your system's PATH.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required packages (using pip):
   
   ```bash
   pip install -r requirements.txt
   ```

## Usage

   ```bash
   python class_graph.py /path/to/your/python/project/
   ```
## Notes

- The script assumes that your Python code is syntactically correct. It might skip files with syntax errors.
- You can customize the output filename and format by modifying the `graph.render()` call in the script.
- For complex projects, the graph might become large. Consider using Graphviz's layout options to improve readability.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
  
