%global source0_hash 77aa9d8f28c532f2e7a5157a7f4ba8df1001f00fa1cb72cb70b388b3d0e16b61
%global debug_package %{nil}
%define _default_patch_fuzz 2
%define debug 0 
%define final 1 
%define redhatify 1
%define arts 1
%define _with_libutempter 1
%define _with_samba --with-samba
%define pim 1
%global _changelog_trimtime %(date +%s -d "1 year ago")
%global __brp_remove_la_files %nil
Name:    kdebase3
Summary:        KDE 3 core files
Version: 3.5.10
Release:        1%{?dist}
License: GPL-2.0-only
Url: http://www.kde.org
Source0:        https://download.kde.org/stable/%{version}/src/kdebase-%{version}.tar.bz2
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
Patch31: kdebase-3.5.10-konsolesu-kdesu.patch
Patch36: kdebase-3.5.9-userdiskmount.patch
Patch37: kdebase-3.5.10-libkrdb_dep.patch
Patch39: kdebase-3.5.10-samba4.patch
Patch40: kdebase-3.5.10-printmanager-desktop-fix.patch
Patch41: kdebase-3.5.10-libtirpc.patch
Patch42: kdebase-3.5.10-uic.patch
Patch100: kdebase-3.5.10-minicli-decimal-comma.patch
Patch150: kdebase-3.5.10-openssl-1.1.patch
Patch151: kdebase3-configure-c99.patch
Patch300: kde3-acinclude.patch
Patch301: kde3-automake-version.patch
Patch302: kde3-automake-add-missing.patch
Patch303: kde3-libtool-aarch64.patch
Patch304: kde3-autoconf-version.patch
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
Requires: psmisc
%ifnarch s390 s390x
Requires: eject
%endif
%if 0%{?_with_samba:1}
%endif
%ifarch %{ix86} x86_64 ia64 ppc ppc64
%define _with_suspend 1
%endif
%ifnarch s390 s390x
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  bdftopcf
BuildRequires:  bzip2-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  imake
BuildRequires:  kdelibs3-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXtst-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  libfontenc-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  mkfontdir
BuildRequires:  mkfontscale
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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

unset QTDIR && . /etc/profile.d/qt.sh
export DO_NOT_COMPILE="kappfinder kdesktop kdesu klipper kdm kmenuedit kpager kpersonalizer ktip nsplugins"
export DO_NOT_COMPILE="$DO_NOT_COMPILE konqueror kscreensaver ksysguard knetattach kwin"
export DO_NOT_COMPILE="$DO_NOT_COMPILE kdialog kicker ksplashml khelpcenter kxkb"
export DO_NOT_COMPILE="$DO_NOT_COMPILE khotkeys kdepasswd kcheckpass drkonqi"
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
%{__cxx} $CXXFLAGS -o mailsettings %{SOURCE7}
%install
%make_install RUN_KAPPFINDER=no
find %{buildroot} -name "man2html*" | xargs rm -rf
rm -rf  %{buildroot}%{_datadir}/config/kdm
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
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins
rm -f %{buildroot}%{_datadir}/fonts/override/fonts.dir
rm -f %{buildroot}%{_datadir}/applnk/.hidden/.directory
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
rm -f %{buildroot}%{_datadir}/applications/kde/cookies.desktop
rm -f %{buildroot}%{_datadir}/applications/kde/desktop.desktop
rm -f %{buildroot}%{_libdir}/kde3/kded_mediamanager.*
rm -f %{buildroot}%{_libdir}/kde3/kded_medianotifier.*
rm -f %{buildroot}%{_libdir}/kde3/kcm_media.*
rm -f %{buildroot}%{_datadir}/services/kded/mediamanager.desktop
rm -f %{buildroot}%{_datadir}/services/kded/medianotifier.desktop
rm -f %{buildroot}%{_datadir}/applications/kde/media.desktop
rm -f %{buildroot}%{_datadir}/config/katerc
pushd %{buildroot}%{_docdir}/HTML/en/
rm -rf kate kcontrol kdebugdialog kdesu kdm kfind khelpcenter kinfocenter \
       kioslave klipper kmenuedit knetattach konqueror konsole ksysguard \
       kwrite kxkb 
popd
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
export QA_RPATHS=0x0001
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?extras}
%files -f %{oreon_filedir}/main.list
%files -n kdebase3-devel -f %{oreon_filedir}/kdebase3-devel.list
%files -n kdebase3-libs -f %{oreon_filedir}/kdebase3-libs.list
%files -n kdebase3-pim-ioslaves -f %{oreon_filedir}/kdebase3-pim-ioslaves.list

%changelog

%autochangelog
%endif
