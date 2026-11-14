# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 57f4898498a368918b0d49c826aa434bb5b703d2c3b169beb348016ab25617ce

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: opensp
Version: 1.5.2
Release: 1%{?dist}
Summary: SGML and XML parser
License: X11
URL: http://openjade.sourceforge.net/
Source0: https://downloads.sourceforge.net/openjade/OpenSP-%{version}.tar.gz
Patch0: opensp-multilib.patch
Patch1: opensp-nodeids.patch
Patch2: opensp-sigsegv.patch
Patch3: opensp-manpage.patch
Patch4: opensp-configure-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: make
BuildRequires: xmlto

Requires: sgml-common >= 0.5

Provides: bundled(gettext) = 0.14.5

%description
OpenSP is an implementation of the ISO/IEC 8879:1986 standard SGML
(Standard Generalized Markup Language). OpenSP is based on James
Clark's SP implementation of SGML. OpenSP is a command-line
application and a set of components, including a generic API.

%package devel
Summary: Files for developing applications that use OpenSP
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libtool library for developing applications that use OpenSP.

%prep
%oreon_sha256
%autosetup -p1 -n OpenSP-%{version}
iconv -f latin1 -t utf8 ChangeLog -o ChangeLog.tmp
mv -f ChangeLog.tmp ChangeLog
touch lib/parser_inst.cxx

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-http \
    --enable-default-catalog=/etc/sgml/catalog \
    --enable-default-search-path=/usr/share/sgml:/usr/share/xml
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
for file in nsgmls sgmlnorm spam spent sx; do
    ln -s o$file %{buildroot}%{_bindir}/$file
    echo ".so man1/o${file}.1" > %{buildroot}%{_mandir}/man1/${file}.1
done
mv %{buildroot}%{_bindir}/sx %{buildroot}%{_bindir}/sgml2xml
mv %{buildroot}%{_mandir}/man1/{sx,sgml2xml}.1
rm -rf %{buildroot}%{_docdir}/OpenSP
rm -rf %{buildroot}%{_datadir}/OpenSP
%find_lang sp5

%check
make check SHOWSTOPPERS=

%ldconfig_scriptlets

%files -f sp5.lang
%license COPYING
%doc doc/*.htm
%doc docsrc/releasenotes.html
%doc AUTHORS BUGS ChangeLog NEWS README
%doc pubtext/opensp-implied.dcl
%{_bindir}/*
%{_libdir}/libosp.so.*
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/OpenSP/
%{_libdir}/libosp.so

%changelog
%autochangelog
