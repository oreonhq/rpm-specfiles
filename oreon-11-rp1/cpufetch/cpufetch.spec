%global source0_hash dc3ec8f9c9d41d8434702a778cc150b196d5d178fd768a964f57d22f268a2c17
Name: cpufetch
Summary:        Simple tool for determining CPU architecture
License: GPL-2.0-only
Version: 1.07
Release:        1%{?dist}
URL: https://github.com/Dr-Noob/cpufetch
Source0:        https://github.com/Dr-Noob/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch1: 0001-L2-cache-may-not-exist.patch
Patch2: 0002-ppc-variable-name.patch
ExclusiveArch: %{arm} aarch64 x86_64 ppc ppc64 ppc64le %{riscv}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
%{name} is a simple, yet fancy, CPU architecture fetching tool.
It currently supports x86_64 CPUs (both Intel and AMD), ARM, and PowerPC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install
rm %{buildroot}%{_datadir}/licenses/cpufetch-git/LICENSE
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/%{name} --debug
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
