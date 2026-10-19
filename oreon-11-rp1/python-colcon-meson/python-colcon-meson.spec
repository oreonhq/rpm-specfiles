%global source0_hash e1bec86278daf211ac48106feba70c82e6f6804239d80d81fdecbda5d040c5de
Name:           python-colcon-meson
Version:        0.6.1
Release:        1%{?dist}
Summary:        Extension for colcon to support Meson packages.
License:        ...
URL:            https://github.com/colcon/colcon-meson
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_meson/colcon_meson-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-meson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-meson
Summary:        Extension for colcon to support Meson packages.
%description -n python3-colcon-meson

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_meson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-meson usr/lib/python3*/site-packages/colcon_meson* usr/lib64/python3*/site-packages/colcon_meson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_meson* usr/lib64/python3*/site-packages/colcon_meson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-meson -f %{oreon_filedir}/python3-colcon-meson.list

%changelog

%autochangelog
