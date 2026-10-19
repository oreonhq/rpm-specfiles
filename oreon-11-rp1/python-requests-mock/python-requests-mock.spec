%global source0_hash e9e12e333b525156e82a3c852f22016b9158220d2f47454de9cae8a77d371401
%if %{defined el8}
%bcond_with tests
%else
%bcond_without tests
%endif
Name:           python-requests-mock
Version:        1.12.1
Release:        7%{?dist}
Summary:        Mock out responses from the requests package
License:        Apache-2.0
URL:            https://requests-mock.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/r/requests-mock/requests-mock-%{version}.tar.gz
Patch:          0003-Allow-skipping-purl-tests-if-it-is-not-present.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 56
Requires:       python3-requests-mock = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-requests-mock
Summary:        Mock out responses from the requests package
%description -n python3-requests-mock

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir requests-mock-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-mock usr/lib/python3*/site-packages/requests_mock* usr/lib64/python3*/site-packages/requests_mock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_mock* usr/lib64/python3*/site-packages/requests_mock* usr/bin/*

%check

%if %{with tests}
%pytest -v tests/pytest
%else
%pyproject_check_import -e requests_mock.contrib.fixture
%endif
%files
%files -n python3-requests-mock -f %{oreon_filedir}/python3-requests-mock.list

%changelog

%autochangelog
