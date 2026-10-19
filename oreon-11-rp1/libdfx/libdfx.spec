%global source0_hash 1ec5738b8d94e76440a700c45d93db89ad083d9b9b8bf5ca4ecfb1bdee9ad347
Name:    libdfx
Version: 2025.2
Release:        1%{?dist}
Summary:        A lightweight user-space library that provides APIs to configure the PL
License: MIT
URL:     https://github.com/Xilinx/libdfx
Source0:        https://github.com/Xilinx/%{name}/archive/refs/tags/xilinx_v%{version}.tar.gz#/%{name}-xilinx_v%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-g++
# /oreon:deps
%description
The library is a lightweight user-space library that provides APIs
for application to configure the PL (programable logic) AKA FPGA.

%package devel
Summary: Development files for using PL (programable logic)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header and static library files for
development applications using PL (programable logic).

%package static
Summary: Static libraries for using PL (programable logic)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
This package contains the static library files for %{name}
for building PL (programable logic) applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-xilinx_v%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libdfx-devel -f %{oreon_filedir}/libdfx-devel.list
%files -n libdfx-static -f %{oreon_filedir}/libdfx-static.list

%changelog

%autochangelog
