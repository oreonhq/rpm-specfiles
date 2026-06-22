%global source0_hash 437f55a4e0c1b01a4f3077cc470e6991d47430970e36fbcb77e2be0df4fc1cd6

Name:           python-cachetools
Version:        7.1.4
Release:        %autorelease
Summary:        Extensible memoizing collections and decorators

# SPDX
License:        MIT
URL:            https://pypi.python.org/pypi/cachetools
Source:         %{pypi_source cachetools}

BuildArch:      noarch
BuildRequires:  python3-devel

# cachetools is a direct runtime dependency of tox,
# so we don't use tox to generate test dependencies or run tests
BuildRequires:  python3-pytest

%global _description\
This module provides various memoizing collections and decorators,\
including a variant of the Python 3 Standard Library @lru_cache\
function decorator.\
\
This module provides multiple cache implementations based on different\
cache algorithms, as well as decorators for easily memoizing function\
and method calls.\


%description %_description

%package -n python3-cachetools
Summary:        %{summary}

%description -n python3-cachetools %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cachetools-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cachetools

%check
%pytest

%files -n python3-cachetools -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
