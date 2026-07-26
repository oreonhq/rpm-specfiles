%global source0_hash none

BuildRequires: cmake >= 2.8
BuildRequires: gcc >= 4.5
BuildRequires: gcc-c++ >= 4.5
BuildRequires: coreutils
BuildRequires: sed
BuildRequires: readline-devel
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libzstd-devel
BuildRequires: perl-podlators
Requires(pre): %{_sbindir}/useradd
Requires(pre): %{_sbindir}/groupadd
Requires: logrotate

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

Name: tarantool
Version: 2.4.2.68
Release: 20%{?dist}
Summary: In-Memory Database
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://tarantool.org/
# Add dependency on network configuration files used by `socket` module
# https://github.com/tarantool/tarantool/issues/1794
Requires: /etc/protocols
Requires: /etc/services
# Deps for built-in package manager
# https://github.com/tarantool/tarantool/issues/2612
Requires: openssl
Requires: curl
Recommends: tarantool-devel
Recommends: git-core
Recommends: cmake >= 2.8
Recommends: make
Recommends: gcc >= 4.5
Recommends: gcc-c++ >= 4.5
Source0: http://download.tarantool.org/tarantool/2.4/src/tarantool-%{version}.tar.gz
Patch0: 10-rundir.patch
ExclusiveArch: %{ix86} x86_64
%description
Tarantool is an open-source database that can store everything in RAM.
You can use it as a cache with on-disk persistence. Tarantool is able to
process up to 1 million RPS and supports SQL and secondary index searching.

In Tarantool, you can run your code at the same place where your data is.
That speeds up all the operations. Apply any business logic in Lua programming
language. Get rid of the outdated database records. Synchronize with other
data sources. Implement HTTP-service.

This package provides the server daemon and admin tools.

%package devel
Summary: Server development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Tarantool is an open-source database that can store everything in RAM.
You can use it as a cache with on-disk persistence. Tarantool is able to
process up to 1 million RPS and supports SQL and secondary index searching.

In Tarantool, you can run your code at the same place where your data is.
That speeds up all the operations. Apply any business logic in Lua programming
language. Get rid of the outdated database records. Synchronize with other
data sources. Implement HTTP-service.

This package provides server development files needed to create
C and Lua/C modules.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1

%build
# RHBZ #1301720: SYSCONFDIR an LOCALSTATEDIR must be specified explicitly
%cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DCMAKE_INSTALL_LOCALSTATEDIR:PATH=%{_localstatedir} \
         -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
         -DENABLE_BUNDLED_LIBYAML:BOOL=ON \
         -DENABLE_BUNDLED_MSGPUCK:BOOL=ON \
         -DENABLE_BUNDLED_LIBCURL:BOOL=OFF \
         -DENABLE_BUNDLED_ZSTD:BOOL=OFF \
         -DENABLE_BACKTRACE:BOOL=OFF \
         -DWITH_SYSTEMD:BOOL=ON \
         -DSYSTEMD_UNIT_DIR:PATH=%{_unitdir} \
         -DSYSTEMD_TMPFILES_DIR:PATH=%{_tmpfilesdir} \
         -DENABLE_DIST:BOOL=ON
%cmake_build --target tarantool api man-tarantool man-tarantoolctl

%install
%cmake_install
# %%doc and %%license macroses are used instead
rm -rf %{buildroot}%{_datarootdir}/doc/tarantool/

%check
%ctest

%pre
/usr/sbin/groupadd -r tarantool > /dev/null 2>&1 || :
/usr/sbin/useradd -M -N -g tarantool -r -d /var/lib/tarantool -s /sbin/nologin\
    -c "Tarantool Server" tarantool > /dev/null 2>&1 || :

%post
%tmpfiles_create tarantool.conf
%systemd_post 'tarantool@.service'

%preun
# Sic: doesn't work
#systemd_preun 'tarantool@*.service'

%postun
%systemd_postun_with_restart 'tarantool@*.service'

%files
%{_bindir}/tarantool
%{_mandir}/man1/tarantool.1*
%doc README.md
%license LICENSE AUTHORS
# tarantool package should own module directories
%dir %{_libdir}/tarantool
%dir %{_datadir}/tarantool
%{_datadir}/tarantool/luarocks
%{_bindir}/tarantoolctl
%{_mandir}/man1/tarantoolctl.1*
%config(noreplace) %{_sysconfdir}/sysconfig/tarantool
%dir %{_sysconfdir}/tarantool
%dir %{_sysconfdir}/tarantool/instances.available
%config(noreplace) %{_sysconfdir}/tarantool/instances.available/example.lua
%attr(-,tarantool,tarantool) %dir %{_localstatedir}/lib/tarantool/
%attr(-,tarantool,tarantool) %dir %{_localstatedir}/log/tarantool/
%config(noreplace) %{_sysconfdir}/logrotate.d/tarantool
%{_unitdir}/tarantool@.service
%{_tmpfilesdir}/tarantool.conf

%files devel
%dir %{_includedir}/tarantool
%{_includedir}/tarantool/lauxlib.h
%{_includedir}/tarantool/luaconf.h
%{_includedir}/tarantool/lua.h
%{_includedir}/tarantool/lua.hpp
%{_includedir}/tarantool/luajit.h
%{_includedir}/tarantool/lualib.h
%{_includedir}/tarantool/module.h

%changelog
%autochangelog
