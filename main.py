import os
from time import sleep
import re
import json

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def startup():
  print("Version 3.0.0")
  sleep(0.5)
  print("You are not allowed you reproduce, sell, or license this software to anybody else.")
  sleep(2)
  cls()
def split(text):
  return [char for char in text]

def encrypt(o_key, o_text, func):
  temp_key = o_key
  while len(temp_key) < len(o_text):
    temp_key += o_key 
  key = split(temp_key)
  del temp_key
  text = split(o_text)
  count = 0
  while count < len(key):
    key[count] = ord(str(key[count]))
    count += 1
  count = 0
  while count < len(text):
    text[count] = ord(str(text[count]))
    count += 1
  count = 0
  while count < len(text):
    if func == "e":
      text[count] += key[count]
    if func == "d":
      text[count] -= key[count]
    if text[count] > 122:
      text[count] -= 122
    try:
      text[count] = chr(text[count])
    except:
      text[count] = chr(text[count]+122)
    count += 1
  strtext = ""
  for char in text:
    strtext += str(char)
  return strtext
      
  
def rot(text, func):
  text = text.lower()
  text = split(text)
  count = 0
  for char in text:
    text[count] = int(ord(str(text[count])))-96
    count += 1
  if func == "e":
    count = 0
    for char in text:
      text[count] += 1
      count += 1
  if func == "d":
    count = 0
    for char in text:
      text[count] -= 1
      count += 1
  count = 0
  for char in text:
    text[count] = chr(text[count]+96)
    count += 1
  ctext = ""
  for char in text:
    ctext = ctext + str(char)
  print("This is your encrypted text:\n" + ctext + "\n")
  save(ctext)
  return ctext

def matrix(text, key, func):
  if func == "e":
    while len(text) % key != 0:
      text += " "
    text = split(text)
    matrix = 0
    grid = []
    temp = []
    for letter in text:
      temp.append(letter)
      matrix += 1
      if matrix == key:
        grid.append(temp)
        temp = []
        matrix = 0
    encrypted = ""
    for i in range(key):
      for item in grid:
        encrypted += item[i]
    return encrypted
  elif func == "d":
    text = split(text)
    temp = text
    while len(text) % key != 0:
      temp += " "
    div = int(len(temp)/key)
    matrix = 0
    grid = []
    temp = []
    for letter in text:
      temp.append(letter)
      matrix += 1
      if matrix == div:
        grid.append(temp)
        temp = []
        matrix = 0
    encrypted = ""
    for i in range(div):
      for item in grid:
        encrypted += item[i]
    return encrypted
    
  else:
    print("An error occured")

def save(conversion):
  while True:
    save = input("Would you like to save this in a text file?(y/n)\n")
    if save == "y":
      try:
        loc = input("Please enter the location and name of the file you would like to name it in:\n")
        save = open(loc, "w")
        save.write(conversion)
        save.close()
        break
      except:
        print("Sorry, but it seems that an error occured. Make sure your path is correct and try again.")
        sleep(3)
        cls()
    if save == "n":
      break

def terminal():
  while True:
    func = input("Please select a function:\n1) Encrypt\n2) Decrypt\n")
    cls()
    if func == "1" or func == "2":
      while True:
        cipher = input("Select a cipher:\n1) Vigenete square\n2) ROT1\n3) Matrix\n")
        if cipher == "1":
          cls()
          key = input("Please enter your key: ")
          cls()
          file_o_ent = input("Would you like to enter your text or read from a text file?(t for type/f for file)\n")
          cls()
          text = ""
          if file_o_ent == "t":
            text = input("Please enter your text:\n")
          else:
            while True:
              text = input("Please enter your file location:\n")
              try:
                file = open(text, "r")
                text = file.read()
                file.close()
                break
              except:
                print("Sorry, but it seems like that file does not exist, please try again.")
                sleep(2)
              cls()
          code = None
          if func == "2":
            code = encrypt(key, text, "d")
          elif func == "1":
            code = encrypt(key, text, "e")
          print("This is your encrypted text:\n" + code + "\n")
          save(code)
          cls()
          break
        elif cipher == "2":
          cls()
          file_o_ent = input("would you like to enter you text of read from a text file?(t for type/f for file)\n")
          cls()
          text = ""
          if file_o_ent == "t":
            text = input("Please enter your text:\n")
          else:
            text = input("Please enter your file location:\n")
            file = open(text, "r")
            text = file.read()
            file.close()
          code = None
          if func == "2":
            code = rot(text, "d")
          elif func == "1":
            code = rot(text, "e")
          break
          print("This is your encrypted text:\n"+code)
          save(code)
        elif cipher == "3":
          cls()
          file_o_ent = input("would you like to enter you text of read from a text file?(t for type/f for file)\n")
          cls()
          text = ""
          if file_o_ent == "t":
            text = input("Please enter your text:\n")
          else:
            text = input("Please enter your file location:\n")
            file = open(text, "r")
            text = file.read()
            file.close()
          key = input("Enter your numerical key:")
          key = int(key)
          code = None
          if func == "2":
            code = matrix(text, key, "d")
          elif func == "1":
            code = matrix(text, key, "e")
          print("This is your encrypted text:\n"+code)
          save(code)
          break
        else:
          print("Sorry that is not a valid choice, please try again!")
          sleep(2)
          cls()
      break
    else:
      print("Sorry, that is not a valid choice, please try again!")
      sleep(2)
      cls()
startup()
while True:
  terminal()
  cls()