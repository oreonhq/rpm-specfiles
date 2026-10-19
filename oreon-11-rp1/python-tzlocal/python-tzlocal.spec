%global source0_hash 8dbb8660838688a7b6ba4fed31d18dedf842afb4d47ca050d6d891c2c15f3be4
Name:           python-tzlocal
Version:        5.4.4
Release:        1%{?dist}
Summary:        tzinfo object for the local timezone
License:        MIT
URL:            https://github.com/regebro/tzlocal
Source0:        https://files.pythonhosted.org/packages/source/t/tzlocal/tzlocal-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-tzlocal = %{version}-%{release}
# /oreon:deps
%package -n       python3-tzlocal+testing
Summary:        Metapackage for python3-tzlocal testing extras
Requires:       python3-tzlocal = %{version}-%{release}
Requires:       python3dist(pytest) >= 4.3
Requires:       python3dist(pytest-mock) >= 3.3
Provides:       python3dist(tzlocal[testing]) = %{version}-%{release}

%description -n python3-tzlocal+testing
Metapackage for python3-tzlocal testing extras.

%package -n       python3-tzlocal+devenv
Summary:        Metapackage for python3-tzlocal devenv extras
Requires:       python3-tzlocal = %{version}-%{release}
Provides:       python3dist(tzlocal[devenv]) = %{version}-%{release}

%description -n python3-tzlocal+devenv
Metapackage for python3-tzlocal devenv extras.

%description

%package -n     python3-tzlocal
Summary:        tzinfo object for the local timezone
%description -n python3-tzlocal

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tzlocal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tzlocal usr/lib/python3*/site-packages/tzlocal* usr/lib64/python3*/site-packages/tzlocal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tzlocal* usr/lib64/python3*/site-packages/tzlocal* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tzlocal -f %{oreon_filedir}/python3-tzlocal.list

%changelog

%autochangelog
