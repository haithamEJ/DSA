import pyfiglet
from termcolor import colored

# Create one-line ASCII text
ascii_text = pyfiglet.figlet_format("Welcome Haitham !", font="smslant")

# Add color
colored_ascii = colored(ascii_text, "cyan")

# Print the final message
print(colored_ascii)
