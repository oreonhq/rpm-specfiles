%global source0_hash 475ddad4fd5c50f6b20a07af57e3376cf7ac9667ab3a0e170134cb8e2071aab9
Name:           python-catkin-pkg
Version:        1.1.1
Release:        1%{?dist}
Summary:        catkin package library
License:        ...
URL:            https://github.com/ros-infrastructure/catkin_pkg
Source0:        https://files.pythonhosted.org/packages/source/c/catkin_pkg/catkin_pkg-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-catkin-pkg = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-catkin-pkg
Summary:        catkin package library
%description -n python3-catkin-pkg

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir catkin_pkg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-catkin-pkg usr/lib/python3*/site-packages/catkin_pkg* usr/lib64/python3*/site-packages/catkin_pkg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/catkin_pkg* usr/lib64/python3*/site-packages/catkin_pkg* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-catkin-pkg -f %{oreon_filedir}/python3-catkin-pkg.list

%changelog

%autochangelog
