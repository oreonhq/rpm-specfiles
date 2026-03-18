Summary:        Library providing low-level IEEE-1394 access - 2.1.2-
Name:           libraw1394
Version:        2.1.2
Release:        25%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Source:         http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.xz
URL:            http://www.dennedy.org/libraw1394/
ExcludeArch:    s390 s390x
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires: make

%description
The libraw1394 library provides direct access to the IEEE-1394 bus.
Support for both the obsolete ieee1394 interface and the new firewire
intererface are included, with run-time detection of the active stack.

%package devel
Summary:        Development libs for libraw1394
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development libraries needed to build applications against libraw1394.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libraw1394.la

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc README NEWS
%{_bindir}/dumpiso
%{_bindir}/sendiso
%{_bindir}/testlibraw
%{_libdir}/libraw1394.so.*
%{_mandir}/man1/dumpiso.1*
%{_mandir}/man1/sendiso.1*
%{_mandir}/man1/testlibraw.1*
%{_mandir}/man5/isodump.5*

%files devel
%doc doc/libraw1394.sgml
%{_includedir}/libraw1394/
%{_libdir}/libraw1394.so
%{_libdir}/pkgconfig/libraw1394.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.2-25
- Prepare for Oreon 11 (RP1)
