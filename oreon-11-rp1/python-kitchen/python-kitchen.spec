%global source0_hash 6963dd84819713aafdd55e5314dcce6df5a37430b62fd9c48770e9f1a467b2b0
Name:           python-kitchen
Version:        1.2.6
Release:        1%{?dist}
Summary:        Small, useful pieces of code to make python coding easier
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pypi.python.org/pypi/kitchen/
Source0:        https://github.com/fedora-infra/kitchen/archive/%{version}.tar.gz
Patch0:         kitchen-1.2.6-sphinx-ext-imgmath.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  langpacks-pt_BR
BuildRequires:  python3-chardet
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-test
# /oreon:deps
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
%install
%{py3_install}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-kitchen -f %{oreon_filedir}/python3-kitchen.list
%files -n python3-kitchen-doc -f %{oreon_filedir}/python3-kitchen-doc.list

%changelog

%autochangelog
