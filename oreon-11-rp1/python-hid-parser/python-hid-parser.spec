%global source0_hash e7e96dd7c91772cf2de528e1200c40e571d9a5277ff4e6e04fe82dce1be5db99
Name:           python-hid-parser
Version:        0.1.0
Release:        1%{?dist}
Summary:        Typed pure Python library to parse HID report descriptors
License:        MIT
URL:            https://github.com/usb-tools/python-hid-parser
Source0:        https://files.pythonhosted.org/packages/source/h/hid_parser/hid_parser-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/usb-tools/python-hid-parser/pull/23.patch#/%{name}-pytest-8.patch
Patch:          https://github.com/usb-tools/python-hid-parser/pull/18.patch#/%{name}-fix-GenericDesktopControls-Rz.patch
Patch:          %{name}-solaar.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-hid-parser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-hid-parser
Summary:        Typed pure Python library to parse HID report descriptors
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.4.0
# /oreon:reqs
%description -n python3-hid-parser

%prep
%global oreon_srcdir hid_parser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hid-parser usr/lib/python3*/site-packages/hid_parser* usr/lib64/python3*/site-packages/hid_parser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hid_parser* usr/lib64/python3*/site-packages/hid_parser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hid-parser -f %{oreon_filedir}/python3-hid-parser.list

%changelog

%autochangelog
