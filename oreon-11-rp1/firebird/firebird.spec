%global source0_hash 5041b97b480c9fe241c92ad0adf89e36faad0a8f0e21f1371dfbcc96a6f38e12

%global         upversion 5.0.4.1812
%global         pkgversion Firebird-%{upversion}-0

%global         major 5.0
%global         _hardened_build 1
# firebird is mis-compiled when LTO is enabled. A root
# cause analysis has not yet been completed. Reported upstream.
# Disable LTO for now
%global         _lto_cflags %nil

Name:           firebird
Version:        %{upversion}
Release:        1%{?dist}

Summary:        SQL relational database management system
# Automatically converted from old format: Interbase - review is highly recommended.
License:        Interbase-1.0
URL:            http://www.firebirdsql.org/

Source0:        https://github.com/FirebirdSQL/firebird/releases/download/v5.0.4/%{pkgversion}-source.tar.xz
Source1:        firebird-logrotate
Source2:        README.Fedora
Source3:        firebird.service
Source4:        fb_config

# from OpenSuse
Patch101:       add-pkgconfig-files.patch

# from Debian to be sent upstream
Patch203:       no-copy-from-icu.patch
Patch205:       cloop-honour-build-flags.patch

# from upstream
Patch401:       btyacc-honour-build-flags.patch

# not yet upstream
Patch501:       examples-honour-build-flags.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtommath-devel
BuildRequires: libtool
BuildRequires: ncurses-devel
BuildRequires: libicu-devel
BuildRequires: libedit-devel
BuildRequires: gcc-c++
BuildRequires: libstdc++-static
BuildRequires: systemd-rpm-macros
BuildRequires: chrpath
BuildRequires: zlib-devel
BuildRequires: procmail
BuildRequires: make
BuildRequires: libtomcrypt-devel
BuildRequires: unzip
BuildRequires: sed
BuildRequires: cmake

Requires(postun): /usr/sbin/userdel
Requires(postun): /usr/sbin/groupdel
Recommends:     logrotate
Requires:       libfbclient2 = %{version}-%{release}
Requires:       libib-util = %{version}-%{release}
Requires:       %{name}-utils = %{version}-%{release}


%description
Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package devel
Requires:       %{name} = %{version}-%{release}
Requires:       libfbclient2-devel = %{version}-%{release}
Summary:        UDF support library for Firebird SQL server

%description devel
This package is needed for development of client applications and user
defined functions (UDF) for Firebird SQL server.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package -n libib-util
Summary:        Firebird SQL UDF support library

%description -n libib-util
libib_util contains utility functions used by
User-Defined Functions (UDF) for memory management etc.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package -n libfbclient2
Summary:        Firebird SQL server client library

%description -n libfbclient2
Shared client library for Firebird SQL server.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package -n libfbclient2-devel
Summary:        Development libraries and headers for Firebird SQL server
Requires:       %{name}-devel = %{version}-%{release}
Requires:       libfbclient2 = %{version}-%{release}
Requires:       pkgconfig

%description -n libfbclient2-devel
Development files for Firebird SQL server client library.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package doc
Requires:       %{name} = %{version}-%{release}
Summary:        Documentation for Firebird SQL server
BuildArch:      noarch

%description doc
Documentation for Firebird SQL server.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package utils
Requires:       libfbclient2 = %{version}-%{release}
Summary:        Firebird SQL user utilities

%description utils
Firebird SQL user utilities.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%package examples
Requires:       %{name}-doc = %{version}-%{release}
Summary:        Examples for Firebird SQL server
BuildArch:      noarch

%description examples
Examples for Firebird SQL server.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{pkgversion}-source
%patch -P101 -p1
%patch -P203 -p1
%patch -P205 -p1
%patch -P401 -p1
%patch -P501 -p1

# Create a sysusers.d config file
cat >firebird.sysusers.conf <<EOF
u firebird - - - -
EOF


%build
%ifarch s390x
%global _lto_cflags %{nil}
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="${CFLAGS} -fno-delete-null-pointer-checks"
NOCONFIGURE=1 ./autogen.sh
%configure --disable-rpath --prefix=%{_prefix} \
  --with-system-editline \
  --with-fbbin=%{_bindir} --with-fbsbin=%{_sbindir} \
  --with-fbconf=%{_sysconfdir}/%{name} \
  --with-fblib=%{_libdir} --with-fbinclude=%{_includedir} \
  --with-fbdoc=%{_defaultdocdir}/%{name} \
  --with-fbsample=%{_defaultdocdir}/%{name}/sample \
  --with-fbsample-db=%{_localstatedir}/lib/%{name}/data \
  --with-fbhelp=%{_localstatedir}/lib/%{name}/system \
  --with-fbintl=%{_libdir}/%{name}/intl \
  --with-fbmisc=%{_datadir}/%{name}/misc \
  --with-fbsecure-db=%{_localstatedir}/lib/%{name}/secdb \
  --with-fbmsg=%{_localstatedir}/lib/%{name}/system \
  --with-fblog=%{_localstatedir}/log/%{name} \
  --with-fbglock=%{_rundir}/%{name} \
  --with-fbplugins=%{_libdir}/%{name}/plugins \
  --with-fbtzdata=%{_localstatedir}/lib/%{name}/tzdata 

make %{?_smp_mflags}
cd gen
sed -i '/linkFiles "/d' ./install/makeInstallImage.sh
./install/makeInstallImage.sh
chmod -R u+w buildroot%{_docdir}/%{name}

%install
chmod u+rw,a+rx gen/buildroot/%{_includedir}/firebird/impl
cp -r gen/buildroot/* ${RPM_BUILD_ROOT}/
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
cp -v gen/install/misc/*.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/
install -m0644 -D firebird.sysusers.conf %{buildroot}%{_sysusersdir}/firebird.conf

cd ${RPM_BUILD_ROOT}
rm -vf .%{_sbindir}/*.sh
mv -v .%{_sbindir}/fb_config .%{_libdir}/
install -p -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}/fb_config
rm -vf .%{_includedir}/perf.h
rm -vf .%{_libdir}/libicu*.so
chmod -R u+w .%{_docdir}/%{name}
mv -v .%{_datadir}/%{name}/misc/upgrade/udf/* .%{_docdir}/%{name}/
rm -rvf .%{_datadir}/%{name}/misc
mv -v .%{_sysconfdir}/%{name}/README.md .%{_sysconfdir}/%{name}/CHANGELOG.md \
  .%{_docdir}/%{name}/
mv -v .%{_sysconfdir}/%{name}/IDPLicense.txt .%{_docdir}/%{name}/
mv -v .%{_sysconfdir}/%{name}/IPLicense.txt .%{_docdir}/%{name}/
install -p -m 0644 -D %{SOURCE2} .%{_docdir}/%{name}/README.Fedora
mv -v .%{_bindir}/gstat .%{_bindir}/gstat-fb
mv -v .%{_bindir}/isql .%{_bindir}/isql-fb
rm -rvf .%{_defaultdocdir}/%{name}/sample/prebuilt

mkdir -p .%{_localstatedir}/log/%{name}
mkdir -p .%{_sysconfdir}/logrotate.d
echo 1 > .%{_localstatedir}/log/%{name}/%{name}.log
sed "s@%{name}.log@%{_localstatedir}/log/%{name}/%{name}.log@g" %{SOURCE1} > .%{_sysconfdir}/logrotate.d/%{name}

mkdir -p .%{_unitdir}
cp -f %{SOURCE3} .%{_unitdir}/%{name}.service


%pre 
# Add gds_db to /etc/services if needed
FileName=/etc/services
newLine="gds_db 3050/tcp  # Firebird SQL Database Remote Protocol"
oldLine=`grep "^gds_db" $FileName`
if [ -z "$oldLine" ]; then
 echo $newLine >> $FileName
fi


%post 
%systemd_post firebird.service


%postun 
%systemd_postun_with_restart firebird.service


%preun 
%systemd_preun firebird.service


%files
%{_docdir}/%{name}/
%{_bindir}/fbtracemgr
%{_sbindir}/firebird
%{_sbindir}/fbguard
%{_sbindir}/fb_lock_print
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/databases.conf
%config(noreplace) %{_sysconfdir}/%{name}/fbtrace.conf
%config(noreplace) %{_sysconfdir}/%{name}/firebird.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins.conf
%config(noreplace) %{_sysconfdir}/%{name}/replication.conf
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_libdir}/%{name}/intl
%{_libdir}/%{name}/plugins

%dir %{_localstatedir}/lib/%{name}
%dir %attr(0700,%{name},%{name}) %{_localstatedir}/lib/%{name}/secdb
%dir %attr(0700,%{name},%{name}) %{_localstatedir}/lib/%{name}/data
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/lib/%{name}/system
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/lib/%{name}/tzdata
%attr(0600,firebird,firebird) %config(noreplace) %{_localstatedir}/lib/%{name}/secdb/security5.fdb
%attr(0644,firebird,firebird) %{_localstatedir}/lib/%{name}/system/firebird.msg
%attr(0644,firebird,firebird) %{_localstatedir}/lib/%{name}/tzdata/*.res
%ghost %dir %attr(0775,%{name},%{name}) /run/%{name}
%ghost %attr(0644,%{name},%{name}) /run/%{name}/fb_guard
%dir %{_localstatedir}/log/%{name}
%config(noreplace) %attr(0664,%{name},%{name})  %{_localstatedir}/log/%{name}/%{name}.log
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/logrotate.d/%{name}

%attr(0644,root,root) %{_unitdir}/%{name}.service
%{_sysusersdir}/firebird.conf


%files devel
%{_includedir}/*.h
%{_includedir}/%{name}
%{_libdir}/fb_config
%{_sbindir}/fb_config


%files -n libfbclient2
%{_libdir}/libfbclient.so.2
%{_libdir}/libfbclient.so.%{major}*


%files -n libfbclient2-devel
%{_libdir}/libfbclient.so
%{_libdir}/pkgconfig/fbclient.pc


%files -n libib-util
%{_libdir}/libib_util.so


%files doc
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/sample
%exclude %{_docdir}/%{name}/IDPLicense.txt
%exclude %{_docdir}/%{name}/IPLicense.txt


%files utils
%{_bindir}/gstat-fb
%{_bindir}/fbsvcmgr
%{_bindir}/gbak
%{_bindir}/gfix
%{_bindir}/gpre
%{_bindir}/gsec
%{_bindir}/isql-fb
%{_bindir}/nbackup
%{_bindir}/gsplit


%files examples
%{_docdir}/%{name}/sample
%attr(0600,firebird,firebird) %{_localstatedir}/lib/%{name}/data/employee.fdb



%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.4.1812-1
- Import for Oreon 11
