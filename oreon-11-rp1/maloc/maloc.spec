%global source0_hash 58e1197fcd4c74d3cbb1d39d712eb0a3c5886a1e6629f22c5c78ce2bac983fc0

Name: maloc
Version: 1.5
Release: 35%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.fetk.org
Summary: Minimal Abstraction Layer for Object-oriented C
Source0: http://www.fetk.org/codes/download/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: libtool
BuildRequires: readline-devel

# removes hardcoded libdir setting
Patch0: maloc-makefile.am.patch

%description
MALOC is a small, portable, abstract C environment library for
object-oriented C programming. MALOC is used as the foundation layer
for a number of scientific applications, including MC, SG, and
APBS. MALOC can be used as a small stand-alone abstraction environment
for writing portable C programs which need access to resources which
are typically architecture-dependent, such as INET sockets, timing
routines, and so on. MALOC provides abstract datatypes, memory
management routines, timing routines, machine epsilon, access to UNIX
and INET sockets, MPI, and so on. All things that can vary from one
architecture to another are abstracted out of an application code and
placed in MALOC.

%package devel
Summary: Header files and library for developing programs with maloc
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel

This package contains libraries and header files needed for program
development using MALOC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p0

aclocal
libtoolize --automake
autoconf
automake --gnu --add-missing
autoheader

%build
%configure --disable-static
%make_build

make maloc_doc -C doc/doxygen

%install
%make_install

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0.0

%files devel
%doc doc/api/html/*
%{_libdir}/*.so
%{_includedir}/maloc/

%changelog
%autochangelog
