%global source0_hash 5ec8f6f621725b4805a17760042a81094a7e66ec5b71353c85cbcd27000b6ea0
Name:           python-colcon-ros-bundle
Version:        0.1.1
Release:        1%{?dist}
Summary:        Plugin for colcon to bundle ros applications
License:        ...
URL:            https://github.com/colcon/colcon-bundle/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon-ros-bundle/colcon-ros-bundle-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-0.1.0-unittest-mock.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-ros-bundle = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-ros-bundle
Summary:        Plugin for colcon to bundle ros applications
%description -n python3-colcon-ros-bundle

%prep
%global oreon_srcdir colcon-ros-bundle-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-ros-bundle usr/lib/python3*/site-packages/colcon_ros_bundle* usr/lib64/python3*/site-packages/colcon_ros_bundle* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_ros_bundle* usr/lib64/python3*/site-packages/colcon_ros_bundle* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-ros-bundle -f %{oreon_filedir}/python3-colcon-ros-bundle.list

%changelog

%autochangelog
