%global source0_hash 633a2a84d87237caacd227c9fb42a4b5cd7dec83864f277e933916c2e8e4f0c1
%global project_owner MapServer
%global project_name mapcache
%global maj 1
%global min 14
%global micro 1
ExcludeArch: i686
Name:           mod_mapcache
Version:        %{maj}.%{min}.%{micro}
Release:        1%{?dist}
Summary:        Caching server for WMS layers
License:        MIT AND BSD-3-Clause
URL:            http://mapserver.org/mapcache/
Source0:        https://github.com/%{project_owner}/%{project_name}/releases/download/rel-%{maj}-%{min}-%{maj}/%{project_name}-%{version}.tar.gz
Requires:       httpd
Requires:       libmapcache%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  fcgi-devel
BuildRequires:  gcc
BuildRequires:  gdal-devel
BuildRequires:  geos-devel
BuildRequires:  httpd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  lmdb-devel
BuildRequires:  pixman-devel
BuildRequires:  proj-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmltoman
# /oreon:deps
%description
This is the MapCache module for the Apache web server implementing OGC web
services. An alternative mapcache FastCGI program is available in
libmapcache-fcgi.

%pre

%sysusers_create_compat %{SOURCE1}
%package -n libmapcache
Summary: The shared library for mapcache
Requires: mapserver%{?_isa}
%description -n libmapcache
The shared library files for libmapcache

%package -n libmapcache-devel
Summary: Development files for mapcache
%description -n libmapcache-devel
Development files for mapcache; these files are needed when building binary
packages against libmapcache.

%package -n libmapcache-doc
Summary: Documentation files for mapcache
BuildArch: noarch
%description -n libmapcache-doc
Documentation files for mapcache.

%package -n libmapcache-fcgi
Summary: An fcgi implementation for mapcache
Requires: libmapcache%{?_isa} = %{version}-%{release}
%description -n libmapcache-fcgi
This package contains the mapcache FastCGI program, as alternative to the
 Apache module available in mod_mapcache.

%package -n libmapcache-tools
Summary: Tools for mapcache
%description -n libmapcache-tools
Provides command-line utilities for mapcache

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{project_name}-%{version}

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DWITH_MEMCACHE=1 -DCMAKE_SKIP_BUILD_RPATH=TRUE . 
%cmake_build
%install
%cmake_install
for f in \
  %{buildroot}%{_bindir}/{mapcache_seed,mapcache.fcgi,mapcache_detail} \
  %{buildroot}%{_libdir}/libmapcache.so* \
  %{buildroot}%{_libdir}/httpd/modules/mod_mapcache.so;
do
 chrpath --delete $f 
done
install -p -D -m 0644 mapcache.xml %{buildroot}%{_sysconfdir}/mapcache.xml
install -p -D -m 0644 mapcache.xml.sample %{buildroot}%{_datadir}/mapcache/mapcache.xml.sample
pushd include
for f in *.h; do
  install -p -D -m 0644 $f %{buildroot}%{_includedir}/libmapcache/$f;
done
popd
install -p -D -d -m 0755 %{buildroot}%{_localstatedir}/cache/mapcache/
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/mapcache.conf
install -p -D -d -m 0755 %{buildroot}%{_mandir}/man1
xmltoman %{SOURCE2} > %{buildroot}%{_mandir}/man1/mapcache_detail.1
xmltoman %{SOURCE3} > %{buildroot}%{_mandir}/man1/mapcache_seed.1
%oreon_autofiles libmapcache usr/*/lib*.so.*
%oreon_autofiles libmapcache-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libmapcache-doc usr/*/lib*.so.*
%oreon_autofiles libmapcache-fcgi usr/*/lib*.so.*
%oreon_autofiles libmapcache-tools usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmapcache -f %{oreon_filedir}/libmapcache.list
%files -n libmapcache-devel -f %{oreon_filedir}/libmapcache-devel.list
%files -n libmapcache-doc -f %{oreon_filedir}/libmapcache-doc.list
%files -n libmapcache-fcgi -f %{oreon_filedir}/libmapcache-fcgi.list
%files -n libmapcache-tools -f %{oreon_filedir}/libmapcache-tools.list

%changelog

%autochangelog
