%global source0_hash 35f949964615a1d0dead0711212dc73d0f0b8a323e27e9cab3b26d14649ad006

Name:           python-pyzolib
Version:        0.3.4
Release:        1%{?dist}
Summary:        Utilities for the Pyzo environment

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.pyzo.org
Source0:        https://pypi.python.org/packages/source/p/pyzolib/pyzolib-%{version}.tar.gz

BuildArch:      noarch

%global _description\
This package implements several small sub-modules and sub-packages that expose\
common functionality in a range of packages and applications in the Pyzo\
framework.

%description %_description

%package -n python%{python3_pkgversion}-pyzolib
Summary:        Utilities for the Pyzo environment
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-pyzolib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyzolib-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-pyzolib
%doc
%{python3_sitelib}/pyzolib/
%{python3_sitelib}/pyzolib-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
