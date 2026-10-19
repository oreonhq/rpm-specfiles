%global source0_hash da185ee316d877021beb6395f2d80ced22a99c2876c42d54994e3bad3c3daf4d
Name:           python-testscenarios
Version:        0.7.0
Release:        1%{?dist}
Summary:        Testscenarios, a unittest extension for dependency injection
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/testing-cabal/testscenarios
Source0:        https://files.pythonhosted.org/packages/source/t/testscenarios/testscenarios-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-testscenarios = %{version}-%{release}
# /oreon:deps
%package -n       python3-testscenarios+test
Summary:        Metapackage for python3-testscenarios test extras
Requires:       python3-testscenarios = %{version}-%{release}
Requires:       python3dist(testtools) >= 2.8.7
Provides:       python3dist(testscenarios[test]) = %{version}-%{release}

%description -n python3-testscenarios+test
Metapackage for python3-testscenarios test extras.

%package -n       python3-testscenarios+dev
Summary:        Metapackage for python3-testscenarios dev extras
Requires:       python3-testscenarios = %{version}-%{release}
Requires:       python3dist(ruff) == 0.16.4
Requires:       python3dist(mypy) >= 1.20.0
Provides:       python3dist(testscenarios[dev]) = %{version}-%{release}

%description -n python3-testscenarios+dev
Metapackage for python3-testscenarios dev extras.

%description

%package -n     python3-testscenarios
Summary:        Testscenarios, a unittest extension for dependency injection
%description -n python3-testscenarios

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir testscenarios-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-testscenarios usr/lib/python3*/site-packages/testscenarios* usr/lib64/python3*/site-packages/testscenarios* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/testscenarios* usr/lib64/python3*/site-packages/testscenarios* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-testscenarios -f %{oreon_filedir}/python3-testscenarios.list

%changelog

%autochangelog
