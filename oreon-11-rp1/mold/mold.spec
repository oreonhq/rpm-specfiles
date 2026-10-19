%global source0_hash 0580221bfdad7148ceeafd0ad3c1c7b3ca9e66b45950405230cc3f81a205c816
%global use_gcc_toolset 0%{?el8}
%global use_system_tbb  0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%global has_32bit_support 0%{?rhel} < 10
Name:           mold
Version:        2.42.1
Release:        1%{?dist}
Summary:        A Modern Linker
License:        MIT AND (Apache-2.0 OR MIT)
URL:            https://github.com/rui314/mold
Source0:        https://github.com/rui314/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Use-system-compatible-include-path-for-xxhash.h.patch
%if %{use_gcc_toolset}
%else
%endif
%if %{use_system_tbb}
%else
Provides:       bundled(tbb) = 2022.1
%endif
%if ! 0%{?el8}
%ifarch x86_64
%if %{has_32bit_support}
%endif
%endif
%endif
Requires(post): alternatives
Requires(postun): alternatives
# oreon:deps
BuildRequires:  blake3-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  glibc-static
BuildRequires:  libdwarf-tools
BuildRequires:  libstdc++-static
BuildRequires:  libzstd-devel
BuildRequires:  llvm
BuildRequires:  mimalloc-devel
BuildRequires:  perl-interpreter
BuildRequires:  tbb-devel
BuildRequires:  xxhash-static
BuildRequires:  zlib-devel
# /oreon:deps
%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than the LLVM lld linker.
mold is designed to increase developer productivity by reducing
build time, especially in rapid debug-edit-rebuild cycles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
rm -r third-party/{blake3,mimalloc,xxhash,zlib,zstd}
%if %{use_system_tbb}
rm -r third-party/tbb
%endif

%build

%if %{use_gcc_toolset}
. /opt/rh/gcc-toolset-13/enable
%endif
%if %{use_system_tbb}
%define tbb_flags -DMOLD_USE_SYSTEM_TBB=ON
%endif
%cmake -DMOLD_USE_SYSTEM_MIMALLOC=ON %{?tbb_flags}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%post

if [ "$1" = 1 ]; then
  update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.mold 1
fi
%postun

if [ "$1" = 0 ]; then
  update-alternatives --remove ld %{_bindir}/ld.mold
fi
%check

%if %{use_gcc_toolset}
. /opt/rh/gcc-toolset-13/enable
%endif
%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
