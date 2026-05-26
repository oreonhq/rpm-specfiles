Summary: A file compression and packaging utility compatible with PKZIP
Name: zip
Version: 3.0
Release: 45%{?dist}
License: Info-ZIP
Source: http://downloads.sourceforge.net/infozip/zip30.tar.gz
URL: http://www.info-zip.org/Zip.html

# This patch will probably be merged to zip 3.1
# http://www.info-zip.org/board/board.pl?m-1249408491/
Patch1: zip-3.0-exec-shield.patch
# Not upstreamed.
Patch2: zip-3.0-currdir.patch
# Not upstreamed.
Patch3: zip-3.0-time.patch
Patch4: man.patch
Patch5: zip-3.0-format-security.patch
Patch6: zipnote.patch
Patch7: zip-gnu89-build.patch
Patch8: buffer_overflow.patch
Patch9: zip-3.0-man-strip-extra.patch
# oreon url source checksums begin
%global source0_sha256 f0e8bb1f9b7eb0b01285495a2699df3a4b766784c1765a8f1aeedf63c0806369
%global source0_file zip30.tar.gz
# oreon url source checksums end
BuildRequires: make
BuildRequires: bzip2-devel, gcc
Requires: unzip

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/zip30.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f0e8bb1f9b7eb0b01285495a2699df3a4b766784c1765a8f1aeedf63c0806369" || { echo "oreon: Source0 SHA256 mismatch for zip30.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n zip30
%patch -P1 -p1 -b .exec-shield
%patch -P2 -p1 -b .currdir
%patch -P3 -p1 -b .time
%patch -P4 -p1 -b .man
%patch -P5 -p1 -b .format-security
%patch -P6 -p1 -b .zipnote
%patch -P7 -p1 -b .gnu89-build
%patch -P8 -p1
%patch -P9 -p1

%build
%{make_build} -f unix/Makefile prefix=%{_prefix} "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS" generic_gcc

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

%{make_install} -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} \
        MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%files
%license LICENSE
%doc README CHANGES TODO WHATSNEW WHERE README.CR
%doc proginfo/algorith.txt
%{_bindir}/zipnote
%{_bindir}/zipsplit
%{_bindir}/zip
%{_bindir}/zipcloak
%{_mandir}/man1/zip.1*
%{_mandir}/man1/zipcloak.1*
%{_mandir}/man1/zipnote.1*
%{_mandir}/man1/zipsplit.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-45
- Prepare for Oreon 11 (RP1)
