%global source0_hash 948412457cfccf0c775dd08e0913fb00f90896a33c79737d571c7312aeaf55c6

# Turn off the brp-python-bytecompile script
%global srcname pmw

Name: python-pmw
Version: 2.1.1
Release: 16%{?dist}
Summary: Python powerwidgets
License: MIT AND GPL-2.0-or-later
URL: https://pmw.sourceforge.net/
Source: https://downloads.sourceforge.net/pmw/Pmw-%{version}.tar.gz
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: dos2unix
BuildArch: noarch

# Fix identation errors, patch created by using 'autopep8-1.6.0'
Patch0: %{name}-fix_identation_error.patch

%description
Pmw is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It consists of a set of base classes and a
library of flexible and extensible megawidgets built on this
foundation. These megawidgets include notebooks, comboboxes, selection
widgets, paned widgets, scrolled widgets and dialog windows

%package -n python3-%{srcname}
Summary: Python powerwidgets
Requires: python3-tkinter
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pmw is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It consists of a set of base classes and a
library of flexible and extensible megawidgets built on this
foundation. These megawidgets include notebooks, comboboxes, selection
widgets, paned widgets, scrolled widgets and dialog windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Pmw-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files Pmw

# file fixes
chmod 644 Pmw/Pmw_1_3_3/doc/*
chmod 644 Pmw/Pmw_2_1_1/doc/*

rm -rf %{buildroot}%{python3_sitelib}/Pmw/Pmw_1_3_3

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc Pmw/Pmw_2_1_1/doc

%changelog
%autochangelog
