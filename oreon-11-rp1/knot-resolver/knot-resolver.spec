%global source1_hash 82a9f95c0070e6ae5ee3f17c1ff564f63893e779c4b010065842f71c4aa23357
%global source0_hash 854ad23367bab66392f7d74f142f2219e3090ae81126b635430fce7b1916f1a3
%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}
%define GPG_CHECK 1
%define repodir %{_builddir}/%{name}-%{version}
%define NINJA ninja-build
Name:           knot-resolver
Version:        6.4.2
Release:        1%{?dist}
Summary:        Caching full DNS Resolver
License:        GPL-3.0-or-later
URL:            https://www.knot-resolver.cz/
Source0:        https://secure.nic.cz/files/%{name}/%{name}-%{version}.tar.xz
ExclusiveArch:	%{arm} aarch64 %{ix86} x86_64
%if 0%{GPG_CHECK}
Source1:        https://secure.nic.cz/files/%{name}/%{name}-%{version}.tar.xz.asc
Source100:      kresd-keyblock.asc
%endif
Requires:       systemd
Requires(post): systemd
%if "x%{?suse_version}" == "x"
%endif
%if "x%{?suse_version}" == "x"
%endif
%if 0%{?suse_version}
%define NINJA ninja
Requires(pre):  shadow
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libdnssec)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libfstrm)
BuildRequires:  pkgconfig(libknot)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libzscanner)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The Knot Resolver is a DNSSEC-enabled caching full resolver implementation
written in C and LuaJIT, including both a resolver library and a daemon.
Modular architecture of the library keeps the core tiny and efficient, and
provides a state-machine like API for extensions.

The package is pre-configured as local caching resolver.
To start using it, start a single kresd instance:
$ systemctl start kresd@1.service

%package devel
Summary:        Development headers for Knot Resolver
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The package contains development headers for Knot Resolver.

%if "x%{?suse_version}" == "x"
%package module-dnstap
Summary:        dnstap module for Knot Resolver
Requires:       %{name} = %{version}-%{release}
%description module-dnstap
dnstap module for Knot Resolver supports logging DNS responses to a unix socket
in dnstap format using fstrm framing library.  This logging is useful if you
need effectively log all DNS traffic.
%endif

%if "x%{?suse_version}" == "x"
%package module-http
Summary:        HTTP module for Knot Resolver
Requires:       %{name} = %{version}-%{release}
Requires:       lua-http
Requires:       lua-mmdb
%description module-http
HTTP module for Knot Resolver can serve as API endpoint for other modules or
provide a web interface for local visualization of the resolver cache and
queries. It can also serve DNS-over-HTTPS, but it is deprecated in favor of
native C implementation, which doesn't require this package.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{GPG_CHECK}
export GNUPGHOME=./gpg-keyring
mkdir -m 700 ${GNUPGHOME}
gpg2 --import %{SOURCE100}
gpg2 --verify %{SOURCE1} %{SOURCE0}
%endif
%setup -q -n %{name}-%{version}

# Create a sysusers.d config file
cat >knot-resolver.sysusers.conf <<EOF
u knot-resolver - 'Knot Resolver' %{_sysconfdir}/knot-resolver -
EOF

%build

CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" meson build_rpm \
    -Dsystemd_files=enabled \
    -Dclient=enabled \
%if "x%{?suse_version}" == "x"
    -Ddnstap=enabled \
%endif
    -Dunit_tests=enabled \
    -Dmanaged_ta=enabled \
    -Dkeyfile_default="%{_sharedstatedir}/knot-resolver/root.keys" \
    -Dinstall_root_keys=enabled \
    -Dinstall_kresd_conf=enabled \
    -Dmalloc=jemalloc \
    --buildtype=plain \
    --prefix="%{_prefix}" \
    --sbindir="%{_sbindir}" \
    --libdir="%{_libdir}" \
    --includedir="%{_includedir}" \
    --sysconfdir="%{_sysconfdir}" \
%{NINJA} -v -C build_rpm
%check

meson test -C build_rpm
%install
DESTDIR="${RPM_BUILD_ROOT}" %{NINJA} -v -C build_rpm install
install -m 0755 -d %{buildroot}%{_unitdir}/multi-user.target.wants
ln -s ../kresd.target %{buildroot}%{_unitdir}/multi-user.target.wants/kresd.target
rm %{buildroot}%{_libdir}/knot-resolver/kres_modules/etcd.lua
rm %{buildroot}%{_prefix}/lib/sysusers.d/knot-resolver.conf
%if 0%{?suse_version}
rm %{buildroot}%{_libdir}/knot-resolver/kres_modules/experimental_dot_auth.lua
rm -r %{buildroot}%{_libdir}/knot-resolver/kres_modules/http
rm %{buildroot}%{_libdir}/knot-resolver/kres_modules/http*.lua
rm %{buildroot}%{_libdir}/knot-resolver/kres_modules/prometheus.lua
%endif
install -m0644 -D knot-resolver.sysusers.conf %{buildroot}%{_sysusersdir}/knot-resolver.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%post

systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 2 ] ; then
        systemctl try-restart kres-cache-gc.service >/dev/null 2>&1 || :
fi
%tmpfiles_create %{_tmpfilesdir}/knot-resolver.conf
%preun

%systemd_preun kres-cache-gc.service kresd.target
%postun

%systemd_postun_with_restart 'kresd@*.service' kres-cache-gc.service
%files -f %{oreon_filedir}/main.list
%files -n knot-resolver-devel -f %{oreon_filedir}/knot-resolver-devel.list
%files -n knot-resolver-module-dnstap -f %{oreon_filedir}/knot-resolver-module-dnstap.list
%files -n knot-resolver-module-http -f %{oreon_filedir}/knot-resolver-module-http.list

%changelog

%autochangelog
