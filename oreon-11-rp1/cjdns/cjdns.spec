%global source3_hash dd3720127190f4edb78ed32bf7cf01909d725f01f593e983ee18d0c0c48fd96d
%global source0_hash 99e20274d581949b9a5998564485f567732e7888ac786c2edb43493048e4d0ef
%bcond_with subnode
%bcond_with embedded
%bcond_without generic
%bcond_without libsodium
%bcond_without seccomp
%bcond_with libuv
%bcond_with python2
%bcond_without python3
%if %{with embedded}
%global use_embedded 1
%else
%global use_embedded 0
%endif
%if %{with libuv}
%global use_libuv 1
%else
%global use_libuv 0
%endif
%if %{with generic}
%global generic_build 1
%else
%global generic_build 0
%endif
%if %{with libsodium}
%global use_libsodium 1
%global nacl_name libsodium
%global nacl_version 1.0.14
%global nacl_lib %{_libdir}/libsodium.so
%else
%global use_libsodium 0
%global nacl_name nacl
%global nacl_version 20110221
%global nacl_lib %{_libdir}/libnacl.so
%endif
%global use_systemd 1
%global use_upstart 0
%global use_marked 0
%global makeman pandoc -s -tman
%global with_admin 0
%{!?__restorecon: %global __restorecon /sbin/restorecon}
Name:           cjdns
Version:        22.3
Release:        1%{?dist}
Summary:        The privacy-friendly network without borders
License:        GPLv3 and MIT and BSD and ISC
URL:            http://hyperboria.net/
Source0:        https://github.com/cjdelisle/cjdns/archive/%{name}-v%{version}.tar.gz
Source1: cjdns.README_Fedora.md
Source2: cjdns.service
%if 0%{?use_marked}
Source3: https://github.com/kapouer/marked-man/archive/0.7.0.tar.gz#/marked-man-0.7.0.tar.gz
%endif
Source4: python-cjdns-0.2.tar.gz
Patch0: cjdns.selinux.patch
Patch2: cjdns.warnings.patch
Patch4:  cjdns.genconf.patch
Patch5:  cjdns.sbin.patch
Patch6:  cjdns.dyn.patch
Patch9:  cjdns.man.patch
Patch10: cjdns.tools.patch
Patch11: cjdns.sodium.patch
Patch12: cjdns.sign.patch
Patch18: cjdns.libuv.patch
Patch20: cjdns.sysctl.patch
Patch22: cjdns.gcc10.patch
Patch23: cjdns.flagdup.patch
Patch100: cjdns-add-riscv64-support.patch
%if !0%{use_embedded}
%endif
Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires(pre): shadow-utils
%if 0%{use_libuv}
%else
Provides: bundled(libuv) = 0.11.19
%endif
%if 0%{use_embedded}
Provides: bundled(nacl) = 20110221
%endif
ExclusiveArch: %{nodejs_arches}
# oreon:deps
BuildRequires:  checkpolicy
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gyp
BuildRequires:  libsodium-devel
BuildRequires:  make
BuildRequires:  nodejs
BuildRequires:  pandoc
BuildRequires:  policycoreutils
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
# /oreon:deps
%description
Cjdns implements an encrypted IPv6 network using public-key cryptography for
address allocation and a distributed hash table for routing. This provides
near-zero-configuration networking, and prevents many of the security and
scalability issues that plague existing networks.

%package selinux
Summary: Targeted SELinux policy module for cjdns
BuildRequires: policycoreutils, checkpolicy, selinux-policy-devel
Requires: policycoreutils, selinux-policy-targeted
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description selinux
Targeted SELinux policy module for cjdns.

# FIXME: keep C tools separate?
%package tools
Summary: Nodejs tools for cjdns
Requires: nodejs, %{name} = %{version}-%{release}
BuildArch: noarch
%description tools
Nodejs tools for cjdns. Highlights:
peerStats          show current peer status
cjdnslog           display cjdroute log
cjdns-traceroute   trace route to cjdns IP
sessionStats       show current crypto sessions

%if %{with python2}
%package -n python2-cjdns
%{?python_provide:%python_provide python2-cjdns}
Provides: %{name}-python = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary: Python tools for cjdns
BuildRequires: python-rpm-macros
Requires: python2, %{name} = %{version}-%{release}
BuildArch: noarch
%description -n python2-cjdns
Python tools for cjdns.
%endif

%if %{with python3}
%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary: Python tools for cjdns
BuildRequires: python3-rpm-macros, python3-devel
Requires: python3, %{name} = %{version}-%{release}
BuildArch: noarch
%if !%{with python2}
Obsoletes: python2-%{name} < 20.4-2
%endif
%description -n python3-%{name}
Python tools for cjdns.
%endif

%package graph
Summary: Python peer graph tools for cjdns
%if %{with python3}
Requires: python3-%{name} = %{version}-%{release}
Requires: python3-networkx
%else
Requires: python2-%{name} = %{version}-%{release}
Requires: python2-networkx
%endif
BuildArch: noarch
%description graph
Python peer graph tools for cjdns.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn cjdns-%{name}-v%{version}
%patch -P0 -b .selinux

%patch -P4 -b .genconf
%patch -P5 -b .sbin

cp %{SOURCE2} contrib/systemd

%if 0%{use_embedded}
# disable CPU opt
%else
# use system nacl library if provided.  
if test -x %{nacl_lib}; then
%if 0%{use_libsodium}
%patch -P11 -b .sodium
%else
%patch -P6 -b .dyn
%endif
  rm -rf node_build/dependencies/cnacl
# use static library if system nacl doesn't provide dynamic
elif test -d %{_includedir}/nacl && test -r %{_libdir}/libnacl.a; then
  cd node_build/dependencies
  rm -rf cnacl
  mkdir -p cnacl/jsbuild
  ln -s %{_libdir}/libnacl.a cnacl/jsbuild
  ln -s %{_includedir}/nacl cnacl/jsbuild/include
  cd -
fi
%patch -P12 -b .sign
cd crypto/sign
sed -i -e'/^#include / s,[<>],",g' crypto*int*.h
cd -
%endif

%patch -P9 -b .man
%patch -P10 -b .tools
#patch13 -b .ppc64
#patch14 -b .entropy
#patch15 -b .benc
#patch16 -b .python3
%if 0%{use_libuv}
%patch -P18 -p1 -b .libuv
rm -rf node_build/dependencies/libuv
%else
rm -rf node_build/dependencies/libuv/build/gyp # use system gyp
%ifarch armv7hl
sed -i -e '/optimizeLevel:/ s/-O0/-O3/' node_build/make.js
%else
sed -i -e '/optimizeLevel:/ s/-O0/-O3/' node_build/make.js
%endif
%endif
#patch19 -p1 -b .fuzz
#patch20 -p1 -b .sysctl
#patch22 -b .gcc10
%patch -P23 -b .flagdup
%patch -P2 -b .warn

%ifarch riscv64
%patch -P100 -p1 -b .riscv64
%endif

cp %{SOURCE1} README_Fedora.md

# Remove #!env from python scripts
chmod a+x contrib/python/cjdnsadmin/cli.py
find contrib/python/cjdnsadmin ! -executable -name "*.py" |
        xargs sed -e '\,^#!/usr/bin/env, d' -i
find contrib/python -type f |
        xargs sed -e '1 s,^#!/usr/bin/env ,#!/usr/bin/,' -i 
sed -e '$ s,^python ,/usr/bin/python2 ,' -i contrib/python/cjdnsa

# Remove #!env from nodejs scripts
find tools -type f | xargs grep -l '^#!\/usr\/bin\/env ' |
        xargs sed -e '1 s,^#!/usr/bin/env ,#!/usr/bin/,' -i

# Fix deprecated Buffer ctor except on EL6
sed -e '1,$ s/new Buffer/Buffer.from/' -i \
        tools/lib/publicToIp6.js tools/lib/cjdnsadmin/cjdnsadmin.js

# Remove unpackaged code with undeclared licenses
%if !%{with_admin}
rm -rf contrib/nodejs   # GPLv3 and ASL 2.0
%endif
rm -rf contrib/http     # GPLv2 and MIT

cat >cjdns-up.sh <<'EOF'
#!/bin/sh

cjdev="$(cjdns-online -i)" || exit 1

for s in %{_sysconfdir}/cjdns/up.d/*.sh; do
  if test -x "$s"; then
    "$s" up $cjdev
  fi
done
EOF

chmod a+x cjdns-up.sh

sed -i -e 's/-march=native/-mtune=generic/' node_build/make.js
#rm node_build/dependencies/cnacl/node_build/plans/*_AVX_plan.json
# Leaving SSE2 code in since x86 is secondary arch and pretty much everyone
# is going to have SSE2, except things like XO-1 which needs custom build.
#rm node_build/dependencies/cnacl/node_build/plans/x86_SSE2_plan.json

%if !%{use_marked}
for i in contrib/doc/*.md; do
  sed -i -e'1,1 s/^/% /' -e'1,1 s/--/|/' -e'2,2d' $i
done
%endif

# remove hidden files from node_modules/nthen
cd node_modules/nthen
rm -f .f* .j* .t*
cd -

# python3 API
%if %{with python3}
tar xvfz %{SOURCE4}
mv python-cjdns-* python-cjdns
%endif

# FIXME: grep Version_CURRENT_PROTOCOL util/version/Version.h and
# check that it matches major %%{version}

%build

cd contrib/selinux
ln -s /usr/share/selinux/devel/Makefile .
make 
cd -
%if 0 && %{with python3}
cd python-cjdns
python3 setup.py build 
cd -
%endif
%if !%{with seccomp}
export Seccomp_NO=1
%endif
%if %{with subnode}
export SUBNODE=1
%endif
(IFS='='; env -0 | while read -d $'\0' KEY VALUE; do printf 'export %s=%q\n' "$KEY" "$VALUE"; done) >rpm.env
NO_TEST=1 CJDNS_RELEASE_VERSION="%{name}-%{version}-%{release}" ./do 
%check

build_linux/test_testcjdroute_c all >test.out
%install
mkdir -p %{buildroot}%{_sbindir}
install -p cjdroute %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
install -pm 644 contrib/systemd/cjdns*.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/cjdns/up.d
mkdir -p %{buildroot}/var/empty/cjdns
mkdir -p %{buildroot}%{_datadir}/selinux/targeted
install -pm 644 contrib/selinux/cjdns.pp %{buildroot}%{_datadir}/selinux/targeted
ln -f contrib/selinux/cjdns.{te,fc} .  # for doc dir
mkdir -p %{buildroot}%{_libexecdir}/cjdns/{node_build,contrib}
install -p publictoip6 privatetopublic mkpasswd makekeys randombytes sybilsim \
        %{buildroot}%{_libexecdir}/cjdns
rm -f node_modules/nthen/.npmignore
cp -pr tools node_modules %{buildroot}%{_libexecdir}/cjdns
cp -p cjdns-up.sh %{buildroot}%{_libexecdir}/cjdns/cjdns-up
mkdir -p %{buildroot}%{_bindir}
%if %{with python3}
mkdir -p %{buildroot}%{_libexecdir}/cjdns/python
cd python-cjdns
python3 setup.py install -O1 --root %{buildroot}
cd -
mv %{buildroot}/%{_bindir}/* %{buildroot}/%{_libexecdir}/cjdns/python
rm -f %{buildroot}%{python3_sitelib}/cjdnsadmin/bencode.py.LICENSE.txt
rm -f %{buildroot}%{_libexecdir}/cjdns/python/README.md
rm -f %{buildroot}%{_libexecdir}/cjdns/python/cjdns-dynamic.conf
%endif
for t in peerStats sessionStats cjdnslog search dumpLinks dumptable \
         dumpRumorMill pathfinderTree pingAll; do
  ln -sf %{_libexecdir}/cjdns/tools/$t %{buildroot}%{_bindir}
done
for t in traceroute; do
  ln -sf %{_libexecdir}/cjdns/tools/$t %{buildroot}%{_bindir}/cjdns-$t
done
for t in publictoip6 randombytes makekeys; do
  ln -sf %{_libexecdir}/cjdns/$t %{buildroot}%{_bindir}
done
install -pm 755 contrib/systemd/cjdns-online.sh \
        %{buildroot}%{_bindir}/cjdns-online
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
install -pm 644 doc/man/cjdroute.conf.5 %{buildroot}%{_mandir}/man5
cd contrib/doc
for m in *.md; do
  case ${m%.md} in
  traceroute) M="1"
    %{makeman} $m >%{buildroot}%{_mandir}/man$M/cjdns-${m%.md}.$M
    continue ;;
  privatetopublic|sybilsim) M="8" ;;
  *) M="1" ;;
  esac
  %{makeman} $m >%{buildroot}%{_mandir}/man$M/${m%.md}.$M
done
cd -
%if %{with python2}
%if !%{with python3}
cp -pr contrib/python %{buildroot}%{_libexecdir}/cjdns
rm %{buildroot}%{_libexecdir}/cjdns/python/README.md
rm %{buildroot}%{_libexecdir}/cjdns/python/cjdns-dynamic.conf
rm %{buildroot}%{_libexecdir}/cjdns/python/cjdnsadmin/bencode.py.LICENSE.txt
%endif
mkdir -p %{buildroot}%{python2_sitelib}
cp -pr contrib/python/cjdnsadmin %{buildroot}%{python2_sitelib}
%endif
%if %{with python2} || %{with python3}
for t in pingAll.py trashroutes \
         getLinks ip6topk pktoip6 cjdnsa searches findnodes; do
  ln -sf %{_libexecdir}/cjdns/python/$t %{buildroot}%{_bindir}
done
%endif
for t in drawgraph dumpgraph graphStats; do
  ln -sf %{_libexecdir}/cjdns/python/$t %{buildroot}%{_bindir}
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

getent group cjdns > /dev/null || groupadd -r cjdns
getent passwd cjdns > /dev/null || /usr/sbin/useradd -g cjdns \
        -c "End to end encrypted IPv6 mesh" \
        -r -d %{_libexecdir}/cjdns -s /sbin/nologin cjdns
exit 0
%post

%systemd_post cjdns.service
%postun

%systemd_postun_with_restart cjdns.service
%preun

%systemd_preun cjdns.service
%post selinux

/usr/sbin/semodule -s targeted -i %{_datadir}/selinux/targeted/cjdns.pp \
        &>/dev/null || :
%{__restorecon} %{_sbindir}/cjdroute
%postun selinux

if [ $1 -eq 0 ] ; then
/usr/sbin/semodule -s targeted -r cjdns &> /dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
