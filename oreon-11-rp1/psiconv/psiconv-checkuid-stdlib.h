Include <stdlib.h> for the exit function.  This avoids an implicit
function declaration, increasing compatibility with future compilers.
Implicit function declarations have been removed from the C language
in 1999.

diff --git a/program/extra/checkuid.c b/program/extra/checkuid.c
index d78e7de723abc44c..eae7d60e5bc74a08 100644
--- a/program/extra/checkuid.c
+++ b/program/extra/checkuid.c
@@ -19,6 +19,7 @@
 
 
 #include <stdio.h>
+#include <stdlib.h>
 
 unsigned long uid1[32] = { /* bit 0  */  0x000045A0,
                            /* bit 1  */  0x00008B40,
