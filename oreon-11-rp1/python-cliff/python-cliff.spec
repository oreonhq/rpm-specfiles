%global source0_hash 85314ad49bd62f90a51094d4e31b1cb4d3b92fb83cb3935eeba0236c32839e75
Name:           python-cliff
Version:        4.16.0
Release:        1%{?dist}
Summary:        Command Line Interface Formulation Framework
License:        Apache-2.0
URL:            https://docs.openstack.org/cliff/
Source0:        https://files.pythonhosted.org/packages/source/c/cliff/cliff-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-cliff = %{version}-%{release}
# /oreon:deps
%package -n       python3-cliff+sphinxext
Summary:        Metapackage for python3-cliff sphinxext extras
Requires:       python3-cliff = %{version}-%{release}
Requires:       python3dist(sphinx) >= 9.0.4
Requires:       python3dist(docutils) >= 0.21.2
Provides:       python3dist(cliff[sphinxext]) = %{version}-%{release}

%description -n python3-cliff+sphinxext
Metapackage for python3-cliff sphinxext extras.

%description

%package -n     python3-cliff
Summary:        Command Line Interface Formulation Framework
%description -n python3-cliff

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cliff-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cliff usr/lib/python3*/site-packages/cliff* usr/lib64/python3*/site-packages/cliff* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cliff* usr/lib64/python3*/site-packages/cliff* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cliff -f %{oreon_filedir}/python3-cliff.list

%changelog

%autochangelog
