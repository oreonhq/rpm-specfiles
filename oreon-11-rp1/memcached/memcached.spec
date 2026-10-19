%global source0_hash d362c64e6d8d5287153501eabf7c85b4a761432fbf53f5d7b085d0bb1653c1dd
%global source2_hash 4feb34eb8ce7f76b33211cb7fd666ef590bfccd705d4512aadb8f83f14ba4b2e
%bcond_without sasl
%bcond_with seccomp
%bcond_with tests
%global selinuxtype	targeted
%global selinuxmoduletype	contrib
%global selinuxmodulename	memcached
%global selinuxmodulever	1.0.3
%global selinuxmoduledir	%{selinuxmodulename}-selinux-%{selinuxmodulever}
Name:           memcached
Version:        1.6.45
Release:        1%{?dist}
Epoch:          0
Summary:        High Performance, Distributed Memory Object Cache
License:        BSD-3-clause AND Zlib AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://www.memcached.org/
Source0:        https://www.memcached.org/files/%{name}-%{version}.tar.gz
Source1:        memcached.sysconfig
Source2:        memcached-selinux-%{selinuxmodulever}.tar
Source3:	memcached.conf
Patch1:         memcached-unit.patch
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
%{?with_seccomp:BuildRequires: libseccomp-devel}
Requires(pre):  shadow-utils
Requires: (%{name}-selinux if selinux-policy-targeted)
%{?systemd_requires}
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package devel
Summary: Files needed for development using memcached protocol
Requires: %{name} = %{epoch}:%{version}-%{release}
%description devel
Install memcached-devel if you are developing C/C++ applications that require
access to the memcached binary include files.

%package selinux
Summary:             Selinux policy module
License:             GPL-2.0-only
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%description selinux
Install memcached-selinux to ensure your system contains the latest SELinux policy
optimised for use with this version of memcached.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
# Unpack memcached sources into memcached-X.X.X directory
# and SELinux policy sources into memcached-selinux-X.X
%setup -q -b 2
%autopatch -p1

%build

%configure \
  %{?with_sasl: --enable-sasl --enable-sasl-pwdb} \
  %{?with_seccomp: --enable-seccomp} \
  --enable-tls
make %{?_smp_mflags}
pushd ../%{selinuxmoduledir}
make
popd
%check

%{!?with_tests: exit 0}
rm -f t/whitespace.t
if [ `id -u` -ne 0 ]; then
  rm -f t/daemonize.t t/watcher.t t/expirations.t
fi
make test
%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
rm -f %{buildroot}/%{_bindir}/memcached-debug
install -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
install -Dp -m0644 scripts/memcached-tool.1 \
        %{buildroot}%{_mandir}/man1/memcached-tool.1
install -Dp -m0644 scripts/memcached.service \
        %{buildroot}%{_unitdir}/memcached.service
install -Dp -m0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
pushd ../%{selinuxmoduledir}
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{selinuxmoduletype}
install -m 0644 %{selinuxmodulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
popd
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/memcached.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post

%systemd_post memcached.service
%post selinux

%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2 &> /dev/null
%preun

%systemd_preun memcached.service
%postun

%systemd_postun_with_restart memcached.service
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{selinuxmodulename}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype} &> /dev/null
%files -f %{oreon_filedir}/main.list
%files -n memcached-devel -f %{oreon_filedir}/memcached-devel.list
%files -n memcached-selinux -f %{oreon_filedir}/memcached-selinux.list

%changelog

%autochangelog
