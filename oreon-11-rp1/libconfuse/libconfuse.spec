%global source0_hash d98a793f4cafc1b3c18e2509ba54f6cb9ac6291b181bcda152dc987cb78f43ec
Name:           libconfuse
Version:        3.4
Release:        1%{?dist}
Summary:        A configuration file parser library
License:        ISC
URL:            https://github.com/martinh/libconfuse
Source0:        https://github.com/martinh/libconfuse/releases/download/v%{version}/confuse-%{version}.tar.gz
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
# /oreon:deps
%description
libConfuse is a configuration file parser library, licensed under
the terms of the ISC license, and written in C. It supports
sections and (lists of) values (strings, integers, floats,
booleans or other sections), as well as some other features (such
as single/double-quoted strings, environment variable expansion,
functions and nested include statements). It makes it very
easy to add configuration file capability to a program using
a simple API.

The goal of libConfuse is not to be the configuration file parser
library with a gazillion of features. Instead, it aims to be
easy to use and quick to integrate with your code.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n confuse-%{version}
perl -pi.orig -e 's|confuse.h|../src/confuse.h|g' tests/check_confuse.c

%build

%configure --enable-shared --disable-static
make %{?_smp_mflags} AM_CFLAGS="-Wall -Wextra"
%check

make check
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
cp -p doc/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3/
mkdir -p ex2/examples
cp -p examples/{ftpconf.c,ftp.conf,simple.c,simple.conf,reread.c,reread.conf} \
    ex2/examples/
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/confuse
%find_lang confuse
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libconfuse-devel -f %{oreon_filedir}/libconfuse-devel.list

%changelog

%autochangelog
