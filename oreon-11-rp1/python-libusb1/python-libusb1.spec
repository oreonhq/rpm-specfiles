%global source0_hash 9cf5638506d54f21bf36550d97ea63189111a23c4d8078f630103a2052135f45
Name:           python-libusb1
Version:        3.4.0
Release:        1%{?dist}
Summary:        Pure-python wrapper for libusb-1.0
License:        LGPL-2.1-or-later
URL:            https://github.com/vpelletier/python-libusb1
Source0:        https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libusb1 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-libusb1
Summary:        Pure-python wrapper for libusb-1.0
%description -n python3-libusb1

%prep
%global oreon_srcdir libusb1-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-libusb1 usr/lib/python3*/site-packages/libusb1* usr/lib64/python3*/site-packages/libusb1* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libusb1* usr/lib64/python3*/site-packages/libusb1* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-libusb1 -f %{oreon_filedir}/python3-libusb1.list

%changelog

%autochangelog
