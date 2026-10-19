%global source0_hash 4a0a02cb1dc48bc9a0873ebb3ef9b031f9288baf13a3573f885a8504f9c317c5
Name:           cdsclient
Version:        4.07
Release:        1%{?dist}
Summary:        Tools to query databases at CDS
License:        GPL-3.0-only
URL:            https://cdsarc.u-strasbg.fr/doc/cdsclient.html
Source0:        https://cdsarc.cds.unistra.fr/ftp/pub/sw/cdsclient-%{version}.tar.gz
Patch0:         fix_makefile_debuginfo.patch
Patch1:         abibcode_share_location_trim.patch
Requires:       wget
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The cdsclient package is a set of C and shell routines which can be built on
Unix stations or PCs running Linux, which once compiled allow to query some 
databases located at CDS or on mirrors over the network.

The cdsclient package includes two generic query programs:
- vizquery, a program to remotely query VizieR. It connects the VizieR server
  via the HTTP protocol (requires an access to the port 80)
- find_cats, a program for fast access to large surveys from a list of 
  positions, via a dedicated client (requires an access to the port 1660)
  Specific programs like find2mass or finducac3 are connecting directly to one
  of the very large surveys available from CDS (a very large survey has 107 
  or more rows).
  

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
sed -i -e '1 s|python|python3|' catClient.py

%build

CFLAGS="$CFLAGS --std=gnu17"
%configure 
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_datadir}/%{name}
%make_install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}
rm -f %{buildroot}%{_prefix}/versions
rm -f %{buildroot}%{_bindir}/find_cats.gz
mv %{buildroot}%{_bindir}/abibcode.awk %{buildroot}%{_datadir}/%{name}/abibcode.awk
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
