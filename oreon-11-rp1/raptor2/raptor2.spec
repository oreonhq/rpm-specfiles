%global source0_hash 089db78d7ac982354bdbf39d973baf09581e6904ac4c92a98c5caadb3de44680

Summary: RDF Parser Toolkit for Redland
Name:    raptor2
Version: 2.0.16
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ or LGPLv2+ or ASL 2.0 - review is highly recommended.
License: GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR Apache-2.0
Source:        http://download.librdf.org/source/raptor2-%{version}.tar.gz
URL:     http://librdf.org/raptor/

## upstreamable patches
Patch5: raptor2-libxml2.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: curl-devel
BuildRequires: gtk-doc
BuildRequires: libicu-devel
BuildRequires: pkgconfig(libxslt)
%if ! 0%{?rhel}
BuildRequires: yajl-devel
%endif

# when /usr/bin/rappor moved here  -- rex
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# hack to nuke rpaths
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

## unpackaged files
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
