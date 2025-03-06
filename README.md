# Fortune Cookie Simulator 🥠

A simple command-line fortune cookie simulator that generates random fortunes and wisdom with fancy terminal effects.

## Features

- Generates random fortune cookie messages
- Colorful terminal output with fancy text
- Loading animations
- Easy to customize with your own fortunes
- Beautiful ASCII art

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/fortune-cookie-simulator.git
   cd fortune-cookie-simulator
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Make the script executable:
   ```
   chmod +x fortune.py
   ```

## Usage

Run the fortune cookie simulator:

```
python fortune.py
```

For a new fortune, simply run the command again.

### Options

- `-n` or `--no-color`: Disable colored output
- `-c` or `--count [number]`: Generate multiple fortunes (default: 1)
- `-h` or `--help`: Show help message

Example:
```
python fortune.py -c 3
```

## Customizing Fortunes

To add your own fortunes, edit the `fortunes.txt` file. Each fortune should be on a new line.

## License

MIT