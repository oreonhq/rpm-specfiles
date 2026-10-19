%global source0_hash 5c9ee9b2155d9e578ae3ce8d6460deb6b8a8d51cff897b88ce0357bb9512d3e8
Name:           rudesocket
Version:        1.3.0
Release:        40%{?dist}
Summary:        Library (C++ API) for creating client sockets
License:        GPL-2.0-or-later
URL:            http://www.rudeserver.com/socket
Source0:        http://homeless.fedorapeople.org/rudesocket/rudesocket-%{version}.tar.bz2
Patch0:         rudesocket-1.3.0-leak-connection.patch
Patch1:         rudesocket-1.3.0-timeout.patch
Requires:       openssl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
rudesocket is a library provides client socket services to an application.
In addition to normal and SSL TCP connections, it supports 
proxies, SOCK4 and SOCKS5 servers. Furthermore, it allows you 
to chain proxies together.

%package        devel
Summary:        Development files for rudesocket
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
rudesocket is a library provides client socket services to an application.
In addition to normal and SSL TCP connections, it supports 
proxies, SOCK4 and SOCKS5 servers. Furthermore, it allows you 
to chain proxies together. The rudesocket-devel package 
contains libraries, header files, and documentation needed 
to develop C++ applications using rudesocket. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .leak
%patch -P1 -p1 -b .timeout

%build

autoreconf --verbose --force --install
%configure --disable-static --with-openssl
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rudesocket-devel -f %{oreon_filedir}/rudesocket-devel.list

%changelog

%autochangelog
