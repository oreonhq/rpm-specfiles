%global source0_hash da876e20dbc68b38a7427af95761f9eeb9d4e947f3cf509679ad5e73863439ef
Name:           python-fastrand
Version:        3.1.0
Release:        1%{?dist}
Summary:        Fast random number generation in Python
License:        Apache-2.0
URL:            https://github.com/lemire/fastrand
Source0:        https://files.pythonhosted.org/packages/source/f/fastrand/fastrand-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-fastrand = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fastrand
Summary:        Fast random number generation in Python
%description -n python3-fastrand

%prep
%global oreon_srcdir fastrand-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastrand usr/lib/python3*/site-packages/fastrand* usr/lib64/python3*/site-packages/fastrand* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastrand* usr/lib64/python3*/site-packages/fastrand* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastrand -f %{oreon_filedir}/python3-fastrand.list

%changelog

%autochangelog
