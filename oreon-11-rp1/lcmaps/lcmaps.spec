%global source0_hash eeb3f2521fc0fab79c4a2a813b9b05586ee4828d663529d2425b60a68c9fc401
Summary:        Grid (X.509) and VOMS credentials to local account mapping service
Name: lcmaps
Version: 1.6.7
Release:        1%{?dist}
License: Apache-2.0
URL: https://wiki.nikhef.nl/grid/LCMAPS
Source0:        https://software.nikhef.nl/security/lcmaps/lcmaps-%{version}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gsi-credential-devel
BuildRequires:  globus-gsi-proxy-core-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  make
BuildRequires:  voms-devel
# /oreon:deps
%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

%package without-gsi
Summary: Grid mapping service without GSI
%description without-gsi
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

This version is built without support for the GSI protocol.

%package devel
Summary: LCMAPS plug-in API header files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-common-devel%{?_isa} = %{version}-%{release}
Requires: globus-gssapi-gsi-devel%{?_isa}
Requires: openssl-devel%{?_isa}
Provides: %{name}-globus-interface = %{version}-%{release}
Obsoletes: %{name}-globus-interface < 1.6.1-4
Provides: %{name}-openssl-interface = %{version}-%{release}
Obsoletes: %{name}-openssl-interface < 1.6.1-4
Provides: %{name}-interface = %{version}-%{release}
Obsoletes: %{name}-interface < 1.4.31-1
%description devel
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

This package contains the files necessary to compile and link
against the LCMAPS library.

%package common-devel
Summary: LCMAPS plug-in API header files
Provides: %{name}-basic-interface = %{version}-%{release}
Obsoletes: %{name}-basic-interface < 1.6.1-4
%description common-devel
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the header files and interface definitions
for client applications.

%package without-gsi-devel
Summary: LCMAPS development libraries
Requires: %{name}-without-gsi%{?_isa} = %{version}-%{release}
Requires: %{name}-common-devel%{?_isa} = %{version}-%{release}
%description without-gsi-devel
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

This package contains the development libraries to build
without the GSI protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

mkdir build-without-gsi && cd build-without-gsi && ln -s ../configure
%configure --disable-gsi-mode --disable-static
%define fixlibtool() sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool\
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool\
sed -i -e 's! -shared ! -Wl,--as-needed\\0!g' libtool
%fixlibtool
make %{?_smp_mflags}
cd ..
mkdir build && cd build && ln -s ../configure
%{configure} --disable-static
%fixlibtool
make %{?_smp_mflags}
cd ..
%install
rm -rf $RPM_BUILD_ROOT
cd build-without-gsi
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
cd build
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/lcmaps
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/lcmaps
rm -rf ${RPM_BUILD_ROOT}%{_docdir}
%ldconfig_scriptlets
%ldconfig_scriptlets without-gsi
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lcmaps-without-gsi -f %{oreon_filedir}/lcmaps-without-gsi.list
%files -n lcmaps-devel -f %{oreon_filedir}/lcmaps-devel.list
%files -n lcmaps-common-devel -f %{oreon_filedir}/lcmaps-common-devel.list
%files -n lcmaps-without-gsi-devel -f %{oreon_filedir}/lcmaps-without-gsi-devel.list

%changelog

%autochangelog
