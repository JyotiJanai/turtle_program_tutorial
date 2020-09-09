import webbrowser
import time

total_break = 3
break_count = 0
while(break_count < total_break):
	print("This program started on" +time.ctime())
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=LSYpxo7behA")
	break_count += 1

