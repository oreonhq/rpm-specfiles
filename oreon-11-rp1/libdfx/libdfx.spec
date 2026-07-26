%global source0_hash 1ec5738b8d94e76440a700c45d93db89ad083d9b9b8bf5ca4ecfb1bdee9ad347

Name:    libdfx
Version: 2025.2
Release: 3%{?dist}
Summary: A lightweight user-space library that provides APIs to configure the PL
License: MIT
URL:     https://github.com/Xilinx/libdfx
Source:  %{url}/archive/refs/tags/xilinx_v%{version}.tar.gz#/%{name}-xilinx_v%{version}.tar.gz

ExcludeArch: %{ix86}
BuildRequires: cmake
BuildRequires: gcc-g++

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

%autosetup -p1 -n %{name}-xilinx_v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%{_libdir}/libdfx.so.1*

%files devel
%{_includedir}/libdfx.h
%{_libdir}/libdfx.so

%files static
%{_libdir}/libdfx.a

%changelog
%autochangelog
