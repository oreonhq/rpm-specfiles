#global candidate rc2

Name:          libi2cd
Version:       1.0.3
Release:       10%{?candidate:.%{candidate}}%{?dist}
Summary:       C library for interacting with linux I2C devices

License:       LGPL-2.1-or-later
URL:           https://github.com/sstallion/libi2cd/
Source0:       https://github.com/sstallion/libi2cd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: automake autoconf libtool
BuildRequires: gcc
BuildRequires: libcmocka-devel
BuildRequires: make

%description
libi2cd provides a simple and straightforward API for accessing I2C devices from
userspace. It relies on the i2c-dev Linux kernel module and is intended to
complement existing tools and libraries, such as those provided by i2c-tools.
It provides both high- and low-level access to the underlying ioctl requests.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q -n %{name}-%{version}%{?candidate:-%{candidate}}

%build
autoreconf -vif
%configure --disable-static

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/i2cd.h
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/libi2cd.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-10
- Prepare for Oreon 11 (RP1)
