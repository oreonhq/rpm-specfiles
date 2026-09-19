%global source0_hash 6cff0ff8394c553549ac7433359ccfc955fb26794260314620dfa5e4cd4b727f

Summary:        Random number generator tester and timer
Name:           dieharder
Version:        3.31.1
Release:        45%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        http://www.phy.duke.edu/~rgb/General/%{name}/%{name}-%{version}.tgz
URL:            http://www.phy.duke.edu/~rgb/General/dieharder.php
Patch0:         dieharder-3.31.1_urandom_64bit.patch 
Patch1:         dieharder-3.31.1_aarch64.patch
Patch2:         dieharder-3.31.1_BZ1100855.patch
Patch3:         dieharder-3.31.1_autoconf_c99.patch

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
# Needed for building manual
BuildRequires:  texlive-latex
BuildRequires:  latex2html

BuildRequires:  gsl-devel
BuildRequires: make automake autoconf libtool

%define _legacy_common_support 1

%description 
dieharder is a fairly involved random number/uniform deviate generator
tester.  It can either test any of its many pre-built and linked
generators (basically all of those in the Gnu Scientific Library plus
some others) or a potentially random data-set in a file.  With file
input, it can manage either a variety of ASCII-formatted input or a raw
binary bit string.  It is thus suitable for use in testing both software
RNG's and hardware RNG's.

dieharder does all of its work with a standalone, extensible library,
libdieharder. Therefore its tests can be integrated into other programs.

dieharder encapsulates following random number tests: George Marsaglia's
"Diehard" battery of tests, STS (v1.6) from NIST FIPS, Knuth's tests,
and more.  Check the documentation for complete list of the tests and
references where possible. It is intended to be the "Swiss army knife of
random number testers", or "the last suite of random number testers
you'll ever wear".

########################################################################
# LIBRARY: This is the basic dieharder library
########################################################################

%package libs
Summary:        A library of random number generator tests and timing routines

%description libs

libdieharder is the core library of dieharder designed to be "the last
suite of random number testers you'll ever wear".  It can test any of
its many pre-built and library linked generators (basically all of those
in the Gnu Scientific Library plus a number of others from various
sources) or a potentially random data-set in either an ASCII-formatted
or raw (presumed 32 bit unsigned int) binary file.  It is fairly
straightforward to wrap new software generators for testing, or to add
hardware generators that have a software interface for testing, and the
file input method permits pretty much any software or hardware RNG to be
tested using libdieharder calls.

libdieharder has as a design goal the full encapsulation in an
extensible shell of basically all the random number tests: George
Marsaglia's "Diehard" battery of tests, STS (v1.6) from NIST FIPS,
Knuth's tests, and more.  Check the documentation for complete list.  

%package devel
Summary: A library of random number generator tests and timing routines
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}

########################################################################
# The main section common to all builds.
########################################################################
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -vi
%configure
###SMP build is not working
###make %{?_smp_mflags} V=1
make V=1

# Build pdf manual
pushd manual
make

%check
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
rm -rf %{buildroot}%{_libdir}/libdieharder.la
rm -rf %{buildroot}%{_libdir}/libdieharder.a

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -p ChangeLog Copyright README COPYING NOTES %{name}.html manual/%{name}.pdf %{buildroot}%{_defaultdocdir}/%{name}

########################################################################
# Command to execute post install or uninstall of libdieharder
########################################################################
%ldconfig_scriptlets libs

########################################################################
# Files installed with the dieharder tty UI
########################################################################
%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_defaultdocdir}/*

%files libs
%{_libdir}/*.so.*
%{_mandir}/man3/lib%{name}.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so

%changelog
%autochangelog
