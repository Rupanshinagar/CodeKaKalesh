import random
tasks=[]
lazy_excuses = [
    "Added. Maybe.",
    "Sure, buddy.",
    "Good luck.",
    "We'll see.",
    "Do it. ",
    "Tomorrow. ",
    "Bold move.",
    "Nice try.",
    "Cool story.",
    "Noted... ish.",
    "Dream on.",
    "As if.",
    "Big plans?",
    "Stay lazy.",
    "Another? ",
    "Go touch it.",
    "One more?",
    "Oops, added.",
    "Good luck. ",
    "Panic later."
]
done_hype = [
    "Task smashed.",
    "Easy win.",
    "Let's go.",
    "Built different.",
    "Huge W.",
    "Mission done.",
    "Too easy.",
    "Peak human.",
    "GG.",
    "Level up.",
    "No excuses.",
    "Big flex.",
    "Keep going.",
    "Certified winner.",
    "You did it.",
    "Well played.",
    "Nice work.",
    "Crushed it.",
    "Done and dusted.",
    "Victory."
]
delete_roast = [
    "Task deleted.",
    "Gone already?",
    "Poof. Gone.",
    "Mission aborted.",
    "No witnesses.",
    "Vanished.",
    "Gone forever.",
    "RIP task.",
    "Nice escape.",
    "Clean slate.",
    "Problem solved.",
    "Task erased.",
    "Gone. Nice.",
    "Goodbye, task.",
    "One less.",
    "History.",
    "Deleted. Oops.",
    "Out it goes.",
    "Bye-bye task.",
    "Never existed."
]
invalid_roast = [
    "Wrong choice.",
    "Try again.",
    "Not an option.",
    "Read first.",
    "Nice guess.",
    "Numbers only.",
    "Bro, count.",
    "Invalid. Again?",
    "Use your eyes.",
    "Math is hard?",
    "Close... not really.",
    "Nope.",
    "That's illegal.",
    "You tried.",
    "Think harder.",
    "Pick a number.",
    "404: Brain.",
    "Skill issue.",
    "Try harder.",
    "Not even close."
]
def show_menu():
    print("\n===== TO-DO LIST (with attitude) =====")
    print("1. Add Task (why not)")
    print("2. View Tasks (reality check)")
    print("3. Mark Done (about time)")
    print("4. Delete Task (nice escape)")
    print("5. Exit (see ya)")

