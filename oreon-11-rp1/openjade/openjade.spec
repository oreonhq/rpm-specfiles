# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1d2d7996cc94f9b87d0c51cf0e028070ac177c4123ecbfd7ac1cb8d0b7d322d1

Name: openjade
Version: 1.3.2
Release: 1%{?dist}
Summary: DSSSL implementation
License: LicenseRef-DMIT
URL: https://openjade.sourceforge.net/
Source0: https://downloads.sourceforge.net/openjade/openjade-%{version}.tar.gz
Patch0: openjade-ppc64.patch
Patch1: openjade-1.3.1-nsl.patch
Patch2: openjade-deplibs.patch
Patch3: openjade-nola.patch
Patch4: openjade-1.3.2-gcc46.patch
Patch5: openjade-getoptperl.patch
Patch6: openjade-configure-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: opensp-devel
BuildRequires: perl-interpreter

Requires: sgml-common
Provides: jade = %{version}-%{release}

%description
OpenJade implements DSSSL and can transform SGML and XML documents into
formats including XML, RTF, TeX, MIF, and SGML.

%prep
%oreon_sha256
%autosetup -n openjade-%{version} -p1
automake_libdir=$(automake --print-libdir)
cp -p "$automake_libdir"/config.guess "$automake_libdir"/config.sub config/

%build
export CXXFLAGS="%{build_cxxflags} -fno-lifetime-dse"
%oreon_configure \
    --disable-static \
    --datadir=%{_datadir}/sgml/%{name}-%{version} \
    --enable-splibdir=%{_libdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|' libtool
%oreon_make

%install
make install install-man DESTDIR=%{buildroot}
ln -s openjade %{buildroot}%{_bindir}/jade
printf '.so man1/openjade.1\n' > %{buildroot}%{_mandir}/man1/jade.1
cp dsssl/catalog %{buildroot}%{_datadir}/sgml/%{name}-%{version}/
cp dsssl/dsssl.dtd dsssl/style-sheet.dtd dsssl/fot.dtd \
    %{buildroot}%{_datadir}/sgml/%{name}-%{version}/
mkdir -p %{buildroot}%{_sysconfdir}/sgml
touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}.soc
ln -s %{name}-%{version}.soc %{buildroot}%{_sysconfdir}/sgml/%{name}.soc
rm -f %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/*.la

%check
./jade/openjade -v 2>&1 | grep -F 'OpenJade'

%post
%{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>&1 || :

%preun
if [ "$1" -eq 0 ]; then
    %{_bindir}/install-catalog --remove \
        %{_sysconfdir}/sgml/%{name}-%{version}.soc \
        %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>&1 || :
    touch %{_sysconfdir}/sgml/%{name}-%{version}.soc
fi

%files
%license COPYING
%doc README VERSION jadedoc/* dsssl/README.jadetex
%config(noreplace) %{_sysconfdir}/sgml/%{name}-%{version}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*
%{_datadir}/sgml/%{name}-%{version}

%changelog
%autochangelog
