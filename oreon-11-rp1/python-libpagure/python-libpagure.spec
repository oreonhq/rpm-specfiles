%global source0_hash af48a3fe5069d3714f6669a4714874380928954a390320e092871696bae7cbd6
%global modname libpagure
Name:           python-libpagure
Version:        0.22
Release:        1%{?dist}
Summary:        A Python library for Pagure APIs
License:        GPL-2.0-or-later
URL:            https://pagure.io/libpagure/
Source0:        https://pagure.io/releases/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-libpagure
Summary:        A Python library for Pagure APIs
%{?python_provide:%python_provide python3-libpagure}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:  python3-requests
%description -n python3-libpagure
A Python library for Pagure APIs

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-libpagure usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-libpagure -f %{oreon_filedir}/python3-libpagure.list

%changelog

%autochangelog
