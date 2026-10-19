%global source0_hash ff3f941f82aa00f6e8326e9ae5d2adaf265cd227e3890d2051c3514b124467cb
%global srcname simpleline
Name: python-%{srcname}
Summary:        A Python library for creating text UI
Url: https://github.com/rhinstaller/python-%{srcname}
Version: 1.9.2
Release:        1%{?dist}
Source0:        https://github.com/rhinstaller/%{name}/releases/download/%{version}/%{srcname}-%{version}.tar.gz
License: LGPL-3.0-or-later
BuildArch: noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Simpleline is a Python library for creating text UI.
It is designed to be used with line-based machines
and tools (e.g. serial console) so that every new line
is appended to the bottom of the screen.
Printed lines are never rewritten!

%package -n python3-%{srcname}
Summary: A Python3 library for creating text UI
Requires: rpm-python3
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
Simpleline is a Python3 library for creating text UI.
It is designed to be used with line-based machines
and tools (e.g. serial console) so that every new line
is appended to the bottom of the screen.
Printed lines are never rewritten!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{srcname}-%{version}

%build

%make_build
%install
make DESTDIR=%{buildroot} install
%find_lang python-%{srcname}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n python3-simpleline -f %{oreon_filedir}/python3-simpleline.list

%changelog

%autochangelog
