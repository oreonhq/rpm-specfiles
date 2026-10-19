%global source0_hash 35b39a4cb92cf328d6eca61cbbf65f68a37c2ceb3085f0f853cbb2e52a59fc23
Name:           python-deepmerge
Version:        3.0.1
Release:        1%{?dist}
Summary:        A toolset for deeply merging Python dictionaries.
License:        MIT
URL:            http://deepmerge.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/d/deepmerge/deepmerge-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 69
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-deepmerge = %{version}-%{release}
# /oreon:deps
%package -n       python3-deepmerge+dev
Summary:        Metapackage for python3-deepmerge dev extras
Requires:       python3-deepmerge = %{version}-%{release}
Provides:       python3dist(deepmerge[dev]) = %{version}-%{release}

%description -n python3-deepmerge+dev
Metapackage for python3-deepmerge dev extras.

%description

%package -n     python3-deepmerge
Summary:        A toolset for deeply merging Python dictionaries.
%description -n python3-deepmerge

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir deepmerge-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-deepmerge usr/lib/python3*/site-packages/deepmerge* usr/lib64/python3*/site-packages/deepmerge* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/deepmerge* usr/lib64/python3*/site-packages/deepmerge* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-deepmerge -f %{oreon_filedir}/python3-deepmerge.list

%changelog

%autochangelog
