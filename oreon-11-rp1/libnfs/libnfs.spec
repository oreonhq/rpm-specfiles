%global source0_hash 188a8a5de2ad2099a2e97e42f34721bfc4c16c8d33808de0f7484f99d714a3df
Name:		libnfs
Version:	7.0.2
Release:        1%{?dist}
Summary:        Client library for accessing NFS shares over a network
License:	LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
URL:		https://github.com/sahlberg/libnfs
Source0:        https://github.com/sahlberg/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The libnfs package contains a library of functions for accessing NFSv2
and NFSv3 servers from user space. It provides a low-level, asynchronous
RPC library for accessing NFS protocols, an asynchronous library with
POSIX-like VFS functions, and a synchronous library with POSIX-like VFS
functions.

%package devel
Summary:	Development files for libnfs
License:	LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The libnfs-devel package contains libraries and header files for
developing applications that use libnfs.

%package utils
Summary:	Utilities for accessing NFS servers
License:	GPL-3.0-or-later
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description utils
The libnfs-utils package contains simple client programs for accessing
NFS servers using libnfs.

%prep

%setup -q -n %{name}-%{name}-%{version}
autoreconf -vif

%build

%configure --disable-static --disable-examples --disable-werror \
           --enable-pthread
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build V=1
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libnfs-devel -f %{oreon_filedir}/libnfs-devel.list
%files -n libnfs-utils -f %{oreon_filedir}/libnfs-utils.list

%changelog

%autochangelog
