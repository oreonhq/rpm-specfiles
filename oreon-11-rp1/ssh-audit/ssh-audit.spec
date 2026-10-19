%global source0_hash 618ec29801c3abefcef8bb8177f918dcba6b3542f0803ce510cd13bfcd13815d
Name:           ssh-audit
Version:        3.9.0
Release:        1%{?dist}
Summary:        An SSH server & client configuration security auditing tool
License:        MIT
URL:            https://github.com/jtesta/ssh-audit
Source0:        https://github.com/jtesta/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-ssh-audit = %{version}-%{release}
# /oreon:deps
%description
ssh-audit is an SSH server & client security auditing (banner, key exchange,
encryption, mac, compression, compatibility, security, etc)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup

#remove shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' src/ssh_audit/ssh_audit.py

%build

%pyproject_wheel
%install
%pyproject_install
install -t %{buildroot}%{_mandir}/man1 -Dpm 0644 ssh-audit.1
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
