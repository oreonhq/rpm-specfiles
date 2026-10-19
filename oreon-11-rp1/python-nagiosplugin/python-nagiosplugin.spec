%global source0_hash 23169b04a23c4ad4419ef9b7666d401f48df3247b3dfc3f874be2c14fd2db401
Name:           python-nagiosplugin
Version:        1.4.0
Release:        1%{?dist}
Summary:        Class library for writing Nagios _Icinga_ plugins
License:        ZPL-2.1
URL:            https://github.com/mpounsett/nagiosplugin
Source0:        https://files.pythonhosted.org/packages/source/n/nagiosplugin/nagiosplugin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nagiosplugin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-nagiosplugin
Summary:        Class library for writing Nagios _Icinga_ plugins
%description -n python3-nagiosplugin

%prep
%global oreon_srcdir nagiosplugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nagiosplugin usr/lib/python3*/site-packages/nagiosplugin* usr/lib64/python3*/site-packages/nagiosplugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nagiosplugin* usr/lib64/python3*/site-packages/nagiosplugin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nagiosplugin -f %{oreon_filedir}/python3-nagiosplugin.list

%changelog

%autochangelog
