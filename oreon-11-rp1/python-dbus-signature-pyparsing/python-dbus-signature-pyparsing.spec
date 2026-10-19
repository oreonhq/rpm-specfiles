%global source0_hash cb9db46f199f204a78f9aa689837a9d3a4a10e621a800b6c457023a16dadbdf3
Name:           python-dbus-signature-pyparsing
Version:        0.4.3
Release:        1%{?dist}
Summary:        dbus signature parser
License:        Apache-2.0
URL:            https://github.com/stratis-storage/dbus-signature-pyparsing
Source0:        https://files.pythonhosted.org/packages/source/d/dbus_signature_pyparsing/dbus_signature_pyparsing-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-dbus-signature-pyparsing = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dbus-signature-pyparsing
Summary:        dbus signature parser
%description -n python3-dbus-signature-pyparsing

%prep
%global oreon_srcdir dbus_signature_pyparsing-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dbus-signature-pyparsing usr/lib/python3*/site-packages/dbus_signature_pyparsing* usr/lib64/python3*/site-packages/dbus_signature_pyparsing* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dbus_signature_pyparsing* usr/lib64/python3*/site-packages/dbus_signature_pyparsing* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dbus-signature-pyparsing -f %{oreon_filedir}/python3-dbus-signature-pyparsing.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-1
- Prepare for Oreon 11 (RP1)
