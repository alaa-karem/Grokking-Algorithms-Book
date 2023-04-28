# Recursion code:     I wanna search for a key in some boxes in big box
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)    #Recursion!
        elif item.is_a_key():
            print ("found the key!")


# Loop code:   The same previous thing
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print ("found the key!")