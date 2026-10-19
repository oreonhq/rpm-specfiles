%global source0_hash daece55f03d76d0674f481b0c1b73ad877229b721386a14adbe9c9991c9f3025
Name:           python-pluginlib
Version:        0.11.0
Release:        1%{?dist}
Summary:        A framework for creating and importing plugins
License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/pluginlib
Source0:        https://files.pythonhosted.org/packages/source/p/pluginlib/pluginlib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pluginlib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pluginlib
Summary:        A framework for creating and importing plugins
%description -n python3-pluginlib

%prep
%global oreon_srcdir pluginlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pluginlib usr/lib/python3*/site-packages/pluginlib* usr/lib64/python3*/site-packages/pluginlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pluginlib* usr/lib64/python3*/site-packages/pluginlib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pluginlib -f %{oreon_filedir}/python3-pluginlib.list

%changelog

%autochangelog
