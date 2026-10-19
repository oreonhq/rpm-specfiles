%global source0_hash 8b0fa586f0d23688b15b94714812f9048ca255d64906d06746084189bf536c86
%undefine _cmake_shared_libs
Summary:        AMDGPU Userspace Register Debugger
Name: umr
Version: 1.0.11
Release:        1%{?dist}
License: MIT
URL: https://gitlab.freedesktop.org/tomstdenis/umr
Source0:        https://gitlab.freedesktop.org/tomstdenis/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
%global disablellvm 1
%global disablelibdrm 1
Requires: bash-completion
ExclusiveArch:  x86_64 aarch64 ppc64le
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpciaccess-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  nanomsg-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
AMDGPU Userspace Register Debugger (UMR) is a tool to read and display, as well
as write to AMDGPU device MMIO, PCIE, SMC, and DIDT registers via userspace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{!?cmake:%global cmake %%cmake3}
%cmake %{?disablellvm:-DUMR_NO_LLVM=ON} \
        %{?disablelibdrm:-DUMR_NO_DRM=ON} \
        %{?enablert:-DUMR_NEED_RT=ON} \
        -DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build
%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
