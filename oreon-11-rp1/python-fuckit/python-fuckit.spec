%global source0_hash 059488e6aa2053da9db5eb5101e2498f608314da5118bf2385acb864568ccc25
%global srcname fuckit
Name:           python-%{srcname}
Version:        4.8.1
Release:        14%{?dist}
Summary:        The Python Error Steamroller
License:        WTFPL
URL:            https://github.com/ajalt/fuckitpy
Source0:        https://pypi.python.org/packages/source/f/fuckit/fuckit-4.8.1.zip
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        The Python Error Steamroller
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
FuckIt.py uses state-of-the-art technology to make sure your Python code runs
whether it has any right to or not. Some code has an error? Fuck it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{srcname}-%{version}

find -name '*.txt' | xargs chmod -x
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-fuckit -f %{oreon_filedir}/python3-fuckit.list

%changelog

%autochangelog
