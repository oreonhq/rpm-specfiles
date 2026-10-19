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
%{?!WITH_PYTHON:        %global WITH_PYTHON 0}
%ifnarch %{mono_arches}
%define WITH_MONO 0
%endif
%global _hardened_build 1
%global _changelog_trimtime %(date +%s -d "1 year ago")
%define rc rc2
Name:             avahi
Version:          0.9%{?rc:~%{rc}}
Release:        1%{?dist}
Summary:        Local network service discovery
License:          LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause-Views AND MIT
URL:              http://avahi.org
Requires:         dbus
Requires:         expat
Requires:         libdaemon >= 0.11
Requires(post):   dbus
Requires(pre):    coreutils
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
%if %{WITH_GTK3}
%endif
%if %{without bootstrap}
%endif
%global python2_dbus dbus-python
%global python2_libxml2 libxml2-python
%if 0%{?rc:1}
%global source0_hash f64efed6a972cf92cb2dfb35abf6aa9173d62b843b15850c2f40af76a4238f8a
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{WITH_MONO}.9-%{rc}.tar.gz#/%{name}-%{WITH_MONO}.9-%{rc}.tar.gz
%else
%global source0_hash none
%endif
Patch1: avahi-0.9-CVE-2024-52615.patch
Patch2: avahi-0.9-address-data-size.patch
Patch100: avahi-0.6.30-mono-libdir.patch
Patch102: avahi-0.8-no_undefined.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcap-devel
BuildRequires:  libdaemon-devel
BuildRequires:  libtool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  qt3-devel
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  xmltoman
# /oreon:deps
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
Requires:         gdbm
Requires:         pygtk2
Requires:         pygtk2-libglade
Requires:         python2-avahi = %{version}-%{release}
Requires:         %{python2_dbus}
Requires:         python2-gobject-base
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
%if %{WITH_GTK3}
Requires:         %{name}-ui-gtk3%{?_isa} = %{version}-%{release}
%endif
%description ui-devel
The avahi-ui-devel package contains the header files and libraries
necessary for developing programs using avahi-ui.
%endif

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

%package libs
Summary:          Libraries for avahi run-time use
%description libs
The avahi-libs package contains the libraries needed
to run programs that use avahi.

%package devel
Summary:          Libraries and header files for avahi development
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
        --disable-gtk \
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
        --enable-qt3 \
        --enable-qt4 \
%if ! %{WITH_QT5}
        --disable-qt5 \
%endif
%if ! %{WITH_MONO}
        --disable-mono \
%endif
;
%make_build -k V=1 || make V=1
%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/ssh.service
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service
mkdir -p %{buildroot}%{_localstatedir}/run/avahi-daemon
mkdir -p %{buildroot}%{_localstatedir}/lib/avahi-autoipd
rm -rfv %{buildroot}%{_datadir}/%{name}-%{version}
mkdir -p %{buildroot}%{_sysconfdir}/avahi/etc
touch %{buildroot}%{_sysconfdir}/avahi/etc/localtime
%if %{WITH_COMPAT_HOWL}
ln -s avahi-compat-howl.pc  %{buildroot}/%{_libdir}/pkgconfig/howl.pc
%endif
%if %{WITH_COMPAT_DNSSD}
ln -s avahi-compat-libdns_sd.pc %{buildroot}/%{_libdir}/pkgconfig/libdns_sd.pc
ln -s avahi-compat-libdns_sd/dns_sd.h %{buildroot}/%{_includedir}/
%endif
mkdir -p %{buildroot}%{python3_sitelib}/avahi/
cp -r %{buildroot}%{python2_sitelib}/avahi/* %{buildroot}%{python3_sitelib}/avahi/
rm -fv %{buildroot}%{buildroot}%{python3_sitelib}/avahi/*.py{c,o}
sed -i 's!/usr/bin/python2!/usr/bin/python3!' %{buildroot}%{python3_sitelib}/avahi/ServiceTypeDatabase.py
for i in %{buildroot}%{_datadir}/applications/*.desktop ; do
if [ -n "$(grep '^GenericName=$' $i)" ]; then
  desktop-file-edit --copy-name-to-generic-name $i
fi
done
rm -fv %{buildroot}%{_sysconfdir}/rc.d/init.d/avahi-daemon
rm -fv %{buildroot}%{_sysconfdir}/rc.d/init.d/avahi-dnsconfd
%find_lang %{name}
install -m0644 -D avahi.sysusers.conf %{buildroot}%{_sysusersdir}/avahi.conf
install -m0644 -D avahi-autoipd.sysusers.conf %{buildroot}%{_sysusersdir}/avahi-autoipd.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
  %make_build check
%endif
%if %{without bootstrap}
  for i in %{buildroot}%{_datadir}/applications/b*.desktop ; do
    desktop-file-validate $i
  done
%endif
  desktop-file-validate %{buildroot}%{_datadir}/applications/avahi-discover.desktop
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
