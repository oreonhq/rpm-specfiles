%global source0_hash b2a34a8af0a6625ccbdf45cd343b854fc6c1a85231dadc80b8805db836756323
Name:           python-dialog
Version:        3.5.3
Release:        1%{?dist}
Summary:        Python interface to the Unix dialog utility
License:        LGPL-2.1-or-later
URL:            http://pythondialog.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/p/pythondialog/pythondialog-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-dialog
Requires:       dialog
Summary:        Python interface to the Unix dialog utility
%{?python_provide:%python_provide python3-dialog}
%description -n python3-dialog

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pythondialog-%{version}

find examples -name '*.py' -print -exec sed -r -i 's|(.!)\s+/usr/bin/env python.*|\1%{__python3}|' {} \;

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-dialog usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import dialog
%files -f %{oreon_filedir}/main.list
%files -n python3-dialog -f %{oreon_filedir}/python3-dialog.list

%changelog

%autochangelog
