%global source0_hash 6ac51b6dd39690a6ccc62e807f065e92131498687d4201a69ae9570b68bab1e5
%global     full_version C_ICAP_%{version}
Name:       c-icap
Version:    0.6.5
Release:        1%{?dist}
Summary:        An implementation of an ICAP server
License:    LGPL-2.1-or-later and GPL-2.0-or-later
URL:        http://%{name}.sourceforge.net/
Source0:        https://github.com/%{name}/%{name}-server/archive/%{full_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:    %{name}.logrotate
Source3:    %{name}.tmpfiles.conf
Source4:    %{name}.service
Source5:    %{name}.sysusers.conf
Patch0:     %{name}-conf.in.patch
Patch3: c-icap-configure-c99.patch
Patch4: c-icap-gcc15.patch
Requires:       logrotate
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  brotli-devel
BuildRequires:  bzip2-devel
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
# /oreon:deps
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
./test_cache
./test_headers
./test_lists
./test_md5
./test_ops
./test_shared_locking
popd
%install
%make_install
find %{buildroot} -name "*.la" -delete
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_datadir}/c_icap/{contrib,templates}/
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}/
mkdir -p %{buildroot}/run/%{name}/
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
rm -f %{buildroot}%{_sysconfdir}/%{name}/*.default
rm -fr %{buildroot}%{_docdir}/%{name}
%oreon_autofiles c-icap-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles c-icap-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n c-icap-devel -f %{oreon_filedir}/c-icap-devel.list
%files -n c-icap-libs -f %{oreon_filedir}/c-icap-libs.list

%changelog

%autochangelog
