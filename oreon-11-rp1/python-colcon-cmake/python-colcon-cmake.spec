%global source0_hash ab0ce0df58f525d1c560b66fd22eb6a62394695a2775166483829debbbb4c84e
Name:           python-colcon-cmake
Version:        0.2.30
Release:        1%{?dist}
Summary:        Extension for colcon to support CMake packages.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-cmake/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_cmake/colcon_cmake-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-cmake = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-cmake
Summary:        Extension for colcon to support CMake packages.
%description -n python3-colcon-cmake

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_cmake-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-cmake usr/lib/python3*/site-packages/colcon_cmake* usr/lib64/python3*/site-packages/colcon_cmake* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_cmake* usr/lib64/python3*/site-packages/colcon_cmake* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-cmake -f %{oreon_filedir}/python3-colcon-cmake.list

%changelog

%autochangelog
