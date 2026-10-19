%global source0_hash b6c57ee128a5867548181ae9b0a0d8b4333863734a7f80375d42fcda97293100
Name:           python-pywizlight
Version:        0.6.6
Release:        1%{?dist}
Summary:        A python connector for WiZ light bulbs _e.g SLV Play_
License:        MIT
URL:            https://github.com/sbidy/pywizlight
Source0:        https://files.pythonhosted.org/packages/source/p/pywizlight/pywizlight-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pywizlight = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pywizlight
Summary:        A python connector for WiZ light bulbs _e.g SLV Play_
%description -n python3-pywizlight

%prep
%global oreon_srcdir pywizlight-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pywizlight usr/lib/python3*/site-packages/pywizlight* usr/lib64/python3*/site-packages/pywizlight* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pywizlight* usr/lib64/python3*/site-packages/pywizlight* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pywizlight -f %{oreon_filedir}/python3-pywizlight.list

%changelog

%autochangelog
