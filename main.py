# Even colourful game
# Authors: Arya Singh, and Henry Chen
# Date: November, 18, 2020

#for AI
import random
import manip
import pygame
import numpy



from manip import welcome
from manip import create_initial_board
from manip import pretty_print_matrix
from manip import removeheader
from manip import max
from manip import is_even
from manip import calc_sumcols
from manip import calc_sumrows
from manip import create_transposeimg
from manip import get_colors
from manip import to_int
from manip import create_transposeimg
from manip import get_colors2
import cmpt120imageWeek9


#read the csv files
board_one = open("board1.csv")
board_two = open("board2.csv")
board_three = open("board3.csv")
image = open("colorcoding.csv")
#gets rid of header
image.readline()
#create the boards from the csv files
board1 = create_initial_board(board_one)
board2 = create_initial_board(board_two)
board3 = create_initial_board(board_three)


#stores amount of games played
games_count = 1

#stores players score
total_score = 0


#displays welcome message 
welcome()

#while loop condition
condition = True

play_game_not_properly_answered = True
while play_game_not_properly_answered:
  play_game = input("Would you like to play? (y/n): ").lower().strip("!,.?/")
  if play_game not in ["y","n"]:
    print("That is not a valid value, please re-enter")
  if play_game in ["y","n"]:
    play_game_not_properly_answered = False

while condition and play_game == "y":
  #Ask the user what levelboard of game they want to play
  print("\nGame: "+ str(games_count) + "\n========\n\n")
  level_not_answered_properly = True
  
  while level_not_answered_properly:
    level = input("Which level would you want to play ('solo' or 'AI')): ").lower().strip("!,.?/")
    if level not in ["solo","ai"]:
      print("That is not a valid value, please re-enter")
    if level in ["solo","ai"]:
      level_not_answered_properly = False 
      #Ask the user what board do they want
      board_not_answered_properly = True
      while board_not_answered_properly:
        board = input("Which initial board do you want to use(1,2 or 3): ").lower().strip("!,.?/")
        if board not in ["1","2","3"]:
          print("That is not a valid value, please re-enter")
        if board == "1":
          pretty_print_matrix("Initial board",board1)
          initial_board = board1
          board_not_answered_properly = False
        elif board == "2":
          pretty_print_matrix("Initial board",board2)
          initial_board = board2
          board_not_answered_properly = False
        elif board == "3":
          pretty_print_matrix("Initial board",board3)
          initial_board = board3
          board_not_answered_properly = False

  turns_not_answered_properly = True
  while turns_not_answered_properly:
    amount_of_turns = int(input("How many turns would you like to play? \n( >= 0 and <= 3): "))
    
    if amount_of_turns not in [0,1,2,3]:
       print("That is not a valid value, please re-enter")
  
    if amount_of_turns == 0:
      print("I see that you liked the board and you don't want changes!")
      turns_not_answered_properly = False
    if amount_of_turns in [1,2,3]:
      for i in range(amount_of_turns):
        print("User, where do you want your digit? (-1 if you want no more turns)")
        
        row_not_answered_properly = True
        while row_not_answered_properly:
          row = int(input("row? (>=0 and <= 3): "))
          if row not in [-1,0,1,2,3]:
             print("That is not a valid value, please re-enter")
          if row == -1:
            row_not_answered_properly = False
            amount_of_turns  = 0
          if row in [-1,0,1,2,3]:
            row_not_answered_properly = False
         
            
        column_not_answered_properly = True
        while column_not_answered_properly:
          column = int(input("column?(>=0 and <= 3): "))
          if column not in [-1,0,1,2,3]:
            print("That is not a valid value, please re-enter")
          
          elif column == -1:
            column_not_answered_properly = False
            amount_of_turns = 0
      
          elif column in [-1,0,1,2,3]:
            column_not_answered_properly = False
        

        digit_not_answered_properly = True
        while digit_not_answered_properly:
          digit = int(input("digit (0 to 9): "))
          if digit not in [0,1,2,3,4,5,6,7,8,9]:
              print("That is not a valid value, please re-enter")
          if digit in [0,1,2,3,4,5,6,7,8,9]:
              digit_not_answered_properly = False
        
        
        turns_not_answered_properly = False
        matrix_row = row + 1
        initial_board[matrix_row][column] = str(digit)
        if row in [0,1,2,3] and column in [0,1,2,3]:
          pretty_print_matrix("New board",initial_board)
          

  #for AI to choose from
  #board one does not have 3 rows/col
  board_one_col = [0,1,2]
  board_one_row = [0,1,2]
  col_list = [0,1,2,3]
  row_list = [0,1,2,3]
  digit_list = [0,1,2,3,4,5,6,7,8,9]
  #AI's turn
  if "ai" in level and initial_board == board2 or initial_board == board3:
    print("The computer will now play!")
    ai_check = input("Hit enter to continue..")
    # matrix = row + 1
    initial_board[random.choice(row_list)][random.choice(col_list)] = str(random.choice(digit_list))
    pretty_print_matrix("New board",initial_board)
  elif "ai" in level and initial_board == board1:
    print("The computer will now play!")
    ai_check = input("Hit enter to continue..")
    # matrix = row + 1
    initial_board[random.choice(board_one_row)][random.choice(board_one_col)] = str(random.choice(digit_list))
    pretty_print_matrix("New board",initial_board)
  
  #need to create a copy of board to be manipulated so it doesnt mess up the original
  board_cpy = initial_board[::]


  #calc the sums of rows/cols using methods
  total_col = calc_sumcols(removeheader(board_cpy))
  total_row = calc_sumrows(board_cpy)
  board_colors = get_colors(image,total_col,total_row)
  poo = get_colors2(image,total_row,total_col)
  
  #find max of sums of row and col
  max_both = max(total_col + total_row)
  
  #fixes dividing by 0 error when calculating total when amount_of_turns = 0
  if amount_of_turns == 0 :
    amount_of_turns +=1

  round_score = (max_both//amount_of_turns)

  print("Totals for this game")
  print("--------------------")
  print("The 'final line' with the sum of all columns is: "+ str(total_col))
  print("The 'final column' with the sum of all rows is: "+ str(total_row))
 
  print ("The points resulting from this board are: "+ str(round_score))
 
  print("Points were calculated as: ")
  print("  the maximum of all numbers in the final line and column ("+ str(max_both) + ")")
  
  user_won = 0
  ai_won = 0

  if (is_even(total_col)) and (is_even(total_row)) :
    print("")
    print("Congrats you won!")
    print("All numbers in the final line and column are even!")
    print("You will be added " + str(round_score) + " points from your total" )
    print("")
    print("Your points so far are: "+ str(total_score + round_score))
    total_score = total_score + round_score
    print("")
    user_won += 1
  else:
    print("")
    print("So sorry, User, you lost this game!")
    print("Not all sums in the final line and column are even!")
    print("You will be substracted " + str(round_score) + " points from your total")
    print("")
    print("Your points so far are: "+ str(total_score - round_score))
    total_score = total_score - round_score
    print("")
    ai_won +=1

  #Keep playing?
  keep_playing = input("Would you like to keep playing? (y/n)").lower().strip("!,.?/")
  if keep_playing == "n":
    print("TOTALS ALL GAMES")
    print("Total points user in all games: " + str(total_score))
    print("Total games the user won: " + str(user_won))
    print("Total games the computer won: " + str(ai_won))
    print("")
    print("In preparation for the images for the final line and column...")
    square_size = input("How many pixels (columns) would you like per square? (recommend <= 60) ")
    print("Number of pixels-->" + square_size)
    square_size=int(square_size)
    
    
    # line width = 240 and height = 50 reverse for column
    
    col_helper = cmpt120imageWeek9.getImage("col.jpg")
    line_helper = cmpt120imageWeek9.getImage("line.jpg")
    
    black_line = cmpt120imageWeek9.createBlackImage(len(col_helper),len(col_helper[0]))
    black_column =cmpt120imageWeek9.createBlackImage(len(col_helper[0]),len(col_helper))
    
    print(board_colors)

  
    black_image_line = cmpt120imageWeek9.createBlackImage(square_size,square_size)
    black_image_col = cmpt120imageWeek9.createBlackImage(square_size,square_size)
    
    
    
    print(board_colors)
    cmpt120imageWeek9.showImage(black_image_line,"line")
  
    cmpt120imageWeek9.showImage(manip.image_black(black_line,board_colors,square_size),"board")
    

    print("Bye!!")
    # condition = False

  
  #update games 
  else:
   games_count +=1 