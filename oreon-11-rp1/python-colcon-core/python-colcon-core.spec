%global source0_hash 0e781b3f5d82fbd974e2ed61e40d37b711e2f94fac18971d6944cf7308ecb8d0
Name:           python-colcon-core
Version:        0.21.3
Release:        1%{?dist}
Summary:        Command line tool to build sets of software packages.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-core/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_core/colcon_core-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-0.5.3-remove-pytest.patch
Patch1:         %{name}-0.19.0-pytest-compat.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-core
Summary:        Command line tool to build sets of software packages.
%description -n python3-colcon-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-core usr/lib/python3*/site-packages/colcon_core* usr/lib64/python3*/site-packages/colcon_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_core* usr/lib64/python3*/site-packages/colcon_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-core -f %{oreon_filedir}/python3-colcon-core.list

%changelog

%autochangelog
