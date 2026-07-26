%global source0_hash none

%global debug_package %{nil}

%define _default_patch_fuzz 2

%define debug 0 
%define final 1 
%define redhatify 1
%define arts 1

%define _with_libutempter 1
%define _with_samba --with-samba

# make -pim-ioslaves subpkg
%define pim 1

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Name:    kdebase3
Summary: KDE 3 core files
Version: 3.5.10
Release: 85%{?dist}

# programs: GPLv2, libs: LGPLv2
License: GPL-2.0-only
Url: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebase-%{version}.tar.bz2

Source1: konsole.desktop

Source5: kde-np.pamd
Source6: logrotate-kdm
Source7: mailsettings.cc
Source8: env.sh
Source9: cr16-app-package_games_kids.png
Source10: cr32-app-package_games_kids.png
Source11: cr48-app-package_games_kids.png

Source50:   kde-np-legacy.pamd
Source1001: kde.pamd
Source1002: kde-legacy.pamd

Patch0: kdebase-3.5.5-redhat-pam.patch
Patch1: kdebase-3.5.9-redhat-startkde.patch
Patch2: kdebase-3.3.92-vroot.patch
Patch3: kdebase-3.x-shortcuts.patch
Patch4: kdebase-3.2.0-keymap.patch
Patch5: kdebase-3.1-startpage.patch
Patch6: kdebase-3.1.3-konsole-double-esc.patch
Patch7: kdebase-3.3.92-kpersonalizer.patch
Patch8: kdebase-3.2.92-logo.patch 
Patch10: kdebase-3.4.2-kdesktop-konsole.patch
Patch11: kdebase-3.5.1-xdg.patch
Patch13: kdebase-3.5.5-dbus.patch
Patch14: kdebase-3.5.1-kdm-readme.patch
Patch15: kdebase-3.5.1-konsole-fonts.patch
Patch18: kdebase-3.5.2-kconf_update-klipper.patch
Patch20: kdebase-3.5.5-keyinit.patch
Patch21: kdebase-3.5.3-khelpcenter-sort.patch
Patch22: kdebase-3.5.4-htdig.patch
Patch24: kdebase-3.5.4-tango-icon-theme.patch
Patch25: kdebase-3.5.4-konqueror-shortcut.patch
Patch26: kdebase-3.5.5-suspend.patch
Patch27: kdebase-3.5.8-consolekit-kdm.patch
Patch28: kdebase-3.5.6-kdm-alternatebackground.patch
Patch30: kdebase-3.5.7-kio_media_mounthelper.patch
# kdebase: "Root Shell" sessions will not close, http://bugzilla.redhat.com/301841
Patch31: kdebase-3.5.10-konsolesu-kdesu.patch
# modified version of kubuntu_9915_userdiskmount.diff
# fixes NTFS (#378041) and adds PolicyKit support (#428212)
Patch36: kdebase-3.5.9-userdiskmount.patch
# don't link kcm_colors against libkrdb (and don't call runRdb)
Patch37: kdebase-3.5.10-libkrdb_dep.patch
# find the Samba 4 libsmbclient.h using pkg-config (fixes FTBFS)
Patch39: kdebase-3.5.10-samba4.patch
# remove obsolete MimeType from printmgr/printers.desktop (#587568)
# patch by Ilya Chernykh from openSUSE
Patch40: kdebase-3.5.10-printmanager-desktop-fix.patch
# patch to use libtirpc for RPC, from Cygwin Ports
# https://github.com/cygwinports/kdebase3/blob/master/3.5.10-libtirpc.patch
Patch41: kdebase-3.5.10-libtirpc.patch
Patch42: kdebase-3.5.10-uic.patch

# http://aseigo.blogspot.com/2008/10/dear-kde3-kdesktop-users.html
Patch100: kdebase-3.5.10-minicli-decimal-comma.patch

## Trinity backports
# OpenSSL 1.1 support by Slávek Banko (with prerequisite patches by Timothy
# Pearson), backported by Kevin Kofler
# The patch also fixes OpenSSL 1.0 support, by using the KSSLProxy abstraction.
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=30e57327d5921be080bad5394860fce33b7c3f74
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=4040124e875f442f1ef618c669e108a3d2bc9662
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=48c6b8ff3d2cac37dccce46db29499a14fb025b1
# http://git.trinitydesktop.org/cgit/tdebase/commit/?id=d9b4ee04db7e614a59470acc38a6482c15aed032
Patch150: kdebase-3.5.10-openssl-1.1.patch
Patch151: kdebase3-configure-c99.patch

# security fixes

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# fix for autoconf 2.7x
Patch304: kde3-autoconf-version.patch
# fix FTBFS due to gcc14
Patch305: kdebase3-ftbfs-gcc14.patch
Patch306: kdebase3-autoconf-2.72.patch

Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?extras} == 0
Obsoletes: kdebase-extras < 6:%{version}-%{release}
Provides: kdebase-extras = 6:%{version}-%{release}
%endif
%if 0%{?pim}
Requires: kdebase3-pim-ioslaves = %{version}-%{release}
%else
Obsoletes: kdebase3-pim-ioslaves < %{version}-%{release}
Provides: kdebase3-pim-ioslaves = %{version}-%{release}
%endif

#Requires(post): coreutils fileutils
#Requires(postun): coreutils fileutils
# /sbin/fuser
Requires: psmisc

%ifnarch s390 s390x
Requires: eject
%endif

BuildRequires: kdelibs3-devel >= %{version}-16
BuildRequires: libxslt-devel libxml2-devel
%if 0%{?_with_samba:1}
BuildRequires: libsmbclient-devel
%endif
BuildRequires: pam-devel
BuildRequires: gettext
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: sed
BuildRequires: automake libtool
BuildRequires: pkgconfig
BuildRequires: doxygen
%ifarch %{ix86} x86_64 ia64 ppc ppc64
%define _with_suspend 1
## drop runtime dep, https://bugzilla.redhat.com/show_bug.cgi?id=1208312
#Requires: pm-utils
%endif
BuildRequires: bzip2-devel
BuildRequires: freetype-devel
BuildRequires: openldap-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libart_lgpl-devel
## X11 support details (xmkmf, bdftopcf)
BuildRequires: bdftopcf mkfontdir mkfontscale
BuildRequires: imake
BuildRequires: xorg-x11-proto-devel
BuildRequires: libfontenc-devel
BuildRequires: libtirpc-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXfixes-devel
BuildRequires: libXext-devel
BuildRequires: libXtst-devel
BuildRequires: libxkbfile-devel
%ifnarch s390 s390x
BuildRequires: libraw1394-devel
%if 0%{?fedora} > 36
BuildRequires: libusb-compat-0.1-devel
%else
BuildRequires: libusb-devel
%endif
%endif
# Moving dependency to compat package openexr2.
BuildRequires: pkgconfig(OpenEXR) < 3
BuildRequires: gtk2-devel
BuildRequires: make

%description
Core runtime files for KDE 3, for compatibility with KDE 3 applications.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: kdelibs3-devel
%description devel
Header files for developing applications using %{name}.
Install %{name}-devel if you want to develop or compile Konqueror,
Kate plugins or KWin styles.

%if 0%{?extras}
%package extras
Summary: Extra applications from %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description extras
%{summary}, including:
 * kappfinder
 * kpager
 * ktip
 * kpersonalizer
%endif

%package libs
Summary: %{name} runtime libraries
Requires: kdelibs3 >= %{version}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libs
%{summary}.

%if 0%{?pim}
%package pim-ioslaves
Summary: PIM KIOslaves from %{name}
%description pim-ioslaves
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp
%endif

%prep
%setup -q -n kdebase-%{version}
%patch -P0 -p1 -b .redhat-pam
%patch -P1 -p1 -b .redhat-startkde
%patch -P2 -p1 -b .vroot
%patch -P3 -p1 -b .shortcuts
%patch -P4 -p1 -b .keymap
%patch -P5 -p1
%patch -P6 -p1 -b .konsole
%patch -P7 -p1 -b .kper
%patch -P8 -p1 -b .logo
%patch -P10 -p1 -b .kdestop-konsole
%patch -P11 -p1 -b .xdg
%{?_with_hal:%patch -P13 -p1 -b .dbus}
%patch -P14 -p1 -b .kdm-readme
%patch -P15 -p1 -b .konsole-fonts
%patch -P18 -p1 -b .klipper
%patch -P20 -p1 -b .keyinit
%patch -P21 -p1 -b .khelpcenter-sort
%patch -P22 -p1 -b .htdig
%patch -P24 -p1 -b .tango-icon-theme
%patch -P25 -p1 -b .konqueror-shortcut
%{?_with_suspend:%patch -P26 -p1 -b .suspend}
%{?_with_hal:%patch -P27 -p1 -b .consolekit}
%patch -P28 -p1 -b .kdm-alternatebackground
%patch -P30 -p1 -b .bz#265801
%patch -P31 -p1 -b .konsolesu-kdesu
%patch -P36 -p1 -b .userdiskmount
%patch -P37 -p1 -b .libkrdb_dep
%patch -P39 -p1 -b .samba4
%patch -P40 -p1 -b .printmanager-desktop
%patch -P41 -p2 -b .libtirpc
%patch -P42 -p1 -b .uic
%patch -P100 -p1 -b .minicli-decimal-comma

%patch -P150 -p1 -b .openssl-1.1
%patch -P151 -p1 -b .configure-c99

# hacks to omit stuff that doesn't support DO_NOT_COMPILE
# colors is pending on http://bugzilla.redhat.com/443343
sed -i.omit -e 's|^FONTINST_SUBDIR=kfontinst|#FONTINST_SUBDIR=kfontinst|' \
  -e 's/background//' -e 's/clock//' -e 's/display//' -e 's/energy//' \
  -e 's/fonts//' -e 's/icons//' \
  -e 's/kdm//' -e 's/kicker//' -e 's/krdb//' -e 's/kthememanager//' \
  -e 's/locale//' \
  -e 's/screensaver//' -e 's/style//' -e 's/taskbar//' -e 's/xinerama//' \
  kcontrol/Makefile.am

# security fixes

%if %redhatify
   cp %{SOURCE1} konsole
   # set Konqueror version
   perl -pi -e "s,^#define.*KONQUEROR_VERSION.*,#define KONQUEROR_VERSION \"%{version}-%{release} Fedora\"," konqueror/version.h
%endif

# add missing icons for package_games_kids
install -p -m644 %{SOURCE9} %{SOURCE10} %{SOURCE11} pics/crystalsvg/

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .autoconf2.7x
%patch -P305 -p1 -b .ftbfs-gcc14
%patch -P306 -p1 -b .autoconf-2.72

make -f admin/Makefile.common cvs

%build
# set some default enviroments
unset QTDIR && . /etc/profile.d/qt.sh

export DO_NOT_COMPILE="kappfinder kdesktop kdesu klipper kdm kmenuedit kpager kpersonalizer ktip nsplugins"
export DO_NOT_COMPILE="$DO_NOT_COMPILE konqueror kscreensaver ksysguard knetattach kwin"
export DO_NOT_COMPILE="$DO_NOT_COMPILE kdialog kicker ksplashml khelpcenter kxkb"
export DO_NOT_COMPILE="$DO_NOT_COMPILE khotkeys kdepasswd kcheckpass drkonqi"
# Keep these (kcontrol for kcms, konsole for KonsolePart, kioslave for ioslaves
# kate for kscope
# export DO_NOT_COMPILE="$DO_NOT_COMPILE kcontrol konsole kioslave kate"

%configure \
   --disable-new-ldflags \
   --disable-dependency-tracking \
   --with-xdmdir=%{_sysconfdir}/X11/xdm \
   --with-pam=yes \
   --with-kdm-pam=kdm \
   --with-kcp-pam=kcheckpass \
   --with-kss-pam=kscreensaver \
%ifnarch s390 s390x
   --with-libraw1394 \
%endif
   --with-openexr \
   --with-xinerama \
   --with-xscreensaver \
   --without-shadow \
   --disable-shadow \
   --disable-rpath \
   --sysconfdir=%{_sysconfdir} \
   --disable-greet-lib \
%if %{arts} == 0
   --without-arts \
%endif
%if %{final}
%ifnarch s390x
   --enable-final \
%endif
%endif
%if %{debug} == 0
   --disable-debug \
   --disable-warnings \
%else
   --enable-debug \
%endif
   --includedir=%{_includedir}/kde \
  %{?_with_hal} %{!?_with_hal:--without-hal} \
  %{?_with_samba} %{!?_with_samba:--without-samba}

%make_build

# build mail setting tool
%{__cxx} $CXXFLAGS -o mailsettings %{SOURCE7}

%install
%make_install RUN_KAPPFINDER=no

# Nuke man2html - we get it from man
find %{buildroot} -name "man2html*" | xargs rm -rf

# nuke default kdm setup in favor of our own
rm -rf  %{buildroot}%{_datadir}/config/kdm

# Make symlinks relative
pushd %{buildroot}/%{_docdir}/HTML/en
for i in */*/*; do
   if [ -d "$i" -a -L "$i"/common ]; then
      rm -f $i/common
      ln -s ../../../common $i
   fi
done
for i in */*; do
   if [ -d "$i" -a -L "$i"/common ]; then
      rm -f $i/common
      ln -s ../../common $i
   fi
done
for i in *; do
   if [ -d "$i" -a -L "$i"/common ]; then
      rm -f $i/common
      ln -s ../common $i
   fi
done
popd

%if %{redhatify}
   rm -f %{buildroot}%{_datadir}/locale/l10n/*/flag.png
   # mark KDE-Only
   pushd %{buildroot}%{_datadir}/applications/kde
      for f in *.desktop ; do
         if [ "$f" == "konqbrowser.desktop" ] ; then
            cat $f | grep -v Categories >$f.o
            echo "Categories=Qt;KDE;Network;" >>$f.o
            mv $f.o $f
         else
            echo "OnlyShowIn=KDE;" >> $f
         fi
      done
   popd
   for f in $(find %{buildroot}%{_datadir}/applnk -name "*.desktop") ; do
      echo "OnlyShowIn=KDE;" >> $f
   done
%endif

# Own Mozilla plugin dir
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins

# exclude fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/override/fonts.dir

# now in kde-filesystem (see #321771)
rm -f %{buildroot}%{_datadir}/applnk/.hidden/.directory

# remove conflicts with kdebase-workspace
pushd %{buildroot}%{_bindir}
rm -f genkdmconf kaccess kappfinder kapplymousetheme kate kbookmarkmerger \
      kblankscrn.kss kcheckrunning kcminit kcminit_startup kcontroledit kdebugdialog \
      kdeinstallktheme kdepasswd kdialog kdm kdmctl keditbookmarks \
      keditfiletype kfind kfmclient kfontinst kfontview khelpcenter khc_* \
      khotkeys kinfocenter klipper \
      kmenuedit konqueror konsole krandom.kss krandrtray kreadconfig ksmserver \
      ksplashsimple kstart ksysguard ksysguardd ksystraycmd ktip ktrash kwin \
      kwin_killer_helper kwin_rules_dialog kwrite kwriteconfig kxkb \
      nspluginscan nspluginviewer startkde kdeeject kcontrol
popd
rm -f %{buildroot}%{_sysconfdir}/ksysguarddrc
rm -f %{buildroot}%{_libdir}/kconf_update_bin/khotkeys_update
rm -f %{buildroot}%{_libdir}/kconf_update_bin/kwin_update_default_rules
rm -f %{buildroot}%{_libdir}/kconf_update_bin/kwin_update_window_settings
rm -f %{buildroot}%{_datadir}/config.kcfg/kcm_useraccount.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/keditbookmarks.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/klaunch.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/konqueror.kcfg
rm -f %{buildroot}%{_datadir}/config.kcfg/kwin.kcfg
rm -f %{buildroot}%{_datadir}/config/klipperrc
rm -f %{buildroot}%{_datadir}/config/kshorturifilterrc
rm -f %{buildroot}%{_datadir}/xsessions/kde.desktop

# dups of kde4 services
rm -f %{buildroot}%{_datadir}/applications/kde/cookies.desktop
rm -f %{buildroot}%{_datadir}/applications/kde/desktop.desktop

# remove mediamanager stuff #447852 and kdebug:163717
rm -f %{buildroot}%{_libdir}/kde3/kded_mediamanager.*
rm -f %{buildroot}%{_libdir}/kde3/kded_medianotifier.*
rm -f %{buildroot}%{_libdir}/kde3/kcm_media.*
rm -f %{buildroot}%{_datadir}/services/kded/mediamanager.desktop
rm -f %{buildroot}%{_datadir}/services/kded/medianotifier.desktop
rm -f %{buildroot}%{_datadir}/applications/kde/media.desktop

# remove conflicts with kdesdk
rm -f %{buildroot}%{_datadir}/config/katerc

# remove docs
pushd %{buildroot}%{_docdir}/HTML/en/
rm -rf kate kcontrol kdebugdialog kdesu kdm kfind khelpcenter kinfocenter \
       kioslave klipper kmenuedit knetattach konqueror konsole ksysguard \
       kwrite kxkb 
popd
# remove .desktop files for apps we don't ship
pushd %{buildroot}%{_datadir}/applications/kde/
rm -f Help.desktop Home.desktop Kfind.desktop installktheme.desktop \
      kappfinder.desktop kate.desktop kdepasswd.desktop kfmclient.desktop \
      kfmclient_dir.desktop kfmclient_html.desktop kfmclient_war.desktop \
      kinfocenter.desktop klipper.desktop kmenuedit.desktop \
      konqbrowser.desktop konquerorsu.desktop konsole.desktop \
      konsolesu.desktop krandrtray.desktop ksysguard.desktop ktip.desktop \
      kwrite.desktop KControl.desktop

sed -i -e "s,^OnlyShowIn=KDE;,OnlyShowIn=KDE3;," *.desktop
popd

# hicolor
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kappfinder.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kate.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/khelpcenter.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/knetattach.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kfind.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kfm.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/khotkeys.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kmenuedit.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/konqueror.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/konsole.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ksplash.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/ktip.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kwrite.*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*/apps/kxkb.*
rm -rf %{buildroot}%{_datadir}/locale/en_US/
rm -rf %{buildroot}%{_datadir}/locale/l10n/
rm -rf %{buildroot}%{_datadir}/autostart/*
rm -rf %{buildroot}%{_datadir}/desktop-directories/*
rm -rf %{buildroot}%{_datadir}/templates/*
rm -rf %{buildroot}%{_datadir}/templates/.source/*
rm -rf %{buildroot}%{_datadir}/wallpapers/*
rm -rf %{buildroot}%{_libdir}/kconf_update_bin
rm -rf %{buildroot}%{_datadir}/fonts
rm -rf %{buildroot}%{_datadir}/apps/kdm
rm -rf %{buildroot}%{_datadir}/apps/konqueror
rm -rf %{buildroot}%{_datadir}/apps/apps/kbookmark
rm -rf %{buildroot}%{_datadir}/apps/ksmserver
rm -rf %{buildroot}%{_datadir}/applnk
rm -rf %{buildroot}/etc/xdg/menus/

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001

# legacy scriptlets
%if 0%{?fedora} < 25
%post
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :

%posttrans
gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg  2> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :
  gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg  &> /dev/null || :
fi

%if 0%{?extras}
%post extras
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null ||:

%posttrans extras
gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg &> /dev/null ||:

%postun extras
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg &> /dev/null ||:
fi
%endif
%endif

%if 0%{?extras}
%files extras
# kappfinder
%{_bindir}/kappfinder
%{_datadir}/applications/kde/kappfinder.desktop
%{_datadir}/applnk/System/kappfinder.desktop
%{_datadir}/apps/kappfinder/
%{_datadir}/icons/hicolor/*/apps/kappfinder.png

# ktip
%{_bindir}/ktip
%{_datadir}/applications/kde/ktip.desktop
%{_datadir}/applnk/Toys/ktip.desktop
%{_datadir}/apps/kdewizard
%{_datadir}/autostart/ktip.desktop
%{_datadir}/icons/hicolor/*/apps/ktip*

# kpersonalizer
%{_bindir}/kpersonalizer
%{_datadir}/applications/kde/kpersonalizer.desktop
%{_datadir}/applnk/System/kpersonalizer.desktop
%{_datadir}/apps/kpersonalizer/
%{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png

# kpager
%{_bindir}/kpager
%{_datadir}/applications/kde/kpager.desktop
%{_datadir}/applnk/Utilities/kpager.desktop
%{_datadir}/icons/hicolor/*/apps/kpager.png
%endif

%files
%if 0%{?extras}
# kappfinder
%exclude %{_datadir}/applications/kde/kappfinder.desktop
%exclude %{_datadir}/applnk/System/kappfinder.desktop
%exclude %{_datadir}/apps/kappfinder/
%exclude %{_datadir}/icons/hicolor/*/apps/kappfinder.png

# ktip
%exclude %{_datadir}/applications/kde/ktip.desktop
%exclude %{_datadir}/applnk/Toys/ktip.desktop
%exclude %{_datadir}/apps/kdewizard
%exclude %{_datadir}/autostart/ktip.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/ktip*

# kpersonalizer
%exclude %{_datadir}/applications/kde/kpersonalizer.desktop
%exclude %{_datadir}/applnk/System/kpersonalizer.desktop
%exclude %{_datadir}/apps/kpersonalizer/
%exclude %{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png

# kpager
%exclude %{_datadir}/applications/kde/kpager.desktop
%exclude %{_datadir}/applnk/Utilities/kpager.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/kpager.png
%endif

%doc AUTHORS README
%license COPYING
%{_docdir}/HTML/en/*
%if "%{name}" == "kdebase"
%{_sysconfdir}/kde/env/*
%config(noreplace) /etc/logrotate.d/kdm
%config(noreplace) /etc/ksysguarddrc
%config(noreplace) /etc/pam.d/*
%config(noreplace) %{_datadir}/xsessions/*
%{_bindir}/drkonqi
%{_bindir}/genkdmconf
%{_bindir}/kaccess
%{_bindir}/kapplymousetheme
%{_bindir}/kate
%{_bindir}/kblankscrn.kss
%{_bindir}/kbookmarkmerger
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/kcontrol
%{_bindir}/kcontroledit
%{_bindir}/kdebugdialog
%{_bindir}/kdeinstallktheme
%{_bindir}/kdepasswd
%{_bindir}/kdesu
%attr(0755,root,root) %{_bindir}/kdesud
%{_bindir}/kdialog
%{_bindir}/kdm
%{_bindir}/kdmctl
%{_bindir}/keditbookmarks
%{_bindir}/keditfiletype
%{_bindir}/kfind
%{_bindir}/kfmclient
%{_bindir}/khelpcenter
%{_bindir}/khotkeys
%{_bindir}/kinfocenter
%{_bindir}/klipper
%{_bindir}/kmenuedit
%{_bindir}/konqueror
%{?_with_libutempter:%attr(2755,root,utempter) }%{_bindir}/konsole
%{_bindir}/krandom.kss
%{_bindir}/krandrtray
%{_bindir}/krdb
%{_bindir}/kreadconfig
%{_bindir}/ksmserver
%{_bindir}/ksplashsimple
%{_bindir}/kstart
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_bindir}/ksystraycmd
%{_bindir}/ktrash
%{_bindir}/kwin
%{_bindir}/kwin_killer_helper
%{_bindir}/kwin_rules_dialog
%{_bindir}/kwrite
%{_bindir}/kwriteconfig
%{_bindir}/kxkb
%{_bindir}/nspluginscan
%{_bindir}/nspluginviewer
%{_bindir}/startkde
%{_bindir}/kcheckrunning
%{_bindir}/kdesktop
%{_bindir}/kdesktop_lock
%{_bindir}/kdm_config
%{_bindir}/kdm_greet
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/krootimage
%{_bindir}/kwebdesktop
%{_datadir}/autostart/*
%{_datadir}/desktop-directories/*
%{_datadir}/locale/*/entry.desktop
%{_datadir}/locale/l10n
%{_datadir}/templates/*
%{_datadir}/templates/.source/*
%{_datadir}/wallpapers/*
%config(noreplace) /etc/xdg/menus/*
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%{_bindir}/appletproxy
%{_bindir}/extensionproxy
%{_bindir}/kasbar
%{_bindir}/kcheckpass
%{_bindir}/kdeeject
%{_bindir}/khc_docbookdig.pl
%{_bindir}/khc_htdig.pl
%{_bindir}/khc_htsearch.pl
%{_bindir}/khc_indexbuilder
%{_bindir}/khc_mansearch.pl
%{_bindir}/kicker
%{_bindir}/knetattach
%{_bindir}/kompmgr
%{_bindir}/kpm
%{_bindir}/ksplash
%{_bindir}/mailsettings
%{_libdir}/kconf_update_bin
%{_datadir}/applnk/*.desktop
%{_datadir}/applnk/*/*
%{_datadir}/applnk/.hidden/*
%config(noreplace) %{_datadir}/config/*
%if ! %{redhatify}
%{_datadir}/fonts/bitmap-fonts/*
%endif
%dir %{_localstatedir}/lib/kdm
%ghost %{_localstatedir}/lib/kdm/kdmsts
%endif
%{_datadir}/config.kcfg/*
%{_bindir}/kde3
%{_bindir}/kio_media_mounthelper
%{_bindir}/kio_system_documenthelper
%{_bindir}/kdcop
%{_bindir}/kdeprintfax
%{_bindir}/kjobviewer
%{_bindir}/klocaldomainurifilterhelper
%{_bindir}/kprinter
%{_datadir}/applications/*/*
%{_datadir}/apps/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/sounds/*
%{_libdir}/kde3/*
%{_libdir}/libkdeinit_*.*
%if 0%{?pim}
# exclude pim-ioslaves files from main package
%exclude %{_libdir}/kde3/kio_ldap.*
%exclude %{_libdir}/kde3/kio_nntp.*
%exclude %{_libdir}/kde3/kio_pop3.*
%exclude %{_libdir}/kde3/kio_smtp.*
%exclude %{_datadir}/services/ldap*.protocol
%exclude %{_datadir}/services/nntp*.protocol
%exclude %{_datadir}/services/pop3*.protocol
%exclude %{_datadir}/services/smtp*.protocol
%endif

%ldconfig_scriptlets libs

%files libs
%exclude %{_libdir}/libkdeinit_*.*
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%if 0%{?pim}
%files pim-ioslaves
%{_libdir}/kde3/kio_ldap.*
%{_libdir}/kde3/kio_nntp.*
%{_libdir}/kde3/kio_pop3.*
%{_libdir}/kde3/kio_smtp.*
%{_datadir}/services/ldap*.protocol
%{_datadir}/services/nntp*.protocol
%{_datadir}/services/pop3*.protocol
%{_datadir}/services/smtp*.protocol
%endif

%files devel
%{_includedir}/kde/*.h
%dir %{_includedir}/kde/kate
%{_includedir}/kde/kate/*
%if "%{name}" == "kdebase"
%dir %{_includedir}/kde/kwin
%{_includedir}/kde/kwin/*
%dir %{_includedir}/kde/ksgrd
%{_includedir}/kde/ksgrd/*
%dir %{_includedir}/kde/ksplash
%{_includedir}/kde/ksplash/*
%endif
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.*

%changelog
%autochangelog
