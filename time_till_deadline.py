from datetime import datetime

user_input = input("Introduce your goal with a deadline(dd/mm/yyyy) separated by dash:\n")
input_list = user_input.split("-")
user_goal = input_list[0]
user_goal_deadline = datetime.strptime((input_list[1]), "%d/%m/%Y")
today_date = datetime.today()
time_till_deadline = user_goal_deadline - today_date
if (time_till_deadline.days < 0):
  print("You are overdue")
elif( time_till_deadline.days > 0):
  print(f"Days remaining for {user_goal} is {time_till_deadline.days}")
else:
  print(f"Hours remaining for {user_goal} is {int(time_till_deadline.total_seconds()/60/60)}")
