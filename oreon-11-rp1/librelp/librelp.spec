Summary: The Reliable Event Logging Protocol library
Name: librelp
Version: 1.12.0
Release: 1%{?dist}
License: GPL-3.0-or-later
URL: http://www.rsyslog.com/
Source0: http://download.rsyslog.com/%{name}/%{name}-%{version}.tar.gz

%description
Librelp is an easy to use library for the RELP protocol. RELP (stands
for Reliable Event Logging Protocol) is a general-purpose, extensible
logging protocol.

%package devel
Summary: Development files for the %{name} package
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: gnutls-devel >= 1.4.0
BuildRequires: openssl-devel

%description devel
Librelp is an easy to use library for the RELP protocol. The
librelp-devel package contains the header files and libraries needed
to develop applications using librelp.

%prep
%autosetup -p1

%build
autoreconf -ivf
%configure --disable-static --enable-tls --enable-tls-openssl
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING NEWS README doc/*html
%{_libdir}/librelp.so.*

%files devel
%{_includedir}/*
%{_libdir}/librelp.so
%{_libdir}/pkgconfig/relp.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.0-1
- Import
