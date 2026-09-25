%global source0_hash 04598b0fba9e3fa290f27e4f8d1762a9d61b75f1e38b53e9d8d861af53eb0d2a

Name:           python-pam
Version:        2.1.0
Release:        1%{?dist}
Summary:        Pure Python interface to the Pluggable Authentication Modules system on Linux
License:        MIT
URL:            https://github.com/FirefighterBlu3/python-pam
Source0:        https://files.pythonhosted.org/packages/source/p/python_pam/python_pam-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

# https://github.com/FirefighterBlu3/python-pam/pull/49
# Don't ship pam/pam.py, which appears to be solely a footgun
# https://github.com/FirefighterBlu3/python-pam/pull/47
# Drop use of six, we haven't supported Python 2 for years
# This was an undeclared dependency, seems better to drop it
# than declare it
# Modified to correct the indent issue and drop changes to pam.py
# since the prior patch demotes it to an example
# https://github.com/FirefighterBlu3/python-pam/pull/50
# Do not require wheel for building
# The dependency is not necessary and is undesired in RHEL;
# upstream has closed the PR and switched to poetry-core instead,
# but that change is more disruptive to backport (and also undesired in RHEL).


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
%autosetup -p1 -n python_pam-%{version}

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
%autochangelog
