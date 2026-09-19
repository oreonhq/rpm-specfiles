%global source0_hash 25d39a2107767b622a59dd9fa790112c1516564b8518fc6ac0fab081d5ac3ab0

# Copyright (c) 2015 Dave Love, Liverpool University
# The licence for this file is as for the package itself.

Name:		dssp
Version:	3.0.0
Release:	29%{?dist}
Summary:	Protein secondary structure assignment
%{?el5:Group:		Applications/Engineering}
License:	BSL-1.0
URL:		http://swift.cmbi.ru.nl/gv/dssp/
Source0:	ftp://ftp.cmbi.ru.nl/pub/software/dssp/dssp-%version.tgz
# don't suppress make output
Patch1:		dssp-make.patch
# Fix build with boost 1.66 (#1537546)
Patch2:		dssp-tuple.patch
# Fix build with GCC 15 (#2384563)
Patch3:         dssp-nullptr.patch
# Fix build with Boost 1.90.0 which has no libboost_system.so
Patch4:         dssp-boost_system.patch
BuildRequires:	zlib-devel bzip2-devel boost-devel gcc-c++
BuildRequires: make

%if 0%{?epel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif

%description
The DSSP program standardizes protein secondary structure assignment.
DSSP is a database of secondary structure assignments (and much more)
for all protein entries in the Protein Data Bank (PDB).  DSSP is also
the program that calculates DSSP entries from PDB entries.  DSSP does
not predict secondary structure.

References:
"A series of PDB related databases for everyday needs.", Robbie
P. Joosten, Tim A.H. te Beek, Elmar Krieger, Maarten L. Hekkelman, Rob
W.W. Hooft, Reinhard Schneider, Chris Sander, and Gert Vriend.
Nucleic Acids Research 2011 January; 39(Database issue): D411-D419.
doi: 10.1093/nar/gkq1105

"Dictionary of protein secondary structure: pattern recognition of
hydrogen-bonded and geometrical features.", Kabsch W, Sander C,
Biopolymers. 1983 22 2577-2637.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .make
%patch -P2 -p1 -b .tuple
%patch -P3 -p1 -b .nullptr
%patch -P4 -p1 -b .boost_system
chmod -x src/buffer.h

%build
# This changed somewhere between EPEL6 and Fedora 21.
## Set Boost's library directories
if [ -f %{_libdir}/%{?el5:boost141/}libboost_thread-mt.so ]; then
  echo "BOOST_LIB_SUFFIX = -mt" > make.config
else
  echo "BOOST_LIB_SUFFIX = " > make.config
fi
echo "CFLAGS=$RPM_OPT_FLAGS -I/usr/include
LDOPTS=%__global_ldflags -L%_libdir" >>make.config
# The original makefile uses -O3, presumably for good reason, but
# avoid compiler ICE on ppc64le (#1280387).
%ifarch ppc64le
COPT=-O2 \
%endif
make %{?_smp_mflags}

%install
make install DEST_DIR=%_prefix DESTDIR=$RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%_mandir/man1/*

%{!?_licensedir:%global license %%doc}
%files
%license LICENSE_1_0.txt
%doc changelog README.txt
%_bindir/mkdssp
%_mandir/man1/mkdssp.1*

%changelog
%autochangelog
