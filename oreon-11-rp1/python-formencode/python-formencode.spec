%global source0_hash e17f16199d232e54f67912004f3ad333cdbbb81a1a1a10238acf09bab99f9199
%global srcname FormEncode
Name:           python-formencode
Version:        2.1.1
Release:        1%{?dist}
Summary:        HTML form validation, generation, and convertion package
License:        LicenseRef-Callaway-Python
URL:            http://formencode.org/
Source0:        https://files.pythonhosted.org/packages/source/f/formencode/formencode-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm) >= 7
Requires:       python3-formencode = %{version}-%{release}
# /oreon:deps
%description
FormEncode validates and converts nested structures. It allows for a 
declarative form of defining the validation, and decoupled processes 
for filling and generating forms.

%package -n python3-formencode
Summary: HTML form validation, generation, and convertion package
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-wheel
BuildRequires: python3-pip
BuildRequires: python3-setuptools_scm
Requires: python3-setuptools
Requires: python-formencode-langpacks
%description -n python3-formencode
FormEncode validates and converts nested structures. It allows for a.
declarative form of defining the validation, and decoupled processes.
for filling and generating forms.

This package contains the python3 version of the module.

%package -n python-formencode-langpacks
Summary: Locale files for the python-formencode library
%description -n python-formencode-langpacks
The FormEncode library validates and converts nested structures.  This package
contains the locale files for localizing the message strings in code within the
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir formencode-%{version}
%oreon_prep
%build

sed -i "s|'setuptools_scm_git_archive',||" setup.py
%pyproject_wheel
%install
%pyproject_install
rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/docs/
rm -f $RPM_BUILD_ROOT%{_prefix}/LICENSE.txt
%oreon_autofiles python3-formencode usr/lib/python3*/site-packages/formencode* usr/lib64/python3*/site-packages/formencode* usr/bin/*
%oreon_autofiles python-formencode-langpacks usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/formencode* usr/lib64/python3*/site-packages/formencode* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n python3-formencode -f %{oreon_filedir}/python3-formencode.list
%files -n python-formencode-langpacks -f %{oreon_filedir}/python-formencode-langpacks.list

%changelog

%autochangelog
