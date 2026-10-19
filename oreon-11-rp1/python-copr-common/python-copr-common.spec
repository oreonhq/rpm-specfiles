%global source0_hash 5198817796896895b2537e97320490a02f3b4fe6ff3dae20d871d645ce1a31d2
Name:           python-copr-common
Version:        1.8
Release:        1%{?dist}
Summary:        Common python code used by Copr.
License:        ...
URL:            https://github.com/fedora-copr/copr
Source0:        https://files.pythonhosted.org/packages/source/c/copr_common/copr_common-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-copr-common = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-copr-common
Summary:        Common python code used by Copr.
%description -n python3-copr-common

%prep
%global oreon_srcdir copr_common-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-copr-common usr/lib/python3*/site-packages/copr_common* usr/lib64/python3*/site-packages/copr_common* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/copr_common* usr/lib64/python3*/site-packages/copr_common* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-copr-common -f %{oreon_filedir}/python3-copr-common.list

%changelog

%autochangelog
