%global source0_hash bb537b70b15b732f6d8827dd6578e3d8ce166636ce1f18ea9a074184fcce9177
%global         upstreamname  bats-core
Name:           bats
Version:        1.14.0
Release:        1%{?dist}
Summary:        Bash Automated Testing System
License:        MIT
URL:            https://github.com/%{upstreamname}/%{upstreamname}
Source0:        https://github.com/%{upstreamname}/%{upstreamname}/archive/v%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       parallel
# oreon:deps
BuildRequires:  parallel
BuildRequires:  procps-ng
# /oreon:deps
%description
Bats is a TAP-compliant testing framework for Bash. It provides a simple way to
verify that the UNIX programs you write behave as expected. Bats is most useful
when testing software written in Bash, but you can use it to test any UNIX
program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname}-%{version} -p1

%install
./install.sh ${RPM_BUILD_ROOT}%{_prefix}
%oreon_autofiles main

%check

./bin/bats test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

