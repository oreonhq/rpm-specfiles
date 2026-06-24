%global source0_hash none

Name:		libnfs
Version:	6.0.2
Release:	7%{?dist}
Summary:	Client library for accessing NFS shares over a network
# The library is licensed as LGPL-2.1-or-later
# The protocol definition is BSD-2-Clause
# The utility and examples are GPL-3.0-or-later
License:	LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
URL:		https://github.com/sahlberg/libnfs
Source0:	%{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

# https://github.com/sahlberg/libnfs/pull/518
Patch0:         libnfs-6.0.2-fix_gnutls_undefined_symbols.patch
# https://github.com/sahlberg/libnfs/commit/2cdfedaba379cbb512d3c203a1b9eae795f4fb23
Patch1:         libnfs-6.0.2-fix_missing_include.patch

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
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
%{_libdir}/libnfs.so.16*
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

