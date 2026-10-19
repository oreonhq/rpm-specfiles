%global source0_hash 0ffc9994def10260f98a55cd132deefa8dc4a9835451cc0e982747bd458e2356
%{?!rhel:%global rhel 0}
%{?!fedora:%global fedora 0}
%if 0%{?rhel} == 6 || (0%{?oreon} >= 11)
%global fedora 12
%endif
%if 0%{?rhel} == 7 || (0%{?oreon} >= 11)
%global fedora 19
%endif
%if 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%global fedora 27
%endif
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
%if 0%{?fedora} < 5 || (0%{?oreon} >= 11)
%global force_sound_aplay       1
%endif
%if 0%{?fedora} >= 5 || (0%{?oreon} >= 11)
%global dbus_integration        1
%global gstreamer_integration   1
%global nm_integration          1
%global modular_x               1
%endif
%if 0%{?fedora} >= 6 || (0%{?oreon} >= 11)
%global dbus_glib_splt          1
%global bonjour_support         1
%global meanwhile_integration   1
%endif
%if 0%{?fedora} <= 6 || (0%{?oreon} >= 11)
%global use_gnome_open          1
%endif
%if 0%{?fedora} >= 7 || (0%{?oreon} >= 11)
%global perl_devel_separated    1
%endif
%if 0%{?fedora} >= 8 || (0%{?oreon} >= 11)
%global perl_embed_separated    1
%global api_docs                1
%endif
%if 0%{?fedora} >= 10 || (0%{?oreon} >= 11)
%global nss_md2_disabled        1
%endif
%if 0%{?fedora} >= 11 || (0%{?oreon} >= 11)
%global vv_support              1
%global libidn_support          1
%global use_system_certs        1
%endif
%if 0%{?fedora} >= 12 || (0%{?oreon} >= 11)
%global krb4_removed            1
%endif
%if 0%{?fedora} >= 13 || (0%{?oreon} >= 11)
%global split_evolution         1
%endif
%if 0%{?fedora} >= 16 || (0%{?oreon} >= 11)
%global use_system_libgadu      1
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global use_system_libgadu      0
%endif
%if 0%{?rhel} >= 7 || (0%{?oreon} >= 11)
%global api_docs                0
%endif
%if 0%{?fedora} >= 18 || (0%{?oreon} >= 11)
%global disable_evolution       1
%global split_evolution         0
%endif
%if 0%{?fedora} >= 22 || (0%{?oreon} >= 11)
%global gstreamer_version       1.0
%global farstream_version       0.2
%global gst1                    1
%endif
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
%global nm_libnm_integration    1
%endif
%ifarch %{valgrind_arches}
%global has_valgrind 1
%endif
Name:           pidgin
Version:        2.14.14
Release:        1%{?dist}
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:            http://pidgin.im/
Summary:        A Gtk+ based multiprotocol instant messaging client
Obsoletes:      gaim < 999:1
Provides:       gaim = 999:1
Obsoletes:      pidgin-evolution <= 2.10.6%{?dist}
Source0:        https://downloads.sourceforge.net/pidgin/pidgin-%{version}.tar.bz2
Source1:        purple-fedora-prefs.xml
Patch0:        pidgin-NOT-UPSTREAM-2.5.2-rhel4-sound-migration.patch
Patch1:        pidgin-2.14.4-valgrind.patch
Patch100:        pidgin-rb4404.patch
%global glib_ver %(pkg-config --modversion glib-2.0 2>/dev/null || echo -n "999" | cut -d. -f 1,2)
Requires:       glib2 >= %{glib_ver}
Requires:       libpurple%{?_isa} = %{version}-%{release}
%if ! %{build_only_libs}
%if ! %{disable_evolution}
%endif
%endif
%if ! %{krb4_removed}
%endif
Requires:       libgnome
%if 0%{?fedora} >= 17 || (0%{?oreon} >= 11)
%else
%endif
Requires:       gstreamer%{?gst1}-plugins-good
%if 0%{?fedora} >= 12 || (0%{?oreon} >= 11)
Requires:       gstreamer%{?gst1}-plugins-bad-free
%endif
%if 0%{?has_valgrind}
%endif
%if 0%{?fedora} >= 15 || (0%{?oreon} >= 11)
%global __provides_exclude_from ^%{_libdir}/purple
%define __requires_exclude ^%(cat %{_builddir}/%{?buildsubdir}/plugins.list)|perl\\(Purple\\)
%endif
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  autoconf
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkspell-devel
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libgnt-devel
BuildRequires:  libidn-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  meanwhile-devel
BuildRequires:  ncurses-devel
BuildRequires:  nss-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  startup-notification-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
# /oreon:deps
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
Obsoletes:  gaim < 999:1
Obsoletes:  gaim-meanwhile < %{version}-%{release}
Requires:   glib2 >= %{glib_ver}
Requires:   cyrus-sasl-plain, cyrus-sasl-md5
%if 0%{?fedora} >= 19 || (0%{?oreon} >= 11)
Requires:   cyrus-sasl-scram
%endif
Requires:   ca-certificates
%if 0%{?rhel} == 5 || (0%{?oreon} >= 11)
Obsoletes:  pidgin-docs = 2.5.2
%endif
Requires:   python3-dbus
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
Requires:   dbus-devel >= 0.60
Requires:   dbus-glib-devel >= 0.70
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
echo "FEDORA=%{fedora} RHEL=%{rhel}"
%setup -q
## Patches 0-99: Fedora specific or upstream wont accept
%patch -P0 -p1 -b .aplay
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
    SWITCHES="$SWITCHES --enable-dbus"
%if 0%{?fedora} >= 27 || (0%{?oreon} >= 11)
    SWITCHES="$SWITCHES --with-python=%{__python3}"
%endif
    SWITCHES="$SWITCHES --enable-nm"
    SWITCHES="$SWITCHES --with-gstreamer=%{gstreamer_version}"
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
    SWITCHES="$SWITCHES --with-system-ssl-certs=/etc/pki/tls/certs"
autoreconf --force --install
%configure --enable-gnutls=no --enable-nss=yes --enable-cyrus-sasl \
           --enable-tcl --enable-tk \
           --disable-schemas-install $SWITCHES
make %{?_smp_mflags} V=1 LIBTOOL=/usr/bin/libtool
cd libpurple/plugins/
make one_time_password.so V=1 LIBTOOL=/usr/bin/libtool
cd -
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
find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/relnot.so
rm -f $RPM_BUILD_ROOT%{_bindir}/nullclient
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/purple/
install -m 644 prefs.xml $RPM_BUILD_ROOT%{_sysconfdir}/purple/prefs.xml
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/liboscar.so
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/libjabber.so
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/libymsg.so
chmod -R u+w $RPM_BUILD_ROOT/*
%find_lang pidgin
%if ! %{build_only_libs}
ln -sf pidgin $RPM_BUILD_ROOT%{_bindir}/gaim
%endif
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/purple.schemas
find %{buildroot}/%{_libdir}/purple-2 -name \*.so\* -printf '%f|' | sed -e 's/|$//' > plugins.list
%oreon_autofiles libpurple usr/*/lib*.so.*
%oreon_autofiles libpurple-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libpurple-perl usr/*/lib*.so.*
%oreon_autofiles libpurple-tcl usr/*/lib*.so.*
%oreon_autofiles finch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles finch-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if ! %{build_only_libs}
%files -f %{oreon_filedir}/main.list
%files -n pidgin-devel -f %{oreon_filedir}/pidgin-devel.list
%files -n pidgin-perl -f %{oreon_filedir}/pidgin-perl.list
%files -n libpurple -f %{oreon_filedir}/libpurple.list
%files -n libpurple-devel -f %{oreon_filedir}/libpurple-devel.list
%files -n libpurple-perl -f %{oreon_filedir}/libpurple-perl.list
%files -n libpurple-tcl -f %{oreon_filedir}/libpurple-tcl.list
%files -n finch -f %{oreon_filedir}/finch.list
%files -n finch-devel -f %{oreon_filedir}/finch-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14.14-4
- Import
%endif
