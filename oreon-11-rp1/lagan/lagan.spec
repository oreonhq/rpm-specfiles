%global source0_hash a65e61ed4fd6608f4e5ad5b11a1b77f4fec1a207d822c5885b3e86727496e1fe

Name:           lagan
Version:        2.0
Release:        46%{?dist}
Summary:        Local, global, and multiple alignment of DNA sequences

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://lagan.stanford.edu
Source0:        http://lagan.stanford.edu/lagan_web/lagan20.tar.gz
Patch0:         lagan20-chris.patch
Patch1:         lagan20-gcc10.patch
Patch2:         lagan-c99.patch
BuildRequires:  perl-generators
BuildRequires:  gcc-c++
BuildRequires: make

%description
LAGAN toolkit is a set of tools for local, global, and multiple alignment of
DNA sequences.  Please visit http://lagan.stanford.edu for publications
describing LAGAN and its components.

The 4 main parts of LAGAN are:

1. CHAOS local alignment tool
2. LAGAN pairwise global alignment tool
3. MLAGAN multiple global alignment tool.
4. Shuffle-LAGAN pairwise global alignment

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lagan20
%patch -P0 -p1 -b .chris
%patch -P1 -p1 -b .gcc10
%patch -P2 -p1

sed -i 's/^CC .*$/CC = gcc $(RPM_OPT_FLAGS)/;
        s/^CPP .*$/CPP = g++ $(RPM_OPT_FLAGS)/' Makefile
sed -i 's|getenv ("LAGAN_DIR")|"%_libdir/lagan"|g' src/*.c src/utils/*.c
sed -i 's|getenv ("LAGAN_DIR")|"%_libdir/lagan"|g' src/utils/*.cpp
sed -i 's|$ENV{LAGAN_DIR}|"%_libdir/lagan"|g' *.pl src/*.pl utils/*.pl src/utils/*.pl
sed -i 's|$LAGAN_DIR|%_libdir/lagan|g' Readmes/README.shuffle src/*.c
sed -i 's/getline/GetLine/g' src/anchors.c
sed -i 's/^inline /inline __attribute__ ((always_inline)) /' src/fchaos.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/filebuffer.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/utils/scorecontigs.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/utils/overlay.c
sed -i '/<stdio.h>/a#include <ctype.h>' src/utils/cstat.c
sed -i 's/^int indeces/extern int indeces/' src/thrtrie.h
sed -i '/^int nnodes=0;/aint indeces[256];' src/thrtrie.c
rm prolagan
chmod -x src/glocal/*

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir $RPM_BUILD_ROOT/%_libdir/lagan/utils
install -m755 chaos ${RPM_BUILD_ROOT}%{_bindir}
install -m755 mlagan ${RPM_BUILD_ROOT}%{_bindir}
install -m755 prolagan ${RPM_BUILD_ROOT}%{_bindir}
install -m755 lagan.pl ${RPM_BUILD_ROOT}%{_bindir}/lagan
install -m755 slagan.pl ${RPM_BUILD_ROOT}%{_bindir}/slagan
for f in anal_gloc.pl anchors glocal order rechaos.pl \
  supermap.pl xmfa2mfa.pl; do
  install -m755 $f $RPM_BUILD_ROOT/%_libdir/lagan
done
for f in bin2bl bin2mf cextract cmerge2.pl contigorder cstat dotplot \
  draft.pl fa2xfa getbounds getcontigpos getlength getoverlap Glue \
  mextract.pl mf2bin.pl mpretty.pl mproject.pl mrunfile.pl mrunpairs.pl \
  mrun.pl mviz.pl rc scorealign scorecontigs seqmerge overlay; do
  install -m755 utils/$f $RPM_BUILD_ROOT/%_libdir/lagan/utils
done
install -m644 *.txt *.score $RPM_BUILD_ROOT/%_libdir/lagan
rm -f Readmes/*.chris

%files
%doc Readmes/* sample.*
%_bindir/chaos
%_bindir/lagan
%_bindir/mlagan
%_bindir/slagan
%_bindir/prolagan
%_libdir/lagan/

%changelog
%autochangelog
