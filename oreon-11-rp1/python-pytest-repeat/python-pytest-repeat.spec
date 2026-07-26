%global source0_hash 010d114890c7efc1652ed1c6d7f736534a15005c9db5383c7e6695e293b1ad74

%global srcname pytest-repeat

Name:           python-%{srcname}
Version:        0.9.3
Release:        10%{?dist}
Summary:        A pytest plugin for repeating test execution

License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-repeat
Source0:        https://github.com/pytest-dev/pytest-repeat/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
pytest-repeat is a plugin for py.test that makes it easy to repeat a single
test, or multiple tests, a specific number of times.
}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_buildrequires

%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_wheel

%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_install
%pyproject_save_files pytest_repeat

%check
%pytest test_repeat.py

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.rst README.rst

%changelog
%autochangelog
