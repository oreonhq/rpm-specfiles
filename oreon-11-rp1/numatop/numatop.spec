Name:           numatop
Version:        2.5.1
Release:        %autorelease
Summary:        Memory access locality characterization and analysis

License:        BSD-3-Clause
URL:            https://01.org/numatop
Source:         https://github.com/intel/numatop/archive/refs/tags/v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 c312d4b6cc10d12680aa8ff04db5a02fca7b39a5494b0f41d280a7e1772db9c8
%global source0_file v2.5.1.tar.gz
# oreon url source checksums end

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  check-devel
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel

# This only works for Intel and Power CPUs
ExclusiveArch:  x86_64 ppc64le


%description
NumaTOP is an observation tool for runtime memory locality characterization and
analysis of processes and threads running on a NUMA system. It helps the user
characterize the NUMA behavior of processes and threads and identify where the
NUMA-related performance bottlenecks reside.

NumaTOP supports the Intel Xeon processors, AMD Zen processors and PowerPC
processors.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v2.5.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c312d4b6cc10d12680aa8ff04db5a02fca7b39a5494b0f41d280a7e1772db9c8" || { echo "oreon: Source0 SHA256 mismatch for v2.5.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
autoreconf --force --install --symlink
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.1-1
- Import
