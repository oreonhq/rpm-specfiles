%global source0_hash 537512904744b35e232912055ccf8ec66d768639ff3abe5788d90d792ec5f48b
%global _vpath_srcdir build/meson
Name:           lz4
Version:        1.10.0
Release:        1%{?dist}
Summary:        Extremely fast compression algorithm
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://lz4.github.io/lz4/
Source0:        https://github.com/lz4/lz4/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Obsoletes:      %{name} < 1.7.5-3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
# /oreon:deps
%description
LZ4 is an extremely fast loss-less compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-core CPU. It also features
an extremely fast decoder, with speed in multiple GB/s per core, typically
reaching RAM speed limits on multi-core systems.

%package        libs
Summary:        Libaries for lz4
Obsoletes:      %{name} < 1.7.5-3
%description    libs
This package contains the libaries for lz4.

%package        devel
Summary:        Development files for lz4
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This package contains the header(.h) and library(.so) files required to build
applications using liblz4 library.

%package        static
Summary:        Static library for lz4
%description    static
LZ4 is an extremely fast loss-less compression algorithm. This package
contains static libraries for static linking of applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -Dprograms=true \
  -Ddefault_library=both \
  %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lz4-libs -f %{oreon_filedir}/lz4-libs.list
%files -n lz4-devel -f %{oreon_filedir}/lz4-devel.list
%files -n lz4-static -f %{oreon_filedir}/lz4-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.0-4
- Prepare for Oreon 11 (RP1)
