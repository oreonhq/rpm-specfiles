# The upstream Makefile is broken in multiple ways.
# 1. It doesn't allow for parallel building, due to many missing dependencies.
# 2. It only builds static libraries.  Yes, there is an "oshared" target that
#    supposedly builds a shared library.  Try it and see how it works for you.
# 3. Each target starts by doing a clean.  That means that if you want to build
#    more than one target (we want to build 3), then each invocation of make
#    destroys all the work you did in the previous target.
# 4. A number of targets explicitly invoke make, when they should have done
#    their work in the context of the current invocation of make.
#
# Forget it!  I'm writing my own Makefile.

CC = gcc
INCLUDES = -I/usr/include/flexiblas -Iinclude -Isrc/solver -Isrc/sdp -Isrc/vecmat
CFLAGS = @RPM_OPT_FLAGS@ -fPIC -DDSDP_TIME $(INCLUDES)
BFLAGS = @RPM_OPT_FLAGS@ -DDSDP_TIME -Iinclude -Lsrc
LDFLAGS = @RPM_LD_FLAGS@ -Wl,--as-needed -lflexiblas -lm
BDFLAGS = @RPM_LD_FLAGS@ -Wl,--as-needed -ldsdp -lflexiblas -lm
SONAME = -Wl,-h,libdsdp.so.5

SOLVER_OBJS = src/solver/dualalg.o src/solver/dualimpl.o \
	src/solver/dsdpcops.o src/solver/dsdpschurmat.o src/solver/dsdpcg.o \
	src/solver/dsdpconverge.o src/solver/dsdpsetup.o \
	src/solver/dsdpcone.o src/solver/dsdpsetoptions.o \
	src/solver/dsdpsetdata.o src/solver/dsdprescone.o \
	src/solver/dsdpobjcone.o src/solver/dsdpprintout.o \
	src/solver/dsdpschurmatadd.o src/solver/dsdpx.o

SDP_OBJS = src/sdp/dsdpstep.o src/sdp/printsdpa.o src/sdp/sdpconevec.o \
	src/sdp/sdpsss.o src/sdp/dsdpadddata.o src/sdp/dsdpadddatamat.o \
	src/sdp/dsdpblock.o src/sdp/sdpcone.o src/sdp/sdpkcone.o \
	src/sdp/sdpcompute.o src/sdp/sdpconesetup.o src/sdp/dsdpdsmat.o \
	src/sdp/dsdpdatamat.o src/sdp/dsdpdualmat.o src/sdp/dsdpxmat.o

LP_OBJS = src/lp/dsdplp.o

VECMAT_OBJS = src/vecmat/vech.o src/vecmat/vechu.o src/vecmat/drowcol.o \
	src/vecmat/dlpack.o src/vecmat/dufull.o src/vecmat/sdpvec.o \
	src/vecmat/identity.o src/vecmat/spds.o src/vecmat/zeromat.o \
	src/vecmat/onemat.o src/vecmat/diag.o src/vecmat/rmmat.o \
	src/vecmat/cholmat.o src/vecmat/cholmat2.o src/vecmat/dtrsm2.o \
	src/vecmat/sdpmatx.o src/vecmat/sdpnfac.o src/vecmat/sdporder.o \
	src/vecmat/sdpalloc.o src/vecmat/sdpsymb.o src/vecmat/sdpxlist.o \
	src/vecmat/sdpdvct.o src/vecmat/sdpexit.o

SYS_OBJS = src/sys/dsdperror.o src/sys/dsdploginfo.o src/sys/dsdplog.o \
	src/sys/dsdptime.o

BOUNDS_OBJS = src/bounds/dbounds.o src/bounds/allbounds.o

LIB_OBJS = $(SOLVER_OBJS) $(SDP_OBJS) $(LP_OBJS) $(VECMAT_OBJS) $(SYS_OBJS) \
	$(BOUNDS_OBJS)

EXAMPLES = examples/maxcut examples/theta examples/dsdp5 examples/stable \
	examples/color

all: $(EXAMPLES)

src/libdsdp.so.@version@: $(LIB_OBJS)
	$(CC) $(CFLAGS) -shared $(SONAME) -o $@ $^ $(LDFLAGS)

src/libdsdp.so.5: src/libdsdp.so.@version@
	ln -s libdsdp.so.@version@ $@

src/libdsdp.so: src/libdsdp.so.5
	ln -s libdsdp.so.5 $@

examples/maxcut: examples/maxcut.c src/libdsdp.so
	$(CC) $(BFLAGS) $< -o $@ $(BDFLAGS)

examples/theta: examples/theta.c src/libdsdp.so
	$(CC) $(BFLAGS) $< -o $@ $(BDFLAGS)

examples/dsdp5: examples/readsdpa.c src/libdsdp.so
	$(CC) $(BFLAGS) $< -o $@ $(BDFLAGS)

examples/stable: examples/stable.c src/libdsdp.so
	$(CC) $(BFLAGS) $< -o $@ $(BDFLAGS)

examples/color: examples/color.c src/libdsdp.so
	$(CC) $(BFLAGS) $< -o $@ $(BDFLAGS)
