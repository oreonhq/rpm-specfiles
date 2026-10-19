%global source0_hash 2f7beb5a3b2529c8d72dc0df9b8cdca31ab0e0c14d1e3421210f5e6ec0ab3b75
%global _hardened_build 1
%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global _hardlink /usr/bin/hardlink
%else
%global _hardlink /usr/sbin/hardlink
%endif
%ifarch %{ix86}
%global _file_offset_bits -D_FILE_OFFSET_BITS=64
%endif
Summary:        Open source remote desktop protocol (RDP) server
Name:      xrdp
Epoch:     1
Version:   0.10.6.1
Release:        1%{?dist}
License:   Apache-2.0 AND GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:       http://www.xrdp.org/
Source0:        https://github.com/neutrinolabs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:   xrdp-sesman.pamd
Source2:   xrdp.sysconfig
Source3:   xrdp.logrotate
Source4:   openssl.conf
Source5:   README.md
Source6:   xrdp.te
Source7:   xrdp-polkit-1.rules
Source8:   %{name}-tmpfiles.conf
Source9:   %{name}.sysusers
Patch0:    xrdp-0.10.2-sesman.patch
Patch1:    xrdp-0.10.3-xrdp-ini.patch
Patch2:    xrdp-0.10.1-service.patch
Patch3:    xrdp-0.10.0-scripts-libexec.patch
Patch4:    xrdp-0.9.6-script-interpreter.patch
Patch5:    xrdp-0.9.16-arch.patch
Patch6:    xrdp-0.9.18-vnc-uninit.patch
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Patch8:    xrdp-0.10.5-sesman-ini.patch
%endif
Requires: tigervnc-server-minimal
Requires: xorg-x11-xinit
Requires: util-linux
Requires: fuse3
Requires(post): systemd
Requires(post): systemd-sysv
Requires(post): /sbin/ldconfig
Requires(posttrans): openssl
Requires(preun): systemd
Requires(posttrans): systemd
# oreon:deps
BuildRequires:  /usr/bin/hardlink
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  checkpolicy
BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  openssl
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%package devel
Summary: Headers and pkg-config files needed to compile xrdp backends
Requires: %{name} = %{epoch}:%{version}-%{release}
%description
xrdp provides a fully functional RDP server compatible with a wide range
of RDP clients, including FreeRDP and Microsoft RDP client.

%description devel
This package contains headers necessary for developing xrdp backends that
talk to xrdp.

%package selinux
Summary: SELinux policy module required tu run xrdp
Requires: %{name} = %{epoch}:%{version}-%{release}
%if "%{_selinux_policy_version}" != ""
Requires: selinux-policy >= %{_selinux_policy_version}
%endif
Requires(post): /usr/sbin/semodule
Requires(postun): /usr/sbin/semodule
%description selinux
This package contains SELinux policy module necessary to run xrdp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?prerelease}
%{__cp} %{SOURCE5} .

# SELinux policy module
%{__mkdir} SELinux
%{__cp} -p %{SOURCE6} SELinux

# create 'bash -l' based startwm, to pick up PATH etc.
echo '#!/bin/bash -l
. %{_libexecdir}/xrdp/startwm.sh' > sesman/startwm-bash.sh

%build

autoreconf -vif
CFLAGS="$RPM_OPT_FLAGS %{?_missing_braces} %{?_file_offset_bits}" \
%configure --enable-fuse \
           --enable-pixman \
           --enable-painter \
           --enable-vsock \
           --enable-ipv6 \
           --enable-utmp \
           --with-socketdir=%{_rundir}/%{name} \
           --with-imlib2
%make_build
cd SELinux
for selinuxvariant in %{selinux_variants}
do
  %{__make} NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  %{__mv} %{name}.pp %{name}.pp.${selinuxvariant}
  %{__make} NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -
%install
%make_install
%{__install} -Dp -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/xrdp-sesman
%{__install} -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/xrdp
%{__install} -Dp -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/xrdp
%{__install} -Dp -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/xrdp/openssl.conf
%{__install} -Dp -m 755 sesman/startwm-bash.sh %{buildroot}%{_libexecdir}/xrdp/startwm-bash.sh
%{__mv} -f %{buildroot}%{_sysconfdir}/xrdp/startwm.sh %{buildroot}%{_libexecdir}/xrdp/
%{__mv} -f %{buildroot}%{_sysconfdir}/xrdp/reconnectwm.sh %{buildroot}%{_libexecdir}/xrdp/
%{__install} -Dp -m 644 %{SOURCE7} %{buildroot}%{_datadir}/polkit-1/rules.d/xrdp.rules
%{__mkdir_p} %{buildroot}%{_tmpfilesdir}
%{__install} -m 0644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/%{name}.conf
for selinuxvariant in %{selinux_variants}
do
  %{__install} -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  %{__install} -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
               %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done
%{_hardlink} -cv %{buildroot}%{_datadir}/selinux
%{__install} -p -D -m 0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/xrdp.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{?ldconfig}
%systemd_post xrdp.service
%preun

%systemd_preun xrdp.service
if [ $1 -eq 0 ]; then
  systemctl stop xrdp.service &>/dev/null || :
  systemd-tmpfiles --remove %{name}.conf &>/dev/null || :
fi
%triggerun -- xrdp < 0.6.0-1

systemd-sysv-convert --save xrdp &>/dev/null || :
systemctl preset xrdp.service &>/dev/null || :
/sbin/chkconfig --del xrdp &>/dev/null || :
if [ "`systemctl is-active xrdp.service`" = 'active' ]; then
    systemctl stop xrdp.service &>/dev/null || :
    systemctl start xrdp.service &>/dev/null || :
fi
%ldconfig_postun
%posttrans

if [ ! -s %{_sysconfdir}/xrdp/rsakeys.ini ]; then
  (umask 0137
   %{_bindir}/xrdp-keygen xrdp %{_sysconfdir}/xrdp/rsakeys.ini &>/dev/null)
fi
if [ ! -s %{_sysconfdir}/xrdp/cert.pem ]; then
  (umask 0337
   openssl req -x509 -newkey rsa:2048 -nodes -days 3652 \
               -keyout %{_sysconfdir}/xrdp/key.pem \
               -out %{_sysconfdir}/xrdp/cert.pem \
               -config %{_sysconfdir}/xrdp/openssl.conf &>/dev/null)
fi
chgrp xrdp %{_sysconfdir}/xrdp/{rsakeys.ini,{key,cert}.pem}
chmod 0640 %{_sysconfdir}/xrdp/{rsakeys.ini,{key,cert}.pem}
%post selinux

for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{name}.pp &> /dev/null || :
done
%postun selinux

if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -r %{name} &> /dev/null || :
  done
fi
%files -f %{oreon_filedir}/main.list
%files -n xrdp-devel -f %{oreon_filedir}/xrdp-devel.list
%files -n xrdp-selinux -f %{oreon_filedir}/xrdp-selinux.list

%changelog

%autochangelog
