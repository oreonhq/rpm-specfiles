%global source0_hash 96400a52a531aa9a425ac3e30e738937dbbbdd3316a057965ef30dd1dea9c40f

%global     full_version C_ICAP_%{version}

Name:       c-icap
Version:    0.6.3
Release:    5%{?dist}
Summary:    An implementation of an ICAP server
License:    LGPL-2.1-or-later and GPL-2.0-or-later
URL:        http://%{name}.sourceforge.net/

Source0:    https://github.com/%{name}/%{name}-server/archive/%{full_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    %{name}.logrotate
Source3:    %{name}.tmpfiles.conf
Source4:    %{name}.service
Source5:    %{name}.sysusers.conf

# Adjust some paths to standard Fedora/EPEL ones:
Patch0:     %{name}-conf.in.patch
# Patches from the c_icap_0_6_x branch:
Patch3: c-icap-configure-c99.patch
# Patch for gcc15 in F42
Patch4: c-icap-gcc15.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  brotli-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libatomic
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel

Requires:       logrotate
%if 0%{?fedora} < 42
Requires(pre):	shadow-utils
%endif

%description
C-icap is an implementation of an ICAP server. It can be used with HTTP proxies
that support the ICAP protocol to implement content adaptation and filtering
services. Most of the commercial HTTP proxies must support the ICAP protocol,
the open source Squid 3.x proxy server supports it too.

%package devel
Summary:     Development tools for %{name}
Requires:    %{name}-libs%{?_isa} = %{version}-%{release}
Requires:    zlib-devel

%description devel
The c-icap-devel package contains the static libraries and header files for
developing software using c-icap.

%package libs
Summary:    Libraries used by %{name}

%description libs
The c-icap-libs package contains all runtime libraries used by c-icap and the
utilities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n c-icap-server-%{full_version}

# See RECONF
echo "master-%{full_version}" > VERSION.m4
autoreconf -vif

%build
%configure \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --enable-shared \
  --disable-static \
  --enable-ipv6 \
  --enable-large-files \
  --enable-lib-compat \
  --without-bdb \
  --with-brotli \
  --with-ldap \
  --with-lmdb \
  --with-openssl \
  --with-zlib

%make_build

%check
pushd tests
./test_allocators
./test_arrays
./test_atomics
./test_atomics_cplusplus
./test_base64
# Requires input:
#./test_body
./test_cache
# Requires input:
#./test_filetype
./test_headers
./test_lists
./test_md5
./test_ops
./test_shared_locking
# Requires input:
#./test_tables
popd

%install
%make_install

find %{buildroot} -name "*.la" -delete

mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_datadir}/c_icap/{contrib,templates}/
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}/
mkdir -p %{buildroot}/run/%{name}/

# Required before bin/sbin merge in F42
%if 0%{?fedora} < 42
mv -f %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/
%endif

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service

%if 0%{?fedora} >= 42
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf
%endif

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/%{name}/*.default

# Let rpm pick up the docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

# Required prior to sysusers.d support in F42
%if 0%{?fedora} < 42
%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null ||
    useradd -r -g %{name} -d /run/%{name} -s /sbin/nologin \
    -c "C-ICAP Service user" %{name}
exit 0
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if 0%{?rhel} == 7
%ldconfig_scriptlets libs
%endif

%files
%license COPYING
%doc AUTHORS README TODO
%doc contrib/*.pl
%attr(750,root,%{name}) %dir %{_sysconfdir}/%{name}
%attr(640,root,%{name}) %config(noreplace) %{_sysconfdir}/%{name}/*.conf
%attr(640,root,%{name}) %config(noreplace) %{_sysconfdir}/%{name}/*.magic
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0755,%{name},%{name}) %dir /run/%{name}/
%{_bindir}/%{name}-client
%{_bindir}/%{name}-mklmdb
%{_bindir}/%{name}-stretch
%{_sbindir}/%{name}
%{_datadir}/c_icap
%dir %{_libdir}/c_icap
%{_libdir}/c_icap/dnsbl_tables.so
%{_libdir}/c_icap/ldap_module.so
%{_libdir}/c_icap/lmdb_tables.so
%{_libdir}/c_icap/shared_cache.so
%{_libdir}/c_icap/srv_echo.so
%{_libdir}/c_icap/srv_ex206.so
%{_libdir}/c_icap/sys_logger.so
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-client.8*
# Removed as BDB support is not enabled:
%exclude %{_mandir}/man8/%{name}-mkbdb.8*
%{_mandir}/man8/%{name}-mklmdb.8*
%{_mandir}/man8/%{name}-stretch.8*
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%attr(750,%{name},%{name}) %dir %{_localstatedir}/log/%{name}

%if 0%{?fedora} >= 42
%{_sysusersdir}/%{name}.conf
%endif

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-libicapapi-config
%{_includedir}/c_icap
%{_libdir}/libicapapi.so
%{_mandir}/man8/%{name}-config.8*
%{_mandir}/man8/%{name}-libicapapi-config.8*

%files libs
%license COPYING
%{_libdir}/libicapapi.so.*

%changelog
%autochangelog
