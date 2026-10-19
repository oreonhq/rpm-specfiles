%global source0_hash 8db5a05c369dbc231dab4c98515ce828f2dffdc14f1534441a6c59b71c6d2031
Name:           python-gnupg
Version:        2.3.1
Release:        1%{?dist}
Summary:        A Python wrapper for GnuPG
License:        GPL-3.0-or-later
URL:            https://github.com/isislovecruft/python-gnupg
Source0:        https://files.pythonhosted.org/packages/source/g/gnupg/gnupg-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gnupg = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gnupg
Summary:        A Python wrapper for GnuPG
%description -n python3-gnupg

%prep
%global oreon_srcdir gnupg-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gnupg usr/lib/python3*/site-packages/gnupg* usr/lib64/python3*/site-packages/gnupg* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gnupg* usr/lib64/python3*/site-packages/gnupg* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gnupg -f %{oreon_filedir}/python3-gnupg.list

%changelog

%autochangelog
