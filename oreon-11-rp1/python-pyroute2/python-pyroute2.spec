%global source0_hash 6bc5e2ea9a372ded682b4ede4028ba00236bd6e35b42d833f39a96b219ef1db2
Name:           python-pyroute2
Version:        0.9.6
Release:        1%{?dist}
Summary:        Python Netlink library
License:        GPL-2.0-or-later OR Apache-2.0
URL:            https://github.com/svinota/pyroute2
Source0:        https://files.pythonhosted.org/packages/source/p/pyroute2/pyroute2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyroute2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyroute2+dev
Summary:        Metapackage for python3-pyroute2 dev extras
Requires:       python3-pyroute2 = %{version}-%{release}
Requires:       python3dist(pytest-asyncio) == 0.26.0
Provides:       python3dist(pyroute2[dev]) = %{version}-%{release}

%description -n python3-pyroute2+dev
Metapackage for python3-pyroute2 dev extras.

%package -n       python3-pyroute2+docs
Summary:        Metapackage for python3-pyroute2 docs extras
Requires:       python3-pyroute2 = %{version}-%{release}
Requires:       python3dist(pytest-asyncio) == 0.26.0
Provides:       python3dist(pyroute2[docs]) = %{version}-%{release}

%description -n python3-pyroute2+docs
Metapackage for python3-pyroute2 docs extras.

%package -n       python3-pyroute2+repo
Summary:        Metapackage for python3-pyroute2 repo extras
Requires:       python3-pyroute2 = %{version}-%{release}
Provides:       python3dist(pyroute2[repo]) = %{version}-%{release}

%description -n python3-pyroute2+repo
Metapackage for python3-pyroute2 repo extras.

%description

%package -n     python3-pyroute2
Summary:        Python Netlink library
%description -n python3-pyroute2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyroute2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyroute2 usr/lib/python3*/site-packages/pyroute2* usr/lib64/python3*/site-packages/pyroute2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyroute2* usr/lib64/python3*/site-packages/pyroute2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyroute2 -f %{oreon_filedir}/python3-pyroute2.list

%changelog

%autochangelog
