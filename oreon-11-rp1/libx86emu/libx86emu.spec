%global source0_hash 03754aede79530baa0e862e1aad5527e9c1bd3371736b1ab5a2bc769e4a3d680
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%global make_flags \\\
        LIBDIR=%{_libdir} \\\
        GIT2LOG=: \\\
        VERSION=%%{version} \\\
        MAJOR_VERSION=%%(echo %{version} |cut -d. -f1) \\\
        CFLAGS="-fPIC %{optflags}" \\\
        LDFLAGS="-fPIC %{__global_ldflags}"
Name:           libx86emu
Version:        3.7
Release:        3%{?dist}
Summary:        x86 emulation library
License:        HPND-sell-variant
URL:            https://github.com/wfeldt/libx86emu
Source0:        https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Small x86 emulation library with focus of easy usage and extended execution
logging functions. The library features an API to create emulation objects
for x86 architecture.

%package devel
Summary:        Development files for libx86emu
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and libraries for developing with libx86emu, a x86 emulation
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build %{make_flags} shared
%ldconfig_scriptlets
%install
%make_install %{make_flags}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libx86emu-devel -f %{oreon_filedir}/libx86emu-devel.list

%changelog

%autochangelog
