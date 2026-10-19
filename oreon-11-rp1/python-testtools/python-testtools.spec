%global source0_hash 39ad9eb9e1b935d6838f4b3aee4d6e72db65df5602f6feda998dbb4fe8de0b19
Name:           python-testtools
Version:        2.9.1
Release:        1%{?dist}
Summary:        Extensions to the Python standard library unit testing framework
License:        MIT
URL:            https://github.com/testing-cabal/testtools
Source0:        https://files.pythonhosted.org/packages/source/t/testtools/testtools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-testtools = %{version}-%{release}
# /oreon:deps
%package -n       python3-testtools+test
Summary:        Metapackage for python3-testtools test extras
Requires:       python3-testtools = %{version}-%{release}
Provides:       python3dist(testtools[test]) = %{version}-%{release}

%description -n python3-testtools+test
Metapackage for python3-testtools test extras.

%package -n       python3-testtools+twisted
Summary:        Metapackage for python3-testtools twisted extras
Requires:       python3-testtools = %{version}-%{release}
Provides:       python3dist(testtools[twisted]) = %{version}-%{release}

%description -n python3-testtools+twisted
Metapackage for python3-testtools twisted extras.

%package -n       python3-testtools+dev
Summary:        Metapackage for python3-testtools dev extras
Requires:       python3-testtools = %{version}-%{release}
Requires:       python3dist(ruff) == 0.15.9
Requires:       python3dist(mypy) >= 1.20.0
Provides:       python3dist(testtools[dev]) = %{version}-%{release}

%description -n python3-testtools+dev
Metapackage for python3-testtools dev extras.

%description

%package -n     python3-testtools
Summary:        Extensions to the Python standard library unit testing framework
%description -n python3-testtools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir testtools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-testtools usr/lib/python3*/site-packages/testtools* usr/lib64/python3*/site-packages/testtools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/testtools* usr/lib64/python3*/site-packages/testtools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-testtools -f %{oreon_filedir}/python3-testtools.list

%changelog

%autochangelog
