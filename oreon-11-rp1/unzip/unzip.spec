# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 036d96991646d0449ed0aa952e4fbe21b476ce994abc276e49d30e686708bd37
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Settings for EL <= 7
%if 0%{?rhel} && 0%{?rhel} <= 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif

Summary: A utility for unpacking zip files
Name: unzip
Version: 6.0
Release: 69%{?dist}
License: Info-ZIP
Source: http://downloads.sourceforge.net/infozip/unzip60.tar.gz

# Not sent to upstream.
Patch1: unzip-6.0-bzip2-configure.patch
# Upstream plans to do this in zip (hopefully also in unzip).
Patch2: unzip-6.0-exec-shield.patch
# Upstream plans to do similar thing.
Patch3: unzip-6.0-close.patch
# Details in rhbz#532380.
# Reported to upstream: http://www.info-zip.org/board/board.pl?m-1259575993/
Patch4: unzip-6.0-attribs-overflow.patch
# Not sent to upstream, as it's Fedora/RHEL specific.
# Modify the configure script to accept var LFLAGS2 so linking can be configurable
# from the spec file. In addition '-s' is still removed as before
Patch5: unzip-6.0-configure.patch
Patch6: unzip-6.0-manpage-fix.patch
# Update match.c with recmatch() from zip 3.0's util.c
# This also resolves the license issue in that old function.
# Original came from here: https://projects.parabolagnulinux.org/abslibre.git/plain/libre/unzip-libre/match.patch
Patch7: unzip-6.0-fix-recmatch.patch
# Update process.c
Patch8: unzip-6.0-symlink.patch
# change using of macro "case_map" by "to_up"
Patch9: unzip-6.0-caseinsensitive.patch
# downstream fix for "-Werror=format-security"
# upstream doesn't want hear about this option again
Patch10: unzip-6.0-format-secure.patch

Patch11: unzip-6.0-valgrind.patch
Patch12: unzip-6.0-x-option.patch
Patch13: unzip-6.0-overflow.patch
Patch14: unzip-6.0-cve-2014-8139.patch
Patch15: unzip-6.0-cve-2014-8140.patch
Patch16: unzip-6.0-cve-2014-8141.patch
Patch17: unzip-6.0-overflow-long-fsize.patch

# Fix heap overflow and infinite loop when invalid input is given (#1260947)
Patch18: unzip-6.0-heap-overflow-infloop.patch

# support non-{latin,unicode} encoding
Patch19: unzip-6.0-alt-iconv-utf8.patch
Patch20: unzip-6.0-alt-iconv-utf8-print.patch
Patch21: 0001-Fix-CVE-2016-9844-rhbz-1404283.patch

# restore unix timestamp accurately
Patch22: unzip-6.0-timestamp.patch

# fix possible heap based stack overflow in passwd protected files
Patch23: unzip-6.0-cve-2018-1000035-heap-based-overflow.patch

Patch24: unzip-6.0-cve-2018-18384.patch

# covscan issues
Patch25: unzip-6.0-COVSCAN-fix-unterminated-string.patch

Patch26: unzip-zipbomb-part1.patch
Patch27: unzip-zipbomb-part2.patch
Patch28: unzip-zipbomb-part3.patch
Patch29: unzip-zipbomb-manpage.patch
Patch30: unzip-zipbomb-part4.patch
Patch31: unzip-zipbomb-part5.patch
Patch32: unzip-zipbomb-part6.patch
Patch33: unzip-zipbomb-part7.patch
Patch34: unzip-zipbomb-switch.patch

Patch35: unzip-gnu89-build.patch
Patch36: unzip-6.0-wcstombs-fortify.patch
URL: http://infozip.sourceforge.net
BuildRequires: make
BuildRequires:  bzip2-devel, gcc

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%oreon_verify_sources
%setup -q -n unzip60
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1
%patch -P21 -p1
%patch -P22 -p1
%patch -P23 -p1
%patch -P24 -p1
%patch -P25 -p1

%patch -P26 -p1
%patch -P27 -p1
%patch -P28 -p1
%patch -P29 -p1
%patch -P30 -p1
%patch -P31 -p1
%patch -P32 -p1
%patch -P33 -p1
%patch -P34 -p1
%patch -P35 -p1
%patch -P36 -p1

%build
# IZ_HAVE_UXUIDGID is needed for right functionality of unzip -X
# NOMEMCPY solve problem with memory overlapping - decompression is slowly,
# but successfull.
%make_build -f unix/Makefile CF_NOOPT="-I. -DUNIX $RPM_OPT_FLAGS -DNOMEMCPY -DIZ_HAVE_UXUIDGID -DNO_LCHMOD" \
                      LFLAGS2="%{?__global_ldflags}" generic_gcc

%install
make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 INSTALL="cp -p" install

%files
%license LICENSE COPYING.OLD
%doc README BUGS
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0-69
- Prepare for Oreon 11 (RP1)
