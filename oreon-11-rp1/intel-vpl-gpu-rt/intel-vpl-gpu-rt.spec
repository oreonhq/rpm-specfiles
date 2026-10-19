%global source0_hash 876c76714e891a44b1da7aad122318059bfedd17a5f4d2b3123efeca35aa0144
Name:           intel-vpl-gpu-rt
Version:        26.1.0
Release:        1%{?dist}
Summary:        Intel Video Processing Library (Intel VPL) GPU Runtime
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64
Source0:        https://github.com/intel/vpl-gpu-rt/archive/intel-onevpl-%{version}/intel-onevpl-%{version}.tar.gz
Requires:       libvpl%{?_isa} >= 1:2.10.1
Obsoletes:      oneVPL-intel-gpu < %{version}-%{release}
Provides:       oneVPL-intel-gpu = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
# /oreon:deps
%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel GPUs.
Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir vpl-gpu-rt-intel-onevpl-%{version}
%oreon_prep
%build

%cmake -DMFX_ENABLE_AENC=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n intel-vpl-gpu-rt-devel -f %{oreon_filedir}/intel-vpl-gpu-rt-devel.list

%changelog

%autochangelog
