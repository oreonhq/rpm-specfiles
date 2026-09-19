%global source0_hash 6963dd84819713aafdd55e5314dcce6df5a37430b62fd9c48770e9f1a467b2b0

Name:           python-kitchen
Version:        1.2.6
Release:        28%{?dist}
Summary:        Small, useful pieces of code to make python coding easier

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pypi.python.org/pypi/kitchen/
Source0:        https://github.com/fedora-infra/kitchen/archive/%{version}.tar.gz

Patch0:         kitchen-1.2.6-sphinx-ext-imgmath.patch

BuildArch:      noarch

BuildRequires:  langpacks-pt_BR

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-test
BuildRequires:  python%{python3_pkgversion}-chardet
%if 0%{?rhel}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%description
kitchen includes functions to make gettext easier to use, handling unicode
text easier (conversion with bytes, outputting xml, and calculating how many
columns a string takes), and compatibility modules for writing code that uses
python-2.7 modules but needs to run on python-2.3.

%package -n python%{python3_pkgversion}-kitchen
Summary:    Small, useful pieces of code to make python 3 coding easier
%{?python_provide:%python_provide python%{python3_pkgversion}-kitchen}

Requires:   python%{python3_pkgversion}
Requires:   python%{python3_pkgversion}-chardet

%description -n python%{python3_pkgversion}-kitchen
kitchen includes functions to make gettext easier to use, handling unicode
text easier (conversion with bytes, outputting xml, and calculating how many
columns a string takes).

This is the python3 version of the kitchen module.

%package -n python%{python3_pkgversion}-kitchen-doc
Summary:    API documentation for the Kitchen python3 module
#Requires: python3-kitchen = %{version}-%{release}
%description -n python%{python3_pkgversion}-kitchen-doc
kitchen includes functions to make gettext easier to use, handling unicode
text easier (conversion with bytes, outputting xml, and calculating how many
columns a string takes).

This package contains the API documenation for programming with the
python-3 version of the kitchen library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n kitchen-%{version}

# Remove bundled egg info, if any.
rm -rf *.egg*

%build
%{py3_build}

# Build docs
%if 0%{?rhel}
sphinx-build kitchen3/docs/ build/sphinx/html
cp -pr build/sphinx/html .
rm -rf html/.buildinfo
%endif

%install
%{py3_install}

# %check
# # In current mock, the PATH isn't being reset.  This causes failures in some
# # subprocess tests as a check tests /root/bin/PROGRAM and fails with Permission
# # Denied instead of File Not Found.  reseting the PATH works around this.
# PATH=/bin:/usr/bin
# PYTHONPATH=.:kitchen3/ nosetests-%{python3_version} kitchen3/tests/

%files -n python%{python3_pkgversion}-kitchen
%doc README.rst NEWS.rst
%license COPYING COPYING.LESSER
%{python3_sitelib}/kitchen*

%files -n python%{python3_pkgversion}-kitchen-doc
%doc kitchen3/docs/*
%license COPYING COPYING.LESSER
%if 0%{?rhel}
%doc html
%endif

%changelog
%autochangelog
