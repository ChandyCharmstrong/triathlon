contestent_name = input("Please enter contestant name: ") #I know this is an extra step but I think it adds something to the end

swimming = int(input("Please enter swimming completion time (in minutes): "))
cycling = int(input("Please enter cycling completion time (in minutes): "))
running = int(input("Please enter running completion time (in minutes): "))
triathlon_time = swimming + cycling + running
if triathlon_time <= 100:
    print("Awarded Provinicial Colours")
elif triathlon_time <=104:
    print("Awareded Provincial Half Colours")
elif triathlon_time <=109:
    print("Awareded Provincial Scroll")
else: 
    print("No Award Granted")

print(contestent_name, "had a total completion time of", triathlon_time, "minutes") 

#How could I add the result to this? It feels really close to something actually workable irl. 