def new_game():
  name = input("What is your name? \n")
  char_file = open(name + ".py", "x")

start = input("Enter Start \n")
while start == "Start":
  main_menu = """
       ________________________________________________________
      |                                                        |
      |   New Game (N)                                         |
      |   Load Game (L)                                        |
      |   Options (O)                                          |
      |   Credits (Credits)                                    |
      |   Quit (Quit)                                          |
      |                                                        |
      |________________________________________________________|
  
  """

  main_menu_choice = input(main_menu + "What do you want to do? \n")

  while main_menu_choice == main_menu_choice:
    if main_menu_choice == "N":
      new_game_confirm = input("Are you sure you want to start a new game? \n")
      if new_game_confirm == "Y":
        new_game()
        break
        if new_game_confirm == "N":
          print("back to main menu")
          break
        else:
          print("ERROR: Incorrect input")
          new_game_confirm = input("Do you want to start a new game? \n")
        break
      elif new_game_confirm == "N":
        print("Back to the main")
      break
    elif main_menu_choice == "L":
      print("Load Game")
      break
    elif main_menu_choice == "O":
      print("Options")
      break
    elif main_menu_choice == "Credits":
      print("""
          Creater: Dakwon Smith
          Writter: Dakwon Smith
      """)
      break
    elif main_menu_choice == "Quit":
      confirm_quit = input("Do you want to quit? (Y/N) \n")
      while confirm_quit == confirm_quit:
        if confirm_quit == "Y":
          print("Program ending....")
        elif confirm_quit == "N":
          print("Returning to main menu....")
        else:
          print("Incorrect input")
          confirm_quit = input("Do you want to quit? (Y/N) \n")
        break
      break
    else:
      print("ERROR")
      main_menu_choice = input(main_menu + " What do you want to do? \n")
  break  
else:
  print("Ending program....")


