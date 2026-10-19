%global source0_hash 48a0ef30a42db65d8f3399045e1d09ab0ba66e3b9efc360d07f80ea55d286025
Name:           python-httplib2
Version:        0.32.0
Release:        1%{?dist}
Summary:        A comprehensive HTTP client library.
License:        MIT
URL:            https://github.com/httplib2/httplib2
Source0:        https://files.pythonhosted.org/packages/source/h/httplib2/httplib2-%{version}.tar.gz
BuildArch:      noarch
Patch1:         python-httplib2.certfile.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-httplib2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-httplib2
Summary:        A comprehensive HTTP client library.
%description -n python3-httplib2

%prep
%global oreon_srcdir httplib2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httplib2 usr/lib/python3*/site-packages/httplib2* usr/lib64/python3*/site-packages/httplib2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httplib2* usr/lib64/python3*/site-packages/httplib2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-httplib2 -f %{oreon_filedir}/python3-httplib2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.0-8
- Prepare for Oreon 11 (RP1)
