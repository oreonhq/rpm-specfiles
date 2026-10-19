%global source0_hash 60224f94a5182ebfcf427263b7b86d71ec882444bf25daf8bf03fd1efe52523a
Name:           python-advisory-parser
Version:        1.14
Release:        1%{?dist}
Summary:        Security flaw parser for upstream security advisories
License:        LGPL-3.0-or-later
URL:            https://github.com/RedHatProductSecurity/advisory-parser
Source0:        https://files.pythonhosted.org/packages/source/a/advisory_parser/advisory_parser-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-advisory-parser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-advisory-parser
Summary:        Security flaw parser for upstream security advisories
%description -n python3-advisory-parser

%prep
%global oreon_srcdir advisory_parser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-advisory-parser usr/lib/python3*/site-packages/advisory_parser* usr/lib64/python3*/site-packages/advisory_parser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/advisory_parser* usr/lib64/python3*/site-packages/advisory_parser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-advisory-parser -f %{oreon_filedir}/python3-advisory-parser.list

%changelog

%autochangelog
