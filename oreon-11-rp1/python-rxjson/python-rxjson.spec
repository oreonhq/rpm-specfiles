%global source0_hash 2ed3d5dadf9e8aef2ef1f3cdfa3cf9abae99c9eac5a2db0267f17a9dae3a66e1
%global srcname rxjson
Name:             python-%{srcname}
Summary:        JSON RX Schema validation tool
Version:          0.3
Release:        29%{?dist}
License:          GPL-2.0-or-later
URL:              https://pypi.python.org/pypi/rxjson
Source0:        https://files.pythonhosted.org/packages/source/%/%{srcname/%{srcname-%{version}.tar.gz
BuildArch:        noarch
# oreon:deps
BuildRequires:  python3-d2to1
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        JSON RX Schema validation tool
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-d2to1
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-rxjson -f %{oreon_filedir}/python3-rxjson.list

%changelog

%autochangelog
