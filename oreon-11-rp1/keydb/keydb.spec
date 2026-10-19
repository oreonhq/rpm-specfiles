%global source0_hash 229190b251f921e05aff7b0d2f04b5676c198131e2abbec1e2cfb2e61215e2f3
%bcond_with     tests
Name:           keydb
Version:        6.3.4
Release:        1%{?dist}
Summary:        Multithreaded Fork of Redis
ExcludeArch:    %{ix86}
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://keydb.dev/
Source0:        https://github.com/snapchat/keydb/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}-sentinel.service
Source3:        %{name}.service
Source4:        %{name}.sysusers
Source5:        %{name}-limit-systemd
Source6:        %{name}.sysconfig
Source7:        %{name}-sentinel.sysconfig
%if %{with tests}
%endif
Requires:       logrotate
Patch:          use_destdir_var.patch
Provides:          bundled(hiredis) = 1.0.0
Provides:          bundled(jemalloc) = 5.2.1
Provides:          bundled(lua-libs) = 5.1.5
Provides:          bundled(linenoise) = 1.0
Provides:          bundled(hdr_histogram) = 0.11.0
Provides:          bundled(memkind) = 1.8.0
Provides:          bundled(rocksdb) = 7.9.2
Provides:          bundled(concurrentqueue)
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  libuuid-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  openssl-devel
BuildRequires:  procps-ng
BuildRequires:  snappy-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl
BuildRequires:  zlib-devel
# /oreon:deps
%description
KeyDB is a multi-threaded fork of Redis, an advanced key-value store.
It is often referred to as a data structure server since keys can contain
strings, hashes, lists, sets and sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Redis works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

KeyDB also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Redis behave like
a cache.

You can use Redis from most programming languages also.

%package           devel
Summary:           Development header for Redis module development
Provides:          %{name}-static = %{version}-%{release}
Conflicts:         redis-devel
%description       devel
Header file required for building loadable KeyDB modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n KeyDB-%{version} -p1
# these deps don't see to be used
rm -rf deps/cpp-statsd-client

mv deps/lua/COPYRIGHT             COPYRIGHT-lua
mv deps/jemalloc/COPYING          COPYING-jemalloc
mv deps/hiredis/COPYING           COPYING-hiredis
mv deps/hdr_histogram/LICENSE.txt LICENSE-hdrhistogram
mv deps/hdr_histogram/COPYING.txt COPYING-hdrhistogram

# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch ppc64le aarch64
sed -e 's/--with-lg-quantum/--with-lg-page=16 --with-lg-quantum/' -i deps/Makefile
%endif

%build

%make_build USE_SYSTEMD=yes PREFIX=%{_prefix} NO_MOTD=yes
%install
%make_install USE_SYSTEMD=yes PREFIX=%{_prefix} NO_MOTD=yes
install -p -D -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -d %{buildroot}%{_sharedstatedir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -pDm640 %{name}.conf  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm640 sentinel.conf %{buildroot}%{_sysconfdir}/%{name}/sentinel.conf
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:3} %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{buildroot}%{_unitdir}
built_man_dir="pkg/rpm/%{name}_build/%{name}_rpm%{_mandir}"
for page in ${built_man_dir}/*/*; do
    manx=$(basename $(dirname "$page"))
    target_dir="%{buildroot}%{_mandir}/$manx"
    mkdir -p "$target_dir"
    install -Dpm 644 "$page" "$target_dir/"
done
install -Dpm 644 src/redismodule.h %{buildroot}%{_includedir}/redismodule.h
install -Dpm 644 %{S:5} %{buildroot}%{_unitdir}/%{name}.service.d/limit.conf
install -Dpm 644 %{S:5} %{buildroot}%{_unitdir}/%{name}-sentinel.service.d/limit.conf
install -Dpm 644 %{S:6} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dpm 644 %{S:7} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-sentinel
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pre

%sysusers_create_compat %{S:4}
%post

%systemd_post %{name}.service
%systemd_post %{name}-sentinel.service
%preun

%systemd_preun %{name}.service
%systemd_preun %{name}-sentinel.service
%postun

%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}-sentinel.service
%check

%if %{with tests}
make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n keydb-devel -f %{oreon_filedir}/keydb-devel.list

%changelog

%autochangelog
