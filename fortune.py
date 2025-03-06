#!/usr/bin/env python3
"""
Fortune Cookie Simulator
A simple terminal-based fortune cookie generator
"""

import random
import os
import sys
import argparse
from datetime import datetime

# ANSI color codes
COLORS = {
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'green': '\033[92m',
    'red': '\033[91m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'bold': '\033[1m',
    'end': '\033[0m'
}

def load_fortunes(filename="fortunes.txt"):
    """Load fortunes from a file."""
    try:
        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))
        fortune_path = os.path.join(script_dir, filename)
        
        with open(fortune_path, 'r', encoding='utf-8') as file:
            fortunes = [line.strip() for line in file.readlines() if line.strip()]
        return fortunes
    except FileNotFoundError:
        # Return default fortunes if file not found
        return [
            "A journey of a thousand miles begins with a single step.",
            "Your hard work will pay off today.",
            "The greatest risk is not taking one.",
            "You will find happiness in unexpected places.",
            "Your creativity will solve a difficult problem.",
            "A smile is your personal welcome mat.",
            "Your talents will be recognized and rewarded.",
            "Good things come to those who wait... but better things come to those who go out and get them.",
            "You will soon embark on a new adventure.",
            "Patience is the key to paradise.",
            "Fortune favors the brave.",
            "The best way to predict the future is to create it.",
            "A problem shared is a problem halved.",
            "You will meet someone special in an unexpected place.",
            "A dream you have will come true when you least expect it."
        ]

def get_random_fortune(fortunes):
    """Return a random fortune from the list."""
    return random.choice(fortunes)

def print_fortune_cookie(fortune, use_color=True):
    """Print a fortune cookie with ASCII art."""
    
    cookie_top = r"""
    .--.
   /    \
  /      \
 |        |
"""
    
    fortune_text = fortune
    cookie_bottom = r"""
 |        |
  \      /
   \____/
"""
    
    if use_color:
        cookie_color = random.choice(['yellow', 'cyan', 'green', 'purple'])
        print(f"{COLORS[cookie_color]}{cookie_top}{COLORS['end']}")
        print(f"{COLORS['bold']}{fortune_text}{COLORS['end']}")
        print(f"{COLORS[cookie_color]}{cookie_bottom}{COLORS['end']}")
    else:
        print(cookie_top)
        print(fortune_text)
        print(cookie_bottom)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Generate fortune cookie messages.')
    parser.add_argument('-n', '--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of fortunes to generate')
    return parser.parse_args()

def main():
    """Main function."""
    args = parse_arguments()
    fortunes = load_fortunes()
    
    # Check if there are any fortunes
    if not fortunes:
        print("Error: No fortunes found!")
        sys.exit(1)
    
    # Print the requested number of fortunes
    for _ in range(args.count):
        fortune = get_random_fortune(fortunes)
        print_fortune_cookie(fortune, not args.no_color)
        if args.count > 1 and _ < args.count - 1:
            print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    # Seed the random number generator
    random.seed(datetime.now().timestamp())
    main()