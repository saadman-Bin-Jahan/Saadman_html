def shutdown(command):
    command = command.lower()
    if command == "yes":
        return "Shutting down"
    elif command == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
user_input = input("Do you want to shut down? (yes/no): ")
print(shutdown(user_input))
