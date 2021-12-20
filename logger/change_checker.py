 
 #!/usr/bin/python

import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
	
class MyHandler(FileSystemEventHandler):

	logpath = "/var/log/openerp-server/erp.log"

	substring = "successful login from"
	
#	logpage = "/var/www/html/login.html"
	logpage = "login.html"
	
	logpage_handler = open(logpage, "a+")
	logstring = ""

#	logpage_11 = [x for x in logpage]
#	print logpage_11


	def on_modified(self, event):
		file_handler = open(self.logpath, "r")
	
		print "I am here"
		
    	
		for line in file_handler:
			if self.substring in line:

				if line in self.log:
					print "line already exisits"
				else:
					self.logpage_handler.write(line+"</br></br>")
		
		print "Hello again"
	
		file_handler.close()
	logpage_handler.close()
		


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
