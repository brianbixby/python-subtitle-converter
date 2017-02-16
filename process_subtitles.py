"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.

filename = "pirates_of_silicon_valley.srt"
"""

import textwrap
textwrap.indent
def indent(text, amount, ch=' '):
    return textwrap.indent(text, amount * ch)

# filename = "small_subtitles.srt"
filename = "pirates_of_silicon_valley.srt"
my_file = open(filename)
out = open('output.js', 'w')
out.write('var SUBTITLES = [' + "\n")
subtitles = []
subtitle = {}
has_printed_comma = False
for line in my_file:
  line = line.strip()
  if '-->' in line:
      line = 'duration: ' + '"' + line + '",'
      line1 = '"' + next(my_file).strip().replace("\"", "\\\"") + '",'
      line2 = '"' + next(my_file).strip().replace("\"", "\\\"") + '",'
      if line2 == '"",':
          temp = 'line1: "",'
          out.write(indent('{' + "\n", 2))
          out.write(indent(line + "\n", 4))
          out.write(indent(temp + "\n", 4))
          out.write(indent('line2: ' + line1 + "\n", 4))
          out.write(indent('},' + "\n", 2))
      else:
          out.write(indent('{' + "\n", 2))
          out.write(indent(line + "\n", 4))
          out.write(indent('line1: ' + line1 + "\n", 4))
          out.write(indent('line2: ' + line2 + "\n", 4))
          out.write(indent('},' + "\n", 2))
out.write('];' + "\n")
out.close()
