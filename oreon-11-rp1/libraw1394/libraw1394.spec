%global source0_hash 03ccc69761d22c7deb1127fc301010dd13e70e44bb7134b8ff0d07590259a55e
Summary:        Library providing low-level IEEE-1394 access - 2.1.2-
Name:           libraw1394
Version:        2.1.2
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
Source0:        http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.xz
URL:            http://www.dennedy.org/libraw1394/
ExcludeArch:    s390 s390x
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libraw1394.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libraw1394-devel -f %{oreon_filedir}/libraw1394-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.2-25
- Prepare for Oreon 11 (RP1)
