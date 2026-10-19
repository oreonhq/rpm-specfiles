%global source0_hash dd3b7d8f773219588867a33ca910999243aa941d2ec3c3b05bc4a26a590100f7
%{?python_enable_dependency_generator}
%global py2support 0
%global srcname cson
Name:           python-%{srcname}
Version:        0.8
Release:        1%{?dist}
Summary:        A Coffescript Object Notation (CSON) parser for Python 2 and Python 3
License:        MIT
URL:            https://github.com/avakar/pycson
Source0:        https://github.com/avakar/pycson/archive/%{version}/pycson-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
A python parser for the Coffeescript Object Notation (CSON).

%package -n python3-%{srcname}
Summary:        A Coffescript Object Notation (CSON) parser for Python 2 and Python 3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
A python parser for the Coffeescript Object Notation (CSON).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pycson-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-cson -f %{oreon_filedir}/python3-cson.list

%changelog

%autochangelog
