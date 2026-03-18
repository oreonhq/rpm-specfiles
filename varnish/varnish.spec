%global _hardened_build 0
# https://github.com/varnishcache/varnish-cache/issues/2269
%global debug_package %{nil}

%global __provides_exclude_from ^%{_libdir}/varnish/vmods

%global abi 71d4d75665f4d1949f7eeca28092a12df7037f3a
%global vrt 22.0

# Package scripts are now external
# https://github.com/varnishcache/pkg-varnish-cache
%global commit1 1f0d212dc45065f38bd80ac57fe22773a20a0595
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Default: Use jemalloc, as adviced by upstream project
# Change to 1 to use system allocator (ie. glibc)
#
# for rhel >= 10, use bundled jemalloc
# for rhel < 10, use system allocator
%bcond system_allocator %[0%{?rhel} && 0%{?rhel} < 10]
%bcond bundled_jemalloc %[0%{?rhel} >= 10]

%define jemalloc_version 5.3.0
%define jemalloc_prefix varnish_

%if %{with system_allocator}
# use _lto_cflags if present
%else
%global _lto_cflags %{nil}
%endif

Summary: High-performance HTTP accelerator
Name: varnish
Version: 8.0.0
Release: 2%{?dist}
License: BSD-2-Clause AND (BSD-2-Clause-FreeBSD AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain AND Zlib)
URL: https://www.varnish-cache.org/
Source0: http://varnish-cache.org/_downloads/%{name}-%{version}.tgz
Source1: https://github.com/varnishcache/pkg-varnish-cache/archive/%{commit1}.tar.gz#/pkg-varnish-cache-%{shortcommit1}.tar.gz
Source2: varnish.sysusers
Source3: https://github.com/jemalloc/jemalloc/releases/download/%{jemalloc_version}/jemalloc-%{jemalloc_version}.tar.bz2
Source4: varnish.tmpfiles

# Fix for h2 switch in varnishtest
# https://github.com/varnishcache/varnish-cache/issues/4298
Patch0:   varnish-7.7.0_fix_4298.patch

%if %{with bundled_jemalloc}
# bundled jemalloc patch
Patch100: jemalloc-5.3.0_fno-builtin.patch
Patch101: jemalloc-5.3.0-aarch64-ts-segfault.patch
%endif

Provides: varnish%{_isa} = %{version}-%{release}
Provides: varnishd(abi)%{_isa} = %{abi}
Provides: varnishd(vrt)%{_isa} = %{vrt}

Provides: vmod(blob)%{_isa} = %{version}-%{release}
Provides: vmod(cookie)%{_isa} = %{version}-%{release}
Provides: vmod(debug)%{_isa} = %{version}-%{release}
Provides: vmod(directors)%{_isa} = %{version}-%{release}
Provides: vmod(h2)%{_isa} = %{version}-%{release}
Provides: vmod(proxy)%{_isa} = %{version}-%{release}
Provides: vmod(purge)%{_isa} = %{version}-%{release}
Provides: vmod(std)%{_isa} = %{version}-%{release}
Provides: vmod(unix)%{_isa} = %{version}-%{release}
Provides: vmod(vtc)%{_isa} = %{version}-%{release}

%if %{with bundled_jemalloc}
Provides: bundled(jemalloc)
%endif

BuildRequires: systemd-rpm-macros
%{?systemd_requires}
%{?sysusers_requires_compat}

BuildRequires: python3, python3-sphinx, python3-docutils
BuildRequires: gcc
%if %{without bundled_jemalloc}
%if %{with system_allocator}
# use glibc
%else
%ifnarch aarch64
BuildRequires: jemalloc-devel
%endif
%endif
%endif

BuildRequires: libedit-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre2-devel
BuildRequires: pkgconfig

%if %{with bundled_jemalloc}
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  perl-generators
%endif

# Extra requirements for the build suite
#   needs haproxy2
%if 0%{?fedora} > 30 || 0%{?rhel} > 8
BuildRequires: haproxy
%endif
BuildRequires: nghttp2

# Varnish actually needs gcc installed to work. It uses the C compiler
# at runtime to compile the VCL configuration files. This is by design.
Requires: gcc
Requires: logrotate
Requires: ncurses
Requires: pcre2
Requires: redhat-rpm-config
Requires(post): /usr/bin/uuidgen

%if %{with system_allocator}
# use glibc
%else
%if %{without bundled_jemalloc}
Requires: jemalloc
%endif
%endif

%description
This is Varnish Cache, a high-performance HTTP accelerator.

Varnish Cache stores web pages in memory so web servers don’t have to
create the same web page over and over again. Varnish Cache serves
pages much faster than any application server; giving the website a
significant speed up.

Documentation wiki and additional information about Varnish Cache is
available on: https://www.varnish-cache.org/

%package devel
Summary: Development files for %{name}
#BuildRequires: ncurses-devel
Provides: varnish-libs-devel%{?isa} = %{version}-%{release}
Provides: varnish-libs-devel = %{version}-%{release}
Obsoletes: varnish-libs-devel < %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: python3

%description devel
Development files for %{name}
Varnish Cache is a high-performance HTTP accelerator

%package docs
Summary: Documentation files for %name

%description docs
Documentation files for %name

%prep
%setup -q
#patch 0 -p1
tar xzf %SOURCE1
ln -s pkg-varnish-cache-%{commit1}/redhat redhat
ln -s pkg-varnish-cache-%{commit1}/debian debian
cp redhat/find-provides .
sed -i 's,rst2man-3.6,rst2man-3.4,g; s,rst2html-3.6,rst2html-3.4,g; s,phinx-build-3.6,phinx-build-3.4,g' configure

# jemalloc
%if %{with bundled_jemalloc}
tar xjf %SOURCE3
sed -i '/^LIBPREFIX/s/@libprefix@/@libprefix@%{jemalloc_prefix}/' jemalloc*/Makefile.in
pushd jemalloc*
%patch 100 -p1 -b .jemalloc
%patch 101 -p1 -b .ts-segfault
popd

# Override PAGESIZE, bz #1545539
%ifarch %ix86 %arm x86_64 s390x riscv64
%define lg_page --with-lg-page=12
%endif

%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Disable thp on systems not supporting this for now
%ifarch %ix86 %arm aarch64 s390x
%define disable_thp --disable-thp
%endif
%endif

%build
%if %{with bundled_jemalloc}
# build bundled jemalloc first
pushd jemalloc*

echo "For debugging package builders"
echo "What is the pagesize?"
getconf PAGESIZE

echo "What mm features are available?"
ls /sys/kernel/mm
ls /sys/kernel/mm/transparent_hugepage || true
cat /sys/kernel/mm/transparent_hugepage/enabled || true

echo "What kernel version and config is this?"
uname -a

%configure %{?disable_thp} %{?lg_page} --enable-prof
make %{?_smp_mflags}
popd
%endif


# varnish
%if %{with system_allocator}
export CFLAGS="%{optflags}"
%else
# nilled _lto_cflags above because they remove the deps on jemalloc.
# On the fedoras, _lto_cflags is -flto=auto and -ffat-lto-objects. The latter is OK.
export CFLAGS="%{optflags} -ffat-lto-objects"
%endif

# https://gcc.gnu.org/wiki/FAQ#PR323
%ifarch %ix86
%if 0%{?fedora} > 21
export CFLAGS="$CFLAGS -ffloat-store -fexcess-precision=standard"
%endif
%endif

%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export CFLAGS="$CFLAGS -std=gnu17"
%endif

%if 0%{?fedora} > 42 || 0%{?rhel} > 10
export CFLAGS="$CFLAGS -Wno-error=discarded-qualifiers"
%endif

%ifarch s390x
export CFLAGS="$CFLAGS -Wno-error=free-nonheap-object"
%endif

# What platform is this
uname -a

# What gcc version is this?
gcc --version

# What is the page size
getconf PAGESIZE

# Man pages are prebuilt. No need to regenerate them.
export RST2MAN=/bin/true
# Explicit python, please
export PYTHON=python3

for f in configure configure.ac; do
  sed -i 's|ljemalloc|l%{jemalloc_prefix}jemalloc|g' $f
done

%if %{with bundled_jemalloc}
export LDFLAGS="$LDFLAGS -L%{_builddir}/%{name}-%{version}/jemalloc-%{jemalloc_version}/lib"
%endif

%configure LT_SYS_LIBRARY_PATH=%_libdir \
 --disable-static \
  --localstatedir=/var/lib  \
  --with-contrib \
  --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}} \
%ifarch %ix86
%if 0%{?fedora} <= 37
  --enable-pcre2-jit=no \
%endif
%endif
%if %{with system_allocator} || %{without bundled_jemalloc}
  --with-jemalloc=no \
%endif

%if %{with bundled_jemalloc}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/jemalloc-%{jemalloc_version}/lib
%endif

%make_build

# One varnish user is enough
sed -i 's,User=varnishlog,User=varnish,g;' redhat/varnishncsa.service

# Clean up the html documentation
rm -rf doc/html/_sources

%check
# check jemalloc first
%if %{with bundled_jemalloc}
pushd jemalloc*
make %{?_smp_mflags} check
popd
%endif

# Up the stack size in tests, necessary on secondary arches
sed -i 's/thread_pool_stack 80k/thread_pool_stack 128k/g;' bin/varnishtest/tests/*.vtc
sed -i 's/file,2M/file,8M/' bin/varnishtest/tests/r04036.vtc

# This is a bug in varnishtest making it incompatible with nghttp2 >= 1.65
#if 0#{?fedora} > 41 || 0#{?rhel} > 10
#rm bin/varnishtest/tests/a02022.vtc
#endif

%if %{with bundled_jemalloc}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/jemalloc-%{jemalloc_version}/lib
%endif

# Just a hack to avoid too high load on secondary arch builders
%ifarch s390x ppc64le
# This works when ran alone, but not in the whole suite. Load and/or timing issues
rm bin/varnishtest/tests/t02014.vtc
make -j2 check
%else
%make_build check
%endif

%install
rm -rf %{buildroot}

# jemalloc
%if %{with bundled_jemalloc}
pushd jemalloc*
make DESTDIR=%{buildroot} install_lib %{?_smp_mflags}

find %{buildroot}%{_libdir}/ -name '*.a' -exec rm -vf {} ';'

# we don't need .pc file
rm  %{buildroot}%{_libdir}/pkgconfig/jemalloc.pc
popd
%endif

%{make_install}

# None of these for fedora
find %{buildroot}/%{_libdir}/ -name '*.la' -exec rm -f {} ';'

mkdir -p %{buildroot}/var/lib/varnish
mkdir -p %{buildroot}/var/log/varnish
mkdir -p %{buildroot}/var/run/varnish
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
install -D -m 0644 etc/example.vcl %{buildroot}%{_sysconfdir}/varnish/default.vcl
install -D -m 0644 redhat/varnish.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/varnish
install -D -m 0644 include/vcs_version.h %{buildroot}%{_includedir}/varnish
install -D -m 0644 include/vrt.h %{buildroot}%{_includedir}/varnish

mkdir -p %{buildroot}%{_unitdir}
install -D -m 0644 redhat/varnish.service %{buildroot}%{_unitdir}/varnish.service
install -D -m 0644 redhat/varnishncsa.service %{buildroot}%{_unitdir}/varnishncsa.service
install -D -m 0755 redhat/varnishreload %{buildroot}%{_sbindir}/varnishreload
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/varnish.conf

# tmpfiles.d configuration
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 -p %{SOURCE4} %{buildroot}%{_tmpfilesdir}/varnish.conf

echo %{_libdir}/varnish > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# No idea why these ends up with mode 600 in the debug package
%if 0%{debug_package}
chmod 644 lib/libvmod_*/*.c
chmod 644 lib/libvmod_*/*.h
%endif

%pre
%sysusers_create_compat %{SOURCE2}

%files
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/*
%endif
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/%{name}
%{_var}/lib/varnish
%attr(0700,varnish,varnish) %dir %{_var}/log/varnish
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*
%license LICENSE
%doc README.rst ChangeLog
%doc etc/builtin.vcl etc/example.vcl
%dir %{_sysconfdir}/varnish/
%config(noreplace) %{_sysconfdir}/varnish/default.vcl
%config(noreplace) %{_sysconfdir}/logrotate.d/varnish
%config %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%{_unitdir}/varnish.service
%{_unitdir}/varnishncsa.service
%{_sysusersdir}/varnish.conf
%{_tmpfilesdir}/varnish.conf

%files devel
%license LICENSE
%doc README.rst
%{_libdir}/lib*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/varnishapi.pc
%{_datadir}/%{name}
%{_datadir}/aclocal/*.m4

%files docs
%license LICENSE
%doc doc/html
%doc doc/changes*.html

%post
%systemd_post varnish varnishncsa
/sbin/ldconfig
test -f /etc/varnish/secret || (uuidgen > /etc/varnish/secret && chmod 0600 /etc/varnish/secret)

%postun
%systemd_postun_with_restart varnish varnishncsa
/sbin/ldconfig


%preun
%systemd_preun varnish varnishncsa


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.0.0-2
- Prepare for Oreon 11 (RP1)
