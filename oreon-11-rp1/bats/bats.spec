%global source0_hash none

%global         upstreamname  bats-core

Name:           bats
Version:        1.13.0
Release:        %autorelease
Summary:        Bash Automated Testing System

License:        MIT
URL:            https://github.com/%{upstreamname}/%{upstreamname}
Source:         https://github.com/%{upstreamname}/%{upstreamname}/archive/v%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildArch:      noarch

Requires:       bash
Requires:       parallel
BuildRequires:  parallel
BuildRequires:  procps-ng

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

%check
./bin/bats test

%files
%doc AUTHORS README.md docs/CHANGELOG.md
%license LICENSE.md
%{_bindir}/%{name}
%{_libexecdir}/%{upstreamname}
%{_prefix}/lib/%{upstreamname}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man7/%{name}.7.gz

%changelog
%autochangelog

