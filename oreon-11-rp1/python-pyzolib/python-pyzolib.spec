%global source0_hash 35f949964615a1d0dead0711212dc73d0f0b8a323e27e9cab3b26d14649ad006
Name:           python-pyzolib
Version:        0.3.4
Release:        1%{?dist}
Summary:        Utilities for the Pyzo environment
License:        LicenseRef-Callaway-BSD
URL:            http://www.pyzo.org
Source0:        https://pypi.python.org/packages/source/p/pyzolib/pyzolib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python%{python3_pkgversion}-pyzolib
Summary:        Utilities for the Pyzo environment
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%description -n python%{python3_pkgversion}-pyzolib

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyzolib-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pyzolib -f %{oreon_filedir}/python3-pyzolib.list

%changelog

%autochangelog
