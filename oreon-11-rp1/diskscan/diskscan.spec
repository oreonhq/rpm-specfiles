%global source0_hash e4d82e0c9f29435e0fffc95fe94efa8f3fafb2573b92d1cb3fb547bd3c40f693
Summary:        Scan disk for bad or near failure sectors, performs disk diagnostics
Name: diskscan
Version: 0.21
Release:        1%{?dist}
URL: https://github.com/baruch/diskscan
Source0:        https://github.com/baruch/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-version.patch
Patch1: %{name}-cmake-4.0.patch
License: Apache-2.0 AND BSD-3-Clause AND (BSD-2-Clause OR CC0-1.0) AND GPL-3.0-or-later
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  zlib-devel
# /oreon:deps
%description
DiskScan is a Unix/Linux tool to scan a block device and check if there are
unreadable sectors, in addition it uses read latency times as an assessment for
a near failure as sectors that are problematic to read usually entail many
retries. This can be used to assess the state of the disk and maybe decide on a
replacement in advance to its imminent failure. The disk self test may or may
not pick up on such clues depending on the disk vendor decision making logic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -GNinja
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
