%global source0_hash 41a7ff0257d5a7a096a8e263da7efc0a96a6162c84ba64af2ebf8972d09e70e1
Name:           python-phonenumbers
Version:        9.0.39
Release:        1%{?dist}
Summary:        Python version of Google_s common library for parsing, formatting, storing and validating international phone numbers.
License:        Apache-2.0
URL:            https://github.com/daviddrysdale/python-phonenumbers
Source0:        https://files.pythonhosted.org/packages/source/p/phonenumbers/phonenumbers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-phonenumbers = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-phonenumbers
Summary:        Python version of Google_s common library for parsing, formatting, storing and validating international phone numbers.
%description -n python3-phonenumbers

%prep
%global oreon_srcdir phonenumbers-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-phonenumbers usr/lib/python3*/site-packages/phonenumbers* usr/lib64/python3*/site-packages/phonenumbers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/phonenumbers* usr/lib64/python3*/site-packages/phonenumbers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-phonenumbers -f %{oreon_filedir}/python3-phonenumbers.list

%changelog

%autochangelog
