%global source0_hash 2f9fbcea86e8dbf1a2d28954225547634a289db7201e7764516a5dce86c116de
Name:           python-pecan
Version:        1.8.0
Release:        1%{?dist}
Summary:        A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
License:        ...
URL:            http://github.com/pecan/pecan
Source0:        https://files.pythonhosted.org/packages/source/p/pecan/pecan-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pecan = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pecan
Summary:        A WSGI object-dispatching web framework, designed to be lean and fast, with few dependencies.
%description -n python3-pecan

%prep
%global oreon_srcdir pecan-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pecan usr/lib/python3*/site-packages/pecan* usr/lib64/python3*/site-packages/pecan* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pecan* usr/lib64/python3*/site-packages/pecan* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pecan -f %{oreon_filedir}/python3-pecan.list

%changelog

%autochangelog
