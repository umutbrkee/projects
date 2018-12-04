menu_cont = {}   #defining 2 choice for "ask_cont" function
menu_cont["1"] = "main menu"
menu_cont["2"] = "exit"
def ask_cont():  # this function is for asking user to continue or exiting the game
    while True:
        options_cont = menu_cont.keys()
        options_cont.sort()
        for entry in options_cont:
            print entry, menu_cont[entry]
        selection_cont = raw_input("Please select:")
        if selection_cont == "1":
            print "Returning to main menu.."
            break
        elif selection_cont == "2":
            print"Exiting.."
            exit()
def add_words():       #this funtion is for adding new word
    add_word = raw_input("please write a word:")
    keys.append(add_word)
    print "New word is added succesfully!"
def add_meaning():      #this function is for adding new meaning of a word
    add_means = raw_input("please write words meaning:")
    values.append(add_means)
    print "Meaning is added succesfully!"
def search_choice():
    search_number = input("which one do you mean please select ")
    print show_list
    if search_number == 1:
        return show_list[0]
    elif search_number == 2:
        return show_list[1]
    elif search_number == 3:
        return show_list[2]

print "Building Dictionary...\n","Dictionary Built!"
keys = []             #keys of created dictionary (words)
values = []      #vaules of created dictionary (meanings)
show_list = []
words= str(keys)
menu = {}
menu["1"]="Add word"
menu["2"]="delete word"
menu["3"]="update word"
menu["4"]="display words definition"
print "please add some words to dictionary to play properly"
while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]
    selection=raw_input("Please Select:")
    if selection=="1":    #first choice = adding new word
        add_words()
        add_meaning()
        dictionary = dict(zip(keys, values))  # combining keys and values into a dictionary
        ask_cont()
    elif selection=="2":    #second choice = deleting a word from dictionary
        key_to_remove = raw_input("please select a word to delete:")
        if key_to_remove in dictionary:
            del dictionary[key_to_remove]
            print "Word is removed from dictionary succesfully!"
            ask_cont()
        else:
            print "there is no such key to remove please try again!"
            ask_cont()
    elif selection=="3":    #third choice = updating a word from dictionary
        while True:
            old_word = raw_input("please select a word to update:")
            if old_word in dictionary:
                new_word = raw_input("please write new word:")
                dictionary[new_word]= dictionary[old_word]
                del dictionary[old_word]
                dictionary = dict(zip(keys, values))  # combining keys and values into a dictionary
                print "Word is updated succesfully!"
                break
                ask_cont()
            else:
                print "That word is not in dictionary please try again!"
                ask_cont()
    elif selection=="4":    #forth choice = displays words defination
        search = raw_input("please search anything:")
        for keys in dictionary:
            if search in dictionary:
                print dictionary[search]
                ask_cont()
            elif search == keys[0:len(search)]:
                show_list.append(keys)
                print dictionary
                print show_list
                search_number = input("which one do you mean please select ")
#                if search_number == 1:
 #                   number = show_list[0]
  #              elif search_number == 2:
   #                 number = show_list[1]
    #            elif search_number == 3:
     #               number = show_list[2]
      #          print dictionary[number]
       #         ask_cont()
        #        break
            else:
                print"These are not in dictionary"
                ask_cont()
    else:
        print "pls try again"

