from playsound import playsound
import time

# Class declaration for Moore Machine
class State:
    def __init__(self, char='', left=None, right=None):
        self.char= char
        self.left= left
        self.right= right

# Functions for decoding Morse Code
def morse_to_char(morse_fsm, morse_string, i=0):
    if i==len(morse_string):
          return morse_fsm.char
    elif morse_string[i] == '.':
          return morse_to_char(morse_fsm.left, morse_string, i+1)
    else:
          return morse_to_char(morse_fsm.right, morse_string, i+1)

def decode_morse(morse_fsm, str):
     decoded = ''
     morse_string = str.split(' ')
     for decode_string in morse_string:
          if decode_string == '/':
               decoded += ' '
          else:
               decoded += morse_to_char(morse_fsm, decode_string)
     return decoded

# Function for encoding a String to Morse Code
def char_to_morse(morse_fsm, character, tmp):
     if morse_fsm == None:
          return False
     elif morse_fsm.char == character:
          return True
     else:
          if char_to_morse(morse_fsm.right,character, tmp) == True:
               tmp.insert(0, "-")
               return True
          elif char_to_morse(morse_fsm.left,character, tmp) == True:
               tmp.insert(0, ".")
               return True

# Function to play Morse Beep sounds
def morse_beep (morse_code):
     for morse_code in morse_code:
          if morse_code == '.':
               playsound("MorseBeeps\dot.wav")
          elif morse_code == '-':
               playsound("MorseBeeps\dash.wav")
          else:
               time.sleep(0.3)

# Morse FSM
morse_fsm = State('',
                State('E',
                     State('I',
                          State('S',
                               State('H',
                                    State('5'),
                                    State('4')),
                               State('V',
                                    State(''),
                                    State('3'))),
                          State('U',
                               State('F',
                                    State(''),
                                    State('')),
                               State('',
                                    State(''),
                                    State('2')))),
                     State('A',
                          State('R',
                               State('L',
                                    State(''),
                                    State('')),
                               State('',
                                    State('+'),
                                    State(''))),
                          State('W',
                               State('P',
                                    State(''),
                                    State('')),
                               State('J',
                                    State(''),
                                    State('1'))))),
                State('T',
                     State('N',
                          State('D',
                               State('B',
                                    State('6'),
                                    State('=')),
                               State('X',
                                    State('/'),
                                    State(''))),
                          State('K',
                               State('C',
                                    State(''),
                                    State('')),
                               State('Y',
                                    State(''),
                                    State('')))),
                     State('M',
                          State('G',
                               State('Z',
                                    State('7'),
                                    State('')),
                               State('Q',
                                    State(''),
                                    State(''))),
                          State('O',
                               State('',
                                    State('8'),
                                    State('')),
                               State('',
                                    State('9'),
                                    State('0'))))))
