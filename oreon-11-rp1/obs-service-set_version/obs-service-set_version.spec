%global source0_hash 000982fa3da7e97e885aecb0011bff72ce0ae4da397e9686093c7def25db4e4f
%global service set_version
Name:           obs-service-%{service}
Version:        0.6.6
Release:        1%{?dist}
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Recommends:     python3dist(packaging)
Requires:       python3
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(ddt)
BuildRequires:  python3dist(packaging)
BuildRequires:  sed
# /oreon:deps
%description
This is a source service for openSUSE Build Service.

Very simply script to update the version in .spec or .dsc files according to
a given version or to the existing files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sed -i -e "1 s,#!/usr/bin/python$,#!%{__python3}," set_version
%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 set_version %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 set_version.service %{buildroot}%{_prefix}/lib/obs/service
%oreon_autofiles main

%check

%{__python3} -m unittest discover tests/
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
