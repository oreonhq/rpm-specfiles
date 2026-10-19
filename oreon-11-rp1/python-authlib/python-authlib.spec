%global source0_hash f3ecd5f1da737262fb53bf1a4d95c4ea1ad9dd509316587a255c99ab1838a4f0
Name:           python-authlib
Version:        1.8.0
Release:        1%{?dist}
Summary:        The ultimate Python library in building OAuth and OpenID Connect servers and clients.
License:        BSD-3-Clause
URL:            https://github.com/authlib/authlib
Source0:        https://files.pythonhosted.org/packages/source/a/authlib/authlib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-authlib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-authlib
Summary:        The ultimate Python library in building OAuth and OpenID Connect servers and clients.
# oreon:reqs
Requires:       python3dist(cryptography) >= 45.0.1
Requires:       python3dist(joserfc) >= 1.6.1
# /oreon:reqs
%description -n python3-authlib

%prep
%global oreon_srcdir authlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-authlib usr/lib/python3*/site-packages/authlib* usr/lib64/python3*/site-packages/authlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/authlib* usr/lib64/python3*/site-packages/authlib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-authlib -f %{oreon_filedir}/python3-authlib.list

%changelog

%autochangelog
