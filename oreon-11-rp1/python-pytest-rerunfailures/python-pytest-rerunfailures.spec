%global source0_hash a77d9ed50f0b26ee0480f4e5092cb5b2ae9f069f45fe13f603d264353ce36c65

%global srcname pytest-rerunfailures

# Needed for Python bootstrap
%bcond_without tests

Name:           python-%{srcname}
Version:        16.6.1
Release:        1%{?dist}
Summary:        A py.test plugin that re-runs failed tests to eliminate flakey failures

License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-rerunfailures
Source0:        https://github.com/pytest-dev/pytest-rerunfailures/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
pytest-rerunfailures is a plugin for py.test that re-runs tests to eliminate
intermittent failures.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_rerunfailures

%if %{with tests}
%check
%pytest tests
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
