%global source0_hash e9304732d6cfa27cebb41ae03e3a241eca25d25caa6858275edc1ed838e49997
Name:           python-colcon-mixin
Version:        0.3.2
Release:        1%{?dist}
Summary:        Extension for colcon to read CLI mixins from files.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-mixin/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_mixin/colcon_mixin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-mixin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-mixin
Summary:        Extension for colcon to read CLI mixins from files.
%description -n python3-colcon-mixin

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_mixin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-mixin usr/lib/python3*/site-packages/colcon_mixin* usr/lib64/python3*/site-packages/colcon_mixin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_mixin* usr/lib64/python3*/site-packages/colcon_mixin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-mixin -f %{oreon_filedir}/python3-colcon-mixin.list

%changelog

%autochangelog
