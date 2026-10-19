%global source0_hash c01ce99d4b86a99ef83fb75ddc97ddd7669eb85996a2c35bc9ad9e83ecad47bc
Name: realtime-tests
Summary:        Programs that test various rt-features
Version: 2.11
Release:        1%{?dist}
License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-or-later
URL: https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git
Source0:        https://www.kernel.org/pub/linux/utils/rt-tests/rt-tests-%{version}.tar.xz
ExcludeArch: %{arm}
Requires: bash
Requires: bc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
realtime-tests is a set of programs that test and measure various components of
real-time kernel behavior. This package measures timer, signal, and hardware
latency. It also tests the functioning of priority-inheritance mutexes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rt-tests-%{version}
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install prefix=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
