%global source0_hash 6b7fa262aebf73fae9edf5bc9e03b298710ac7a2034b51d78e30af04f533bccb
%{!?with_check: %global with_check 0}
Name:           python-pytest-subtests
Version:        0.15.0
Release:        1%{?dist}
Summary:        Support for unittest subTest() and subtests fixture
License:        MIT
URL:            https://github.com/pytest-dev/pytest-subtests
Source0:        https://github.com/pytest-dev/pytest-subtests/archive/v0.15.0/pytest-subtests-0.15.0.tar.gz#/python-pytest-subtests-0.15.0.tar.gz
%if %{undefined rhel} || (0%{?oreon} >= 11)
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2.3
Requires:       python3-pytest-subtests = %{version}-%{release}
# /oreon:deps
%description
pytest-subtests unittest subTest() support and subtests fixture.

%package -n     python3-pytest-subtests
Summary:        Support for unittest subTest() and subtests fixture
%description -n python3-pytest-subtests
%{summary}.

%prep
%global oreon_srcdir pytest-subtests-%{version}
%oreon_prep
%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%install
%pyproject_install
%oreon_autofiles python3-pytest-subtests usr/lib/python3*/site-packages/pytest_subtests* usr/lib64/python3*/site-packages/pytest_subtests* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_subtests* usr/lib64/python3*/site-packages/pytest_subtests* usr/bin/*

%check

%if %{with check}
python3 -m pytest -rs -v tests
%endif
%files
%files -n python3-pytest-subtests -f %{oreon_filedir}/python3-pytest-subtests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.0-1
- Import
