%global source0_hash 92f668d43b51b87952b26be45c0fb1eef325e3bf76a1a2cecc8d2b8a05fc3c8a

Summary: A Python client for the Akamai Fast Purge API
Name: python-fastpurge
Version: 1.0.5
Release: %autorelease
URL: https://github.com/release-engineering/python-fastpurge
# PyPI tarball doesn't have tests
Source: %{url}/archive/v%{version}/fastpurge-%{version}.tar.gz
License: GPL-3.0-or-later
BuildArch: noarch

# https://github.com/release-engineering/python-fastpurge/pull/34
Patch: 0001-Use-unittest.mock-on-Python-3.3.patch

%global _description %{expand:
This library provides a simple asynchronous Python wrapper for the Fast
Purge API, including authentication and error recovery.}

%description %_description

%package -n python3-fastpurge
Summary:	%{summary}
BuildRequires:	python3-devel

%description -n python3-fastpurge %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n python-fastpurge-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -e '/bandit/d' -i test-requirements.txt

%generate_buildrequires
%pyproject_buildrequires test-requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fastpurge

%check
%pytest -v

%files -n python3-fastpurge -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md

%changelog
%autochangelog
