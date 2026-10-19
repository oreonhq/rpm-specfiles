%global source0_hash e7f195f30f0ab4e39c5a66e19e0d0bfee0ce5afb3f49e0ae4e5a491a8417db2a
Name:           python-xvfbwrapper
Version:        0.2.34
Release:        1%{?dist}
Summary:        Manage headless displays with Xvfb _X virtual framebuffer_
License:        MIT
URL:            https://github.com/cgoldberg/xvfbwrapper
Source0:        https://files.pythonhosted.org/packages/source/x/xvfbwrapper/xvfbwrapper-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xvfbwrapper = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xvfbwrapper
Summary:        Manage headless displays with Xvfb _X virtual framebuffer_
%description -n python3-xvfbwrapper

%prep
%global oreon_srcdir xvfbwrapper-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xvfbwrapper usr/lib/python3*/site-packages/xvfbwrapper* usr/lib64/python3*/site-packages/xvfbwrapper* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xvfbwrapper* usr/lib64/python3*/site-packages/xvfbwrapper* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xvfbwrapper -f %{oreon_filedir}/python3-xvfbwrapper.list

%changelog

%autochangelog
