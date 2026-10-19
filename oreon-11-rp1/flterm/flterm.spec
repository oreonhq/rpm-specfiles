%global source0_hash 300c26b0da0b3b4cd228548496ff717b5387d8a5af033e8839eec574ec8f86e7
Name:           flterm
Version:        1.2
Release:        1%{?dist}
Summary:        Firmware download program
License:        GPL-3.0-only
URL:            http://milkymist.org
Source0:        https://github.com/milkymist/milkymist/archive/milkymist-Release_%{version}.tar.gz
Patch0:         flterm-1.2-use-rpm-opt-flags-debug-empty.patch
ExcludeArch:    s390 s390x sparcv9
# oreon:deps
BuildRequires:  clang
BuildRequires:  make
# /oreon:deps
%description
%{name} is a serial terminal, and firmware download program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n milkymist-Release_%{version}
%patch -P0 -p1 

%build

cd tools
make CC=gcc flterm
%install
install -d %{buildroot}%{_bindir}
install -p tools/flterm %{buildroot}%{_bindir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
