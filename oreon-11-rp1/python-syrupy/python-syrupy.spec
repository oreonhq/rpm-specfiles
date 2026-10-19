%global source0_hash 7e584a8df4ede6dd3c1c44a77f9edc46186b6767a73dea6f0083044946839a59
Name:           python-syrupy
Version:        6.1.1
Release:        1%{?dist}
Summary:        Pytest Snapshot Test Utility
License:        MIT
URL:            https://github.com/syrupy-project/syrupy
Source0:        https://files.pythonhosted.org/packages/source/s/syrupy/syrupy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-syrupy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-syrupy
Summary:        Pytest Snapshot Test Utility
# oreon:reqs
Requires:       python3dist(pytest) (>= 8.0.0)
# /oreon:reqs
%description -n python3-syrupy

%prep
%global oreon_srcdir syrupy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-syrupy usr/lib/python3*/site-packages/syrupy* usr/lib64/python3*/site-packages/syrupy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/syrupy* usr/lib64/python3*/site-packages/syrupy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-syrupy -f %{oreon_filedir}/python3-syrupy.list

%changelog

%autochangelog
