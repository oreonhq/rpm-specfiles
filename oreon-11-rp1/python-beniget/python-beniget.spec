%global source0_hash 36db8ff9a129a026a1b0fb5e1c96a27c45e4400f03f71d696e08a7bbf56d01ff

Name:           python-beniget
Version:        0.4.2.post1
Release:        %autorelease
Summary:        Extract semantic information about static Python code
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/beniget/
Source0:        %{url}/archive/%{version}/beniget-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A static analyzer for Python2 and Python3 code.Beniget provides a static over-
approximation of the global and local definitions inside Python
Module/Class/Function. It can also compute def-use chains from each definition.}
%description %_description

%package -n     python3-beniget
Summary:        %{summary}

%description -n python3-beniget %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n beniget-%{version}

%generate_buildrequires
# Don't use tox options to avoid an unwanted dependency in RHEL
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files beniget

%check
# tox.ini has setup.py test, but that's deprecated
# use pytest, but beware the tests are not named test*.py
%pytest -v tests/*.py

%files -n python3-beniget -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
