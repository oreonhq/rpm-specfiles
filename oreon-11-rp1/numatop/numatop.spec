%global source0_hash c312d4b6cc10d12680aa8ff04db5a02fca7b39a5494b0f41d280a7e1772db9c8
Name:           numatop
Version:        2.5.1
Release:        1%{?dist}
Summary:        Memory access locality characterization and analysis
License:        BSD-3-Clause
URL:            https://01.org/numatop
Source0:        https://github.com/intel/numatop/archive/refs/tags/v%{version}.tar.gz#/numatop-2.5.1.tar.gz
ExclusiveArch:  x86_64 ppc64le
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel
# /oreon:deps
%description
NumaTOP is an observation tool for runtime memory locality characterization and
analysis of processes and threads running on a NUMA system. It helps the user
characterize the NUMA behavior of processes and threads and identify where the
NUMA-related performance bottlenecks reside.

NumaTOP supports the Intel Xeon processors, AMD Zen processors and PowerPC
processors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf --force --install --symlink
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.1-1
- Import
