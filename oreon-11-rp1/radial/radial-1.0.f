	program radial3
	print*, " "
	print*, " "
	print*, "------------------------------------------------------"
	print*, " "
	print*, "                Welcome to  Jamie's                   "
	print*, "          FABULOUS RADIAL VELOCITY PROGRAM!           "
	print*, "                                                      "
	print*, "   This program calculates the radial velocities of   "
	print*, "   both stars in a binary system, allowing for user   "
	print*, "   configuration of stellar masses, semimajor axis,   "
	print*, "  inclination of orbital plane, orbital eccentricity, "
	print*, "   time to collect data, and calculation frequency.   "
	print*, "   "
	print*, "   For your convenience, default values have been"
	print*, "   added to the program, so you can run it with"
	print*, "   nothing other than variable eccentricity, if you like."
	print*, " "
	print*, "   This program is free, but donations are welcome. :)"
	print*, " "
	print*, "   Have fun!"
	print*, " "
	print*, "------------------------------------------------------"
	print*, " "
   10	print*, " "
	print*, "Would you like to accept this program's default values"
	print*, "or run a custom configuration?"
	print*, ""
	print*, "            1 - Accept Default Values"
	print*, "            2 - Custom Configuration"
	print*, "           "
	read*, cust
	print*, " "
	print*, " "
c	
c  DEFAULT VALUES:
c	
		pi = 3.141592654
		units = 4.74017744
		wt1 = 0.5
		wt2 = 2.0
		axis = 2.0
		yrs = 5
		q = 4
		tilt = 30
		what2chg = 0
c 	
	    if (cust.eq.1) goto 70
   20		print*, "STELLAR MASSES ..."
           	print*, " "
		print*, "     How massive would you like your stars to be?"
		print*, "     (In Solar Masses)"
		print*, " "
		print*, "Star 1:"
		read*, wt1
		print*, "Star 2:"
		read*, wt2
		print*, " "
		print*, " "
		    if (what2chg.eq.1) goto 80
   30		print*, "SEMIMAJOR AXIS ..."
		print*, "     "
		print*, "     Please specify a semimajor axis. (In AU)"
		print*, " "
		read*, axis
		print*, " "
		print*, " "
		    if (what2chg.eq.2) goto 80
   40		print*, "ORBITAL INCLINATION ..."
		print*, "     "
		print*, "     How far would you like your orbital plane to"
		print*, "     be inclined? (degrees)"
		print*, " "
		read*, tilt
		print*, " "
		print*, " "
		    if (what2chg.eq.3) goto 80
   50		print*, "LENGTH OF TIME FOR WHICH TO CALCULATE ... "
		print*, " "
		print*, "     For how many years would you like to watch?"
		print*, " "
		read*, yrs
		print*, " "
		print*, " "
		    if (what2chg.eq.4) goto 80
   60		print*, "FREQUENCY OF CALCULATIONS ..."
		print*, " "
		print*, "     How many times per year should I calculate?"
		print*, " "
		read*, q
		    if (what2chg.eq.5) goto 80
	print*, " "
	print*, " "
   70	print*, "ORBITAL ECCENTRICITY ..."
	print*, " "
	print*, "     Please enter an orbital eccentricity."
	print*, "     (Must be less than 1. Use 0 for circular orbit.)"
	print*, " "
	read*, ecc
	print*, " "
   80	print*, " "	
c
c COMPUTE axrat, A1, A2, and SEE
c
		axrat = wt1/wt2	
		ax1 = axis/(1+axrat)
		ax2 = (axis*axrat)/(1+axrat)
		see = 1/q
		tilt = (6.283185/360)*tilt
c
	print*, "Here are the values you have chosen:"
	print*, " "
	print*, "-------------------------------------------------------"
	print*, "       Mass of star 1:  ",wt1," Solar Masses"
	print*, "       Mass of star 2:  ",wt2," Solar Masses"
	print*, " "
	print*, "       Semimajor axis:  ",axis," AU"
	print*, "	     for star1:  ",ax1," AU"
	print*, "            for star2:  ",ax2," AU"
	print*, " "
	print*, "       Orbital Eccentricity:  ",ecc
	print*, "        Orbital Inclination:  ",tilt
	print*, " "
	print*, "          sin(tilt) = ",sin(tilt)	
	print*, " "
	print*, "       Time to watch:  ",yrs," yrs"
	print*, "                       ",q," times per year"
	print*, "-------------------------------------------------------"
	print*, " "
	print*, "Are these values OK?"
	print*, " "
	print*, "             1 - These are good, calculate!"
	print*, "             2 - I want to change something."
	print*, " "
	read*, change
	print*, " "
	    if (change.eq.2) then
	    	print*, " "
	    	print*, "What would you like to change?"
		print*, " "
		print*, "              1 - Stellar Masses"
		print*, "              2 - Semimajor Axis"
		print*, "              3 - Orbital Inclination"
		print*, "              4 - Time to Watch"
		print*, "              5 - Frequency of Calculation"
		print*, "	       6 - Orbital Eccentricity"
		print*, "              7 - Everything"
		print*, "              0 - Nothing, I lied. Calculate!"
		print*, " "
		read*, what2chg
		print*, " "
		print*, " "
		    if (what2chg.eq.1) goto 20
		    if (what2chg.eq.2) goto 30
		    if (what2chg.eq.3) goto 40
		    if (what2chg.eq.4) goto 50
		    if (what2chg.eq.5) goto 60
		    if (what2chg.eq.6) goto 70
		    if (what2chg.eq.7) goto 10
	    endif
	    what2chg = 0
	print*, "Processing input, calculating velocities ... please wait."
	print*, " "
	print*, " "
	print*, " Time (yrs)    V1r (km/s)       V2r (km/s)     theta (deg)"
	print*, "=========================================================="         
c
c CALCULATE THE VELOCITIES
c
	do p=0.00, yrs, see
		theta = 2*pi*(axis**(-3/2))*p
		tht = 360*(axis**(-3/2))*p
		top = 2*pi*ax1*(1-(ecc**2))*(sin(tilt))*units
		bot = (axis**(3/2))*(1+(ecc*(cos(theta))))
		v1r = (top*(cos(theta)))/bot
		v2r = (top*axrat*(cos(theta+pi)))/bot
c debugging	print*, top," ",brt," ",bot
		print*, "  ",p,"      ",v1r,"         ",v2r,"      ",tht
	enddo
	print*, "==========================================================="
	print*, " "	
	print*, " "
	print*, "  Would you like to play again?"
	print*, " "
	print*, "                1 - Yes, this was fun! Do it again!"
	print*, "                2 - No, it was lame. I want to leave."
	print*, " "
	read*, play
		if (play.eq.1) goto 10
	print*, " "
	print*, " "
	print*, "Thanks for using Jamie's Fabulous Radial Velocity Program!"
	print*, " "
	print*, "Send questions, comments, money, food, clothing, books,"
	print*, "or anything else to:   hegarty@nhn.ou.edu"
	print*, " "
	print*, "Bye!"
	print*, " "
	print*, " "
	end
