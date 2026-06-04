%global source0_hash 0ffc9994def10260f98a55cd132deefa8dc4a9835451cc0e982747bd458e2356

# OVERRIDE RHEL VERSION HERE, RHEL BUILDSYSTEM DOESN'T HAVE DIST TAG
#%%global rhel 4

# Define Variables that must exist
%{?!rhel:%global rhel 0}
%{?!fedora:%global fedora 0}

# Map RHEL to Fedora version
%if 0%{?rhel} == 6 || (0%{?oreon} >= 11)
%global fedora 12
%endif
%if 0%{?rhel} == 7 || (0%{?oreon} >= 11)
%global fedora 19
%endif
%if 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%global fedora 27
%endif

# Define variables to use in conditionals
%global force_sound_aplay       0
%global dbus_integration        0
%global gstreamer_integration   0
%global nm_integration          0
%global nm_libnm_integration    0
%global modular_x               0
%global dbus_glib_splt          0
%global bonjour_support         0
%global meanwhile_integration   0
%global use_gnome_open          0
%global perl_devel_separated    0
%global perl_embed_separated    0
%global api_docs                0
%global krb4_removed            0
%global nss_md2_disabled        0
%global vv_support              0
%global libidn_support          0
%global disable_evolution       0
%global split_evolution         0
%global use_system_certs        0
%global use_system_libgadu      0
%global build_only_libs         0
%global gstreamer_version       0.10
%global farstream_version       0.1

# RHEL4: Use ALSA aplay to output sounds because it lacks gstreamer
%if 0%{?fedora} < 5 || (0%{?oreon} >= 11)
%global force_sound_aplay       1
%endif
# RHEL4+ and FC5+: dbus, gstreamer, NetworkManager, modular X
%if 0%{?fedora} >= 5 || (0%{?oreon} >= 11)
%global dbus_integration        1
%global gstreamer_integration   1
%global nm_integration          1
%global modular_x               1
%endif
# RHEL4+ and FC6+: dbus-glib split, bonjour, meanwhile
%if 0%{?fedora} >= 6 || (0%{?oreon} >= 11)
%global dbus_glib_splt          1
%global bonjour_support         1
%global meanwhile_integration   1
%endif
# RHEL4 and RHEL5: Use gnome-open instead of xdg-open (RHEL4 and RHEL5)
%if 0%{?fedora} <= 6 || (0%{?oreon} >= 11)
%global use_gnome_open          1
%endif
# F7+: Perl devel separated out
%if 0%{?fedora} >= 7 || (0%{?oreon} >= 11)
%global perl_devel_separated    1
%endif
# F8+: Perl embed separated out, generate pidgin API documentation
%if 0%{?fedora} >= 8 || (0%{?oreon} >= 11)
%global perl_embed_separated    1
%global api_docs                1
%endif
# F10+: New NSS (3.12.3) disables weaker MD2 algorithm
%if 0%{?fedora} >= 10 || (0%{?oreon} >= 11)
%global nss_md2_disabled        1
%endif
# F11+: libidn for punycode domain support, voice and video support,
# use system SSL certificates
%if 0%{?fedora} >= 11 || (0%{?oreon} >= 11)
%global vv_support              1
%global libidn_support          1
%global use_system_certs        1
%endif
# F12+: krb4 removed
%if 0%{?fedora} >= 12 || (0%{?oreon} >= 11)
%global krb4_removed            1
%endif
# F13+ Split Evolution plugin to separate package (#581144)
%if 0%{?fedora} >= 13 || (0%{?oreon} >= 11)
%global split_evolution         1
%endif
# F16+ Use system libgadu (#713888)
%if 0%{?fedora} >= 16 || (0%{?oreon} >= 11)
%global use_system_libgadu      1
%endif
# RHEL does not have libgadu
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global use_system_libgadu      0
%endif
%if 0%{?rhel} >= 7 || (0%{?oreon} >= 11)
%global api_docs                0
%endif
# F18+ Disable evolution integration (temporarily?)
# due to evolution-data-server 3.6 API changes
%if 0%{?fedora} >= 18 || (0%{?oreon} >= 11)
%global disable_evolution       1
%global split_evolution         0
%endif
# F2+ Build against GStreamer 1.x
%if 0%{?fedora} >= 22 || (0%{?oreon} >= 11)
%global gstreamer_version       1.0
%global farstream_version       0.2
%global gst1                    1
%endif
# F29 doesn't support nm-glib anymore.
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
%global nm_libnm_integration    1
%endif
# valgrind available only on selected arches
%ifarch %{valgrind_arches}
%global has_valgrind 1
%endif

Name:           pidgin
Version:        2.14.14
Release:        4%{?dist}
# Automatically converted from old format: BSD and GPLv2+ and GPLv2 and LGPLv2+ and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
# GPLv2+ - libpurple, finch, pidgin, most prpls
# GPLv2 - novell prpls
# MIT - Zephyr prpl
URL:            http://pidgin.im/
Summary:        A Gtk+ based multiprotocol instant messaging client

Obsoletes:      gaim < 999:1
Provides:       gaim = 999:1

%if %{split_evolution}
Obsoletes:      pidgin <= 2.7.1-1%{?dist}
%else
%if %{disable_evolution}
Obsoletes:      pidgin-evolution <= 2.10.6%{?dist}
%endif
%endif

Source0:        https://downloads.sourceforge.net/pidgin/pidgin-%{version}.tar.bz2

## Fedora pidgin defaults
# Only needs regenerating if Pidgin breaks backwards compatibility with prefs.xml
# 1) uninstall any non-default pidgin or libpurple plugins
# 2) run pidgin as new user 3) edit preferences 4) close 5) copy .purple/prefs.xml
# OR 1) edit manually
# - enable ExtPlacement plugin
# - enable History plugin
# - enable Message Notification plugin
#   Insert count of new messages into window title
#   Set window manager "URGENT" hint
# - disable buddy icon in buddy list
# - enable Logging (in HTML)
# - Browser "GNOME Default"
# - Smiley Theme "Default"
Source1:        purple-fedora-prefs.xml

## Patches 0-99: Fedora specific or upstream wont accept
Patch0:         pidgin-NOT-UPSTREAM-2.5.2-rhel4-sound-migration.patch
Patch1:         pidgin-2.14.4-valgrind.patch

# Taken from https://reviews.imfreedom.org/r/4404/ to fix a crash on fedora >= 44:
# https://issues.imfreedom.org/issue/PIDGIN-18152/Pidgin-Keeps-Crashing-and-I-dont-know-why
# https://bugzilla.redhat.com/show_bug.cgi?id=2441401
Patch100:       pidgin-rb4404.patch

## Patches 100+: To be Included in Future Upstream

# Require Binary Compatible glib
# returns bogus value if glib2-devel is not installed in order for parsing to succeed
# bogus value wont make it into a real package
%global glib_ver %(pkg-config --modversion glib-2.0 2>/dev/null || echo -n "999" | cut -d. -f 1,2)
BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires:  glib2-devel
Requires:       glib2 >= %{glib_ver}
# Require exact libpurple
Requires:       libpurple%{?_isa} = %{version}-%{release}

# Basic Library Requirements
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  cyrus-sasl-devel
%if %{nss_md2_disabled}
BuildRequires:  nss-devel >= 3.12.3
%else
BuildRequires:  nss-devel
%endif

%if ! %{build_only_libs}
BuildRequires:  startup-notification-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel
# gtkspell integration (FC1+)
BuildRequires:  gtkspell-devel
# Evolution integration (FC3+, < F18)
%if ! %{disable_evolution}
BuildRequires:  evolution-data-server-devel
%endif
%endif

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  tcl-devel < 1:9.0
BuildRequires:  tk-devel < 1:9.0
BuildRequires:  libxml2-devel
BuildRequires:  libgnt-devel

%if ! %{krb4_removed}
# krb5 needed for Zephyr (FC1+)
BuildRequires:  krb5-devel
%endif
# DBus integration (FC5+)
%if %{dbus_integration}
BuildRequires:  dbus-devel >= 0.60
BuildRequires:  python3
BuildRequires:  python3-devel
%endif
# GStreamer integration (FC5+)
%if %{gstreamer_integration}
BuildRequires:  pkgconfig(gstreamer-%{gstreamer_version})
%endif
# NetworkManager integration (FC5+)
%if %{nm_integration}
%if %{nm_libnm_integration}
BuildRequires:  NetworkManager-libnm-devel >= 1.0.0
%else
BuildRequires:  NetworkManager-glib-devel
%endif
%endif
# Modular X (FC5+)
%if %{modular_x}
BuildRequires:  libSM-devel
BuildRequires:  libXScrnSaver-devel
%endif
# Preferred Applications (xdg for FC6+)
%if %{use_gnome_open}
Requires:       libgnome
%else
Requires:       xdg-utils
%endif
# DBus GLIB Split (FC6+)
%if %{dbus_glib_splt}
BuildRequires:  dbus-glib-devel >= 0.70
%endif
%if %{bonjour_support}
BuildRequires:  pkgconfig(avahi-client) pkgconfig(avahi-glib)
%endif
# Meanwhile integration (F6+)
%if %{meanwhile_integration}
BuildRequires:  meanwhile-devel
%endif
# Perl devel separated out (F7+)
%if %{perl_devel_separated}
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%endif
# Perl embed separated out (F9+)
%if %{perl_embed_separated}
BuildRequires:  perl(ExtUtils::Embed)
%endif
# Voice and video support (F11+)
%if %{vv_support}
%if 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
BuildRequires:  pkgconfig(farstream-%{farstream_version})
%else
BuildRequires:  farsight2-devel
%endif
Requires:       gstreamer%{?gst1}-plugins-good
%if 0%{?fedora} >= 12 || (0%{?oreon} >= 11)
Requires:       gstreamer%{?gst1}-plugins-bad-free
%endif
%endif
# libidn punycode domain support (F11+)
%if %{libidn_support}
BuildRequires:  libidn-devel
%endif
%if %{use_system_libgadu}
BuildRequires:  libgadu-devel
%endif

%if %{api_docs}
BuildRequires:  doxygen
%endif

# Use distribution's valgrind.h
%if 0%{?has_valgrind}
BuildRequires:  valgrind-devel
%endif

# Need rpm 4.9+ to be able to do this filtering in arch packages with binaries
%if 0%{?fedora} >= 15 || (0%{?oreon} >= 11)
# Filter out plugins from provides
%global __provides_exclude_from ^%{_libdir}/purple
# Use define to delay evaluation
%define __requires_exclude ^%(cat %{_builddir}/%{?buildsubdir}/plugins.list)|perl\\(Purple\\)
%endif

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, Simple and Zephyr.
These protocols are implemented using a modular, easy to use design.
To use a protocol, just add an account using the account editor.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, Yahoo! Inc., or ICQ Inc.

%if %{split_evolution}
%package evolution
Summary:    Pidgin Evolution integration plugin
Requires:   %{name} = %{version}-%{release}
Obsoletes:  pidgin <= 2.7.1-1%{?dist}

%description evolution
This package contains the Evolution integration plugin for Pidgin.

%endif


%package devel
Summary:    Development headers and libraries for pidgin
Requires:   %{name} = %{version}-%{release}
Requires:   libpurple-devel = %{version}-%{release}
Requires:   pkgconfig
Requires:   gtk2-devel
Obsoletes:  gaim-devel < %{version}-%{release}

Provides:   gaim-devel = %{version}-%{release}


%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%package perl
Summary:    Perl scripting support for Pidgin
Requires:   libpurple = %{version}-%{release}
Requires:   libpurple-perl = %{version}-%{release}

%description perl
Perl plugin loader for Pidgin. This package will allow you to write or
use Pidgin plugins written in the Perl programming language.


%package -n libpurple
Summary:    libpurple library for IM clients like Pidgin and Finch
# Ensure elimination of gaim.i386 on x86_64
Obsoletes:  gaim < 999:1
%if %{meanwhile_integration}
Obsoletes:  gaim-meanwhile < %{version}-%{release}
%endif
Requires:   glib2 >= %{glib_ver}
# Bug #212817 Jabber needs cyrus-sasl plugins for authentication
Requires:   cyrus-sasl-plain, cyrus-sasl-md5
# Bug #979052 - Can't connect to xmpp server since upgrade from f18 to f19
%if 0%{?fedora} >= 19 || (0%{?oreon} >= 11)
Requires:   cyrus-sasl-scram
%endif
# Use system SSL certificates (F11+)
%if %{use_system_certs}
Requires:   ca-certificates
%endif
# Workaround for accidental shipping of pidgin-docs
%if 0%{?rhel} == 5 || (0%{?oreon} >= 11)
Obsoletes:  pidgin-docs = 2.5.2
%endif
%if %{dbus_integration}
Requires:   python3-dbus
%endif

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, Simple and Zephyr.


%package -n libpurple-devel
Summary:    Development headers, documentation, and libraries for libpurple
Requires:   libpurple = %{version}-%{release}
Requires:   pkgconfig
%if %{dbus_integration}
Requires:   dbus-devel >= 0.60
%endif
%if %{dbus_glib_splt}
Requires:   dbus-glib-devel >= 0.70
%endif

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%package -n libpurple-perl
Summary:    Perl scripting support for libpurple
Requires:   libpurple = %{version}-%{release}

%description -n libpurple-perl
Perl plugin loader for libpurple. This package will allow you to write or
use libpurple plugins written in the Perl programming language.


%package -n libpurple-tcl
Summary:    Tcl scripting support for libpurple
Requires:   libpurple = %{version}-%{release}

%description -n libpurple-tcl
Tcl plugin loader for libpurple. This package will allow you to write or
use libpurple plugins written in the Tcl programming language.


%package -n finch
Summary:    A text-based user interface for Pidgin
Requires:   glib2 >= %{glib_ver}
Requires:   libpurple = %{version}-%{release}

%description -n finch
A text-based user interface for using libpurple.  This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.


%package -n finch-devel
Summary:    Headers etc. for finch stuffs
Requires:   finch = %{version}-%{release}
Requires:   libpurple-devel = %{version}-%{release}
Requires:   pkgconfig
Requires:   ncurses-devel

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.

%if %{api_docs}
%package -n pidgin-docs
Summary:    API docs for pidgin and libpurple
Requires:   pidgin = %{version}-%{release}
Provides:   libpurple-docs = %{version}-%{release}

%description -n pidgin-docs
Doxygen generated API documentation.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }echo "FEDORA=%{fedora} RHEL=%{rhel}"
%setup -q
## Patches 0-99: Fedora specific or upstream wont accept
%if %{force_sound_aplay}
%patch -P0 -p1 -b .aplay
%endif
%patch -P1 -p1 -b .valgrind

## Patches 100+: To be Included in Future Upstream
%patch -P100 -p1 -b .rb4404


# Our preferences
cp %{SOURCE1} prefs.xml

# RHEL5 and earlier did not have xdg-open, so use gnome-open instead
if [ "%{use_gnome_open}" == "1" ]; then
    sed -i "s/value='xdg-open'/value='gnome-open'/" prefs.xml
fi

# Bug #528796: Get rid of #!/usr/bin/env python
# Upstream refuses to use ./configure --python-path= in these scripts.
for file in finch/plugins/pietray.py libpurple/purple-remote libpurple/plugins/dbus-buddyicons-example.py \
            libpurple/plugins/startup.py libpurple/purple-url-handler libpurple/purple-notifications-example; do
    sed -i 's/env python3*/python3/' $file
done

# Bug #1141477
%if 0%{?has_valgrind}
rm -f libpurple/valgrind.h
sed -ie 's/include "valgrind.h"/include <valgrind\/valgrind.h>/' libpurple/plugin.c
%endif

%build
SWITCHES="--with-extraversion=%{release}"
%if ! %{krb4_removed}
    SWITCHES="$SWITCHES --with-krb4"
%endif
    SWITCHES="$SWITCHES --enable-perl"
%if ! %{disable_evolution}
    SWITCHES="$SWITCHES --enable-gevolution"
%else
    SWITCHES="$SWITCHES --disable-gevolution"
%endif
%if %{dbus_integration}
    SWITCHES="$SWITCHES --enable-dbus"
%if 0%{?fedora} >= 27 || (0%{?oreon} >= 11)
    SWITCHES="$SWITCHES --with-python=%{__python3}"
%endif
%else
    SWITCHES="$SWITCHES --disable-dbus"
%endif
%if %{nm_integration}
    SWITCHES="$SWITCHES --enable-nm"
%else
    SWITCHES="$SWITCHES --disable-nm"
%endif
%if %{gstreamer_integration}
    SWITCHES="$SWITCHES --with-gstreamer=%{gstreamer_version}"
%else
    SWITCHES="$SWITCHES --without-gstreamer"
%endif
%if ! %{bonjour_support}
    SWITCHES="$SWITCHES --disable-avahi"
%endif
%if ! %{meanwhile_integration}
    SWITCHES="$SWITCHES --disable-meanwhile"
%endif
%if ! %{libidn_support}
    SWITCHES="$SWITCHES --disable-idn"
%endif
%if ! %{vv_support}
    SWITCHES="$SWITCHES --disable-vv"
%endif
%if %{use_system_certs}
    SWITCHES="$SWITCHES --with-system-ssl-certs=/etc/pki/tls/certs"
%endif
%if %{build_only_libs}
    SWITCHES="$SWITCHES --disable-consoleui --disable-gtkui"
%endif

# remove after irc-sasl patch has been merged upstream
autoreconf --force --install

# gnutls is buggy so use mozilla-nss on all distributions
%configure --enable-gnutls=no --enable-nss=yes --enable-cyrus-sasl \
           --enable-tcl --enable-tk \
           --disable-schemas-install $SWITCHES

make %{?_smp_mflags} V=1 LIBTOOL=/usr/bin/libtool

# one_time_password plugin, included upstream but not built by default
cd libpurple/plugins/
make one_time_password.so V=1 LIBTOOL=/usr/bin/libtool
cd -

%if %{api_docs}
make docs
find doc/html -empty -delete
%endif

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install LIBTOOL=/usr/bin/libtool

install -m 0755 libpurple/plugins/one_time_password.so $RPM_BUILD_ROOT%{_libdir}/purple-2/

%if ! %{build_only_libs}
desktop-file-install --vendor pidgin --delete-original              \
                     --add-category X-Red-Hat-Base                  \
                     --dir $RPM_BUILD_ROOT%{_datadir}/applications  \
                     $RPM_BUILD_ROOT%{_datadir}/applications/pidgin.desktop
%endif

# remove libtool libraries and static libraries
find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -exec rm -f {} ';'
# remove the perllocal.pod file and other unrequired perl bits
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
# remove relnot.so plugin since it is unusable for our package
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/relnot.so
# remove dummy nullclient
rm -f $RPM_BUILD_ROOT%{_bindir}/nullclient
# install Fedora pidgin default prefs.xml
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/purple/
install -m 644 prefs.xml $RPM_BUILD_ROOT%{_sysconfdir}/purple/prefs.xml

# remove non-plugin unrequired library symlinks
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/liboscar.so
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/libjabber.so
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/libymsg.so

# make sure that we can write to all the files we've installed
# so that they are properly stripped
chmod -R u+w $RPM_BUILD_ROOT/*

%find_lang pidgin

%if ! %{build_only_libs}
# symlink /usr/bin/gaim to new pidgin name
ln -sf pidgin $RPM_BUILD_ROOT%{_bindir}/gaim
%endif

%if %{api_docs}
rm -rf html
rm -f doc/html/installdox
mv doc/html/ html/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/
ln -sf ../../doc/pidgin-docs/html/ \
    $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/pidgin
%endif

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/purple.schemas

# Create list of plugins for __requires_exclude
find %{buildroot}/%{_libdir}/purple-2 -name \*.so\* -printf '%f|' | sed -e 's/|$//' > plugins.list

%if ! %{build_only_libs}
%files
%doc NEWS COPYING AUTHORS README ChangeLog doc/PERL-HOWTO.dox
%{_bindir}/pidgin
%{_bindir}/gaim
%{_libdir}/pidgin/
%exclude %{_libdir}/pidgin/perl
%if %{split_evolution}
%exclude %{_libdir}/pidgin/gevolution.so
%endif
%{_mandir}/man1/pidgin.*
%{_datadir}/applications/pidgin.desktop
%{_datadir}/pixmaps/pidgin/
%{_datadir}/icons/hicolor/*/apps/pidgin.*
%{_datadir}/metainfo/pidgin.appdata.xml

%if %{split_evolution}
%files evolution
%{_libdir}/pidgin/gevolution.so
%endif

%files perl
%{_mandir}/man3/Pidgin*
%{_libdir}/pidgin/perl/

%files devel
%{_includedir}/pidgin/
%{_libdir}/pkgconfig/pidgin.pc
%endif

%files -f pidgin.lang -n libpurple
%doc COPYING
%{_libdir}/purple-2/
%exclude %{_libdir}/purple-2/perl
%{_libdir}/libpurple.so.*
%{_datadir}/sounds/purple/
%dir %{_sysconfdir}/purple
%config(noreplace) %{_sysconfdir}/purple/prefs.xml
%if %{dbus_integration}
%{_bindir}/purple-client-example
%{_bindir}/purple-remote
%{_bindir}/purple-send
%{_bindir}/purple-send-async
%{_bindir}/purple-url-handler
%{_libdir}/libpurple-client.so.*
#%%{_datadir}/dbus-1/services/pidgin.service
%doc libpurple/purple-notifications-example
%endif
%exclude %{_libdir}/purple-2/tcl.so
%exclude %{_libdir}/purple-2/perl.so
%exclude %{_libdir}/purple-2/perl/

%files -n libpurple-devel
%{_datadir}/aclocal/purple.m4
%{_libdir}/libpurple.so
%{_includedir}/libpurple/
%{_libdir}/pkgconfig/purple.pc
%if %{dbus_integration}
%{_libdir}/libpurple-client.so
%endif

%files -n libpurple-perl
%{_mandir}/man3/Purple*
%{_libdir}/purple-2/perl.so
%{_libdir}/purple-2/perl/

%files -n libpurple-tcl
%{_libdir}/purple-2/tcl.so

%if ! %{build_only_libs}
%files -n finch
%{_bindir}/finch
%{_libdir}/finch/
%{_mandir}/man1/finch.*

%files -n finch-devel
%{_includedir}/finch/
%{_libdir}/pkgconfig/finch.pc
%endif

%if %{api_docs}
%files -n pidgin-docs
%doc html
%{_datadir}/gtk-doc/html/*
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14.14-4
- Import
