#functions imported to main.py
import cmpt120imageWeek9
import pygame
import numpy
#open color coding
image = open("colorcoding.csv")

#open the csv files
board_one = open("board1.csv")
board_two = open("board2.csv")
board_three = open("board3.csv")

#Description of the game
def welcome() :
  print ("Dear player! Welcome to the \"Even Colorful\" game \n================================================ \n\nWith this system you will be able to play as many games as you want! \nThe objective of this game is that all columns and rows in the board\nadd to an even number.\nFor each game:\n- you will be able to choose to play 'solo' or against the computer ('AI'),\n- you will be able to choose an initial board,\n- at the end of each game you will win (or lose) points, and\n- you will see a colorful representation of the game final board results.\nEnjoy!\n")



#function to change first row of list into nice col display (used in board_# functions)
def header_to_col(list) :
  result = []
  i = 0
  for x in range(int(list[0])):
    result.append("Col " + str(i))
    i+=1
  print("         "+'     '.join(result))

#create lists from csv file
def create_initial_board(board) :
  row = []
  for line in board:
    square = line.strip().split(",")
    row.append(square) 
  return row

#prints a board with a title
def pretty_print_matrix(title, matrix) :
  board_title = title
  
  print("(" +board_title + ")" )
  
  if int(matrix[0][0]) == 3 :
   print("")
   header_to_col(matrix[0])
   print("")
   print( "Row 0      " + '         '.join(matrix[1])  )
   print("")
   print( "Row 1      " + '         '.join(matrix[2])  )
   print("")
   print( "Row 2      " + '         '.join(matrix[3])  )
   print("")

  if int(matrix[0][0]) == 4 :
   print("")
   header_to_col(matrix[0]) 
   print("")
   print("Row 0      " + '         '.join(matrix[1]) )
   print("")
   print( "Row 1      " + '         '.join(matrix[2]) )
   print("")
   print( "Row 2      " + '         '.join(matrix[3]) )
   print("")
   print( "Row 3      " + '         '.join(matrix[4]) )
   print("")
 
#remove the first row in board array(used in calc_sumcols function)
def removeheader(board):
  del [board[0]]
  return board

#return the total sum of columns in a list
def calc_sumcols(board):

  board_length = len(board[0])
  column = [0] * board_length 
  for i in range(board_length): 
    for j in board:
      column[i] += int(j[i])
  return column


#return the total sum of rows in a list
def calc_sumrows(board):  
  list = []
  for row in board:
    sum = 0
    for item in row:
     sum += int(item)
    list.append(sum)  
  return list
  
  
#finds the max element in a list
def max(list):
 temp = 0
 for i in list:
   if i > temp:
     temp = i
 return temp

#returns true if all items in list are even or false if not
def is_even(list):
  is_even = 0
  for i in list:
    if int(i) % 2 == 0:
      is_even +=1
  if is_even == len(list) :
   return True
  else:
    return False


#receives an image as 2D list of list of RGB pixel list and returns the transpose image
def create_transposeimg(img) :
  to_int(img)
  image = cmpt120imageWeek9.showImage(img,"colours")
  return image

#traverses through colorcoding.csv and finds corresponding color values in finalrow/col lists
def get_colors(colorcsv,row,col) :
  color_list = []
  #go thorugh each line in csv and split into lists
  
  for line in colorcsv:
    each_line = line.strip().split(",") 
    #when there are multiple occurences of a number in row and col need to append that many times
    if int(each_line[0]) in row and int(each_line[0]) in col:
      for i in range((row+col).count(int(each_line[0]))) :
        color_list.append(each_line[1:4])
    
    elif int(each_line[0]) in row or int(each_line[0]) in col:
     color_list.append(each_line[1:4])
  
  return color_list



#check line 176
def get_colors2(colorcsv,row,col) :
  color_list1 = []
  #go thorugh each line in csv and split into lists
  

  for col_item in col:
   for line in colorcsv:
     each_line = line.strip().split(",")
     if col_item == int(each_line[0]):
       color_list1.append(each_line[1:4])
  
  for row_item in row:  
    for line in colorcsv:
     each_line = line.strip().split(",")
     if row_item == int(each_line[0]):
        color_list1.append(each_line[1:4])
  return color_list1


#turns a 2dlist of strings into 2dlist of ints
def to_int(list):
  temp = []
  for row in list:
    for i in row:
      i = int(i)
      temp.append(i)
  return temp


def image_black(black_img,board_colors,board_size):
  j = -1
  for line in black_img:
    i = 0
    j +=1
    for x in range((len(line))*1) :
      r= int(board_colors[0][0])
      g= int(board_colors[0][1])
      b= int(board_colors[0][2])
      black_img[j][i]=[r,g,b]
      i +=1
    for x in range((len(line)//3)*2) :
      r= int(board_colors[1][0])
      g= int(board_colors[1][1])
      b= int(board_colors[1][2])
      black_img[j][i]=[r,g,b]
      i +=1
    for x in range((len(line)//3)*3):
      r= int(board_colors[2][0])
      g= int(board_colors[2][1])
      b= int(board_colors[2][2])
      black_img[j][i]=[r,g,b]
      i +=1
  
  return black_img

