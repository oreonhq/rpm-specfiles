%global source0_hash 5041b97b480c9fe241c92ad0adf89e36faad0a8f0e21f1371dfbcc96a6f38e12
%global         upversion 5.0.4.1812
%global         pkgversion Firebird-%{upversion}-0
%global         major 5.0
%global         _hardened_build 1
%global         _lto_cflags %nil
Name:           firebird
Version:        %{upversion}
Release:        1%{?dist}
Summary:        SQL relational database management system
License:        Interbase-1.0
URL:            http://www.firebirdsql.org/
Source0:        https://github.com/FirebirdSQL/%{name}/releases/download/v%{major}.4/%{pkgversion}-source.tar.xz
Source1:        firebird-logrotate
Source2:        README.Fedora
Source3:        firebird.service
Source4:        fb_config
Patch101:       add-pkgconfig-files.patch
Patch203:       no-copy-from-icu.patch
Patch205:       cloop-honour-build-flags.patch
Patch401:       btyacc-honour-build-flags.patch
Patch501:       examples-honour-build-flags.patch
Requires(postun): /usr/sbin/userdel
Requires(postun): /usr/sbin/groupdel
Recommends:     logrotate
Requires:       libfbclient2 = %{version}-%{release}
Requires:       libib-util = %{version}-%{release}
Requires:       %{name}-utils = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libedit-devel
BuildRequires:  libicu-devel
BuildRequires:  libstdc++-static
BuildRequires:  libtomcrypt-devel
BuildRequires:  libtommath-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  procmail
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles libib-util usr/*/lib*.so.*
%oreon_autofiles libfbclient2 usr/*/lib*.so.*
%oreon_autofiles libfbclient2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre 

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
%files -f %{oreon_filedir}/main.list
%files -n firebird-devel -f %{oreon_filedir}/firebird-devel.list
%files -n libib-util -f %{oreon_filedir}/libib-util.list
%files -n libfbclient2 -f %{oreon_filedir}/libfbclient2.list
%files -n libfbclient2-devel -f %{oreon_filedir}/libfbclient2-devel.list
%files -n firebird-doc -f %{oreon_filedir}/firebird-doc.list
%files -n firebird-utils -f %{oreon_filedir}/firebird-utils.list
%files -n firebird-examples -f %{oreon_filedir}/firebird-examples.list

%changelog

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.4.1812-1
- Import for Oreon 11
