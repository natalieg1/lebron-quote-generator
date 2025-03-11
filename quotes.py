#!/usr/bin/env python3
"""
LeBron Quote Generator
A simple terminal-based LeBron James quote generator
"""

import random
import os
import sys
import argparse
from datetime import datetime
import colorama
from termcolor import colored
from pyfiglet import Figlet
from tqdm import tqdm
import time

# Initialize colorama
colorama.init()

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

def load_quotes(filename="quotes.txt"):
    """Load quotes from a file."""
    try:
        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))
        quote_path = os.path.join(script_dir, filename)
        
        with open(quote_path, 'r', encoding='utf-8') as file:
            quotes = [line.strip() for line in file.readlines() if line.strip()]
        return quotes
    except FileNotFoundError:
        # Return default quotes if file not found
        return [
            "There is a lot of pressure put on me, but I don't put a lot of pressure on myself. I feel if I play my game, it will take care of itself.",
            "You know, God gave me a gift to do other things besides play the game of basketball.",
            "I love showcasing my talents, not only to my hometown fans and my own team but to the world.",
            "But ever since I was a kid, I was always the winner.",
            "You know, my family and friends have never been yes-men: 'Yes, you're doing the right thing, you're always right.' No, they tell me when I'm wrong, and that's why I've been able to stay who I am and stay humble."
        ]


def get_random_quote(quotes):
    """Return a random quote from the list."""
    return random.choice(quotes)

def print_quote(quote, use_color=True):
    """Print a quote with ASCII art."""
    
    # Create a figlet font object
    fig = Figlet(font='small')
    
    # Print header
    header = fig.renderText('LeBron Quote Generator')
    
    cookie_top = r"""
                       ..ee$$$$$ee..                         
                   .e$*""    $    ""*$e.                      
                 z$"*.       $         $$c                        
               z$"   *.      $       .P  ^$c                      
              d"      *      $      z"     "b                     
             $"        b     $     4%       ^$                    
            d%         *     $     P         '$                   
           .$          'F    $    J"          $r                  
           4L           b    $    $           J$                                        
"""
    
    quote_text = quote
    cookie_bottom = r"""
                
           4F          4F    $    4r          4P                  
           ^$          $     $     b          $%                  
            3L        .F     $     'r        JP                   
             *c       $      $      3.      z$                    
              *b     J"      $       3r    dP                     
               ^$c  z%       $        "c z$"                      
                 "*$L        $        .d$"                        
                    "*$ee..  $  ..ze$P"                           
                        ""*******""   
"""
    
    if use_color:
        # Using termcolor instead of ANSI codes
        cookie_color = random.choice(['yellow', 'cyan', 'green', 'magenta'])
        print(colored(header, 'red', attrs=['bold']))
        print(colored(cookie_top, cookie_color))
        print(colored(quote_text, 'white', attrs=['bold']))
        print(colored(cookie_bottom, cookie_color))
    else:
        print(header)
        print(cookie_top)
        print(quote_text)
        print(cookie_bottom)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Generate quote cookie messages.')
    parser.add_argument('-n', '--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of quotes to generate')
    return parser.parse_args()

def main():
    """Main function."""
    args = parse_arguments()
    quotes = load_quotes()
    
    # Check if there are any quotes
    if not quotes:
        print("Error: No quotes found!")
        sys.exit(1)
    
    # Print the requested number of quotes
    for _ in range(args.count):
        quote = get_random_quote(quotes)
        print_quote(quote, not args.no_color)
        if args.count > 1 and _ < args.count - 1:
            print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    # Seed the random number generator
    random.seed(datetime.now().timestamp())
    main()