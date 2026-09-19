#ifndef TTH_H
#define TTH_H

/* The function interface to tth.
   Convert a texstring into an htmlstring which has length hlen.
   Stop converting when the length of htmlstring is > hlen-200.
   So hlen must be >200! Returns the number of times it has been called.
*/

int textohtml(char* texstring, char* htmlstring, int hlen,
	      char* errstring, int elen);

#endif
