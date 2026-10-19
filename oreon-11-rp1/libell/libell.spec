%global source0_hash 39a562f5ab2768e69da1ffbb1f98a8eb3483baffc7d2ef6adc3705e4fd4e53fb
Name:           libell
Version:        0.83
Release:        1%{?dist}
Summary:        Embedded Linux library
License:        LGPL-2.0-or-later
URL:            https://01.org/ell
Source0:        https://www.kernel.org/pub/linux/libs/ell/ell-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The Embedded Linux* Library (ELL) provides core, low-level functionality for
system daemons. It typically has no dependencies other than the Linux kernel, C
standard library, and libdl (for dynamic linking). While ELL is designed to be
efficient and compact enough for use on embedded Linux platforms, it is not
limited to resource-constrained systems.

%package devel
Summary:        Embedded Linux library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers for developing against libell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ell-%{version}
%oreon_prep
%build

%configure
%make_build V=1
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libell-devel -f %{oreon_filedir}/libell-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.83-1
- Prepare for Oreon 11 (RP1)
