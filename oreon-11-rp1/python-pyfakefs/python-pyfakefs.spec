%global source0_hash e59a36db447bf509ce9c97ab3d1510c08cc51895c5311325a560a5e5b5dc1940
Name:           python-pyfakefs
Version:        6.2.0
Release:        1%{?dist}
Summary:        Implements a fake file system that mocks the Python file system modules.
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pyfakefs
Source0:        https://files.pythonhosted.org/packages/source/p/pyfakefs/pyfakefs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-pyfakefs = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyfakefs+doc
Summary:        Metapackage for python3-pyfakefs doc extras
Requires:       python3-pyfakefs = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(furo) >= 2025.12.19
Requires:       python3dist(myst-parser) >= 5.0.0
Provides:       python3dist(pyfakefs[doc]) = %{version}-%{release}

%description -n python3-pyfakefs+doc
Metapackage for python3-pyfakefs doc extras.

%description

%package -n     python3-pyfakefs
Summary:        Implements a fake file system that mocks the Python file system modules.
%description -n python3-pyfakefs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyfakefs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyfakefs usr/lib/python3*/site-packages/pyfakefs* usr/lib64/python3*/site-packages/pyfakefs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyfakefs* usr/lib64/python3*/site-packages/pyfakefs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyfakefs -f %{oreon_filedir}/python3-pyfakefs.list

%changelog

%autochangelog
