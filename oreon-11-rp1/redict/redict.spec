%global source0_hash 868220e6b51062709420f6b2343f03c98eac113c77eefac4626ba909085504f7
%bcond_with        tests
Name:              redict
Version:           7.3.6
Release:        1%{?dist}
Summary:        A persistent key-value database
License:           BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0 AND LGPL-3.0-only AND LGPL-3.0-or-later
URL:               https://redict.io
Source0:        https://codeberg.org/redict/redict/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:           %{name}.logrotate
Source2:           %{name}-sentinel.service
Source3:           %{name}.service
Source4:           %{name}.sysusers
Source5:           %{name}-limit-systemd
Source6:           %{name}.sysconfig
Source7:           %{name}-sentinel.sysconfig
Source8:           macros.%{name}
%if %{with tests}
%endif
Requires:          logrotate
Requires(pre):     shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
Provides:          bundled(hiredict) = 1.0.3
Provides:          bundled(jemalloc) = 5.3.0
Provides:          bundled(lua-libs) = 5.1.5
Provides:          bundled(linenoise) = 1.0
Provides:          bundled(lzf)
Provides:          bundled(hdr_histogram) = 0.11.0
Provides:          bundled(fpconv)
%global redict_modules_abi 1
%global redict_modules_dir %{_libdir}/%{name}/modules
Provides:          redict(modules_abi)%{?_isa} = %{redict_modules_abi}
ExcludeArch:       %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  procps-ng
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl
# /oreon:deps
%description
Redict is an advanced key-value store. It is often referred to as a data
structure server since keys can contain strings, hashes, lists, sets and
sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Redict works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

Redict also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Redict behave like
a cache.

You can use Redict from most programming languages also.

%package           devel
Summary:           Development header for Redict module development
Provides:          %{name}-static = %{version}-%{release}
%description       devel
Header file required for building loadable Redict modules.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

mv deps/lua/COPYRIGHT             COPYRIGHT-lua
mv deps/jemalloc/COPYING          COPYING-jemalloc
mv deps/hiredict/LICENSES/BSD-3-Clause.txt COPYING-hiredict-BSD-3-Clause
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
api=`sed -n -e 's/#define REDICTMODULE_APIVER_[0-9][0-9]* //p' src/redictmodule.h`
if test "$api" != "%{redict_modules_abi}"; then
   : Error: Upstream API version is now ${api}, expecting %%{redict_modules_abi}.
   : Update the redict_modules_abi macro, the rpmmacros file, and rebuild.
   exit 1
fi

%global make_flags DEBUG="" V="echo" PREFIX=%{_prefix} BUILD_WITH_SYSTEMD=yes BUILD_TLS=yes

%build

%make_build %{make_flags}
%install
%make_install %{make_flags}
rm -rf %{buildroot}%{_datadir}/%{name}
install -p -D -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -d %{buildroot}%{_sharedstatedir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -d %{buildroot}%{redict_modules_dir}
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -pDm640 %{name}.conf  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm640 sentinel.conf %{buildroot}%{_sysconfdir}/%{name}/sentinel.conf
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:3} %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{buildroot}%{_unitdir}
install -p -D -m 644 %{S:5} %{buildroot}%{_unitdir}/%{name}.service.d/limit.conf
install -p -D -m 644 %{S:5} %{buildroot}%{_unitdir}/%{name}-sentinel.service.d/limit.conf
chmod 755 %{buildroot}%{_bindir}/%{name}-*
install -pDm644 src/%{name}module.h %{buildroot}%{_includedir}/%{name}module.h
install -pDm644 %{S:8} %{buildroot}%{_rpmmacrodir}/macros.%{name}
install -Dpm 644 %{S:6} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dpm 644 %{S:7} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-sentinel
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
taskset -c 1 make %{make_flags} test
make %{make_flags} test-sentinel
%endif
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
%files -f %{oreon_filedir}/main.list
%files -n redict-devel -f %{oreon_filedir}/redict-devel.list

%changelog

%autochangelog
