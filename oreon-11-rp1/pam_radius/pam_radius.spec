%global source1_hash e0576899f6a2f2d4de45e59aee3e132bffaa28f8d4b96a661e72494427446c5c
%global source0_hash a1a174c25ed0eae9b2f71f17f11547d9136a59a051dde5c3bdd53addf16bfecf
Name: pam_radius
Summary:        PAM Module for RADIUS Authentication
Version: 3.0.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.freeradius.org/pam_radius_auth/
%global underscored_v 3_0_0
Source0:        https://github.com/FreeRADIUS/%{name}/releases/download/release_%{underscored_v}/%{name}-%{version}.tar.gz
Source1: https://github.com/FreeRADIUS/pam_radius/releases/download/release_%{underscored_v}/pam_radius-%{version}.tar.gz.sig
Requires: pam
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pam-devel
# /oreon:deps
%description
pam_radius is a PAM module which allows user authentication using 
a radius server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pam_radius-%{version}

%build

%configure --enable-werror
make %{?_smp_mflags} CFLAGS="%{optflags} -Wall -fPIC -Wno-unused-but-set-variable -Wno-strict-aliasing"
%install
mkdir -p %{buildroot}/%{_lib}/security
install -p pam_radius_auth.so %{buildroot}/%{_lib}/security
mkdir -p %{buildroot}%{_sysconfdir}
install -p pam_radius_auth.conf %{buildroot}%{_sysconfdir}/pam_radius_auth.conf
%oreon_autofiles main

%post

if [ -e "/etc/pam_radius.conf" ]; then
    mv "/etc/pam_radius.conf" "/etc/pam_radius_auth.conf"
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
