%global source0_hash 7425d0afa180f0092db903abb1526a130b36858980aad90b3694f48e41420155
Name:           python-rarfile
Version:        4.5
Release:        1%{?dist}
Summary:        RAR archive reader for Python
License:        ISC
URL:            https://github.com/markokr/rarfile
Source0:        https://files.pythonhosted.org/packages/source/r/rarfile/rarfile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rarfile = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rarfile
Summary:        RAR archive reader for Python
%description -n python3-rarfile

%prep
%global oreon_srcdir rarfile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rarfile usr/lib/python3*/site-packages/rarfile* usr/lib64/python3*/site-packages/rarfile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rarfile* usr/lib64/python3*/site-packages/rarfile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rarfile -f %{oreon_filedir}/python3-rarfile.list

%changelog

%autochangelog
