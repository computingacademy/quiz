room = "start"
key = False
looked = False

while room != "end":
  if room == "start":
    print("Actions available: forward, look")
    action = input("> ")
    if action == "forward":
      room = "middle"

  elif room == "middle":
    if looked == True:
      print("Actions available: forward, backward, look, pickup")
    else:
      print("Actions available: forward, backward, look")
    action = input("> ")
    if action == "forward":
      if key == True:
        room = "end"
      else:
        print("The door is locked.")
    elif action == "backward":
      room = "start"
    elif action == "look":
      print("You spot a key on the floor.")
      looked = True
    elif action == "pickup":
      print("You picked up the key!")
      key = True

  if room == "start":
    print("You are standing in the entrace to the castle. There is no exit.")
  elif room == "middle":
    print("You are in the middle room of the castle.")
print("You have unlocked the door and escaped the castle. You win!")
