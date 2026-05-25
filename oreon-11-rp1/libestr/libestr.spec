Name:           libestr
Version:        0.1.11
Release:        13%{?dist}
Summary:        String handling essentials library

License:        LGPL-2.1-or-later
URL:            http://libestr.adiscon.com/
Source0:        http://libestr.adiscon.com/files/download/libestr-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf automake libtool
%description
This package compiles the string handling essentials library
used by the Rsyslog daemon.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The package contains libraries and header files for
developing applications that use libestr.

%prep
%setup -q

%build
%configure --disable-static --with-pic
V=1 make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README AUTHORS ChangeLog
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libestr.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libestr.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.11-13
- Import
