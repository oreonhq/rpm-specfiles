%global source0_hash 97235235ba9b82dbae8068d1099508455949b275f77273ca22fdbd8b1fb5d950

Name:           python-pam
Version:        2.0.2
Release:        18%{?dist}
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
License:        MIT
URL:            https://github.com/FirefighterBlu3/python-pam
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

# https://github.com/FirefighterBlu3/python-pam/pull/49
# Don't ship pam/pam.py, which appears to be solely a footgun
Patch:        https://github.com/FirefighterBlu3/python-pam/pull/50.patch
# https://github.com/FirefighterBlu3/python-pam/pull/47
# Drop use of six, we haven't supported Python 2 for years
# This was an undeclared dependency, seems better to drop it
# than declare it
# Modified to correct the indent issue and drop changes to pam.py
# since the prior patch demotes it to an example
Patch:        https://github.com/FirefighterBlu3/python-pam/pull/50.patch
# https://github.com/FirefighterBlu3/python-pam/pull/50
# Do not require wheel for building
# The dependency is not necessary and is undesired in RHEL;
# upstream has closed the PR and switched to poetry-core instead,
# but that change is more disruptive to backport (and also undesired in RHEL).
Patch:          https://github.com/FirefighterBlu3/python-pam/pull/50.patch


%generate_buildrequires
%pyproject_buildrequires

%description
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%package -n python3-pam
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
%{?python_provide:%python_provide python3-pam}

%description -n python3-pam
This module provides an authenticate function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pam

%check
%pyproject_check_import

%files -n python3-pam -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.2-18
- Prepare for Oreon 11 (RP1)
