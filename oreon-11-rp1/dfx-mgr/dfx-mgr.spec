%global source0_hash 6e55859936277fc8e0a1ae05a9844a74992f3be4a1da1299270b145b62dee093

Name:    dfx-mgr
Version: 2025.2
Release: 3%{?dist}
Summary: A tool for managing programable logic accelerators
License: MIT
URL:     https://github.com/Xilinx/dfx-mgr
Source:  %{url}/archive/refs/tags/xilinx_v%{version}.tar.gz#/%{name}-xilinx_v%{version}.tar.gz

ExcludeArch: %{ix86}
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libdfx-devel
BuildRequires: libdrm-devel
BuildRequires: systemd-devel

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

%autosetup -p1 -n %{name}-xilinx_v%{version}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/accel*
%{_bindir}/dfx-mgr*
%{_bindir}/load_accel*
%{_libdir}/libdfx-mgr.so.*

%files devel
%{_libdir}/libdfx-mgr.a
%{_libdir}/libdfx-mgr.so

%changelog
%autochangelog
