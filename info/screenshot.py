#!/usr/bin/python
import pyscreenshot

def capture(file_name):
  pyscreenshot.grab_to_file(file_name+".png")
  feedback = "Screenshot saved as "+file_name+".png"
  return feedback
