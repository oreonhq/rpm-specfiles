%global source0_hash 089db78d7ac982354bdbf39d973baf09581e6904ac4c92a98c5caadb3de44680
Summary:        RDF Parser Toolkit for Redland
Name:    raptor2
Version: 2.0.16
Release:        1%{?dist}
License: GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR Apache-2.0
Source0:        http://download.librdf.org/source/raptor2-%{version}.tar.gz
URL:     http://librdf.org/raptor/
Patch5: raptor2-libxml2.patch
Conflicts: raptor < 1.4.21-10
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libxslt)
# /oreon:deps
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

%define distrooptions --with-yajl=yes
%configure \
  --disable-static \
  --enable-release \
  --with-icu-config=/usr/bin/icu-config \
  %{distrooptions}
%make_build
%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion raptor2)" = "%{version}"
make check 
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n raptor2-devel -f %{oreon_filedir}/raptor2-devel.list

%changelog

%autochangelog
