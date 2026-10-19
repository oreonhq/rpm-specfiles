%global source0_hash 42aa55fe1d3054ba3c119a4479929913445c48768eb1d36b13db8c6ad1889b81
Name:           systemd-bootchart
Version:        235
Release:        1%{?dist}
Summary:        Boot performance graphing tool
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/systemd/systemd-bootchart
Source0:        https://github.com/systemd/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd
# /oreon:deps
%description
This package provides a binary which can be started during boot early boot to
capture informations about processes and services launched during bootup.
Resource utilization and process information are collected during the boot
process and are later rendered in an SVG chart. The timings for each services
are displayed separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
