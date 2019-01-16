import webbrowser as wb
import time as t

print("Program started")
i = 0
breaks = 5
video = 'https://www.youtube.com/watch?v=jo7mkwvlR9I&list=RDjo7mkwvlR9I&start_radio=1'

while i < breaks:
    t.sleep(1)
    print("BREAK!!! at "+t.ctime())
    wb.get('chrome').open_new_tab(video)
    i += 1
