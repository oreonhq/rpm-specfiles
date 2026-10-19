%global source0_hash 97cd18b9cfc78937b7c9891b22ff8174bf0116c837ddf7a90b87bc85df328ea2
Name:           python-rosdep
Version:        0.27.0
Release:        1%{?dist}
Summary:        rosdep package manager abstraction tool for ROS
License:        ...
URL:            https://github.com/ros-infrastructure/rosdep
Source0:        https://files.pythonhosted.org/packages/source/r/rosdep/rosdep-%{version}.tar.gz
BuildArch:      noarch
Patch0:         intersphinx-mapping.patch
Patch1:         drop-aggressive-asserts.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rosdep = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rosdep
Summary:        rosdep package manager abstraction tool for ROS
%description -n python3-rosdep

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rosdep-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rosdep usr/lib/python3*/site-packages/rosdep* usr/lib64/python3*/site-packages/rosdep* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rosdep* usr/lib64/python3*/site-packages/rosdep* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rosdep -f %{oreon_filedir}/python3-rosdep.list

%changelog

%autochangelog
