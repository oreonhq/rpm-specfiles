%global source0_hash 278e255391c1d481631bf40b6721d0138482fda798caae0a977fff8d44c7f513
%global modname maps
Name:           python-%{modname}
Version:        4.2.0
Release:        1%{?dist}
Summary:        Flavors of Python dictionaries
License:        MIT
URL:            https://github.com/pcattori/maps
Source0:        https://github.com/pcattori/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{summary}.

%package     -n python3-%{modname}
Summary:        Flavors of Python dictionaries
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

py.test-%{python3_version} -v
%files -f %{oreon_filedir}/main.list
%files -n python3-maps -f %{oreon_filedir}/python3-maps.list

%changelog

%autochangelog
