%global source0_hash 2db2163ef51a1b746d6d7781f78856430a2bcf0f10df428fe5986ecc0ef9809c
Name:           python-click-man
Version:        0.5.1
Release:        1%{?dist}
Summary:        Generate man pages for click based CLI applications
License:        MIT
URL:            https://github.com/click-contrib/click-man
Source0:        https://files.pythonhosted.org/packages/source/c/click_man/click_man-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-click-man = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-click-man
Summary:        Generate man pages for click based CLI applications
%description -n python3-click-man

%prep
%global oreon_srcdir click_man-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-man usr/lib/python3*/site-packages/click_man* usr/lib64/python3*/site-packages/click_man* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_man* usr/lib64/python3*/site-packages/click_man* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click-man -f %{oreon_filedir}/python3-click-man.list

%changelog

%autochangelog
