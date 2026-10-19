%global source0_hash 19c23908e7d57e8d91ef85b41f5646307582f10f4f0fb999bbf89ed24ec9c983
%global source50_hash c0b56c1d0b0e9b5d69b309d2afd404b090bc77ab174a55d5435aceea9e0dfbb1
%bcond_with docs
%global doc_version 9.0.2
%bcond_with tests
Name:              valkey
Version:           9.1.2
Release:        1%{?dist}
Summary:        A persistent key-value database
License:           BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0
URL:               https://valkey.io
Source0:        https://github.com/valkey-io/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:           %{name}.logrotate
Source2:           %{name}-sentinel.service
Source3:           %{name}.service
Source4:           %{name}.sysusers
Source5:           %{name}.tmpfiles
Source9:           migrate_redis_to_valkey.sh
Source50:        https://github.com/valkey-io/%{name}-doc/archive/refs/tags/%{doc_version}.tar.gz#/%{name}-doc-%{doc_version}.tar.gz
Patch0:            %{name}-conf.patch
Patch1:            %{name}-loadmod.patch
%if %{with tests}
%endif
%if %{with docs}
%endif
Requires:          logrotate
Provides:          bundled(libvalkey) = 0.2.1
Provides:          bundled(jemalloc) = 5.3.0
Provides:          bundled(lua-libs) = 5.1.5
Provides:          bundled(linenoise) = 1.0
Provides:          bundled(lzf)
Provides:          bundled(hdr_histogram) = 0.11.9
Provides:          bundled(fpconv)
Obsoletes:         valkey-tls  < %{version}-%{release}
Provides:          valkey-tls  = %{version}-%{release}
%global valkey_modules_abi 1
%global valkey_modules_dir %{_libdir}/%{name}/modules
%global valkey_modules_cfg %{_sysconfdir}/%{name}/modules
Provides:          valkey(modules_abi)%{?_isa} = %{valkey_modules_abi}
ExcludeArch:       %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pandoc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  python3-pyyaml
BuildRequires:  rdma-core-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl
# /oreon:deps
%description
Valkey is an advanced key-value store. It is often referred to as a data
structure server since keys can contain strings, hashes, lists, sets and
sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Valkey works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

Valkey also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Valkey behave like
a cache.

You can use Valkey from most programming languages also.

See https://valkey.io/topics/

%package           devel
Summary:           Development header for Valkey module development
Provides:          %{name}-static = %{version}-%{release}
Requires:          %{name}%{?_isa} = %{version}-%{release}
%description       devel
Header file required for building loadable Valkey modules.

%package           rdma
Summary:           RDMA module for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}
Supplements:       %{name}
%description       rdma
%summary.

See https://valkey.io/topics/RDMA/

%package           compat-redis
Summary:           Conversion script and compatibility symlinks for Redis
Requires:          valkey = %{version}-%{release}
Conflicts:         redis < 7.4
BuildArch:         noarch
%description       compat-redis
%summary

%package           compat-redis-devel
Summary:           Compatibility development header for Redis API Valkey modules
Requires:          valkey-devel = %{version}-%{release}
Conflicts:         redis-devel < 7.4
Conflicts:         redis-static < 7.4
BuildArch:         noarch
%description       compat-redis-devel
Header file required for building loadable Valkey modules with the legacy
Redis API.

%if %{with docs}
%package           doc
Summary:           Documentation and extra man pages for %{name}
BuildArch:         noarch
License:           CC-BY-SA-4.0
%description       doc
%summary
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source50_hash}" = "none" || { f="%{SOURCE50}"; test -f "$f" || { echo "oreon: missing Source50 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source50_hash}" || { echo "oreon: Source50 hash mismatch" >&2; exit 1; }; }
# no autosetup due to no support for multiple source extraction
%setup -n %{name}-%{version} -a50
%patch -P0 -p1 -b .rpm
%patch -P1 -p1 -b .loadmod

mv deps/lua/COPYRIGHT             COPYRIGHT-lua
mv deps/jemalloc/COPYING          COPYING-jemalloc
mv deps/libvalkey/COPYING         COPYING-libvalkey
mv deps/hdr_histogram/LICENSE.txt LICENSE-hdrhistogram
mv deps/hdr_histogram/COPYING.txt COPYING-hdrhistogram
mv deps/fpconv/LICENSE.txt        LICENSE-fpconv

# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch %ix86 %arm x86_64 s390x
sed -e 's/--with-lg-quantum/--with-lg-page=12 --with-lg-quantum/' -i deps/Makefile
%endif
%ifarch ppc64 ppc64le aarch64
sed -e 's/--with-lg-quantum/--with-lg-page=16 --with-lg-quantum/' -i deps/Makefile
%endif

# Module API version safety check
api=`sed -n -e 's/#define VALKEYMODULE_APIVER_[0-9][0-9]* //p' src/valkeymodule.h`
if test "$api" != "%{valkey_modules_abi}"; then
   : Error: Upstream API version is now ${api}, expecting %%{valkey_modules_abi}.
   : Update the valkey_modules_abi macro, and rebuild.
   exit 1
fi

# Generates macro file
cat << 'EOF' | tee macros.%{name}
%%valkey_version     %version
%%valkey_modules_abi %valkey_modules_abi
%%valkey_modules_dir %valkey_modules_dir
%%valkey_modules_cfg %valkey_modules_cfg
EOF

%global make_flags DEBUG="" V="echo" PREFIX=%{buildroot}%{_prefix} BUILD_WITH_SYSTEMD=yes BUILD_TLS=yes BUILD_RDMA=module

: RDMA configuration file
cat << EOF | tee rdma.conf
# RDMA module
loadmodule %{valkey_modules_dir}/rdma.so
EOF

%build

%make_build %{make_flags}
%if %{with docs}
pushd %{name}-doc-%{doc_version}
%make_build VALKEY_ROOT=../
%make_build html VALKEY_ROOT=../
popd
%endif
%install
%make_install %{make_flags}
%if %{with docs}
pushd %{name}-doc-%{doc_version}
%make_install INSTALL_MAN_DIR=%{buildroot}%{_mandir} VALKEY_ROOT=../
install -d %{buildroot}%{_docdir}/%{name}/
cp -ra _build/html/* %{buildroot}%{_docdir}/%{name}/
install -d %{buildroot}%{_defaultlicensedir}/valkey-doc/
cp -a LICENSE %{buildroot}%{_defaultlicensedir}/valkey-doc/
popd
%endif
rm -rf %{buildroot}%{_datadir}/%{name}
install -p -D -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -p -D -m 0644 %{S:5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_sharedstatedir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -d %{buildroot}%{valkey_modules_dir}
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -pDm640 %{name}.conf  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm640 sentinel.conf %{buildroot}%{_sysconfdir}/%{name}/sentinel.conf
install -dm750  %{buildroot}%{valkey_modules_cfg}
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:3} %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{buildroot}%{_unitdir}
chmod 755 %{buildroot}%{_bindir}/%{name}-*
install -pDm644 src/%{name}module.h %{buildroot}%{_includedir}/%{name}module.h
install -pDm644 macros.%{name} %{buildroot}%{_rpmmacrodir}/macros.%{name}
install -Dpm 755 %{S:9} %{buildroot}%{_libexecdir}/migrate_redis_to_valkey.sh
install -pDm644 src/redismodule.h %{buildroot}%{_includedir}/redismodule.h
ln -sr %{buildroot}/usr/lib/systemd/system/valkey.service %{buildroot}/usr/lib/systemd/system/redis.service
ln -sr %{buildroot}/usr/lib/systemd/system/valkey-sentinel.service %{buildroot}/usr/lib/systemd/system/redis-sentinel.service
install -pm755 src/valkey-rdma.so %{buildroot}%{valkey_modules_dir}/rdma.so
install -pm640 rdma.conf          %{buildroot}%{valkey_modules_cfg}/rdma.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
taskset -c 1 ./runtest --clients 50 --skiptest "Active defrag - AOF loading"
%endif
%post

%systemd_post %{name}.service
%systemd_post %{name}-sentinel.service
%post compat-redis

%{_libexecdir}/migrate_redis_to_valkey.sh
%preun

%systemd_preun %{name}.service
%systemd_preun %{name}-sentinel.service
%postun

%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}-sentinel.service
%files -f %{oreon_filedir}/main.list
%files -n valkey-devel -f %{oreon_filedir}/valkey-devel.list
%files -n valkey-rdma -f %{oreon_filedir}/valkey-rdma.list
%files -n valkey-compat-redis -f %{oreon_filedir}/valkey-compat-redis.list
%files -n valkey-compat-redis-devel -f %{oreon_filedir}/valkey-compat-redis-devel.list
%files -n valkey-doc -f %{oreon_filedir}/valkey-doc.list

%changelog

%autochangelog
