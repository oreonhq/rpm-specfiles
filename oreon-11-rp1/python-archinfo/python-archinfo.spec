%global source0_hash 8e0006c77e42266f5bd719b7c1ad5116ed60f018c996bd11c1fe89363eb43e3c
Name:           python-archinfo
Version:        10.0.0
Release:        1%{?dist}
Summary:        Classes with architecture-specific information useful to other projects.
License:        BSD-2-Clause
URL:            https://api.angr.io/projects/archinfo/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/a/archinfo/archinfo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-archinfo = %{version}-%{release}
# /oreon:deps
%package -n       python3-archinfo+pcode
Summary:        Metapackage for python3-archinfo pcode extras
Requires:       python3-archinfo = %{version}-%{release}
Requires:       python3dist(pypcode) >= 4.0
Provides:       python3dist(archinfo[pcode]) = %{version}-%{release}

%description -n python3-archinfo+pcode
Metapackage for python3-archinfo pcode extras.

%description

%package -n     python3-archinfo
Summary:        Classes with architecture-specific information useful to other projects.
%description -n python3-archinfo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir archinfo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-archinfo usr/lib/python3*/site-packages/archinfo* usr/lib64/python3*/site-packages/archinfo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/archinfo* usr/lib64/python3*/site-packages/archinfo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-archinfo -f %{oreon_filedir}/python3-archinfo.list

%changelog

%autochangelog
