%global source0_hash dda98990d93cded815ee425101674ad2f48438fff76b3d4d5d3f91e380e9cc49

Name:		dcap
Version:	2.47.14
Release:	12%{?dist}
Summary:	Client Tools for dCache

#		plugins/gssapi/{base64.[ch],util.c} - BSD license
#		the rest - LGPLv2+ license
License:	LGPL-2.0-or-later AND BSD-3-Clause
URL:		https://www.dcache.org/manuals/libdcap.shtml
Source0:	https://github.com/dCache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#		https://github.com/dCache/dcap/pull/28
Patch0:		0001-Add-missing-include-crypt.h.patch
#		https://github.com/dCache/dcap/pull/29
Patch1:		0001-Don-t-define-the-dc_xxx64-macros-while-compiling-dca.patch
#		https://github.com/dCache/dcap/pull/30
Patch2:		0001-Fix-spelling-errors.patch
Patch3:		0002-Avoid-format-errors-when-using-64-bit-time_t-on-32-b.patch

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	globus-gssapi-gsi-devel
BuildRequires:	krb5-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	CUnit-devel
BuildRequires: libxcrypt-devel

%description
dCache is a distributed mass storage system.
This package contains the client tools.

%package libs
Summary:	Client Libraries for dCache
License:	LGPL-2.0-or-later

%description libs
dCache is a distributed mass storage system.
This package contains the client libraries.

%package devel
Summary:	Client Development Files for dCache
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
dCache is a distributed mass storage system.
This package contains the client development files.

%package tunnel-gsi
Summary:	GSI tunnel for dCache
License:	LGPL-2.0-or-later AND BSD-3-Clause
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-gsi
This package contains the gsi tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-krb
Summary:	Kerberos tunnel for dCache
License:	LGPL-2.0-or-later AND BSD-3-Clause
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-krb
This package contains the kerberos tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-ssl
Summary:	SSL tunnel for dCache
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-ssl
This package contains the ssl tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-telnet
Summary:	Telnet tunnel for dCache
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-telnet
This package contains the telnet tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
./bootstrap.sh

%configure \
    --disable-static \
    --with-tunneldir=%{_libdir}/%{name} \
    --with-globus-include=%{_includedir}/globus \
    --with-globus-lib=/dummy
%make_build

%install
%make_install

# Remove libtool archive files
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/%{name}/*.la

# We are installing the docs in the files sections
rm -rf %{buildroot}/%{_docdir}

%check
%make_build check

%files
%{_bindir}/dccp
%{_mandir}/man1/dccp.1*

%files libs
%{_libdir}/libdcap.so.*
%{_libdir}/libpdcap.so.*
%dir %{_libdir}/%{name}
%license LICENSE COPYING.LIB AUTHORS

%files devel
%{_libdir}/libdcap.so
%{_libdir}/libpdcap.so
%{_includedir}/dc_hack.h
%{_includedir}/dcap.h
%{_includedir}/dcap_errno.h

%files tunnel-gsi
%{_libdir}/%{name}/libgsiTunnel.so
%license plugins/gssapi/Copyright

%files tunnel-krb
%{_libdir}/%{name}/libgssTunnel.so
%license plugins/gssapi/Copyright

%files tunnel-ssl
%{_libdir}/%{name}/libsslTunnel.so

%files tunnel-telnet
%{_libdir}/%{name}/libtelnetTunnel.so

%changelog
%autochangelog
