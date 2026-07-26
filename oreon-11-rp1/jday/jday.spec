%global source0_hash 3b15f3a1b552ffae7c343bd47bf89e8073da9ef8c2ec6d79b90d56f8c3a06fda

Name:		jday
Version:        2.4
Release:        %autorelease
Summary:        A simple command to convert calendar dates to julian dates
License:        BSD-3-Clause
URL:            http://sourceforge.net/projects/jday/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch:		configure.patch

# https://bugzilla.redhat.com/797815
Conflicts: netatalk

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  gcc-c++
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:  make

%description
A simple command to convert calendar dates to julian dates. Quite
useful in timing situations where you need elapsed time between dates.
Also useful for astronomy applications.

%package devel
Summary:        Development files for jday
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains library and header files for developing applications that use
jday.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch

%build
autoreconf --install
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc ChangeLog README AUTHORS NEWS
%{_bindir}/dbd
%{_bindir}/j2d
%{_bindir}/jday
%{_mandir}/man1/jday.1*
%{_libdir}/libjday.so.2.0.4
%{_libdir}/libjday.so.2

%files devel
%{_includedir}/jday.h
%{_libdir}/libjday.so
%{_libdir}/pkgconfig/jday.pc

%changelog
%autochangelog
