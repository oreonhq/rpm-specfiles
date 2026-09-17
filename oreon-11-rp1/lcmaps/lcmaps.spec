%global source0_hash 80b6024c5b41465efcfaf817f616f8ac05a48e6a64f25427b11b5165cb9b01a0

# Notes:
# The lcmaps-*-devel packages are meant for developing client
# programs. The preferred model of development is to dlopen() the
# interface library at run-time, which means that a) the libraries are
# not required for development at all and b) client programs become
# independent of the run-time version of LCMAPS.  This is why the
# devel packages only contain header files and the .so symlinks are in
# the run-time package.
#
# The LCMAPS interfaces are:
# -basic, which are very simple and do not require openssl,
# -openssl, which include 'basic' and require openssl for x509 structures,
# -globus, which include 'openssl' and require Globus Toolkit functions.
#
# The lcmaps-devel package is the most inclusive, so it's a safe choice
# to install in case of any development work.

Summary: Grid (X.509) and VOMS credentials to local account mapping service
Name: lcmaps
Version: 1.6.6
Release: 19%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://wiki.nikhef.nl/grid/LCMAPS
Source0: https://software.nikhef.nl/security/lcmaps/lcmaps-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: globus-common-devel
BuildRequires: globus-gssapi-gsi-devel
BuildRequires: globus-gss-assist-devel
BuildRequires: globus-gsi-credential-devel
BuildRequires: globus-gsi-proxy-core-devel
BuildRequires: voms-devel
BuildRequires: flex, bison
BuildRequires: make

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
# the pkgconfig requirement is only necessary for EPEL5 and below;
# it's automatic for Fedora and EPEL6.
%if %{?rhel}%{!?rhel:6} <= 5
Requires: pkgconfig
%endif

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
# the pkgconfig requirement is only necessary for EPEL5 and below;
# it's automatic for Fedora and EPEL6.
%if %{?rhel}%{!?rhel:6} <= 5
Requires: pkgconfig
%endif

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
# the pkgconfig requirement is only necessary for EPEL5 and below;
# it's automatic for Fedora and EPEL6.
%if %{?rhel}%{!?rhel:6} <= 5
Requires: pkgconfig
%endif

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

# First configure and build the without-gsi version
mkdir build-without-gsi && cd build-without-gsi && ln -s ../configure
%configure --disable-gsi-mode --disable-static

# The following lines were suggested by
# https://fedoraproject.org/wiki/Packaging/Guidelines to prevent any
# RPATHs creeping in, and by
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#unused-direct-shlib-dependency
# to prevent unnecessary linking
%define fixlibtool() sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool\
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool\
sed -i -e 's! -shared ! -Wl,--as-needed\\0!g' libtool

%fixlibtool
make %{?_smp_mflags}
cd ..

# configure and build the full version
mkdir build && cd build && ln -s ../configure
%{configure} --disable-static
%fixlibtool
make %{?_smp_mflags}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

# install the without-gsi version
cd build-without-gsi
make DESTDIR=$RPM_BUILD_ROOT install
cd ..

# install the full version
cd build
make DESTDIR=$RPM_BUILD_ROOT install
cd ..

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# create empty lcmaps.db directory
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/lcmaps
# create empty plugin directory
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/lcmaps

# clean up installed files
rm -rf ${RPM_BUILD_ROOT}%{_docdir}

%ldconfig_scriptlets

%ldconfig_scriptlets without-gsi

%files
# The libraries are meant to be dlopened by client applications,
# so the .so symlinks are here and not in devel.
%{_libdir}/liblcmaps.so
%{_libdir}/liblcmaps.so.0
%{_libdir}/liblcmaps.so.0.0.0
%{_libdir}/liblcmaps_gss_assist_gridmap.so
%{_libdir}/liblcmaps_gss_assist_gridmap.so.0
%{_libdir}/liblcmaps_gss_assist_gridmap.so.0.0.0
%{_libdir}/liblcmaps_return_account_from_pem.so
%{_libdir}/liblcmaps_return_account_from_pem.so.0
%{_libdir}/liblcmaps_return_account_from_pem.so.0.0.0
%{_libdir}/liblcmaps_return_poolindex.so
%{_libdir}/liblcmaps_return_poolindex.so.0
%{_libdir}/liblcmaps_return_poolindex.so.0.0.0
%{_libdir}/liblcmaps_verify_account_from_pem.so
%{_libdir}/liblcmaps_verify_account_from_pem.so.0
%{_libdir}/liblcmaps_verify_account_from_pem.so.0.0.0
%{_mandir}/man3/lcmaps.3*
%dir %{_libdir}/lcmaps
%dir %{_sysconfdir}/lcmaps
%doc BUGS AUTHORS LICENSE README README.NO_LDAP NEWS
%doc build/etc/lcmaps.db build/etc/groupmapfile build/etc/vomapfile

%files without-gsi
# These libraries are dlopened, so the .so symlinks cannot be in devel
%{_libdir}/liblcmaps_without_gsi.so
%{_libdir}/liblcmaps_without_gsi.so.0
%{_libdir}/liblcmaps_without_gsi.so.0.0.0
%{_libdir}/liblcmaps_return_poolindex_without_gsi.so
%{_libdir}/liblcmaps_return_poolindex_without_gsi.so.0
%{_libdir}/liblcmaps_return_poolindex_without_gsi.so.0.0.0
%{_libdir}/liblcmaps_gss_assist_gridmap_without_gsi.so
%{_libdir}/liblcmaps_gss_assist_gridmap_without_gsi.so.0
%{_libdir}/liblcmaps_gss_assist_gridmap_without_gsi.so.0.0.0
%{_mandir}/man3/lcmaps.3*
%dir %{_libdir}/lcmaps
%dir %{_sysconfdir}/lcmaps
%doc BUGS AUTHORS LICENSE README README.NO_LDAP NEWS
%doc build-without-gsi/etc/lcmaps.db
%doc build-without-gsi/etc/groupmapfile
%doc build-without-gsi/etc/vomapfile

%files devel
%{_includedir}/lcmaps/lcmaps_return_poolindex.h
%{_includedir}/lcmaps/_lcmaps_return_poolindex.h
%{_includedir}/lcmaps/lcmaps.h
%{_includedir}/lcmaps/lcmaps_globus.h
%{_includedir}/lcmaps/lcmaps_openssl.h
%{_datadir}/pkgconfig/lcmaps-openssl-interface.pc
%{_datadir}/pkgconfig/lcmaps-globus-interface.pc
%{_datadir}/pkgconfig/lcmaps-interface.pc
%{_libdir}/pkgconfig/lcmaps-gss-assist-gridmap.pc
%{_libdir}/pkgconfig/lcmaps-return-account-from-pem.pc
%{_libdir}/pkgconfig/lcmaps-return-poolindex.pc
%{_libdir}/pkgconfig/lcmaps-verify-account-from-pem.pc
%{_libdir}/pkgconfig/lcmaps.pc
%doc LICENSE

%files common-devel
%dir %{_includedir}/lcmaps
%{_includedir}/lcmaps/lcmaps_version.h
%{_includedir}/lcmaps/lcmaps_account.h
%{_includedir}/lcmaps/lcmaps_arguments.h
%{_includedir}/lcmaps/lcmaps_basic.h
%{_includedir}/lcmaps/lcmaps_cred_data.h
%{_includedir}/lcmaps/lcmaps_db_read.h
%{_includedir}/lcmaps/lcmaps_defines.h
%{_includedir}/lcmaps/_lcmaps_gss_assist_gridmap.h
%{_includedir}/lcmaps/lcmaps_gss_assist_gridmap.h
%{_includedir}/lcmaps/_lcmaps.h
%{_includedir}/lcmaps/lcmaps_if.h
%{_includedir}/lcmaps/lcmaps_log.h
%{_includedir}/lcmaps/lcmaps_modules.h
%{_includedir}/lcmaps/_lcmaps_return_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_return_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_types.h
%{_includedir}/lcmaps/lcmaps_utils.h
%{_includedir}/lcmaps/_lcmaps_verify_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_verify_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_vo_data.h
%{_includedir}/lcmaps/lcmaps_return_poolindex_without_gsi.h
%{_includedir}/lcmaps/lcmaps_plugin_typedefs.h
%{_includedir}/lcmaps/lcmaps_plugin_prototypes.h
%{_datadir}/pkgconfig/lcmaps-basic-interface.pc
%doc LICENSE

%files without-gsi-devel
%{_libdir}/pkgconfig/lcmaps-return-poolindex-without-gsi.pc
%{_libdir}/pkgconfig/lcmaps-gss-assist-gridmap-without-gsi.pc
%{_libdir}/pkgconfig/lcmaps-without-gsi.pc
%doc LICENSE

%changelog
%autochangelog
