%global source0_hash 3f6393c9e846d90c56a83c43fb6b803ca11ec4c6efbe53c94ce5b5c62aac3713

%global pypi_name testrepository

Name:           python-%{pypi_name}
Version:        0.0.22
Release:        1%{?dist}
Summary:        A repository of test results

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/testing-cabal/testrepository
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%package -n python3-%{pypi_name}
Summary:        A repository of test results (for Python 3)
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-subunit
BuildRequires:  python3-testtools
BuildRequires:  python3-extras
Requires:       python3-fixtures
Requires:       python3-subunit
Requires:       python3-testtools
Requires:       python3-extras

# Provide a clean upgrade path
Obsoletes:      python-%{pypi_name} < 0.0.20-20
Obsoletes:      python2-%{pypi_name} < 0.0.20-20

%description -n python3-%{pypi_name}
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

This package is for Python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
mv %{buildroot}%{_bindir}/testr{,-%{python3_version}}
ln -s ./testr-%{python3_version} %{buildroot}%{_bindir}/testr

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md Apache-2.0
%{_bindir}/testr
%{_bindir}/testr-%{python3_version}

%changelog
%autochangelog
