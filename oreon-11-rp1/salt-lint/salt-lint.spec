%global source0_hash 1dee5bb2872b435169193ebae63620b365d1715f28db6e89f3bf61fffa901458
Name:           salt-lint
Version:        0.9.2
Release:        1%{?dist}
Summary:        Salt State file (SLS) lint tool
License:        MIT
URL:            https://github.com/warpnet/salt-lint
Source0:        https://github.com/warpnet/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         00-remove-linter-deps.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-salt-lint = %{version}-%{release}
# /oreon:deps
%description
salt-lint checks Salt State files (SLS) for best practices and behavior that
could potentially be improved.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -Dpm 0644 docs/man/salt-lint.1 %{buildroot}%{_mandir}/man1/salt-lint.1
%oreon_autofiles main

%check

%tox
%files

%changelog

%autochangelog
