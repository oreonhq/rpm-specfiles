%global source0_hash 4e0143cc0288280b5fd75ada7c75f697857d694ff48a68da6fcc178b6ffb2726
Name:           python-colcon-package-information
Version:        0.4.1
Release:        1%{?dist}
Summary:        Extension for colcon to output package information.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-package-information/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_package_information/colcon_package_information-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-package-information = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-package-information
Summary:        Extension for colcon to output package information.
%description -n python3-colcon-package-information

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_package_information-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-package-information usr/lib/python3*/site-packages/colcon_package_information* usr/lib64/python3*/site-packages/colcon_package_information* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_package_information* usr/lib64/python3*/site-packages/colcon_package_information* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-package-information -f %{oreon_filedir}/python3-colcon-package-information.list

%changelog

%autochangelog
