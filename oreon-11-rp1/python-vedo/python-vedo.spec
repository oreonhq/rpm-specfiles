%global source0_hash 17fbea620eec0e75831dc326974123fd97f559acf1590c54a8824c1ac71d8bd3
Name:           python-vedo
Version:        2026.6.1
Release:        1%{?dist}
Summary:        A python module for scientific visualization, analysis of 3D objects and point clouds.
License:        MIT
URL:            https://github.com/marcomusy/vedo
Source0:        https://files.pythonhosted.org/packages/source/v/vedo/vedo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-vedo = %{version}-%{release}
# /oreon:deps
%package -n       python3-vedo+all
Summary:        Metapackage for python3-vedo all extras
Requires:       python3-vedo = %{version}-%{release}
Provides:       python3dist(vedo[all]) = %{version}-%{release}

%description -n python3-vedo+all
Metapackage for python3-vedo all extras.

%description

%package -n     python3-vedo
Summary:        A python module for scientific visualization, analysis of 3D objects and point clouds.
%description -n python3-vedo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir vedo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-vedo usr/lib/python3*/site-packages/vedo* usr/lib64/python3*/site-packages/vedo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/vedo* usr/lib64/python3*/site-packages/vedo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-vedo -f %{oreon_filedir}/python3-vedo.list

%changelog

%autochangelog
