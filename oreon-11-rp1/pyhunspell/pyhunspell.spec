%global source0_hash 021f2b713ebf1af972655b7f7a7669e96d8e2c59f4c984164b3fc1b7b5e2a51c

Name:           pyhunspell
Version:        0.5.5
Release:        13%{?dist}
Summary:        Python bindings for hunspell

License:        LGPL-3.0-or-later
URL:            https://github.com/blatinier/pyhunspell
Source0:        https://github.com/blatinier/pyhunspell/archive/pyhunspell-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  python3-devel

# make it build with hunspell-1.7:
Patch0: pyhunspell-fix-build.patch

%global _description\
These are python bindings for hunspell, that allow to use the hunspell library\
in python.

%description %_description

%package -n python3-pyhunspell
Summary: %summary

%description -n python3-pyhunspell
This package contains a Python3 module to use the hunspell library
from Python3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pyhunspell-%{version}
%patch -P0 -p1 -b .hunspell13

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*'

%check
%pyproject_check_import

%files -n python3-pyhunspell -f %{pyproject_files}
%doc AUTHORS.md CHANGELOG.md COPYING COPYING.LESSER gpl-3.0.txt lgpl-3.0.txt PKG-INFO README.md

%changelog
%autochangelog
