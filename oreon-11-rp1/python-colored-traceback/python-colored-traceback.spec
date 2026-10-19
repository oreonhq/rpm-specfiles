%global source0_hash ecbc8e41f0712ea81931d7cd436b8beb9f3eff1595d2498f183e0ef69b56fe84
Name:           python-colored-traceback
Version:        0.4.2
Release:        1%{?dist}
Summary:        Automatically color uncaught exception tracebacks
License:        ISC
URL:            https://www.github.com/staticshock/colored-traceback.py
Source0:        https://files.pythonhosted.org/packages/source/c/colored-traceback/colored-traceback-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-colored-traceback = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colored-traceback
Summary:        Automatically color uncaught exception tracebacks
%description -n python3-colored-traceback

%prep
%global oreon_srcdir colored-traceback-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colored-traceback usr/lib/python3*/site-packages/colored_traceback* usr/lib64/python3*/site-packages/colored_traceback* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colored_traceback* usr/lib64/python3*/site-packages/colored_traceback* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colored-traceback -f %{oreon_filedir}/python3-colored-traceback.list

%changelog

%autochangelog
