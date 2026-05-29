%global source0_hash none

%bcond_with bootstrap
%bcond_without check

%if %{without bootstrap}
%{?!WITH_MONO:          %global WITH_MONO 1}
%else
%{?!WITH_MONO:          %global WITH_MONO 0}
%endif

%{?!WITH_COMPAT_DNSSD:  %global WITH_COMPAT_DNSSD 1}
%{?!WITH_COMPAT_HOWL:   %global WITH_COMPAT_HOWL  1}
%{?!WITH_QT3:           %global WITH_QT3 0}
%{?!WITH_QT4:           %global WITH_QT4 0}

%if %{without bootstrap}
%{?!WITH_GTK2:          %global WITH_GTK2 1}
%{?!WITH_GTK3:          %global WITH_GTK3 1}
%{?!WITH_QT5:           %global WITH_QT5 1}
%else
%{?!WITH_GTK2:          %global WITH_GTK2 0}
%{?!WITH_GTK3:          %global WITH_GTK3 0}
%{?!WITH_QT5:           %global WITH_QT5 0}
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1751484
%{?!WITH_PYTHON:        %global WITH_PYTHON 0}

%ifnarch %{mono_arches}
%define WITH_MONO 0
%endif

%if 0%{?fedora}
%global WITH_QT3 1
%global WITH_QT4 1
%endif

%if 0%{?rhel}
%if 0%{?rhel} > 9
%global WITH_GTK2 0
%endif
%global WITH_MONO 0
%global WITH_QT5 0
%if 0%{?rhel} < 8
%global WITH_PYTHON 1
%endif
%endif

%if 0%{?fedora} == 34 || 0%{?rhel} >= 9
# https://bugzilla.redhat.com/show_bug.cgi?id=1907727
%global _lto_cflags %{nil}
%endif

# http://bugzilla.redhat.com/1008395 - no hardened build
%global _hardened_build 1

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

%define rc rc2

Name:             avahi
Version:          0.9%{?rc:~%{rc}}
Release:          8%{?dist}
Summary:          Local network service discovery
License:          LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause-Views AND MIT
URL:              http://avahi.org
Requires:         dbus
Requires:         expat
Requires:         libdaemon >= 0.11
# For /usr/bin/dbus-send
Requires(post):   dbus
Requires(pre):    coreutils
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    dbus-devel >= 0.90
BuildRequires:    desktop-file-utils
%if %{WITH_GTK2}
BuildRequires:    gtk2-devel
%endif
%if %{WITH_GTK3}
BuildRequires:    gtk3-devel >= 2.99.0
%endif
#BuildRequires:    gobject-introspection-devel
%if %{WITH_QT3}
BuildRequires:    qt3-devel
%endif
%if %{WITH_QT4}
BuildRequires:    qt4-devel
%endif
%if %{WITH_QT5}
BuildRequires:    qt5-qtbase-devel
%endif
BuildRequires:    libdaemon-devel >= 0.11
BuildRequires:    glib2-devel
BuildRequires:    libcap-devel
BuildRequires:    expat-devel
%if %{WITH_PYTHON}
%if %{without bootstrap}
BuildRequires:    pygtk2
%endif
%if 0%{?fedora} > 27
%global python2_dbus python2-dbus
%global python2_libxml2 python2-libxml2
%else
%global python2_dbus dbus-python
%global python2_libxml2 libxml2-python
%endif
BuildRequires:    %{python2_dbus}
BuildRequires:    %{python2_libxml2}
# really only need interpreter + rpm-macros -- rex
BuildRequires:    python2-devel
BuildRequires:    python3-devel
%else
Obsoletes: python2-avahi < %{version}-%{release}
Obsoletes: python3-avahi < %{version}-%{release}
%endif
BuildRequires:    gdbm-devel
BuildRequires:    pkgconfig(pygobject-3.0)
BuildRequires:    pkgconfig(libevent) >= 2.0.21
BuildRequires:    intltool
BuildRequires:    perl-XML-Parser
BuildRequires:    xmltoman
%if %{WITH_MONO}
BuildRequires:    mono-devel
BuildRequires:    monodoc-devel
%endif
BuildRequires:    systemd
BuildRequires:    systemd-devel
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    gettext-devel

%if 0%{?rc:1}
Source0:        https://github.com/avahi/avahi/archive/refs/tags/v%{version_no_tilde}.tar.gz
%else
Source0:        https://github.com/avahi/avahi/releases/download/v%{version_no_tilde}/avahi-%{version_no_tilde}.tar.gz
%endif

## upstream patches
# https://github.com/avahi/avahi/pull/662
Patch1: avahi-0.9-CVE-2024-52615.patch
# https://github.com/avahi/avahi/pull/707
Patch2: avahi-0.9-address-data-size.patch

## downstream patches
Patch100: avahi-0.6.30-mono-libdir.patch
Patch102: avahi-0.8-no_undefined.patch

%description
Avahi is a system which facilitates service discovery on
a local network -- this means that you can plug your laptop or
computer into a network and instantly be able to view other people who
you can chat with, find printers to print to or find files being
shared. This kind of technology is already found in MacOS X (branded
'Rendezvous', 'Bonjour' and sometimes 'ZeroConf') and is very
convenient.

%package tools
Summary:          Command line tools for mDNS browsing and publishing
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description tools
Command line tools that use avahi to browse and publish mDNS services.

%package ui-tools
Summary:          UI tools for mDNS browsing
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
Requires:         %{name}-glib%{?_isa} = %{version}-%{release}
Requires:         %{name}-ui-gtk3%{?_isa} = %{version}-%{release}
Requires:         tigervnc
Requires:         openssh-clients
%if %{WITH_PYTHON}
Requires:         gdbm
Requires:         pygtk2
Requires:         pygtk2-libglade
Requires:         python2-avahi = %{version}-%{release}
Requires:         %{python2_dbus}
Requires:         python2-gobject-base
%endif

%description ui-tools
Graphical user interface tools that use Avahi to browse for mDNS services.

%package glib
Summary:          Glib libraries for avahi
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description glib
Libraries for easy use of avahi from glib applications.

%package glib-devel
Summary:          Libraries and header files for avahi glib development
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
Requires:         %{name}-glib%{?_isa} = %{version}-%{release}
Requires:         glib2-devel

%description glib-devel
The avahi-devel package contains the header files and libraries
necessary for developing programs using avahi with glib.

%package gobject
Summary:          GObject wrapper library for Avahi
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
Requires:         %{name}-glib%{?_isa} = %{version}-%{release}

%description gobject
This library contains a GObject wrapper for the Avahi API

%package gobject-devel
Summary:          Libraries and header files for Avahi GObject development
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
Requires:         %{name}-gobject%{?_isa} = %{version}-%{release}

%description gobject-devel
The avahi-gobject-devel package contains the header files and libraries
necessary for developing programs using avahi-gobject.

%if %{WITH_GTK2}
%package ui
Summary:          Gtk user interface library for Avahi (Gtk+ 2 version)
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
Requires:         %{name}-glib%{?_isa} = %{version}-%{release}
Requires:         gtk2

%description ui
This library contains a Gtk 2.x widget for browsing services.
%endif

%if %{WITH_GTK3}
%package ui-gtk3
Summary:          Gtk user interface library for Avahi (Gtk+ 3 version)
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
Requires:         %{name}-glib%{?_isa} = %{version}-%{release}
Requires:         gtk3

%description ui-gtk3
This library contains a Gtk 3.x widget for browsing services.
%endif

%if %{WITH_GTK2} || %{WITH_GTK3}
%package ui-devel
Summary:          Libraries and header files for Avahi UI development
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
%if %{WITH_GTK2}
Requires:         %{name}-ui%{?_isa} = %{version}-%{release}
%endif
%if %{WITH_GTK3}
Requires:         %{name}-ui-gtk3%{?_isa} = %{version}-%{release}
%endif

%description ui-devel
The avahi-ui-devel package contains the header files and libraries
necessary for developing programs using avahi-ui.
%endif

%if %{WITH_QT3}
%package qt3
Summary:          Qt3 libraries for avahi
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description qt3
Libraries for easy use of avahi from Qt3 applications.

%package qt3-devel
Summary:          Libraries and header files for avahi Qt3 development
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
Requires:         %{name}-qt3%{?_isa} = %{version}-%{release}

%description qt3-devel
The avahi-qt3-devel package contains the header files and libraries
necessary for developing programs using avahi with Qt3.
%endif

%if %{WITH_QT4}
%package qt4
Summary:          Qt4 libraries for avahi
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description qt4
Libraries for easy use of avahi from Qt4 applications.

%package qt4-devel
Summary:          Libraries and header files for avahi Qt4 development
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
Requires:         %{name}-qt4%{?_isa} = %{version}-%{release}

%description qt4-devel
Th avahi-qt4-devel package contains the header files and libraries
necessary for developing programs using avahi with Qt4.
%endif

%if %{WITH_QT5}
%package qt5
Summary:          Qt5 libraries for avahi
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description qt5
Libraries for easy use of avahi from Qt5 applications.

%package qt5-devel
Summary:          Libraries and header files for avahi Qt5 development
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
Requires:         %{name}-qt5%{?_isa} = %{version}-%{release}

%description qt5-devel
Th avahi-qt5-devel package contains the header files and libraries
necessary for developing programs using avahi with Qt5.
%endif

%if %{WITH_MONO}
%package sharp
Summary:          Mono language bindings for avahi mono development
Requires:         mono-core >= 1.1.13
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description sharp
The avahi-sharp package contains the files needed to develop
mono programs that use avahi.

%package ui-sharp
Summary:          Mono language bindings for avahi-ui
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
Requires:         %{name}-ui%{?_isa} = %{version}-%{release}
Requires:         %{name}-sharp%{?_isa} = %{version}-%{release}
Requires:         mono-core >= 1.1.13
Requires:         gtk-sharp2
BuildRequires:    gtk-sharp2-devel
BuildRequires: make

%description ui-sharp
The avahi-sharp package contains the files needed to run
Mono programs that use avahi-ui.

%package ui-sharp-devel
Summary:          Mono language bindings for developing with avahi-ui
Requires:         %{name}-ui-sharp%{?_isa} = %{version}-%{release}

%description ui-sharp-devel
The avahi-sharp-ui-devel package contains the files needed to develop
Mono programs that use avahi-ui.
%endif

%package libs
Summary:          Libraries for avahi run-time use

%description libs
The avahi-libs package contains the libraries needed
to run programs that use avahi.

%package devel
Summary:          Libraries and header files for avahi development
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
# for libavahi-core
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
The avahi-devel package contains the header files and libraries
necessary for developing programs using avahi.

%if %{WITH_COMPAT_HOWL}
%package compat-howl
Summary:          Libraries for howl compatibility
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:        howl-libs < 0.6-16
Provides:         howl-libs = %{version}-%{release}

%description compat-howl
Libraries that are compatible with those provided by the howl package.

%package compat-howl-devel
Summary:          Header files for development with the howl compatibility libraries
Requires:         %{name}-compat-howl%{?_isa} = %{version}-%{release}
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:        howl-devel < 0.6-16
Provides:         howl-devel = %{version}-%{release}

%description compat-howl-devel
Header files for development with the howl compatibility libraries.
%endif

%if %{WITH_COMPAT_DNSSD}
%package compat-libdns_sd
Summary:          Libraries for Apple Bonjour mDNSResponder compatibility
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description compat-libdns_sd
Libraries for Apple Bonjour mDNSResponder compatibility.

%package compat-libdns_sd-devel
Summary:          Header files for the Apple Bonjour mDNSResponder compatibility libraries
Requires:         %{name}-compat-libdns_sd%{?_isa} = %{version}-%{release}
Requires:         %{name}-devel%{?_isa} = %{version}-%{release}

%description compat-libdns_sd-devel
Header files for development with the Apple Bonjour mDNSResponder compatibility
libraries.
%endif

%package autoipd
Summary:          Link-local IPv4 address automatic configuration daemon (IPv4LL)
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description autoipd
avahi-autoipd implements IPv4LL, "Dynamic Configuration of IPv4
Link-Local Addresses"  (IETF RFC3927), a protocol for automatic IP address
configuration from the link-local 169.254.0.0/16 range without the need for a
central server. It is primarily intended to be used in ad-hoc networks which
lack a DHCP server.

%package dnsconfd
Summary:          Configure local unicast DNS settings based on information published in mDNS
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description dnsconfd
avahi-dnsconfd connects to a running avahi-daemon and runs the script
/etc/avahi/dnsconfd.action for each unicast DNS server that is announced on the
local LAN. This is useful for configuring unicast DNS servers in a DHCP-like
fashion with mDNS.

%if %{WITH_PYTHON}
%package -n python2-avahi
Summary:          Python2 Avahi bindings
Obsoletes:        python-avahi < 0.7
Provides:         python-avahi = %{version}-%{release}
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python2-avahi
%{summary}.

%package -n python3-avahi
Summary:          Python3 Avahi bindings
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-avahi
%{summary}.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-%{version_no_tilde} -p1

rm -fv docs/INSTALL

# Create two sysusers.d config files
cat >avahi.sysusers.conf <<EOF
u avahi 70 'Avahi mDNS/DNS-SD Stack' %{_localstatedir}/run/avahi-daemon -
EOF
cat >avahi-autoipd.sysusers.conf <<EOF
u avahi-autoipd 170 'Avahi IPv4LL Stack' %{_localstatedir}/lib/avahi-autoipd -
EOF


%build
## why autogen?
## * kills rpaths
## * fixes -stack-protector flags (once gcc_stack_protect.m4 is removed)
rm -fv missing common/gcc_stack_protect.m4
NOCONFIGURE=1 ./autogen.sh

%configure \
        --with-distro=fedora \
        --disable-monodoc \
        --with-avahi-user=avahi \
        --with-avahi-group=avahi \
        --with-avahi-priv-access-group=avahi \
        --with-autoipd-user=avahi-autoipd \
        --with-autoipd-group=avahi-autoipd \
        --with-systemdsystemunitdir=%{_unitdir} \
        --enable-introspection=no \
        --enable-shared=yes \
        --enable-static=no \
        --disable-silent-rules \
%if %{with check}
        --enable-tests \
%endif
%if %{WITH_GTK2}
        --enable-gtk \
%else
        --disable-gtk \
%endif
%if %{WITH_GTK3}
        --enable-gtk3 \
%else
        --disable-gtk3 \
%endif
%if ! %{WITH_PYTHON}
        --disable-python \
%endif
%if %{WITH_COMPAT_DNSSD}
        --enable-compat-libdns_sd \
%endif
%if %{WITH_COMPAT_HOWL}
        --enable-compat-howl \
%endif
%if %{WITH_QT3}
        --enable-qt3 \
%endif
%if %{WITH_QT4}
        --enable-qt4 \
%endif
%if ! %{WITH_QT5}
        --disable-qt5 \
%endif
%if ! %{WITH_MONO}
        --disable-mono \
%endif
;

# workaround parallel build issues (aarch64 only so far, bug #1564553)
%make_build -k V=1 || make V=1


%install
%make_install

# omit libtool .la files
rm -fv %{buildroot}%{_libdir}/lib*.la

# remove example
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/ssh.service
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service

# create /var/run/avahi-daemon to ensure correct selinux policy for it:
mkdir -p %{buildroot}%{_localstatedir}/run/avahi-daemon
mkdir -p %{buildroot}%{_localstatedir}/lib/avahi-autoipd

# remove the documentation directory - let % doc handle it:
rm -rfv %{buildroot}%{_datadir}/%{name}-%{version}

# Make /etc/avahi/etc/localtime owned by avahi:
mkdir -p %{buildroot}%{_sysconfdir}/avahi/etc
touch %{buildroot}%{_sysconfdir}/avahi/etc/localtime

# fix bug 197414 - add missing symlinks for avahi-compat-howl and avahi-compat-dns-sd
%if %{WITH_COMPAT_HOWL}
ln -s avahi-compat-howl.pc  %{buildroot}/%{_libdir}/pkgconfig/howl.pc
%endif
%if %{WITH_COMPAT_DNSSD}
ln -s avahi-compat-libdns_sd.pc %{buildroot}/%{_libdir}/pkgconfig/libdns_sd.pc
ln -s avahi-compat-libdns_sd/dns_sd.h %{buildroot}/%{_includedir}/
%endif

%if %{WITH_PYTHON}
# Add python3 support
mkdir -p %{buildroot}%{python3_sitelib}/avahi/
cp -r %{buildroot}%{python2_sitelib}/avahi/* %{buildroot}%{python3_sitelib}/avahi/
rm -fv %{buildroot}%{buildroot}%{python3_sitelib}/avahi/*.py{c,o}
sed -i 's!/usr/bin/python2!/usr/bin/python3!' %{buildroot}%{python3_sitelib}/avahi/ServiceTypeDatabase.py

# avoid empty GenericName keys from .desktop files
for i in %{buildroot}%{_datadir}/applications/*.desktop ; do
if [ -n "$(grep '^GenericName=$' $i)" ]; then
  desktop-file-edit --copy-name-to-generic-name $i
fi
done
%endif

rm -fv %{buildroot}%{_sysconfdir}/rc.d/init.d/avahi-daemon
rm -fv %{buildroot}%{_sysconfdir}/rc.d/init.d/avahi-dnsconfd

%find_lang %{name}

install -m0644 -D avahi.sysusers.conf %{buildroot}%{_sysusersdir}/avahi.conf
install -m0644 -D avahi-autoipd.sysusers.conf %{buildroot}%{_sysusersdir}/avahi-autoipd.conf


%check
%if %{with check}
  %make_build check
%endif
%if %{without bootstrap}
  for i in %{buildroot}%{_datadir}/applications/b*.desktop ; do
    desktop-file-validate $i
  done
%endif
%if %{WITH_PYTHON}
  desktop-file-validate %{buildroot}%{_datadir}/applications/avahi-discover.desktop
%endif


%post
%{?ldconfig}
/usr/bin/dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :
if [ "$1" -eq 1 -a -s /etc/localtime ]; then
        /usr/bin/cp -cfp /etc/localtime %{_sysconfdir}/avahi/etc/localtime >/dev/null 2>&1 || :
fi
%systemd_post avahi-daemon.socket avahi-daemon.service

%preun
%systemd_preun avahi-daemon.socket avahi-daemon.service

%postun
%{?ldconfig}
%systemd_postun_with_restart avahi-daemon.socket avahi-daemon.service

%post dnsconfd
%systemd_post avahi-dnsconfd.service

%preun dnsconfd
%systemd_preun avahi-dnsconfd.service

%postun dnsconfd
%systemd_postun_with_restart avahi-dnsconfd.service

%ldconfig_scriptlets glib

%ldconfig_scriptlets compat-howl

%ldconfig_scriptlets compat-libdns_sd

%ldconfig_scriptlets libs

%ldconfig_scriptlets ui

%ldconfig_scriptlets ui-gtk3

%ldconfig_scriptlets gobject

%files -f %{name}.lang
%doc docs/* avahi-daemon/example.service avahi-daemon/sftp-ssh.service avahi-daemon/ssh.service
%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/etc
%ghost %{_sysconfdir}/avahi/etc/localtime
%config(noreplace) %{_sysconfdir}/avahi/hosts
%dir %{_sysconfdir}/avahi/services
%ghost %attr(0755, avahi, avahi) %dir %{_localstatedir}/run/avahi-daemon
%config(noreplace) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %{_datadir}/dbus-1/system.d/avahi-dbus.conf
%{_sbindir}/avahi-daemon
%dir %{_datadir}/avahi
%{_datadir}/avahi/*.dtd
%dir %{_libdir}/avahi
%if %{WITH_PYTHON}
%{_libdir}/avahi/service-types.db
%endif
%{_mandir}/man5/*
%{_mandir}/man8/avahi-daemon.*
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%{_libdir}/libavahi-core.so.*
%{_sysusersdir}/avahi.conf

%files autoipd
%{_sbindir}/avahi-autoipd
%config(noreplace) %{_sysconfdir}/avahi/avahi-autoipd.action
%attr(1770,avahi-autoipd,avahi-autoipd) %dir %{_localstatedir}/lib/avahi-autoipd/
%{_mandir}/man8/avahi-autoipd.*
%{_sysusersdir}/avahi-autoipd.conf

%files dnsconfd
%config(noreplace) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%{_sbindir}/avahi-dnsconfd
%{_mandir}/man8/avahi-dnsconfd.*
%{_unitdir}/avahi-dnsconfd.service

%files tools
%{_bindir}/avahi-browse
%{_bindir}/avahi-browse-domains
%{_bindir}/avahi-publish
%{_bindir}/avahi-publish-address
%{_bindir}/avahi-publish-service
%{_bindir}/avahi-resolve
%{_bindir}/avahi-resolve-address
%{_bindir}/avahi-resolve-host-name
%{_bindir}/avahi-set-host-name

%{_mandir}/man1/avahi-browse.1*
%{_mandir}/man1/avahi-browse-domains.1*
%{_mandir}/man1/avahi-publish.1*
%{_mandir}/man1/avahi-publish-address.1*
%{_mandir}/man1/avahi-publish-service.1*
%{_mandir}/man1/avahi-resolve.1*
%{_mandir}/man1/avahi-resolve-address.1*
%{_mandir}/man1/avahi-resolve-host-name.1*
%{_mandir}/man1/avahi-set-host-name.1*

%if %{without bootstrap}
%files ui-tools
%{_bindir}/bshell
%{_bindir}/bssh
%{_bindir}/bvnc
%{_bindir}/avahi-discover-standalone
%{_mandir}/man1/bshell.1*
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*
%{_datadir}/applications/b*.desktop
%{_datadir}/avahi/interfaces/
%if %{WITH_PYTHON}
# avahi-bookmarks is not really a UI tool, but I won't create a seperate package for it...
%{_bindir}/avahi-bookmarks
%{_mandir}/man1/avahi-discover*
%{_mandir}/man1/avahi-bookmarks*
%{_datadir}/applications/avahi-discover.desktop
%{python2_sitelib}/avahi_discover/
%endif
%endif

%files devel
%{_libdir}/libavahi-common.so
%{_libdir}/libavahi-core.so
%{_libdir}/libavahi-client.so
%{_libdir}/libavahi-libevent.so
%{_includedir}/avahi-client
%{_includedir}/avahi-common
%{_includedir}/avahi-core
%{_includedir}/avahi-libevent
%{_libdir}/pkgconfig/avahi-core.pc
%{_libdir}/pkgconfig/avahi-client.pc
%{_libdir}/pkgconfig/avahi-libevent.pc

%files libs
%doc README
%license LICENSE
%{_libdir}/libavahi-common.so.*
%{_libdir}/libavahi-client.so.*
%{_libdir}/libavahi-libevent.so.*

%files glib
%{_libdir}/libavahi-glib.so.*

%files glib-devel
%{_libdir}/libavahi-glib.so
%{_includedir}/avahi-glib
%{_libdir}/pkgconfig/avahi-glib.pc

%files gobject
%{_libdir}/libavahi-gobject.so.*
#%%{_libdir}/girepository-1.0/Avahi-0.6.typelib
#%%{_libdir}/girepository-1.0/AvahiCore-0.6.typelib

%files gobject-devel
%{_libdir}/libavahi-gobject.so
%{_includedir}/avahi-gobject
%{_libdir}/pkgconfig/avahi-gobject.pc
#%%{_datadir}/gir-1.0/Avahi-0.6.gir
#%%{_datadir}/gir-1.0/AvahiCore-0.6.gir

%if %{WITH_GTK2}
%files ui
%{_libdir}/libavahi-ui.so.*
%endif

%if %{WITH_GTK3}
%files ui-gtk3
%{_libdir}/libavahi-ui-gtk3.so.*
%endif

%if %{WITH_GTK2} || %{WITH_GTK3}
%files ui-devel
%{_includedir}/avahi-ui
%if %{WITH_GTK2}
%{_libdir}/libavahi-ui.so
%{_libdir}/pkgconfig/avahi-ui.pc
%endif
%if %{WITH_GTK3}
%{_libdir}/libavahi-ui-gtk3.so
%{_libdir}/pkgconfig/avahi-ui-gtk3.pc
%endif
%endif

%if %{WITH_QT3}
%ldconfig_scriptlets qt3

%files qt3
%{_libdir}/libavahi-qt3.so.*

%files qt3-devel
%{_libdir}/libavahi-qt3.so
%{_includedir}/avahi-qt3/
%{_libdir}/pkgconfig/avahi-qt3.pc
%endif

%if %{WITH_QT4}
%ldconfig_scriptlets qt4

%files qt4
%{_libdir}/libavahi-qt4.so.*

%files qt4-devel
%{_libdir}/libavahi-qt4.so
%{_includedir}/avahi-qt4/
%{_libdir}/pkgconfig/avahi-qt4.pc
%endif

%if %{WITH_QT5}
%ldconfig_scriptlets qt5

%files qt5
%{_libdir}/libavahi-qt5.so.*

%files qt5-devel
%{_libdir}/libavahi-qt5.so
%{_includedir}/avahi-qt5/
%{_libdir}/pkgconfig/avahi-qt5.pc
%endif

%if %{WITH_MONO}
%files sharp
%{_prefix}/lib/mono/avahi-sharp
%{_prefix}/lib/mono/gac/avahi-sharp
%{_libdir}/pkgconfig/avahi-sharp.pc

%files ui-sharp
%{_prefix}/lib/mono/avahi-ui-sharp
%{_prefix}/lib/mono/gac/avahi-ui-sharp

%files ui-sharp-devel
%{_libdir}/pkgconfig/avahi-ui-sharp.pc
%endif

%if %{WITH_COMPAT_HOWL}
%files compat-howl
%{_libdir}/libhowl.so.*

%files compat-howl-devel
%{_libdir}/libhowl.so
%{_includedir}/avahi-compat-howl
%{_libdir}/pkgconfig/avahi-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc
%endif

%if %{WITH_COMPAT_DNSSD}
%files compat-libdns_sd
%{_libdir}/libdns_sd.so.*

%files compat-libdns_sd-devel
%{_libdir}/libdns_sd.so
%{_includedir}/avahi-compat-libdns_sd
%{_includedir}/dns_sd.h
%{_libdir}/pkgconfig/avahi-compat-libdns_sd.pc
%{_libdir}/pkgconfig/libdns_sd.pc
%endif

%if %{WITH_PYTHON}
%files -n python2-avahi
%{python2_sitelib}/avahi/

%files -n python3-avahi
%{python3_sitelib}/avahi/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9%{?rc:~%{rc}}-8
- Prepare for Oreon 11 (RP1)
