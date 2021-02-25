# World Book Day - tinyReader
 eBook reader for small OLED displays with RP2040

This is a simple microPython script which reads a plain text file (book.txt) and displays it on a small OLED I2C display. Works on Raspberry Pi Pico and other RP2040-based boards. It is being used for a small coin cell powered badge to be worn for World Book Day (4th March 2021). For testing purposes, the book used was Alice's Adventures in Wonderland by Lewis Carroll (sourced from Project Gutenberg)

Currently each page advances every 5 seconds. In a future version, this will be the default 'demo' mode.

## Future control method - one button marked '>'
When in demo mode, pressing the button exits demo mode and goes to the next page.
When not in demo mode, holding down the button for 3 seconds enters demo mode.
