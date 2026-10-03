Name:		libnfs
Version:	7.0.2
Release:	%autorelease
Summary:	Client library for accessing NFS shares over a network
# The library is licensed as LGPL-2.1-or-later
# The protocol definition is BSD-2-Clause
# The utility and examples are GPL-3.0-or-later
License:	LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
URL:		https://github.com/sahlberg/libnfs
Source0:	%{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gnutls-devel
BuildRequires:	krb5-devel
BuildRequires:	libtool
BuildRequires:	make

%description
The libnfs package contains a library of functions for accessing NFSv2
and NFSv3 servers from user space. It provides a low-level, asynchronous
RPC library for accessing NFS protocols, an asynchronous library with
POSIX-like VFS functions, and a synchronous library with POSIX-like VFS
functions.


%package devel
Summary:	Development files for libnfs
# The library is licensed as LGPLv2+, the protocol definition is BSD
# and the example source code is GPLv3+.
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

%files
%{_libdir}/libnfs.so.17*
%doc README
%license COPYING
%license LICENCE-*.txt

%files devel
%{_libdir}/libnfs.so
%{_includedir}/nfsc/
%{_libdir}/pkgconfig/libnfs.pc
%doc examples/*.c

%files utils
%{_bindir}/nfs-*
%{_mandir}/man1/nfs-*.1*

%changelog
%autochangelog
