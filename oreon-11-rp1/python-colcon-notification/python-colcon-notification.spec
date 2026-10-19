%global source0_hash a97cf4f9cf9ad60a78c3576ea633e50f7c9caae1d4aef57e55bdbb40d21151e0
Name:           python-colcon-notification
Version:        0.3.3
Release:        1%{?dist}
Summary:        Extension for colcon to provide status notifications.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-notification/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_notification/colcon_notification-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-0.2.8-data-files.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-notification = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-notification
Summary:        Extension for colcon to provide status notifications.
%description -n python3-colcon-notification

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_notification-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-notification usr/lib/python3*/site-packages/colcon_notification* usr/lib64/python3*/site-packages/colcon_notification* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_notification* usr/lib64/python3*/site-packages/colcon_notification* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-notification -f %{oreon_filedir}/python3-colcon-notification.list

%changelog

%autochangelog
