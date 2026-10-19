%global source0_hash 3a498e7e85ef3249343d5710618d641a414da0fbae6d23053ada7976ee83ea5f
Name:           python-uritools
Version:        6.1.3
Release:        1%{?dist}
Summary:        URI parsing, classification and composition
License:        MIT
URL:            https://github.com/tkem/uritools/
Source0:        https://files.pythonhosted.org/packages/source/u/uritools/uritools-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 8.2
Requires:       python3-uritools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-uritools
Summary:        URI parsing, classification and composition
%description -n python3-uritools

%prep
%global oreon_srcdir uritools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-uritools usr/lib/python3*/site-packages/uritools* usr/lib64/python3*/site-packages/uritools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uritools* usr/lib64/python3*/site-packages/uritools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-uritools -f %{oreon_filedir}/python3-uritools.list

%changelog

%autochangelog
