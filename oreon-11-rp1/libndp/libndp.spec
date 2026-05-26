Name: libndp
Version: 1.9
Release: 5%{?dist}
Summary: Library for Neighbor Discovery Protocol
License: LGPL-2.1-or-later
URL: http://www.libndp.org/
Source: http://www.libndp.org/files/libndp-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a8ab214e01dc3a9b615276905395637f391298c84d77651f0cbf0b1082dd2dd4
%global source0_file libndp-1.9.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires: make
%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%package devel
Summary: Libraries and header files for libndp development
Requires: libndp = %{version}-%{release}

%description devel
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libndp-1.9.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a8ab214e01dc3a9b615276905395637f391298c84d77651f0cbf0b1082dd2dd4" || { echo "oreon: Source0 SHA256 mismatch for libndp-1.9.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name \*.la -delete

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*so.*
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-5
- Prepare for Oreon 11 (RP1)
