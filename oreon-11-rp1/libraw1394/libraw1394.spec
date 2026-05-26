# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 03ccc69761d22c7deb1127fc301010dd13e70e44bb7134b8ff0d07590259a55e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
