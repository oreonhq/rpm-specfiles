%global source0_hash 0493484b714418c75ffa3810883c3ce2570d6210cea9ce98e3e616b1b99bc494
Name:           python-asn1
Version:        3.3.0
Release:        1%{?dist}
Summary:        Python-ASN1 is a simple ASN.1 encoder and decoder for Python 2.7+ and 3.5+.
License:        MIT
URL:            https://github.com/andrivet/python-asn1
Source0:        https://files.pythonhosted.org/packages/source/a/asn1/asn1-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-asn1 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-asn1
Summary:        Python-ASN1 is a simple ASN.1 encoder and decoder for Python 2.7+ and 3.5+.
%description -n python3-asn1

%prep
%global oreon_srcdir asn1-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-asn1 usr/lib/python3*/site-packages/asn1* usr/lib64/python3*/site-packages/asn1* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asn1* usr/lib64/python3*/site-packages/asn1* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-asn1 -f %{oreon_filedir}/python3-asn1.list

%changelog

%autochangelog
