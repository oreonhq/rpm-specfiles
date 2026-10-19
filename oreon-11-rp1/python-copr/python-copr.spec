%global source0_hash 43aaa884003425cc456f5f6e650b1389ca6ab12aeaa6fc09e510a1cca7c1f122
Name:           python-copr
Version:        2.7
Release:        1%{?dist}
Summary:        Python client for copr service.
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-copr/copr
Source0:        https://files.pythonhosted.org/packages/source/c/copr/copr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-copr = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-copr
Summary:        Python client for copr service.
%description -n python3-copr

%prep
%global oreon_srcdir copr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-copr usr/lib/python3*/site-packages/copr* usr/lib64/python3*/site-packages/copr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/copr* usr/lib64/python3*/site-packages/copr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-copr -f %{oreon_filedir}/python3-copr.list

%changelog

%autochangelog
