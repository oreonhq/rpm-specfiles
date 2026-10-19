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
%if %{with check}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-regressions = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-regressions
Summary:        Pytest fixtures for writing regression tests
%description -n python3-pytest-regressions

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-regressions-%{version}
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-regressions usr/lib/python3*/site-packages/pytest_regressions* usr/lib64/python3*/site-packages/pytest_regressions* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_regressions* usr/lib64/python3*/site-packages/pytest_regressions* usr/bin/*
%if %{with check}
%check

if [ "$(uname -m)" = s390x ]; then
  sed -i 's/int64/<i8/' tests/test_ndarrays_regression.py
fi
%pyproject_check_import
%pytest
%endif
%files
%files -n python3-pytest-regressions -f %{oreon_filedir}/python3-pytest-regressions.list

%changelog

%autochangelog
