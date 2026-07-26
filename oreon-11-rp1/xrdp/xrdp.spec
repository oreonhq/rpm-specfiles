%global source0_hash 9abc96d164de4b1c40e2f3f537d0593d052a640cf3388978c133715ea69fb123

#%%global prerelease -rc.1

%global _hardened_build 1

%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})

%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
%global _hardlink /usr/bin/hardlink
%else
%global _hardlink /usr/sbin/hardlink
%endif

%if ! 0%{?fedora} && 0%{?rhel} <= 7
%global _missing_braces -Wno-error=missing-braces
%endif

%ifarch %{ix86}
%global _file_offset_bits -D_FILE_OFFSET_BITS=64
%endif

Summary:   Open source remote desktop protocol (RDP) server
Name:      xrdp
Epoch:     1
Version:   0.10.5
Release:   1%{?dist}
# Automatically converted from old format: ASL 2.0 and GPLv2+ and MIT - review is highly recommended.
License:   Apache-2.0 AND GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:       http://www.xrdp.org/
Source0:   https://github.com/neutrinolabs/xrdp/releases/download/v%{version}%{?prerelease}/xrdp-%{version}%{?prerelease}.tar.gz
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
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
Patch8:    xrdp-0.10.5-sesman-ini.patch
%endif

BuildRequires: make
BuildRequires: gcc
BuildRequires: automake autoconf libtool
BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrandr-devel
BuildRequires: imlib2-devel
BuildRequires: openssl
BuildRequires: pam-devel
BuildRequires: pkgconfig(fuse3)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(systemd)
BuildRequires: nasm
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: noopenh264-devel
%endif

BuildRequires: checkpolicy, selinux-policy-devel
BuildRequires: %{_hardlink}

BuildRequires: systemd-rpm-macros
%if 0%{?fedora} < 42 || 0%{?rhel}
%{?sysusers_requires_compat}
%endif

# tigervnc-server-minimal provides Xvnc (default for now)
# xorgxrdp is another back end, depends on specific Xorg binary, omit
Requires: tigervnc-server-minimal
Requires: xorg-x11-xinit
Requires: util-linux
Requires: fuse3

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: %{name}-selinux = %{epoch}:%{version}-%{release}
%endif

Requires(post): systemd
Requires(post): systemd-sysv
Requires(post): /sbin/ldconfig
Requires(posttrans): openssl
Requires(preun): systemd
%if 0%{?fedora}
Requires(preun): systemd-tmpfiles
%endif
Requires(posttrans): systemd

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
%if 0%{?fedora} || 0%{?rhel} > 8
           --enable-openh264 \
%endif
           --enable-utmp \
           --with-socketdir=%{_rundir}/%{name} \
           --with-imlib2

%make_build

# SELinux policy module
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

#install sesman pam config /etc/pam.d/xrdp-sesman
%{__install} -Dp -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/xrdp-sesman

#install xrdp sysconfig /etc/sysconfig/xrdp
%{__install} -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/xrdp

#install logrotate /etc/logrotate.d/xrdp
%{__install} -Dp -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/xrdp

#install openssl.conf /etc/xrdp
%{__install} -Dp -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/xrdp/openssl.conf

#install 'bash -l' startwm script
%{__install} -Dp -m 755 sesman/startwm-bash.sh %{buildroot}%{_libexecdir}/xrdp/startwm-bash.sh

#move startwm and reconnectwm scripts to libexec
%{__mv} -f %{buildroot}%{_sysconfdir}/xrdp/startwm.sh %{buildroot}%{_libexecdir}/xrdp/
%{__mv} -f %{buildroot}%{_sysconfdir}/xrdp/reconnectwm.sh %{buildroot}%{_libexecdir}/xrdp/

#install xrdp.rules /usr/share/polkit-1/rules.d
%{__install} -Dp -m 644 %{SOURCE7} %{buildroot}%{_datadir}/polkit-1/rules.d/xrdp.rules

# Temporary files for socket
%{__mkdir_p} %{buildroot}%{_tmpfilesdir}
%{__install} -m 0644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# SELinux policy module
for selinuxvariant in %{selinux_variants}
do
  %{__install} -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  %{__install} -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
               %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done
%{_hardlink} -cv %{buildroot}%{_datadir}/selinux

%{__install} -p -D -m 0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/xrdp.conf

%if 0%{?fedora} < 42 || 0%{?rhel}
%pre
%sysusers_create_compat %{SOURCE9}
%endif

%post
%{?ldconfig}
%systemd_post xrdp.service

%preun
%systemd_preun xrdp.service
if [ $1 -eq 0 ]; then
  # Stop services on package removal (see bug 1349083)
  systemctl stop xrdp.service &>/dev/null || :
  systemd-tmpfiles --remove %{name}.conf &>/dev/null || :
fi

%triggerun -- xrdp < 0.6.0-1
systemd-sysv-convert --save xrdp &>/dev/null || :

# If the package is allowed to autostart:
systemctl preset xrdp.service &>/dev/null || :

# Run these because the SysV package being removed won't do them
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

%files
%doc COPYING README.md
%dir %{_libdir}/xrdp
%dir %{_sysconfdir}/xrdp
%dir %{_sysconfdir}/xrdp/pulse
%dir %{_datadir}/xrdp
%dir %{_libexecdir}/xrdp
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/xrdp.conf
%config(noreplace) %{_sysconfdir}/xrdp/xrdp.ini
%config(noreplace) %{_sysconfdir}/pam.d/xrdp-sesman
%config(noreplace) %{_sysconfdir}/logrotate.d/xrdp
%config(noreplace) %{_sysconfdir}/sysconfig/xrdp
%config(noreplace) %{_sysconfdir}/xrdp/sesman.ini
%config(noreplace) %{_sysconfdir}/xrdp/km*.ini
%config(noreplace) %{_sysconfdir}/xrdp/openssl.conf
%config(noreplace) %{_sysconfdir}/xrdp/xrdp_keyboard.ini
%config(noreplace) %{_sysconfdir}/xrdp/gfx.toml
%config(noreplace) %{_sysconfdir}/xrdp/pulse/default.pa
%exclude %ghost %{_sysconfdir}/xrdp/*.pem
%exclude %ghost %{_sysconfdir}/xrdp/rsakeys.ini
%{_libexecdir}/xrdp/startwm*.sh
%{_libexecdir}/xrdp/reconnectwm.sh
%{_libexecdir}/xrdp/waitforx
%{_libexecdir}/xrdp/xrdp-sesexec
%{_libexecdir}/xrdp/xrdp-droppriv
%{_bindir}/xrdp-genkeymap
%{_bindir}/xrdp-sesadmin
%{_bindir}/xrdp-keygen
%{_bindir}/xrdp-sesrun
%{_bindir}/xrdp-dis
%{_bindir}/xrdp-dumpfv1
%{_sbindir}/xrdp-chansrv
%{_sbindir}/xrdp
%{_sbindir}/xrdp-sesman
%{_datadir}/xrdp/ad256.bmp
%{_datadir}/xrdp/cursor0.cur
%{_datadir}/xrdp/cursor1.cur
%{_datadir}/xrdp/xrdp256.bmp
%{_datadir}/xrdp/sans-10.fv1
%{_datadir}/xrdp/sans-18.fv1
%{_datadir}/xrdp/ad24b.bmp
%{_datadir}/xrdp/xrdp24b.bmp
%{_datadir}/xrdp/xrdp_logo.bmp
%{_datadir}/xrdp/xrdp_logo.png
%{_datadir}/xrdp/xrdp-chkpriv
%{_datadir}/xrdp/README.logo
%{_datadir}/polkit-1/rules.d/xrdp.rules
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_mandir}/man1/*
%{_libdir}/xrdp/lib*.so*
%exclude %{_libdir}/xrdp/libcommon.so
%exclude %{_libdir}/xrdp/libxrdp.so
%exclude %{_libdir}/xrdp/libxrdpapi.so
%{_unitdir}/xrdp-sesman.service
%{_unitdir}/xrdp.service
%exclude %{_includedir}/painter.h
%exclude %{_libdir}/libpainter.*
%exclude %{_libdir}/pkgconfig/libpainter.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/xrdp/*.a
%if 0%{?rhel}
%exclude %{_libdir}/*.la
%exclude %{_libdir}/xrdp/*.la
%endif
%ghost %{_localstatedir}/log/xrdp.log
%ghost %{_localstatedir}/log/xrdp-sesman.log
%exclude %{_libdir}/pkgconfig/rfxcodec.pc

%files devel
%{_includedir}/ms-*
%{_includedir}/xrdp*
%{_includedir}/rfxcodec_*.h
%{_libdir}/xrdp/libcommon.so
%{_libdir}/xrdp/libxrdp.so
%{_libdir}/xrdp/libxrdpapi.so
%{_libdir}/pkgconfig/rfxcodec.pc
%{_libdir}/pkgconfig/xrdp.pc

%files selinux
%doc SELinux/%{name}.te
%{_datadir}/selinux/*/%{name}.pp

%changelog
%autochangelog
