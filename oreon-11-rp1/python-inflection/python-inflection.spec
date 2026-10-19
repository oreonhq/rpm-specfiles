%global source0_hash 1a29730d366e996aaacffb2f1f1cb9593dc38e2ddd30c91250c6dde09ea9b417
%global srcname inflection
Name:           python-%{srcname}
Version:        0.5.1
Release:        20%{?dist}
Summary:        Port of Ruby on Rails inflector to Python
License:        MIT
URL:            https://github.com/jpvanhal/inflection
Source0:        https://files.pythonhosted.org/packages/source/p/python-inflection/python-inflection-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description

%package     -n python3-%{srcname}
Summary:        Port of Ruby on Rails inflector to Python
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%description -n python3-%{srcname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%python3 -m pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-inflection -f %{oreon_filedir}/python3-inflection.list

%changelog

%autochangelog
