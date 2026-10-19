%global source0_hash 6faaa0ac942d388bbabfac8840949a0548d351400005adca008df6291ee99819
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 riscv64
%global arch_has_asan 1
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 riscv64
%global arch_has_ubsan 1
%endif
%ifarch x86_64 ppc64 ppc64le aarch64 s390x riscv64
%global arch_has_tsan 1
%endif
%bcond asan 0%{?arch_has_asan:1}
%bcond ubsan 0%{?arch_has_ubsan:1}
%bcond tsan 0%{?arch_has_tsan:1}
Name:           wlcs
Version:        1.8.1
Release:        1%{?dist}
Summary:        Wayland Conformance Test Suite
License:        GPL-3.0-only AND (LGPL-2.0-only OR LGPL-3.0-only)
SourceLicense:  %{shrink:
                %{license} AND
                (GPL-2.0-only OR GPL-3.0-only) AND
                GPL-2.0-or-later AND
                HPND-sell-variant AND
                MIT
                }
URL:            https://github.com/MirServer/wlcs
Source0:        https://github.com/MirServer/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with asan}
%endif
%if %{with ubsan}
%endif
%if %{with tsan}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
# /oreon:deps
%description
wlcs aspires to be a protocol-conformance-verifying test suite usable by
Wayland compositor implementors.

It is growing out of porting the existing Weston test suite to be run in Mir’s
test suite, but it is designed to be usable by any compositor.

wlcs relies on compositors providing an integration module, providing wlcs with
API hooks to start a compositor, connect a client, move a window, and so on.

This makes both writing and debugging tests easier - the tests are (generally)
in the same address space as the compositor, so there is a consistent global
clock available, it’s easier to poke around in compositor internals, and
standard debugging tools can follow control flow from the test client to the
compositor and back again.

%package        devel
Summary:        Development files for wlcs
Requires:       wlcs%{?_isa} = %{version}-%{release}
%description    devel
wlcs aspires to be a protocol-conformance-verifying test suite usable by
Wayland compositor implementors.

The wlcs-devel package contains libraries and header files for developing
Wayland compositor tests that use wlcs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
# WLCS_FATAL_COMPILE_WARNINGS: makes sense for upstream CI, but too strict for
#                              downstream packaging
%cmake \
    -DWLCS_BUILD_ASAN=%{?with_asan:ON}%{?!with_asan:OFF} \
    -DWLCS_BUILD_TSAN=%{?with_tsan:ON}%{?!with_tsan:OFF} \
    -DWLCS_BUILD_UBSAN=%{?with_ubsan:ON}%{?!with_ubsan:OFF} \
    -DWLCS_FATAL_COMPILE_WARNINGS:BOOL=OFF \
    -GNinja

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n wlcs-devel -f %{oreon_filedir}/wlcs-devel.list

%changelog

%autochangelog
