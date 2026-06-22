%global source0_hash 482ab530ea066dde980b2a9991749b3a721c2e70603a9fd957d454f0022f27e8

%bcond_without check

Name:           python-pytest-regressions
Version:        2.11.0
Release:        1%{?dist}
Summary:        Pytest fixtures for writing regression tests
License:        MIT
URL:            https://pytest-regressions.readthedocs.io/
Source0:        https://github.com/ESSS/pytest-regressions/archive/v%{version}/pytest-regressions-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
This pytest plugin makes it simple to test general data, images, files, and
numeric tables by saving expected data in a data directory (courtesy of
pytest-datadir) that can be used to verify that future runs produce the same
data.}

%description %_description

%package -n     python3-pytest-regressions
Summary:        %{summary}

%description -n python3-pytest-regressions %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n pytest-regressions-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x num,image,dataframe

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_regressions

%if %{with check}
%check
if [ "$(uname -m)" = s390x ]; then
  sed -i 's/int64/<i8/' tests/test_ndarrays_regression.py
fi
%pyproject_check_import
%pytest
%endif

%files -n python3-pytest-regressions -f %{pyproject_files}
%doc CHANGELOG.rst README.rst
%license LICENSE

%changelog
%autochangelog
