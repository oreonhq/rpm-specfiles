# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ada7f0ba54787b33485d090d3d2680533520cd4426d2f7fb4782dd4a6a1480ed
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: RDF Parser Toolkit for Redland
Name:    raptor2
Version: 2.0.15
Release: 1%{?dist}

License: GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR Apache-2.0
Source0:        http://download.librdf.org/source/raptor2-%{version}.tar.gz
URL:     http://librdf.org/raptor/

Patch1: 0001-Calcualte-max-nspace-declarations-correctly-for-XML-.patch
Patch2: 0001-CVE-2020-25713-raptor2-malformed-input-file-can-lead.patch

Patch3: raptor2-configure-c99.patch
Patch4: raptor2-c99.patch
Patch5: raptor2-libxml2.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: curl-devel
BuildRequires: gtk-doc
BuildRequires: libicu-devel
BuildRequires: pkgconfig(libxslt)
%if ! 0%{?rhel}
BuildRequires: yajl-devel
%endif

Conflicts: raptor < 1.4.21-10

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package devel
Summary: Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%oreon_sha256
%autosetup -p1

%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif

%build

%if 0%{?rhel}
%define distrooptions --with-yajl=no
%else
%define distrooptions --with-yajl=yes
%endif

%configure \
  --disable-static \
  --enable-release \
  --with-icu-config=/usr/bin/icu-config \
  %{distrooptions}

%make_build

%install
%make_install

rm -fv %{buildroot}%{_libdir}/lib*.la

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion raptor2)" = "%{version}"
make check 

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING* LICENSE.txt LICENSE-2.0.txt
%{_libdir}/libraptor2.so.0*
%{_bindir}/rapper
%{_mandir}/man1/rapper*

%files devel
%doc UPGRADING.html
%{_includedir}/raptor2/
%{_libdir}/libraptor2.so
%{_libdir}/pkgconfig/raptor2.pc
%{_mandir}/man3/libraptor2*
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/raptor2/

%changelog
%autochangelog
