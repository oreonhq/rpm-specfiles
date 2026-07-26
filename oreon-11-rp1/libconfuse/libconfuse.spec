%global source0_hash 3a59ded20bc652eaa8e6261ab46f7e483bc13dad79263c15af42ecbb329707b8

Name:           libconfuse
Version:        3.3
Release:        16%{?dist}
Summary:        A configuration file parser library

License:        ISC
URL:            https://github.com/martinh/libconfuse
Source0:	https://github.com/martinh/libconfuse/releases/download/v%{version}/confuse-%{version}.tar.gz

Patch0:         d73777c2c3566fb2647727bb56d9a2295b81669b.patch

BuildRequires:  gcc
BuildRequires:  check-devel, pkgconfig
BuildRequires:  perl-interpreter
BuildRequires: make

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

%patch -P0 -p0

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags} AM_CFLAGS="-Wall -Wextra"

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
# Nuke libtool archive(s)
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# Install man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
cp -p doc/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3/
# Extract the example sources
mkdir -p ex2/examples
cp -p examples/{ftpconf.c,ftp.conf,simple.c,simple.conf,reread.c,reread.conf} \
    ex2/examples/

#Remove spurious docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/confuse

%find_lang confuse

%ldconfig_scriptlets

%files -f confuse.lang
%license LICENSE
%doc AUTHORS README.md
%doc doc/html
%{_libdir}/libconfuse.so.2*
%{_mandir}/man?/*.*

%files devel
%doc ex2/examples
%{_includedir}/confuse.h
%{_libdir}/libconfuse.so
%{_libdir}/pkgconfig/libconfuse.pc

%changelog
%autochangelog
