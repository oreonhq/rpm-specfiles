%global source0_hash 7e7e93de0e94a42314300ef6d15dd2c44c64ef74b7c749243bc226be2ab90687
Name:           python-pypresence
Version:        4.6.2
Release:        1%{?dist}
Summary:        Discord RPC client written in Python
License:        MIT
URL:            https://github.com/qwertyquerty/pypresence
Source0:        https://files.pythonhosted.org/packages/source/p/pypresence/pypresence-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-pypresence = %{version}-%{release}
# /oreon:deps
%package -n       python3-pypresence+dev
Summary:        Metapackage for python3-pypresence dev extras
Requires:       python3-pypresence = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0.0
Requires:       python3dist(pytest-asyncio) >= 0.21.0
Requires:       python3dist(pytest-mock) >= 3.10.0
Requires:       python3dist(pytest-cov) >= 4.0.0
Requires:       python3dist(black) >= 23.0.0
Requires:       python3dist(flake8) >= 6.0.0
Requires:       python3dist(mypy) >= 1.0.0
Requires:       python3dist(isort) >= 5.12.0
Requires:       python3dist(sphinx) >= 5.0.0
Requires:       python3dist(sphinx-rtd-theme) >= 1.2.0
Provides:       python3dist(pypresence[dev]) = %{version}-%{release}

%description -n python3-pypresence+dev
Metapackage for python3-pypresence dev extras.

%description

%package -n     python3-pypresence
Summary:        Discord RPC client written in Python
%description -n python3-pypresence

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pypresence-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pypresence usr/lib/python3*/site-packages/pypresence* usr/lib64/python3*/site-packages/pypresence* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pypresence* usr/lib64/python3*/site-packages/pypresence* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pypresence -f %{oreon_filedir}/python3-pypresence.list

%changelog

%autochangelog
