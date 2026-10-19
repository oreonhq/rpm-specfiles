%global source0_hash 43b695c90d888fee2e66365a01d508aa5792727d7968892d790cebc0dd79afc9
%bcond tests 1
Name:           python-pytest-split
Summary:        Pytest plugin to split the test suite into sub-suites
Version:        0.11.0
Release:        1%{?dist}
License:         MIT
URL:             https://github.com/jerry-git/pytest-split
Source0:        https://github.com/jerry-git/pytest-split/archive/refs/tags/%{version}/pytest-split-%{version}.tar.gz
BuildArch:       noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-pytest-split = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pytest-split
Summary:        Pytest plugin to split the test suite into sub-suites
%description -n python3-pytest-split

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest-split-%{version}
# Remove pytest configuration to avoid dependency on coverage (pytest-cov)
tomcli set pyproject.toml del 'tool.pytest.ini_options'

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH="%{buildroot}%{python3_sitelib}" help2man \
    --version-string %{version} \
    %{buildroot}%{_bindir}/slowest-tests | \
    gzip > %{buildroot}%{_mandir}/man1/slowest-tests.1.gz
%oreon_autofiles python3-pytest-split usr/lib/python3*/site-packages/pytest_split* usr/lib64/python3*/site-packages/pytest_split* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_split* usr/lib64/python3*/site-packages/pytest_split* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%pytest tests
%endif
%files
%files -n python3-pytest-split -f %{oreon_filedir}/python3-pytest-split.list

%changelog

%autochangelog
