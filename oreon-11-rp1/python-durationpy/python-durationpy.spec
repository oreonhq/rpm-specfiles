%global source0_hash 181898e1ae282e288f0a2291829656bf1b6b3aadf30a97993b85db4943642905
Name:           python-durationpy
Version:        0.11
Release:        1%{?dist}
Summary:        Module for converting between datetime.timedelta and Go_s Duration strings.
License:        MIT
URL:            https://github.com/icholy/durationpy
Source0:        https://files.pythonhosted.org/packages/source/d/durationpy/durationpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-durationpy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-durationpy
Summary:        Module for converting between datetime.timedelta and Go_s Duration strings.
%description -n python3-durationpy

%prep
%global oreon_srcdir durationpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-durationpy usr/lib/python3*/site-packages/durationpy* usr/lib64/python3*/site-packages/durationpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/durationpy* usr/lib64/python3*/site-packages/durationpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-durationpy -f %{oreon_filedir}/python3-durationpy.list

%changelog

%autochangelog
