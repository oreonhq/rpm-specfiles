%global source0_hash 1d6c53acf160edc9b42e4ba535343b3567f2f341d289b9e63ca6a84372c2c518
%global srcname uswid
Name:           python-%{srcname}
Version:        0.5.2
Release:        1%{?dist}
Summary:        Python module for working with Firmware SBoMs
License:        LGPL-2.1-or-later
URL:            https://github.com/hughsie/python-uswid
Source0:        https://files.pythonhosted.org/packages/source/%/%{srcname/%{srcname-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  git-core
BuildRequires:  python3-cbor2
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-pefile
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Python module for working with Firmware SBoMs
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-cbor2
BuildRequires:  python3-lxml
BuildRequires:  python3-pefile
BuildRequires:  python3-wheel
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' %{srcname}/*.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-uswid -f %{oreon_filedir}/python3-uswid.list

%changelog

%autochangelog
