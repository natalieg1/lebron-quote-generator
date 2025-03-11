# LeBron Quote Generator 🏀

A simple command-line LeBron James quote simulator that generates quotes and wisdom with fun terminal imagery.

## Features

- Generates random LeBron quotes
- Colorful terminal output with fancy text
- Easy to customize with your own quotess
- Beautiful ASCII art

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/natalieg1/lebron-quote-generator.git
   cd lebron-quote-generator
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Make the script executable:
   ```
   chmod +x quotes.py
   ```

## Usage

Run the LeBron quotes generator:

```
python quotes.py
```

For a new quote, simply run the command again.

### Options

- `-n` or `--no-color`: Disable colored output
- `-c` or `--count [number]`: Generate multiple quotess (default: 1)
- `-h` or `--help`: Show help message

Example:
```
python quotes.py -c 3
```

## Customizing quotess

To add your own quotess, edit the `quotes.txt` file. Each quote should be on a new line.
