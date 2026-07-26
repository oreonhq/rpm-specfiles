%global source0_hash e9e12e333b525156e82a3c852f22016b9158220d2f47454de9cae8a77d371401

%if %{defined el8}
# Disable tests on epel8 - dependencies dont exist.
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
Source:         %{pypi_source requests-mock}
Patch:          0003-Allow-skipping-purl-tests-if-it-is-not-present.patch
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-requests-futures
%endif

%global _description %{expand:
requests-mock provides a building block to stub out the HTTP requests portions
of your testing code. You should checkout the docs for more information.}

%description %_description

%package -n python3-requests-mock
Summary:        %{summary}

%description -n python3-requests-mock %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requests-mock-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x fixture}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files requests_mock

%check
%if %{with tests}
%pytest -v tests/pytest
%else
%pyproject_check_import -e requests_mock.contrib.fixture
%endif

%files -n python3-requests-mock -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
