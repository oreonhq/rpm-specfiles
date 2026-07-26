c
c	sample program to read binary file in fortran
c	this may or may not work! (system dependent)
c	often works with UNIX fortrans
c
	real array(192,94)
	character*1 line(192)

	write(*,*) 'should first run wgrib -d 1 land.grb'

	open(unit=1,file='dump',form='unformatted',status='old')
	read(1) array
	err=1e-6
	do 100 j = 1, 94
	    do 90 i = 1, 192
	        if (array(i,j).eq.0.0) then
		    line(i) = ' '
		else if (abs(array(i,j)-1.0).lt.err) then
		    line(i) = 'x'
		else
		    write(*,*) 'bad values:',array(i,j)
		    stop
		endif
90	    continue
	    if (mod(j,3).eq.0) write(*,*) (line(i),i=1,192,3)
100	continue
	write(*,*) 'should see continents'
	stop
	end
