%global source0_hash 72ed6f7de45a50feea51017df8cf0829a903ca8b8d0b2453261dfbb1cdeb9481
%global modname daemonize
Name:           python-%{modname}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Library for writing system daemons in Python
License:        MIT
URL:            https://github.com/thesharp/daemonize
Source0:        https://github.com/thesharp/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:        Library for writing system daemons in Python
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%description -n python3-%{modname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-daemonize -f %{oreon_filedir}/python3-daemonize.list

%changelog

%autochangelog
