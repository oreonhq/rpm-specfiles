%global source0_hash 1ea2b4fa678b8ca268253798d5963935df39132d47c3e241c0a0732224005e7d
Name:           python-wcmatch
Version:        11.0.1
Release:        1%{?dist}
Summary:        Wildcard/glob file name matcher.
License:        MIT
URL:            https://github.com/facelessuser/wcmatch
Source0:        https://files.pythonhosted.org/packages/source/w/wcmatch/wcmatch-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 0.21.1
Requires:       python3-wcmatch = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wcmatch
Summary:        Wildcard/glob file name matcher.
# oreon:reqs
Requires:       python3dist(bracex) >= 3.0
# /oreon:reqs
%description -n python3-wcmatch

%prep
%global oreon_srcdir wcmatch-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wcmatch usr/lib/python3*/site-packages/wcmatch* usr/lib64/python3*/site-packages/wcmatch* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wcmatch* usr/lib64/python3*/site-packages/wcmatch* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wcmatch -f %{oreon_filedir}/python3-wcmatch.list

%changelog

%autochangelog
