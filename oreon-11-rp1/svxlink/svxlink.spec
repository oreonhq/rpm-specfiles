%global source0_hash 27095fd0a06e3bf7bd597f0472d568d5a651a7f9deab30f1489a1291f05c5e9c

%define __cmake_in_source_build 1

%define main_version 24.02
%define async_version 1.7.0
%define echolib_version 1.3.4
%define qtel_version 1.2.5
%define server_version 1.8.0
%define reflector_version 1.2.0

Name:		svxlink
Epoch:		2
Version:	%{main_version}
Release:	7%{?dist}
Summary:	Repeater controller and EchoLink (simplex or repeater)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.svxlink.org
Source0:	https://github.com/sm0svx/svxlink/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/sm0svx/svxlink-sounds-en_US-heather/releases/download/%{version}/svxlink-sounds-en_US-heather-16k-%{version}.tar.bz2

Source4:	%{name}-tmpfs.conf

# src/svxlink/svxlink/EventHandler.cpp:485:31:
# error: invalid conversion from ‘void*’ to ‘char*’ [-fpermissive]
Patch0:		svxlink-24.02-fpermissive.patch

BuildRequires:	make
BuildRequires:	cmake libsigc++-devel libsigc++20-devel qt-devel
BuildRequires:	speex-devel opus-devel popt-devel libgcrypt-devel tcl-devel
BuildRequires:	gsm-devel doxygen tk-devel desktop-file-utils alsa-lib-devel
BuildRequires:	systemd-units rtl-sdr-devel chrpath
BuildRequires:	jsoncpp-devel libcurl-devel

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
The SvxLink project is a multi purpose voice services system for
ham radio use. For example, EchoLink connections are supported.
Also, the SvxLink server can act as a repeater controller.

%package -n libasync
Summary: Svxlink async libs
Epoch: 2
Version: %{async_version}

%description -n libasync
The Async library is a programming framework that is used to write event driven
applications. It provides abstractions for file descriptor watches, timers,
network communications, serial port communications and config file reading.

Async is written in such a way that it can support other frameworks. Right now
there are two basic frameworks, a simple "select" based implementation and a Qt
implementation. The idea is that advanced libraries can be implemented in such
a way that they only depend on Async. That means that these libraries can be
used in both Qt and pure console applications and in any future frameworks
supported by Async (e.g. Gtk, wxWidgets etc).

Another big part of Async is the audio pipe framework. It is an audio handling
framework that is geared towards single channel (mono) audio applications. The
framework consists of a large number of audio handling classes such as
audio i/o, filtering, mixing, audio codecs etc.

%package -n libasync-devel
Summary: Svxlink async development files
Epoch: 2
Version: %{async_version}
Requires: libasync = %{epoch}:%{async_version}
Obsoletes:	svxlink-server-devel < 0.11.1-2

%description -n libasync-devel
The async library development files

%package -n libasync-doc
Summary: Svxlink async documentation files
Epoch: 2
Version: %{async_version}
Requires: libasync = %{epoch}:%{async_version}

%description -n libasync-doc
The async library documentation files in HTML format

%package -n echolib
Summary: EchoLink communications library
Epoch: 2
Version: %{echolib_version}

%description -n echolib
EchoLib is a library that is used as a base for writing EchoLink applications.
It implements the directory server protocol as well as the station to station
protocol. EchoLink is used to link ham radio stations together over the
Internet.

%package -n echolib-devel
Summary: Development files for the EchoLink communications library
Epoch: 2
Version: %{echolib_version}
Requires: echolib = %{epoch}:%{echolib_version}
Obsoletes:	svxlink-server-devel < 0.11.1-2

%description -n echolib-devel
Development files for the EchoLink communications library

%package -n echolib-doc
Summary: Documentation files for the EchoLink communications library
Epoch: 2
Version: %{echolib_version}
Requires: echolib = %{epoch}:%{echolib_version}

%description -n echolib-doc
Documentation files for the EchoLink communications library in HTML format

%package -n qtel
Summary: The Qt EchoLink Client
Epoch: 1
Version: %{qtel_version}
Requires: hicolor-icon-theme

%description -n qtel
This package contains Qtel, the Qt EchoLink client. It is an implementation of
the EchoLink software in Qt. This is only an EchoLink client, that is it can
not be connected to a transceiver to create a link. If it is a pure link node
you want, install the svxlink-server package.

%package -n svxlink-server
Summary: SvxLink - A general purpose voice services system
Epoch: 1
Version: %{server_version}
Requires: udev
Requires (pre): shadow-utils

%description -n svxlink-server
The SvxLink server is a general purpose voice services system for ham radio
use. Each voice service is implemented as a plugin called a module.
Some examples of voice services are: Help system, Simplex repeater,
EchoLink communications and voice mail.

The core of the system handle the radio interface and is quite flexible
as well. It can act both as a simplex node and as a repeater controller. It is
also possible to link multiple receivers in via TCP/IP. The best receiver is
chosen using a software voter.

%package -n svxlink-reflector
Summary: An audio reflector for connecting SvxLink Servers
Epoch: 1
Version: %{reflector_version}

%description -n svxlink-reflector
The SvxReflector application is meant to be used as a center point
to link SvxLink nodes together. The new SvxLink ReflectorLogic logic core is
used to connect a SvxLink node to the reflector server. One or more logics can
then be connected to the reflector using normal logic linking.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{main_version}
%setup -q -D -T -a 1 -n %{name}-%{main_version}
%patch 0 -p1

# Create a sysusers.d config file
cat >svxlink.sysusers.conf <<EOF
g daemon -
u svxlink -:daemon 'SvxLink Daemon ' - -
m svxlink audio
m svxlink dialout
EOF

%build
%cmake -DLOCAL_STATE_DIR=%{_localstatedir} -DWITH_SYSTEMD=1 \
	-DSYSTEMD_CONFIGURATIONS_FILES_DIR=%{_unitdir} \
	-DSYSTEMD_DEFAULTS_FILES_DIR=%{_sysconfdir}/sysconfig src
make %{?_smp_mflags} all doc
doxygen doc/doxygen.async
doxygen doc/doxygen.echolib

%install
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/svxlink
cp -a en_US-heather-16k %{buildroot}%{_datadir}/svxlink/sounds/en_US
mkdir -p %{buildroot}%{_localstatedir}/log
mkdir -p %{buildroot}%{_localstatedir}/spool/svxlink/{propagation_monitor,qso_recorder,voice_mail}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_sysconfdir}/security/console.perms.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}
install -p -m 755 bin/devcal %{buildroot}%{_bindir}
chrpath --delete %{buildroot}%{_bindir}/devcal
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -p -m 0644 %{SOURCE4} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
touch %{buildroot}%{_localstatedir}/log/svxlink
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications src/qtel/qtel.desktop
cp distributions/fedora/%{_sysconfdir}/logrotate.d/svxlink %{buildroot}%{_sysconfdir}/logrotate.d/svxlink-server
cp distributions/fedora/%{_sysconfdir}/logrotate.d/remotetrx %{buildroot}%{_sysconfdir}/logrotate.d
#don't pack htmlized man files
#seems to confuse cmake rules and doesn't make much
#sense to pack man files in html format
rm %{buildroot}%{_docdir}/svxlink/man1/*html*
rm %{buildroot}%{_docdir}/svxlink/man5/*html*

# Remove static linked files
find %{buildroot} -name '*.a' -exec rm -f {} ';'

sed -i -e "s@EnvironmentFile=/etc/default@EnvironmentFile=/etc/sysconfig@g" %{buildroot}%{_unitdir}/*.service

install -m0644 -D svxlink.sysusers.conf %{buildroot}%{_sysusersdir}/svxlink.conf

%ldconfig_scriptlets -n libasync

%ldconfig_scriptlets -n echolib

%pre -n svxlink-reflector
getent group daemon >/dev/null || groupadd -r daemon
getent passwd svxlink >/dev/null || \
useradd -r -g daemon -d / -s /sbin/nologin \
-c "SvxLink Daemon " svxlink
/usr/sbin/usermod -a -G audio,dialout svxlink >/dev/null 2>&1 || :
exit 0

%post -n svxlink-server
%systemd_post svxlink.service
%systemd_post remotetrx.service

%preun -n svxlink-server
%systemd_preun svxlink.service
%systemd_preun remotetrx.service

%postun -n svxlink-server
%systemd_postun_with_restart svxlink.service
%systemd_postun_with_restart remotetrx.service

%triggerun -- svxlink < 2:14.08.1-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply svxlink
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save svxlink >/dev/null 2>&1 ||:
/usr/bin/systemd-sysv-convert --save remotetrx >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del svxlink >/dev/null 2>&1 || :
/sbin/chkconfig --del remotetrx >/dev/null 2>&1 || :
/bin/systemctl try-restart svxlink.service >/dev/null 2>&1 || :
/bin/systemctl try-restart remotetrx.service >/dev/null 2>&1 || :

%files -n libasync
%doc COPYRIGHT src/async/ChangeLog
%defattr(755,root,root)
%{_libdir}/libasync*.so.*

%files -n libasync-devel
%{_libdir}/libasyncaudio.so
%{_libdir}/libasynccore.so
%{_libdir}/libasynccpp.so
%{_libdir}/libasyncqt.so
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/common.h
%{_includedir}/svxlink/Async*
%{_includedir}/svxlink/CppStdCompat.h

%files -n libasync-doc
%doc %{_pkgdocdir}/async/*

%files -n echolib
%doc COPYRIGHT src/echolib/ChangeLog
%defattr(755,root,root)
%{_libdir}/libecholib*.so.*

%files -n echolib-devel
%{_libdir}/libecholib.so
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/EchoLink*

%files -n echolib-doc
%doc %{_pkgdocdir}/echolib/*

%files -n qtel
%doc COPYRIGHT src/qtel/ChangeLog
%{_bindir}/qtel
%{_datadir}/qtel
%{_datadir}/icons/hicolor/128x128/apps/qtel.png
%{_datadir}/applications/qtel.desktop
%{_metainfodir}/org.svxlink.Qtel.metainfo.xml
%{_mandir}/man*/qtel*

%files -n svxlink-server
%doc COPYRIGHT src/svxlink/ChangeLog
%{_bindir}/devcal
%{_bindir}/svxlink
%{_sbindir}/svxlink_gpio_up
%{_sbindir}/svxlink_gpio_down
%{_bindir}/remotetrx
%{_bindir}/siglevdetcal
%{_unitdir}/svxlink.service
%{_unitdir}/svxlink_gpio_setup.service
%{_unitdir}/remotetrx.service

%dir %{_libdir}/svxlink
%dir /run/%{name}
%{_tmpfilesdir}/svxlink.conf
%{_libdir}/svxlink/Module*.so
%{_libdir}/svxlink/*Logic.so
%dir %{_sysconfdir}/%{name}/svxlink.d
%{_datadir}/svxlink
%defattr(644,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/svxlink
%config(noreplace) %{_sysconfdir}/sysconfig/remotetrx
%config(noreplace) %{_sysconfdir}/%{name}/svxlink.conf
%config(noreplace) %{_sysconfdir}/%{name}/gpio.conf
%config(noreplace) %{_sysconfdir}/%{name}/node_info.json
%config(noreplace) %{_sysconfdir}/%{name}/.procmailrc
%config(noreplace) %{_sysconfdir}/%{name}/svxlink.d/*
%config(noreplace) %{_sysconfdir}/%{name}/TclVoiceMail.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/svxlink-server
%config(noreplace) %{_sysconfdir}/logrotate.d/remotetrx
%config(noreplace) %{_sysconfdir}/%{name}/remotetrx.conf
%{_mandir}/man1/devcal.*.*
%{_mandir}/man1/svxlink.*.*
%{_mandir}/man1/remotetrx.*.*
%{_mandir}/man1/siglevdetcal.*.*
%{_mandir}/man5/*
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink/propagation_monitor
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink/qso_recorder
%attr(755,svxlink,daemon) %dir %{_localstatedir}/spool/svxlink/voice_mail
%ghost %{_localstatedir}/log/svxlink
%{_sysusersdir}/svxlink.conf

%files -n svxlink-reflector
%{_bindir}/svxreflector
%{_bindir}/svxreflector-status
%config(noreplace) %{_sysconfdir}/sysconfig/svxreflector
%config(noreplace) %{_sysconfdir}/%{name}/svxreflector.conf
%{_mandir}/man1/svxreflector.*
%{_mandir}/man5/svxreflector.*
%{_unitdir}/svxreflector.service

%changelog
%autochangelog
