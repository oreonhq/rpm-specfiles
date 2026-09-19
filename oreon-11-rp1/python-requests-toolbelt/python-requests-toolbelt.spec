%global source0_hash 0a052d9b5595718b7ec79c201e45e123dd3b9c6d659561479f24b7a2a85bbe81

%global srcname requests-toolbelt
%global altname requests_toolbelt

Name:           python-%{srcname}
Version:        1.0.0
Release:        15%{?dist}
Summary:        Utility belt for advanced users of python-requests

License:        Apache-2.0
URL:            https://toolbelt.readthedocs.io
Source0:        https://github.com/sigmavirus24/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This is just a collection of utilities for python-requests, but don’t really\
belong in requests proper.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%py_provides    python3-%{altname}
BuildRequires:  python3-devel
BuildRequires:  python3-betamax
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
Requires:       python3-requests

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n toolbelt-%{version}

# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
sed -i -E -e 's/^(\s*)import mock/\1from unittest import mock/' \
          -e 's/^(\s*)from mock import /\1from unittest.mock import /' \
    tests/*.py tests/*/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{altname}

%check
%pyproject_check_import

# Disable tests that need network access and those which are currently failing
py.test-%{python3_version} -v --ignore=tests/test_x509_adapter.py \
       -k "not test_downloadutils and not test_dump and not test_sessions"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.rst

%changelog
%autochangelog
