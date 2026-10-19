%global source0_hash f2672a0381cb59196e9c246bf8bcc43d5568bc457700a697f1a1df762b9af884
Name:		numactl
Summary:        Library for tuning for Non Uniform Memory Access machines
Version:	2.0.19
Release:        4%{?dist}
License:	GPL-2.0-only
URL:		https://github.com/numactl/numactl
Source0:        https://github.com/numactl/numactl/releases/download/v2.0.19/numactl-2.0.19.tar.gz
ExcludeArch: s390 %{arm}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Simple NUMA policy support. It consists of a numactl program to run
other programs with a specific NUMA policy.

%package libs
Summary: libnuma libraries
License: LGPL-2.1-only and GPL-2.0-only
%description libs
numactl-libs provides libnuma, a library to do allocations with
NUMA policy in applications.

%package devel
Summary: Development package for building Applications that use numa
Requires: %{name}-libs = %{version}-%{release}
License: LGPL-2.1-only and GPL-2.0-only
%description devel
Provides development headers for numa library calls

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --prefix=/usr --libdir=%{_libdir}
%make_build
%install
rm -rf $RPM_BUILD_ROOT
%make_install
%ldconfig_scriptlets
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n numactl-libs -f %{oreon_filedir}/numactl-libs.list
%files -n numactl-devel -f %{oreon_filedir}/numactl-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.19-4
- Prepare for Oreon 11 (RP1)
