%global source0_hash 6e55859936277fc8e0a1ae05a9844a74992f3be4a1da1299270b145b62dee093
Name:    dfx-mgr
Version: 2025.2
Release:        3%{?dist}
Summary:        A tool for managing programable logic accelerators
License: MIT
URL:     https://github.com/Xilinx/dfx-mgr
Source0:        https://github.com/Xilinx/%{name}/archive/refs/tags/xilinx_v%{version}.tar.gz#/%{name}-xilinx_v%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libdfx-devel
BuildRequires:  libdrm-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
DFX-MGR provides infrastructure to abstract configuration and
hardware resource management for dynamic deployment of Xilinx
based accelerators (AKA FPGA) across different platforms.

%package devel
Summary: Development files for using PL (programable logic)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel
%description devel
This package contains the header and static library files for
development applications using PL (programable logic).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-xilinx_v%{version}
%oreon_prep
%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dfx-mgr-devel -f %{oreon_filedir}/dfx-mgr-devel.list

%changelog

%autochangelog
