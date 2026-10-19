%global source0_hash ff6233ff752a200ece4d0a6c59f6f9f7d0e96dcff0a7a3458296b997b812482e
Name:           python-robotframework
Version:        7.5
Release:        1%{?dist}
Summary:        Generic automation framework for acceptance testing and robotic process automation _RPA_
License:        ...
URL:            https://github.com/robotframework/robotframework
Source0:        https://files.pythonhosted.org/packages/source/r/robotframework/robotframework-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-robotframework = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-robotframework
Summary:        Generic automation framework for acceptance testing and robotic process automation _RPA_
%description -n python3-robotframework

%prep
%global oreon_srcdir robotframework-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-robotframework usr/lib/python3*/site-packages/robotframework* usr/lib64/python3*/site-packages/robotframework* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/robotframework* usr/lib64/python3*/site-packages/robotframework* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-robotframework -f %{oreon_filedir}/python3-robotframework.list

%changelog

%autochangelog
