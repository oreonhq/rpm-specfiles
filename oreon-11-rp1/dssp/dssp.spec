%global source0_hash 25d39a2107767b622a59dd9fa790112c1516564b8518fc6ac0fab081d5ac3ab0
Name:		dssp
Version:	3.0.0
Release:        1%{?dist}
Summary:        Protein secondary structure assignment
%{?el5:Group:		Applications/Engineering}
License:	BSL-1.0
URL:		http://swift.cmbi.ru.nl/gv/dssp/
Source0:        ftp://ftp.cmbi.ru.nl/pub/software/%{name}/%{name}-%{version}.tgz
Patch1:		dssp-make.patch
Patch2:		dssp-tuple.patch
Patch3:         dssp-nullptr.patch
Patch4:         dssp-boost_system.patch
%if 0%{?epel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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

if [ -f %{_libdir}/%{?el5:boost141/}libboost_thread-mt.so ]; then
  echo "BOOST_LIB_SUFFIX = -mt" > make.config
else
  echo "BOOST_LIB_SUFFIX = " > make.config
fi
echo "CFLAGS=$RPM_OPT_FLAGS -I/usr/include
LDOPTS=%__global_ldflags -L%_libdir" >>make.config
%ifarch ppc64le
COPT=-O2 \
%endif
make %{?_smp_mflags}
%install
make install DEST_DIR=%_prefix DESTDIR=$RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%_mandir/man1/*
%{!?_licensedir:%global license %%doc}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
