%global source0_hash 023bf5a19ce33ed50e3711af92769233e62b1b1b4671d2bb7bfc5e654533f797
Name:           python-rospkg
Version:        1.6.3
Release:        1%{?dist}
Summary:        ROS package library
License:        ...
URL:            https://github.com/ros-infrastructure/rospkg
Source0:        https://files.pythonhosted.org/packages/source/r/rospkg/rospkg-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rospkg = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rospkg
Summary:        ROS package library
%description -n python3-rospkg

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rospkg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rospkg usr/lib/python3*/site-packages/rospkg* usr/lib64/python3*/site-packages/rospkg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rospkg* usr/lib64/python3*/site-packages/rospkg* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rospkg -f %{oreon_filedir}/python3-rospkg.list

%changelog

%autochangelog
