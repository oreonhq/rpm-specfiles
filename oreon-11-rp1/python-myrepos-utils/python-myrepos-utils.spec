%global source0_hash 9886cc40e8c06ceb6e56514c762f9a3a27ace7e5a4e274040b1074694a138ea3
Name:           python-myrepos-utils
Version:        0.0.4.3
Release:        1%{?dist}
Summary:        Additional utilities for myrepos
License:        GPL-2.0-or-later
URL:            https://git.sr.ht/~michel-slm/myrepos-utils
Source0:        https://files.pythonhosted.org/packages/source/m/myrepos_utils/myrepos_utils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-myrepos-utils = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-myrepos-utils
Summary:        Additional utilities for myrepos
%description -n python3-myrepos-utils

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir myrepos_utils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-myrepos-utils usr/lib/python3*/site-packages/myrepos_utils* usr/lib64/python3*/site-packages/myrepos_utils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/myrepos_utils* usr/lib64/python3*/site-packages/myrepos_utils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-myrepos-utils -f %{oreon_filedir}/python3-myrepos-utils.list

%changelog

%autochangelog
