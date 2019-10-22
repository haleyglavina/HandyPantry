# //==============================//
# // Haley Glavina - October 2019 //
# // Handy Pantry User Interface  //
# //==============================//

# This program contains global variables and information that must be maintained when the system loses power. The contents of this file must be saved as nonvolatile memory.

# List of fooditems which have been saved as templates for future inputs of that same item
templates = []

# List of 5 most recently retrieved fooditems
retrieved = [None,None,None,None,None]

# List of fooditems currently help in HP. Is a practice storage array until integrated with memory module.
curr_storage = []
