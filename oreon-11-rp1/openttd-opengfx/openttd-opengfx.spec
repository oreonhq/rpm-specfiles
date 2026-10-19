%global source0_hash 0c3575cf70fb3ccaa2c2a8d3525598d10534a1f4401fa70a98814ecab5287e56
Version:        8.0
%global forgeurl https://github.com/OpenTTD/OpenGFX
%global tag %{version}
%forgemeta
%global ogfx_make_opts V=_ PYTHON=/usr/bin/python3
Name:           openttd-opengfx
Release:        1%{?dist}
Summary:        OpenGFX replacement graphics for OpenTTD
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/OpenGFX-%{version}.tar.gz
Source100:      opengfx-%{version}-revision-info.txt
Source101:      opengfx-%{version}.check.md5
BuildArch:      noarch
Requires:       openttd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gimp
BuildRequires:  grfcodec
BuildRequires:  make
BuildRequires:  nml
BuildRequires:  python3
# /oreon:deps
%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set. The main goal of OpenGFX therefore is to provide a
set of free base graphics which make it possible to play OpenTTD without
requiring the (copyrighted) files from the TTD CD. This potentially increases
the OpenTTD fan base and makes it a true free game (with "free" as in both
"free beer" and "free speech").

As of version 0.2.0 OpenGFX has a full set of sprites. Future versions will aim
to improve the graphics. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
cp %{SOURCE100} .ottdrev

%build

make %{ogfx_make_opts} maintainer-clean
make %{ogfx_make_opts} %{?_smp_mflags}
%install
make install %{ogfx_make_opts} INSTALL_DIR=%{buildroot}%{_datadir}/openttd/baseset/opengfx
%oreon_autofiles main

%check

cp %{SOURCE101} opengfx-%{version}.check.md5
make check %{ogfx_make_opts} || true
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
