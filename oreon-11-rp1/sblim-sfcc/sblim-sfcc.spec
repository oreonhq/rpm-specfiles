%global source0_hash 1b8f187583bc6c6b0a63aae0165ca37892a2a3bd4bb0682cd76b56268b42c3d6

#
# $Id: sblim-sfcc.spec,v 1.4 2010/03/03 07:57:28 vcrhonek Exp $
#
# Package spec for sblim-sfcc
#

Summary: Small Footprint CIM Client Library
Name: sblim-sfcc
Version: 2.2.8
Release: 30%{?dist}
License: EPL-1.0
URL: http://www.sblim.org
Source0:        http://downloads.sourceforge.net/project/sblim/sblim-sfcc/sblim-sfcc-2.2.8.tar.bz2
# Patch0: fixes docdir name and removes install of COPYING with license
#   which is included through %%license
Patch0: sblim-sfcc-2.2.8-docdir-license.patch
Patch1: c99.patch
Patch2: c89.patch
BuildRequires: make
BuildRequires: curl-devel chrpath
BuildRequires: gcc gcc-c++

%Description
Small Footprint CIM Client Library Runtime Libraries

%package devel
Summary: Small Footprint CIM Client Library
Requires: %{name} = %{version}-%{release}

%Description devel
Small Footprint CIM Client Library Header Files and Link Libraries


%prep

%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%autopatch -p1

%build
chmod a-x backend/cimxml/*.[ch]

%configure
make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install
# remove unused libtool files
rm -rf %{buildroot}/%{_libdir}/*a
# remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcmpisfcc.so.1.0.0

%ldconfig_scriptlets


%files
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/libcimcClientXML.so
%{_mandir}/man3/*.3.gz
%{_docdir}/*

%files devel
%{_includedir}/CimClientLib/*
%{_includedir}/cimc/*
%{_libdir}/libcimcclient.so
%{_libdir}/libcmpisfcc.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.8-30
- Prepare for Oreon 11 (RP1)
