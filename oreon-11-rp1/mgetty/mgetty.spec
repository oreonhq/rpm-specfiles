%global source0_hash c8a72f5ca4142e30627ad16725c40692fb09e6284514392b95ac02062cac9a89
%define SENDFAX_UID 78
%ifnarch s390 s390x
%global _hardened_build 1
%endif
Summary:        A getty replacement for use with data and fax modems
Name: mgetty
Version: 1.2.1
Release:        1%{?dist}
Source0:        ftp://mgetty.greenie.net/pub/mgetty/source/1.2/mgetty-%{version}.tar.gz
Source1: ftp://mgetty.greenie.net/pub/mgetty/source/1.2/mgetty-%{version}.tar.gz.asc
Source2: logrotate.mgetty
Source3: logrotate.sendfax
Source4: logrotate.vgetty
Source5: logrotate.vm
Source6: vgetty@.service
Source7: mgetty@.service
Patch0: mgetty-1.2.1-config.patch
Patch1: mgetty-1.2.1-policy.patch
Patch2: mgetty-1.2.1-system-gsm.patch
Patch4: mgetty-1.1.25-voiceconfig.patch
Patch5: mgetty-1.2.1-issue.patch
Patch6: mgetty-1.1.31-issue-doc.patch
Patch7: mgetty-1.1.29-helper.patch
Patch8: mgetty-1.2.1-mktemp.patch
Patch9: mgetty-1.2.1-unioninit.patch
Patch11: mgetty-1.2.1-helper2.patch
Patch12: mgetty-1.2.1-no-acroread.patch
Patch14: mgetty-1.2.1-sendmail_path.patch
Patch15: mgetty-1.2.1-lfs.patch
Patch16: mgetty-1.2.1-162174_tcflush.patch
Patch18: mgetty-1.1.33-bug_63843.patch
Patch19: mgetty-1.1.33-167830_tty_access.patch
Patch20: mgetty-1.2.1-167830.patch
Patch21: mgetty-1.2.1-turn.patch
Patch22: mgetty-1.2.1-time_range.patch
Patch23: mgetty-1.2.1-handle_spaces.patch
Patch24: mgetty-1.1.36-man.patch
Patch25: mgetty-1.1.36-sd.patch
Patch26: mgetty-1.1.36-makefiles.patch
Patch27: mgetty-1.2.1-lockdev.patch
Patch28: mgetty-1.2.1-hardening.patch
Patch29: mgetty-sys_nerr-removed.patch
Patch30: mgetty-manpage-typos.patch
Patch31: mgetty-c99.patch
Patch32: mgetty-gcc15-stdc23.patch
License: GPL-2.0-or-later
Requires: coreutils, /usr/sbin/sendmail, uucp
Requires(post): systemd
Requires(postun): systemd
URL: http://mgetty.greenie.net/
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gsm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  lockdev-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo-tex
BuildRequires:  texlive-dvips
# /oreon:deps
%package sendfax
Summary: Provides support for sending faxes over a modem
Requires: mgetty = %{version}
Requires: coreutils
Requires: netpbm-progs
Conflicts: hylafax+
%package voice
Summary: A program for using your modem and mgetty as an answering machine
Requires: mgetty = %{version}
Requires(post): systemd
Requires(postun): systemd
%package viewfax
Summary: An X Window System fax viewer
%description
The mgetty package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem). If you're using a Class 2 or 2.0
modem, mgetty can receive faxes. If you also need to send faxes,
you'll need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should
install the mgetty package. If you'd like to send faxes using mgetty
and your modem, you'll need to install the mgetty-sendfax program. If
you need a viewer for faxes, you'll also need to install the
mgetty-viewfax package.

%description sendfax
Sendfax is a standalone backend program for sending fax files. The
mgetty program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2
modem.

If you'd like to send faxes over a Class 2 modem, you'll need to
install the mgetty-sendfax and the mgetty packages.

%description voice
The mgetty-voice package contains the vgetty system, which enables
mgetty and your modem to support voice capabilities. In simple terms,
vgetty lets your modem act as an answering machine. How well the
system will work depends upon your modem, which may or may not be able
to handle this kind of implementation.

Install mgetty-voice along with mgetty if you'd like to try having
your modem act as an answering machine.

%description viewfax
Viewfax displays the fax files received using mgetty in an X11 window.
Viewfax is capable of zooming in and out on the displayed fax.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mv policy.h-dist policy.h
%patch -P 0 -p1 -b .config
%patch -P 1 -p1 -b .policy
%patch -P 2 -p1 -b .system-gsm
rm -r voice/libmgsm
%patch -P 4 -p1 -b .voiceconfig
%patch -P 5 -p1 -b .issue
%patch -P 6 -p1 -b .issue-doc
%patch -P 7 -p1 -b .helper
%patch -P 8 -p1 -b .mktemp
%patch -P 9 -p1 -b .unioninit
%patch -P 11 -p1 -b .helper2
%patch -P 12 -p1 -b .no-acroread
%patch -P 14 -p1 -b .sendmail_path
%patch -P 15 -p1 -b .lfs
%patch -P 16 -p1 -b .162174_tcflush
%patch -P 18 -p1 -b .bug_63843
%patch -P 19 -p1 -b .167830_tty_access
%patch -P 20 -p1 -b .167830
%patch -P 21 -p1 -b .turn
%patch -P 22 -p1 -b .time_range
%patch -P 23 -p1 -b .handle_spaces
%patch -P 24 -p1 -b .man
%patch -P 25 -p1 -b .sd
%patch -P 26 -p1 -b .makefile
%patch -P 27 -p1 -b .lockdev
%patch -P 28 -p1 -b .hardening
%patch -P 29 -p1 -b .sys_nerr-removed
%patch -P 30 -p1 -b .manpage-typos
%patch -P 31 -p1 -b .c99
%patch -P 32 -p1 -b .gcc15-stdc23

# Create a sysusers.d config file
cat >mgetty.sysusers.conf <<EOF
u fax %SENDFAX_UID 'mgetty fax spool user' /var/spool/fax -
EOF

%build

%define makeflags CFLAGS="$RPM_OPT_FLAGS -Wall -DAUTO_PPP -D_FILE_OFFSET_BITS=64 -DHAVE_LOCKDEV -fno-strict-aliasing" LIBS="-llockdev" prefix=%{_prefix} spool=%{_var}/spool BINDIR=%{_bindir} SBINDIR=%{_sbindir} LIBDIR=%{_libdir}/mgetty+sendfax HELPDIR=%{_libdir}/mgetty+sendfax CONFDIR=%{_sysconfdir}/mgetty+sendfax MANDIR=%{_mandir} MAN1DIR=%{_mandir}/man1 MAN4DIR=%{_mandir}/man4 MAN5DIR=%{_mandir}/man5 MAN8DIR=%{_mandir}/man8 INFODIR=%{_infodir} ECHO='"echo -e"' INSTALL=%{__install}
make %{makeflags}
make -C voice %{makeflags}
make -C tools %{makeflags}
pushd frontends/X11/viewfax
make OPT="$RPM_OPT_FLAGS" CONFDIR=%{_sysconfdir}/mgetty+sendfax
popd
%install
mkdir -p %{buildroot}{%{_bindir},%{_infodir},%{_libdir}/mgetty+sendfax}
mkdir -p %{buildroot}{%{_mandir},%{_sbindir},/var/spool}
mkdir -p %{buildroot}%{_sysconfdir}/mgetty+sendfax
%define instflags CFLAGS="$RPM_OPT_FLAGS -Wall -DAUTO_PPP" prefix=%{buildroot}%{_prefix} spool=%{buildroot}%{_var}/spool BINDIR=%{buildroot}%{_bindir} SBINDIR=%{buildroot}%{_sbindir} LIBDIR=%{buildroot}%{_libdir}/mgetty+sendfax HELPDIR=%{buildroot}%{_libdir}/mgetty+sendfax CONFDIR=%{buildroot}%{_sysconfdir}/mgetty+sendfax MANDIR=%{buildroot}%{_mandir} MAN1DIR=%{buildroot}%{_mandir}/man1 MAN4DIR=%{buildroot}%{_mandir}/man4 MAN5DIR=%{buildroot}%{_mandir}/man5 MAN8DIR=%{buildroot}%{_mandir}/man8 INFODIR=%{buildroot}%{_infodir} ECHO='echo -e' INSTALL=%{__install}
make install %instflags
install -m700 callback/callback %{buildroot}%{_sbindir}
install -m4711 callback/ct %{buildroot}%{_bindir}
mv %{buildroot}%{_mandir}/man1/fax.1 %{buildroot}%{_mandir}/man1/mgetty_fax.1
make -C tools install %instflags
mkdir -p %{buildroot}%{_var}/spool/voice/{messages,incoming}
make -C voice install %instflags
install -m 600 -c voice/voice.conf-dist %{buildroot}%{_sysconfdir}/mgetty+sendfax/voice.conf
find samples -type f -exec chmod 644 {} \;
make -C frontends/X11/viewfax install %instflags MANDIR=%{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/mgetty
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sendfax
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/vgetty
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/vm
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/
install -m 0644 distro/faxrunqd.service %{buildroot}%{_unitdir}/
rm -f %{buildroot}%{_bindir}/cutbl
rm -f %{buildroot}%{_bindir}/g3topbm
install -m0644 -D mgetty.sysusers.conf %{buildroot}%{_sysusersdir}/mgetty.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post mgetty@.service
%preun

%systemd_preun mgetty@.service
%postun

%systemd_postun_with_restart mgetty@.service
exit 0
%post sendfax

%systemd_post faxrunqd.service
%preun sendfax

%systemd_preun faxrunqd.service
%postun sendfax

%systemd_postun_with_restart faxrunqd.service
exit 0
%post voice

%systemd_post vgetty@.service
%preun voice

%systemd_postun vgetty@.service
%postun voice

%systemd_postun_with_restart vgetty@.service
exit 0
%files -f %{oreon_filedir}/main.list
%files -n mgetty-sendfax -f %{oreon_filedir}/mgetty-sendfax.list
%files -n mgetty-voice -f %{oreon_filedir}/mgetty-voice.list
%files -n mgetty-viewfax -f %{oreon_filedir}/mgetty-viewfax.list

%changelog

%autochangelog
