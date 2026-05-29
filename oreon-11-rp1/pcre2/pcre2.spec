%global source0_hash none

# Add readline edditing in pcre2test tool
%bcond_without pcre2_enables_readline

# Disable SELinux-frindly JIT allocator because it seems not to be fork-safe,
# https://bugs.exim.org/show_bug.cgi?id=1749#c45
%bcond_with pcre2_enables_sealloc

# This is stable release:
#%%global rcversion RC1
Name:       pcre2
Version:    10.47
Release:    %{?rcversion:0.}1%{?rcversion:.%rcversion}%{?dist}.1
%global     myversion %{version}%{?rcversion:-%rcversion}
Summary:    Perl-compatible regular expression library
# the library:                          BSD with exceptions
# pcre2test (linked to GNU readline):   BSD (linked to GPLv3+)
# COPYING:                              see LICENCE file
# LICENSE:                              BSD text with exceptions and
#                                       Public Domain declaration
#                                       for testdata
#Bundled
# src/sljit:                            BSD
#Not distributed in any binary package
# aclocal.m4:                           FSFULLR and GPLv2+ with exception
# ar-lib:                               GPLv2+ with exception
# cmake/COPYING-CMAKE-SCRIPTS:          BSD
# compile:                              GPLv2+ with exception
# config.guess:                         GPLv3+ with exception
# config.sub:                           GPLv3+ with exception
# configure:                            FSFUL and GPLv2+ with exception
# depcomp:                              GPLv2+ with exception
# INSTALL:                              FSFAP
# install-sh:                           MIT
# ltmain.sh:                            GPLv2+ with exception and (MIT or GPLv3+)
# m4/ax_pthread.m4:                     GPLv3+ with exception
# m4/libtool.m4:                        FSFUL and FSFULLR and
#                                       GPLv2+ with exception
# m4/ltoptions.m4:                      FSFULLR
# m4/ltsugar.m4:                        FSFULLR
# m4/ltversion.m4:                      FSFULLR
# m4/lt~obsolete.m4:                    FSFULLR
# m4/pcre2_visibility.m4:               FSFULLR
# Makefile.in:                          FSFULLR
# missing:                              GPLv2+ with exception
# test-driver:                          GPLv2+ with exception
# testdata:                             Public Domain
License:    BSD-3-Clause AND FSFULLR AND X11 AND GPL-2.0-or-later AND FSFAP AND FSFUL AND GPL-3.0-or-later
URL:        https://www.pcre.org/
Source0:        https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.47/pcre2-10.47%{?rcversion:-%rcversion}.tar.bz2
Source1:        https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.47/pcre2-10.47%{?rcversion:-%rcversion}.tar.bz2.sig
# This New-Public-Key was retrieved using
# gpg --keyserver keyserver.ubuntu.com --recv-keys A95536204A3BB489715231282A98E77EB6F24CA8
# gpg --export --armor A95536204A3BB489715231282A98E77EB6F24CA8 > New-Public-Key
# The GPG key changed with the new upstream maintainer
# More in https://github.com/PCRE2Project/pcre2/blob/master/SECURITY.md
Source2:        https://ftp.pcre.org/pub/pcre/New-Public-Key
# Do no set RPATH if libdir is not /usr/lib
Patch0:     pcre2-10.10-Fix-multilib.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
%if %{with pcre2_enables_readline}
BuildRequires:  readline-devel
%endif
BuildRequires:  sed
Requires:       %{name}-syntax = %{version}-%{release}
Provides:       bundled(sljit)

%description
PCRE2 is a re-working of the original PCRE (Perl-compatible regular
expression) library to provide an entirely new API.

PCRE2 is written in C, and it has its own API. There are three sets of
functions, one for the 8-bit library, which processes strings of bytes, one
for the 16-bit library, which processes strings of 16-bit values, and one for
the 32-bit library, which processes strings of 32-bit values. There are no C++
wrappers. This package provides support for strings in 8-bit and UTF-8
encodings. Install %{name}-utf16 or %{name}-utf32 packages for the other ones.

The distribution does contain a set of C wrapper functions for the 8-bit
library that are based on the POSIX regular expression API (see the pcre2posix
man page). These can be found in a library called libpcre2posix. Note that
this just provides a POSIX calling interface to PCRE2; the regular expressions
themselves still follow Perl syntax and semantics. The POSIX API is
restricted, and does not give full access to all of PCRE2's facilities.

%package utf16
Summary:    UTF-16 variant of PCRE2
Provides:   bundled(sljit)
Requires:   %{name}-syntax = %{version}-%{release}
Conflicts:  %{name}%{?_isa} < 10.21-4

%description utf16
This is PCRE2 library working on UTF-16 strings.

%package utf32
Summary:    UTF-32 variant of PCRE2
Provides:   bundled(sljit)
Requires:   %{name}-syntax = %{version}-%{release}
Conflicts:  %{name}%{?_isa} < 10.21-4

%description utf32
This is PCRE2 library working on UTF-32 strings.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-utf16%{?_isa} = %{version}-%{release}
Requires:   %{name}-utf32%{?_isa} = %{version}-%{release}

%description devel
Development files (headers, libraries for dynamic linking, documentation)
for %{name}.  The header file for the POSIX-style functions is called
pcre2posix.h.

%package static
Summary:    Static library for %{name}
Requires:   %{name}-devel%{_isa} = %{version}-%{release}
Provides:   bundled(sljit)

%description static
Library for static linking for %{name}.

%package syntax
Summary:    Documentation for PCRE2 regular expressions
BuildArch:  noarch
Conflicts:  %{name}-devel < 10.34-8

%description syntax
This is a set of manual pages that document a syntax of the regular
expressions implemented by the PCRE2 library.

%package tools
Summary:    Auxiliary utilities for %{name}
# pcre2test:   BSD
License:    BSD-3-Clause
Requires:   %{name}%{_isa} = %{version}-%{release}
Requires:   %{name}-utf32 = %{version}-%{release}
Requires:   %{name}-utf16 = %{version}-%{release}

%description tools
Utilities demonstrating PCRE2 capabilities like pcre2grep or pcre2test.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{myversion} -p1
# Because of multilib patch
libtoolize --copy --force
autoreconf -vif

%build
# There is a strict-aliasing problem on PPC64, bug #881232
%ifarch ppc64
%global optflags %{optflags} -fno-strict-aliasing
%endif
%configure \
%ifarch s390 sparc64 sparcv9
    --disable-jit \
    --disable-pcre2grep-jit \
%else
    --enable-jit \
    --enable-pcre2grep-jit \
%endif
    --disable-bsr-anycrlf \
    --disable-coverage \
    --disable-ebcdic \
    --disable-fuzz-support \
%if %{with pcre2_enables_sealloc}
    --enable-jit-sealloc \
%else
    --disable-jit-sealloc \
%endif
    --disable-never-backslash-C \
    --enable-newline-is-lf \
    --enable-pcre2-8 \
    --enable-pcre2-16 \
    --enable-pcre2-32 \
    --enable-pcre2grep-callout \
    --enable-pcre2grep-callout-fork \
    --disable-pcre2grep-libbz2 \
    --disable-pcre2grep-libz \
    --disable-pcre2test-libedit \
%if %{with pcre2_enables_readline}
    --enable-pcre2test-libreadline \
%else
    --disable-pcre2test-libreadline \
%endif
    --enable-percent-zt \
    --disable-rebuild-chartables \
    --enable-shared \
    --disable-silent-rules \
    --enable-static \
    --enable-unicode \
    --disable-valgrind
%{make_build}

%install
%{make_install}
# Get rid of unneeded *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# These are handled by %%doc in %%files
rm -rf $RPM_BUILD_ROOT%{_docdir}/pcre2

%check
make %{?_smp_mflags} check VERBOSE=yes

%files
%{_libdir}/libpcre2-8.so.0*
%{_libdir}/libpcre2-posix.so.3*

%files utf16
%{_libdir}/libpcre2-16.so.0*

%files utf32
%{_libdir}/libpcre2-32.so.0*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{_mandir}/man1/pcre2-config.*
%{_mandir}/man3/pcre2_*
%{_mandir}/man3/pcre2api.*
%{_mandir}/man3/pcre2build.*
%{_mandir}/man3/pcre2callout.*
%{_mandir}/man3/pcre2convert.*
%{_mandir}/man3/pcre2demo.*
%{_mandir}/man3/pcre2jit.*
%{_mandir}/man3/pcre2posix.*
%{_mandir}/man3/pcre2sample.*
%{_mandir}/man3/pcre2serialize*
%{_bindir}/pcre2-config
%doc doc/*.txt doc/html
%doc README HACKING ./src/pcre2demo.c

%files static
%{_libdir}/*.a
%license COPYING LICENCE.md

%files syntax
%license COPYING LICENCE.md
%doc AUTHORS.md ChangeLog NEWS
%{_mandir}/man3/pcre2.*
%{_mandir}/man3/pcre2compat.*
%{_mandir}/man3/pcre2limits.*
%{_mandir}/man3/pcre2matching.*
%{_mandir}/man3/pcre2partial.*
%{_mandir}/man3/pcre2pattern.*
%{_mandir}/man3/pcre2perform.*
%{_mandir}/man3/pcre2syntax.*
%{_mandir}/man3/pcre2unicode.*

%files tools
%{_bindir}/pcre2grep
%{_bindir}/pcre2test
%{_mandir}/man1/pcre2grep.*
%{_mandir}/man1/pcre2test.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.47-1
- Prepare for Oreon 11 (RP1)
