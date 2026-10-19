%global source0_hash 5823209b0d43af322ce698c689380d7c15ca31fa8e6e3be8459f27031bef0af5
Name:           python-wcwidth
Version:        0.9.1
Release:        1%{?dist}
Summary:        Measures the displayed width of unicode strings in a terminal
License:        MIT
URL:            https://github.com/jquast/wcwidth
Source0:        https://files.pythonhosted.org/packages/source/w/wcwidth/wcwidth-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-wcwidth = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wcwidth
Summary:        Measures the displayed width of unicode strings in a terminal
%description -n python3-wcwidth

%prep
%global oreon_srcdir wcwidth-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wcwidth usr/lib/python3*/site-packages/wcwidth* usr/lib64/python3*/site-packages/wcwidth* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wcwidth* usr/lib64/python3*/site-packages/wcwidth* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wcwidth -f %{oreon_filedir}/python3-wcwidth.list

%changelog

%autochangelog
