%global source0_hash e17f16199d232e54f67912004f3ad333cdbbb81a1a1a10238acf09bab99f9199

%global srcname FormEncode

Name:           python-formencode
Version:        2.1.1
Release:        7%{?dist}
Summary:        HTML form validation, generation, and convertion package  
# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            http://formencode.org/
Source0:        %pypi_source formencode
BuildArch:      noarch

## For test suite
## Note that the test suite requires all kinds of network connectivity, so we
## can't run it in koji.
#BuildRequires: python3-nose
#BuildRequires: python3-dns

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
#BuildRequires: python3-setuptools_scm_git_archive

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

%autosetup -n formencode-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
# remove setuptools_scm_git_archive from setup requires
sed -i "s|'setuptools_scm_git_archive',||" setup.py
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l formencode

rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/docs/
# packaged as license, remove this file with wrong path
rm -f $RPM_BUILD_ROOT%{_prefix}/LICENSE.txt

#%%check
## Note that the test suite requires all kinds of network connectivity, so we
## can't run it in koji.
#PYTHONPATH=$(pwd) nosetests-%%{python3_version}

%check
%pyproject_check_import

%files -n python3-formencode -f %{pyproject_files}
%doc docs
%license LICENSE.txt

%files -n python-formencode-langpacks

%changelog
%autochangelog
