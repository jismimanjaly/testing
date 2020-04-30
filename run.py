import re 
import csv


def buffer_address ():
   """
   """
   gst_log = open ("log.txt", "r")

   buffer_address =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("buffer buffer",line):
                line = line.replace("," , ":")                
                words = line.split(":")
                buffer_address.append (words[-14])
   gst_log.close()
   return buffer_address


def buffer_element ():
   """
   """
   gst_log = open ("log.txt", "r")

   buffer_element =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("gstpad",line):
                line = line.replace("<",">")
                words = line.split(">")
                buffer_element.append (words[1])
   gst_log.close()
   return buffer_element



def buffer_pts ():
   """
   """
   gst_log = open ("log.txt", "r")

   buffer_pts =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("pts",line):
                words = line.split(",")
                buffer_pts.append (words[-7])
   gst_log.close()
   return buffer_pts


def buffer_dts ():
   """
   """ 
   gst_log = open ("log.txt", "r")

   buffer_dts =[]
   n = 0 
   for line in gst_log:
	n = n + 1
        if re.search ("dts",line):
                words = line.split(",")
                buffer_dts.append (words[-6])
   gst_log.close()
   return buffer_dts

def buffer_duration ():
   """
   """
   gst_log = open ("log.txt", "r")
   buffer_duration =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("size",line):
                words = line.split(",")
                buffer_duration.append (words[-5])
   return buffer_duration


def buffer_flags():
   """
   """
   gst_log = open ("log.txt", "r")
   buffer_flags =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("flags", line):
               words = line.split ()
               buffer_flags.append (words[-1])
              
   gst_log.close() 
   return buffer_flags

def buffer_status():
   """
   """
   gst_log = open ("log.txt", "r")
   buffer_status =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("returned", line):
               words = line.split ()
               buffer_status.append (words[-1])

   gst_log.close()
   return buffer_status

def buffer_size ():
   """
   """
   gst_log = open ("log.txt", "r")
   buffer_size =[]
   n = 0
   for line in gst_log:
        n = n + 1
        if re.search ("size",line):
                #words = line.split(",")
                line = line.replace(" " , ":")
                words = line.split(":")
                buffer_size.append (words[-7])
   return buffer_size

  
def get_bufferinfo ():
    """
    """ 
    log = open ("log.txt", "r")
    schedule_log = csv.writer(open('schedule_log.csv', 'wb'))
    Title = ['Buffer Address','Element','Buffer PTS','Buffer DTS','Buffer Duration','Buffer Flag','Buffer Size','Buffer Status']

    buff_address=buffer_address()
    buff_pts=buffer_pts()
    buff_dts=buffer_dts ()
    buff_dur=buffer_duration()
    buff_size=buffer_size()
    buff_flag=buffer_flags ()
    buff_element=buffer_element()
    buff_status=buffer_status()
    schedule_log.writerow(Title)
    
    for i in range(1,len(buff_status)):
	schedule_log.writerow((buff_address[i],buff_element[i],buff_pts[i],buff_dts[i],buff_dur[i],buff_flag[i],buff_size[i],buff_status[i]))        




get_bufferinfo ()
