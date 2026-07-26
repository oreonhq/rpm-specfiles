%global source0_hash dcdb08d97fd9e73203bab97d33216f9b69ca372e1e35ecd2a0f7c0a4332ca22c

# tests are enabled by default
%bcond_without tests

%global         srcname     google-cloud-testutils
%global         forgeurl    https://github.com/googleapis/python-test-utils
Version:        1.4.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python test utilities for Google Cloud APIs

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-google-auth

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This is a collection of common tools used in system tests of Python client
libraries for Google APIs.}

%description %{_description}

%package -n python3-%{srcname}
%py_provides    python3-test-utils
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files test_utils

# Remove extra scripts and tests.
rm %{buildroot}%{_bindir}/lower-bound-checker

%check
%pyproject_check_import -e "tests*"

%if %{with tests}
# Lower bounds checking tests won't work since installing things via
# pip is not going to work during RPM builds.
%pytest --disable-warnings --ignore tests/unit/test_lower_bound_checker.py
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md
%license LICENSE

%changelog
%autochangelog
