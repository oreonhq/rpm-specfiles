%global source0_hash 63ce797b6d85763d4b0e9611bd62d30fe31b0c4edb601838e76a039e4a4cdb59
Name:           python-kiss-headers
Version:        2.5.0
Release:        1%{?dist}
Summary:        Object-oriented HTTP and IMAP _structured_ headers.
License:        MIT
URL:            https://jawah.github.io/kiss-headers
Source0:        https://files.pythonhosted.org/packages/source/k/kiss_headers/kiss_headers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) < 2
BuildRequires:  python3dist(hatchling) >= 1.6.0
Requires:       python3-kiss-headers = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kiss-headers
Summary:        Object-oriented HTTP and IMAP _structured_ headers.
%description -n python3-kiss-headers

%prep
%global oreon_srcdir kiss_headers-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kiss-headers usr/lib/python3*/site-packages/kiss_headers* usr/lib64/python3*/site-packages/kiss_headers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kiss_headers* usr/lib64/python3*/site-packages/kiss_headers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kiss-headers -f %{oreon_filedir}/python3-kiss-headers.list

%changelog

%autochangelog
