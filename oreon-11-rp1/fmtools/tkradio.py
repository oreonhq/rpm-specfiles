#!/usr/bin/python3
# Paulo Roma - simple tkinter interface for fmtools,
#              with lirc and recording support.
# Date: 23/12/2009
# The radio is turned off on exit.

import os, sys, string, pickle, math
import datetime, time, signal
from threading import Thread
from subprocess import Popen, PIPE

try:
    from tkinter import *    # python3
except ImportError:
    try:
        from mtTkinter import *
    except ImportError:
        from Tkinter import *
        print ( "mtTkinter not found: http://tkinter.unpythonic.net/wiki/mtTkinter" )
        print ( "Remote control will not work!!" )

try:
    import pylirc
    use_lirc = True
except ImportError:
    use_lirc = False
    print ( "pylirc not found: http://pylirc.mccabe.nu/" )
    print ( "Remote control will not work!!" )

try:
    import pynotify
    if pynotify.init("tkradio"):
        use_notify = True
    else:
        use_notify = False
        print ( "pynotify module initialization failed" )
except:
    use_notify = False
    print ( "notify-python not found: http://www.galago-project.org/downloads.php" )

# These are stations in the Rio de Janeiro area. 
# Customize for your own locale. They can be set
# in file ~/.fmrc or ~/.radiostations:
# station name, frequency and volume.

stations = [["Globo",        "89.3 100"],
            ["MPB",          "90.3 100"],
            ["CBN",          "92.5 100"],
            ["Band News",    "94.9 100"],
            ["Paradiso",     "95.7 100"],
            ["Tupy",         "96.5 100"],
            ["Beat98 FM",    "98.1 100"],
            ["MEC",          "98.9 100"],
            ["JB FM",        "99.7 100"],
            ["O Dia",        "100.5 100"],
            ["Transamerica", "101.3 100"],
            ["Mix",          "102.1 100"],
            ["Oi",           "102.9 100"],
            ["Nativa",       "103.7 100"]]

radbut   = stations[4][1]  # default radio frequency
volume   = 100             # initial volume [0,100]
state    = False           # keep track of mutting/unmutting
blocking = 0               # lirc blocking control
tid      = 0               # recorder thread id
lid      = 0               # loopback process id
fmrec    = None            # recorder thread variable
irrec    = None            # lirc thread variable

# external programs used

MIXER = "/usr/bin/amixer"     # alsa-utils
PIDOF = "/sbin/pidof"         # sysvinit-tools
PS    = "/bin/ps"             # procps 
GREP  = "/bin/grep"           # grep
FM    = "/usr/bin/fm"         # fmtools
OGG   = "/usr/bin/oggenc"     # vorbis-tools
RPNG  = "/usr/share/pixmaps/radio.png"
RGIF  = "/usr/share/fmtools/radio.gif"
#CHANNEL = "PCM"
CHANNEL = "Master"

class IRRec(Thread):
   """Class for interacting with lirc."""

   def __init__ (self, lirc_handle):
       """Constructor."""

       Thread.__init__ (self)
       self.lirc_handle = lirc_handle
       self.__on = True
  
   def stop ( self ):
       """Kills this thread."""

       self.__on = False 

   def run(self):
      """Run the thread code."""

      code = {"config" : ""}

      while ( self.__on ):
            # Delay...
            time.sleep(1)

            s = pylirc.nextcode(1)
            while ( s ):
               for code in s:
                   if ( code["config"] == "next" ):
                        next()
                   elif ( code["config"] == "previous" ):
                        previous()
                   elif ( code["config"] == "off" ): 
                        mute() 
                   elif ( code["config"] == "on" ):
                        radio ("on")
                   elif ( code["config"] == "volup" ):
                        volup ()
                   elif ( code["config"] == "voldown" ):
                        voldown()
                   elif ( code["config"] in "0123456789" ):
                        time.sleep(1)
                        b=pylirc.nextcode()
                        if ( b and b[0] in "0123456789" ):
                             code["config"] += b[0]
                        setStation ( int (code["config"]) )
                   elif ( code["config"] == "rec" ):
                        rec_on()
                   elif ( code["config"] == "stop" ):
                        rec_off()
                   elif ( code["config"] == "loop" ):
                        loopon()
                   elif ( code["config"] == "quit" ):
                        fini()
                   else:
                        # Print all the configs...
                        print ( "Command: %s, Repeat: %d" % (code["config"], code["repeat"]) )
               if (not blocking):
                   s = pylirc.nextcode(1)
               else:
                   s = []

      # if we get here, the thread is over, so clean up lirc
      pylirc.exit()

class FMRec(Thread):
   """Class for controlling the recording process."""

   def __init__ (self):
       """Constructor."""

       Thread.__init__ (self)
       self.__pid = 0       # arecord process id
       self.__on  = True    # for implementing a thread stop, 
                            # which python does not have
   def __del__ (self):
       """Destructor. Stops the recording, before quitting."""

       self.stop()

   def stop ( self ):

       """Stops the recording, by killing the recorder process."""

       global tid

       tid = 0

       if ( self.__pid ):
            os.kill ( self.__pid, signal.SIGTERM )
       self.__pid = 0
       self.__on = False

   def run(self):
       """Start the thread."""

       while (self.__on):
           if ( not self.__pid ):
                data = str(datetime.date.today())
                hora = list(time.localtime(time.time()))
                hora = str(hora[3])+":"+str(hora[4])+":"+str(hora[5])
                rec_file = '/tmp/tkradio-'+fmstations[cur_station][0]+"-"+data+"-"+hora+'.ogg' 
                if use_notify:
                   n = pynotify.Notification("tkradio recording on file:", rec_file, RPNG)
                   n.show()
                ogge_param [-1] = rec_file
                p1 = Popen(brec_param, stdout=PIPE)
                p2 = Popen(ogge_param, stdin=p1.stdout)
                self.__pid = p1.pid

           time.sleep(1.0) # Suspend execution for the given number of seconds

       # if we get here, the thread is finished
       self.stop ()

def start_irrec ():
    """Start the IRRec thread if lircd is running."""
 
    global irrec
 
    lircid = getpid ( 'lircd' )
    if ( lircid ): # is lirc running?
         # handle lirc events
         path = os.environ.get("HOME")
         fname = path+"/.fmlircrc"
         if ( not os.path.exists (fname) ):
              fname = "/usr/share/fmtools/fmlircrc"
         lirc_handle = pylirc.init("tkradio", fname, blocking)
         if (lirc_handle):
             if ( use_notify ):
                  n = pynotify.Notification("tkradio", "Successfully opened lirc. Handle is "+str(lirc_handle), RPNG)
                  n.set_timeout(2000)
                  n.show()
             irrec = IRRec(lirc_handle)
             irrec.start()

def set_rec_type():
    """Set recording based on alsa or pulseaudio."""

    global REC           # program for recording
    global PLAY          # program for playing
    global arec_param    # recording parameters
    global apla_param    # playing parameters
    global brec_param    # recording parameters for encoding
    global ogge_param    # encoding parameters

    pulseaudio = getpid ( 'pulseaudio' )
    if ( pulseaudio ): # is pulseaudio running?
         REC  = "/usr/bin/parec"    # pulseaudio-utils
         PLAY = "/usr/bin/pacat"    # pulseaudio-utils
         arec_param = [REC]
         brec_param = [REC]
         apla_param = [PLAY] 
         ogge_param = [OGG, '-', '-r', '-Q', '-o', ""] 
    else:
         REC  = "/usr/bin/arecord"  # alsa-utils
         PLAY = "/usr/bin/aplay"    # alsa-utils
         arec_param = [REC, '-D', 'default', '-d', '0', '-f', 'cd']
         brec_param = [REC, '-D', 'default', '-d', '0', '-f', 'cd', '-']
         apla_param = [PLAY, '-f', 'cd', '-D', 'default'] 
         ogge_param = [OGG, '-', '-Q', '-o', ""] 

    return pulseaudio

def radio ( cmd ):
    """Send the given command to the radio."""

    os.system(FM + " " + cmd)

def setCurStation ( frequency ):
    """Update the current station."""

    global cur_station 

    ind = 0
    for st in fmstations:
        if ( st[1] == frequency ):
             cur_station = ind
             break
        ind += 1 

def setstation():
    """Set the station chosen via Radio Button."""
 
    freq = station.get() 
    changeStation ( freq )
    setCurStation ( freq )

def setStation(ind):
    """Set the station to ind."""
 
    if ( ind >= 0 and ind < ns ):
         freq = fmstations[ind][1]
         changeStation ( freq )
         setCurStation ( freq )

def changeStation ( st ):
    """Set the station to the given station."""

    radio ( st )
    freq.delete(0, END)
    freq.insert(0,st.split()[0])
    station.set ( st )

def fini():
    """Quit the radio."""

    radio ("off")
    # kill all threads
    if ( fmrec ): fmrec.stop()
    if ( irrec ): irrec.stop() 
    if ( lid ): os.kill ( lid, signal.SIGTERM )

    os._exit (0)

def mute():
    """Mute/Unmute the radio."""

    global state

    if ( not state ):
        radio ("off")
        state = True 
        btmute.set ( "On" )
        btm.config(state=ACTIVE)
    else:
        radio ("on")
        state = False
        btmute.set ( "Off" )
        btm.config(state=NORMAL)

def setVolume ( v ):
    os.system(MIXER + " -q -c 0 set " + CHANNEL + " " + str(v) + "%")

def getVolume ( ):
    vol = os.popen (MIXER + " -c 0 get " + CHANNEL + " | " + GREP + " -E \"%\"").readline()
    i = str.find (vol,"%")
    j = str.find (vol,"[",0,i)
    return int(vol[j+1:i])

def on_move(value=0):
    """Use slider position to set the volume."""

    setVolume ( scale.get() )

def volup ():
    """Increase the volume."""

    v = scale.get() + 5
    if ( v > 100 ): v = 100
    scale.set ( v )
    setVolume ( v )

def voldown():
    """Decrease the volume."""

    v = scale.get() - 5
    if ( v < 0 ): v = 0
    scale.set ( v )
    setVolume ( v )

def enter ():
    "Enter a new frequency."""

    f = freq.get()+" "+ str(volume)
    changeStation (f)
    setCurStation (f)

def readStations ( ):
    """Read the preset station file."""

    path = os.environ.get("HOME")
    fname = path+"/.radiostations"
    if ( not os.path.exists (fname) ):
         fname = path+"/.fmrc"

    lst = []
    if ( os.path.exists (fname) ):
       textf = open(fname, 'r')

       for line in textf:
           l=line.split(None)
           st = [l[0].replace("_"," "),l[1]+" "+l[2]]
           lst.append ( st )
       textf.close()
    return lst

def next ():
    "Go to the next station."""
 
    global cur_station
    cur_station = (cur_station + 1) % ns
    changeStation ( fmstations[cur_station][1] )

def previous ():
    "Go to the previous station."""

    global cur_station
    cur_station = (cur_station - 1) % ns
    changeStation ( fmstations[cur_station][1] )

def trigger ():
    """Create a thread for recording."""

    global tid, fmrec

    if ( not tid ):
         fmrec = FMRec ()
         fmrec.start()
         tid = 1

def loop():
    """Route the capture sources on the sound card back in as PCM audio."""
  
    global lid

    if ( loopvar.get() == "ON" ): 
         if ( not lid ):
              p1 = Popen(arec_param, stdout=PIPE)
              p2 = Popen(apla_param, stdin=p1.stdout)
              lid = p1.pid
              if ( use_notify ):
                   n = pynotify.Notification("tkradio", "Software Loop Back activated",
                                             RPNG)
                   n.set_timeout(2000)
                   n.show()
    else: 
         if ( lid ):
              os.kill ( lid, signal.SIGTERM )
              lid = 0

def loopon():
    """Toggle the loop variable."""

    if ( loopvar.get() == "ON" ):
         loopvar.set ("OFF")
    else:
         loopvar.set ("ON")
    loop()

def rec():
    """Record the current station."""

    if ( recvar.get() == "ON" ):
         rec_on()
    else:
         rec_off()

def rec_on():
    """Turn the recorder on."""

    recvar.set ("ON")
    trigger()

def rec_off():
    """Turn the recorder off."""

    recvar.set ("OFF")
    if ( fmrec ): fmrec.stop()

def mouse_wheel(event):
    """Respond to mouse wheel events."""

    if event.num == 5 or event.delta == -120:
       voldown ()
    if event.num == 4 or event.delta == 120:
       volup ()

def str2num(datum):
    """A conversion function that "guesses" the best conversion."""

    try:
        return int(datum)
    except:
        try:
            return float(datum)
        except:
            return datum

def getpid(proc):
    """Return the ID of the given process."""

    aid = os.popen ( PIDOF + ' ' + proc ).readline()
    aid = aid.replace('\n','')
    return str2num(aid)

class radioState:
      """Holds the state of the radio (used for persistency)."""

      def __init__ ( self, intial_station ):
          self.volume   = getVolume()
          self.loop     = "OFF"
          self.mute     = False
          self.station  = intial_station
          self.pos      = ""

      def __str__ (self):
          return " Volume = %s\n Loop = %s\n Mute = %d\n Station = %s\n Pos = %s\n" % \
                  ( self.volume, self.loop, self.mute, self.station, self.pos )

def main (argv=None):
    """Main program."""

    global scale         # volume scale
    global state         # toggle mute/umute
    global station       # variable for the station radio buttons
    global btmute        # variable for the text in the mute button
    global btm           # mute button
    global freq          # variable for manually entering a frequency
    global fmstations    # preset fm stations
    global cur_station   # current station
    global ns            # number of preset fm stations
    global recvar        # variable for setting record on/off
    global loopvar       # variable for setting loopback on/off
    global lid           # loopback process id

    def cleanup():
        savedState.volume  = scale.get()
        savedState.loop    = loopvar.get()
        savedState.mute    = state
        savedState.station = station.get()
        savedState.pos     = mw.geometry()
        pf = open(statfile,'wb')
        pickle.dump ( savedState, pf )
        pf.close()
        # print ( savedState )
        raise SystemExit

    if argv is None:
       argv = sys.argv

    pyversion = str.split(sys.version)[0]
    print ( "Python Version: %s" % pyversion )

    # check whether tkradio is already running
    stat = os.popen (PS + " aux | " + GREP + " -E \"python(" + pyversion[0:3] + ")? " + argv[0] + "\"").readline()
    cid = os.getpid()
    if ( stat ): 
         pid = stat.split()[1]
         if ( cid != int(pid) ): 
              sys.exit ( "%s is already running: pid = %s" %(argv[0], pid) )

    path = os.environ.get("HOME")
    statfile = path + '/.tkradio'
    if (sys.hexversion > 0x03000000):
        statfile += '3'
    if ( not os.path.exists (statfile) ):
         savedState = radioState(radbut)
    else:
         pf = open(statfile,'rb')
         savedState = pickle.load(pf)
         pf.close()

    mw = Tk()
    # do not resize the radio
    mw.resizable(False,False)

    station = StringVar()
    station.set (savedState.station)

    btmute = StringVar()
    state = not savedState.mute
    btmute.set ( "OFF" )

    top = Frame(); top.pack()
    bbt = Frame(); bbt.pack()
    bot = Frame(); bot.pack()
    mw.title ("tkradio")

    fmstations = readStations ( )
    if ( not fmstations ):
         fmstations = stations
    ns = len ( fmstations )
    cur_station = -1

    # sets the recording type: alsa or pulse
    if ( set_rec_type() ):        
         Label(top, text = 'pulse: '+CHANNEL).pack()
    else:
         Label(top, text = 'alsa: '+CHANNEL).pack()

    # make tuner buttons
    for st in fmstations:
        Radiobutton(bot,text=st[0],value=st[1],variable=station,command=setstation).pack(anchor=W)

    scale = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=on_move, bd=0,
                  sliderlength=10, width=5, showvalue=0)
    scale.pack(side='top')
    scale.set(savedState.volume)

    # the current radio frequency
    Button(bbt,text="<", command = previous).pack(side="left",anchor=E)
    Button(bbt,text="Enter", command = enter).pack(side="left")
    Button(bbt,text=">", command = next).pack(side="left",anchor=W)
    freq=Entry(top,font="Arial 24",width=5,justify=CENTER)
    freq.insert(0,station.get())
    freq.pack(side="bottom")

    recvar = StringVar()   # creates a checkbutton for the recording state
    loopvar = StringVar()  # creates a checkbutton for the loopback
    recvar.set ( "OFF" )
    aid = getpid ( str.rsplit(REC,'/',1)[1] )
    if ( aid ): # is the loop back already on?
         loopvar.set ( "ON" )
         lid = aid
    else:
         loopvar.set ( savedState.loop )
         loop ()

    # create quit and mute buttons
    Button(top,text="Exit", command = cleanup).pack(side="right")
    btm=Button(top,text="Off", command = mute, textvariable = btmute)
    btm.pack(side="left")
    Checkbutton (top, text="Rec", variable=recvar, onvalue="ON", offvalue="OFF", command=rec).pack(side="top",anchor=W)
    Checkbutton (top, text="Loop", variable=loopvar, onvalue="ON", offvalue="OFF", command=loop).pack(side="right")

    # mouse whell control
    mw.bind("<Button-4>", mouse_wheel)
    mw.bind("<Button-5>", mouse_wheel)

    # turn the radio on
    setstation()
    mute()

    # set an icon for the window
    icon_img = PhotoImage(file=RGIF)
    mw.tk.call('wm', 'iconphoto', mw._w, icon_img)

    # start the lirc thread
    if ( use_lirc ):
         start_irrec()  

    mw.protocol("WM_DELETE_WINDOW", cleanup)

    if ( savedState.pos ): mw.geometry(savedState.pos)

    mw.mainloop()

if __name__=="__main__":
   try:
      sys.exit(main())
   except (KeyboardInterrupt,SystemExit):
      fini()
