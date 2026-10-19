%global source0_hash 9c447d8431c947fe4c8febc4ed9e760bc29011a5b01e5c74b67025bd9fb8ce81
Name:           python-pyasn1
Version:        0.6.4
Release:        1%{?dist}
Summary:        Pure-Python implementation of ASN.1 types and DER/BER/CER codecs _X.208_
License:        BSD-2-Clause
URL:            https://github.com/pyasn1/pyasn1
Source0:        https://files.pythonhosted.org/packages/source/p/pyasn1/pyasn1-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyasn1 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyasn1
Summary:        Pure-Python implementation of ASN.1 types and DER/BER/CER codecs _X.208_
%description -n python3-pyasn1

%prep
%global oreon_srcdir pyasn1-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyasn1 usr/lib/python3*/site-packages/pyasn1* usr/lib64/python3*/site-packages/pyasn1* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyasn1* usr/lib64/python3*/site-packages/pyasn1* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyasn1 -f %{oreon_filedir}/python3-pyasn1.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2-1
- Prepare for Oreon 11 (RP1)
