%if 0%{?fedora} || 0%{?epel}
%global flags 1
%global webkit 0
%endif

# newer libsmbclient incompatible?
# https://bugzilla.redhat.com/show_bug.cgi?id=1604473
%if 0%{?fedora} < 28
%global smb 1
%endif

%if 0%{?fedora} > 21
%global plasma5 1
%endif

%if 0%{?plasma5} && 0%{?fedora} < 24
%global kuiserver 1
%endif

%if 0%{?fedora} < 26
%global drkonqi 1
%endif

%if 0%{?fedora} < 25
%global strigi 1
%endif

%if 0%{?fedora} < 28
# kf5-kwallet supports the same interfaces now
%global kwallet 1
%endif

Name:    kde-runtime
Summary: KDE Runtime
Version: 17.08.3
Release: 36%{?dist}

# http://techbase.kde.org/Policies/Licensing_Policy
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:     https://kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kde-runtime-%{version}.tar.xz

# add shortcuts for search provider
Patch1: kdebase-runtime-4.1.x-searchproviders-shortcuts.patch

# support kdesud -Wl,-z,relro,-z,now linker flags
Patch2: kde-runtime-kdesud_relro.patch

# add OnlyShowIn=KDE  to Desktop/Home.desktop (like trash.desktop)
Patch6: kdebase-runtime-4.3.3-home_onlyshowin_kde.patch

# correct path for htsearch
Patch7: kdebase-runtime-4.5.3-htsearch.patch

# Launch compiz via compiz-manager so we get window decorations and
# other such decadent luxuries (AdamW 2011/01)
Patch8: kdebase-runtime-4.5.95-compiz.patch

# add overrides in default manpath
Patch9: kdebase-runtime-4.3.4-man-overrides.patch

# https://bugs.kde.org/show_bug.cgi?id=310486
# revert the main part of:
# http://commits.kde.org/kde-runtime/deee161a42efda74965ca4aab7d79fb7fb375352
# (Upstream doesn't like this workaround.)
Patch10: kde-runtime-4.9.98-kde#310486.patch

# disable making files read only when moving them into trash
# (Upstream wouldn't accept this)
Patch11: kde-runtime-4.10.4-trash-readonly.patch

## upstreamable patches
# make installdbgsymbols.sh use pkexec instead of su 
# increase some timeouts in an effort to see (some) errors before close
Patch50: kde-runtime-4.9.0-installdbgsymbols.patch
# dnf-based version of patch50
Patch53:  kde-runtime-16.04.1-installdgbsymbols-dnf.patch

# use packagekit to install a possibly-missing gdb
Patch51: kde-runtime-4.11.2-install_gdb.patch

# Fix FTBFS
# workaround missing dependency on glib2 in NetworkManager.pc
Patch52: kde-runtime-15.08.0-fix-build.patch

# patch to use libtirpc for RPC, from Cygwin Ports
# should be upstreamable, considering that glibc's builtin RPC is obsolete
# backport of:
# https://github.com/cygwinports/kf5-kio-extras/blob/master/16.08.3-nfs-libtirpc.patch
# (because:
# https://github.com/cygwinports/kde-runtime/blob/master/15.04.3-libtirpc.patch
# is incomplete)
Patch54: kde-runtime-17.08.3-nfs-libtirpc.patch

# make some components optional (kwalletd)
Patch55: kde-runtime-optional_components.patch

## upstream patches

# rhel patches
Patch300: kde-runtime-4.9.2-webkit.patch

Obsoletes: kdebase-runtime < 4.7.97-10
Provides:  kdebase-runtime = %{version}-%{release}
Obsoletes: kdebase4-runtime < %{version}-%{release}
Provides:  kdebase4-runtime = %{version}-%{release}

Obsoletes: nepomukcontroller < 1:0.2

# knotify4 provides dbus service org.freedesktop.Notifications too 
Provides: desktop-notification-daemon

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
# http://bugzilla.redhat.com/794958
Requires: dbus
# kdeeject
# (eject provided by util-linux that has no ExcludeArch, so not sure if that's still needed here or not )
%ifnarch s390 s390x
Requires: eject
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if 0%{?drkonqi} && ! 0%{?plasma5}
Requires: %{name}-drkonqi = %{version}-%{release}
%endif
%if 0%{?kuiserver}
Requires: %{name}-kuiserver = %{version}-%{release}
%endif
%if ! 0%{?plasma5}
# needed by windowsexethumbnail
Requires: icoutils
%endif
%if 0%{?flags}
Requires: %{name}-flags = %{version}-%{release}
%endif

# ensure default/fallback icon theme present
# beware of bootstrapping, there be dragons
Requires: oxygen-icon-theme

BuildRequires: bzip2-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: gpgme-devel
BuildRequires: kdelibs4-devel >= 4.14.4
%if 0%{?webkit}
BuildRequires: kdelibs4-webkit-devel
%endif
BuildRequires: kactivities-devel
%if 0%{?kwallet}
BuildRequires: libgcrypt-devel >= 1.5.0
%else
Recommends: kf5-kwallet
%endif
BuildRequires: libjpeg-devel
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(exiv2)
# Move to openexr2 compat package in f35+
BuildRequires: pkgconfig(OpenEXR) < 3
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(polkit-qt-1) 
BuildRequires: pkgconfig(libattica)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libpulse)
%if 0%{?strigi}
BuildRequires: pkgconfig(libstreamanalyzer) pkgconfig(libstreams)
%endif
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(glib-2.0)
%if 0%{?fedora} > 21
BuildRequires: pkgconfig(libnm)
%else
BuildRequires: pkgconfig(libnm-glib) pkgconfig(libnm-util)
%endif
# BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(soprano) >= 2.6.50
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(xscrnsaver)
%if 0%{?fedora}
BuildRequires: openslp-devel
%endif
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires: libssh-devel >= 0.6
%endif
BuildRequires: zlib-devel

# some items moved -workspace -> -runtime
Conflicts: kdebase-workspace < 4.5.80
# plasmapkg moved -workspace -> -runtime
Conflicts: kde-workspace < 4.9.60

%if ! 0%{?smb}
# may need to bump this is newer builds ever done for older releases -- rex
Obsoletes: kio-smb < 17.08.3-9
%endif

%description
Core runtime for KDE 4.

%package devel
Summary:  Developer files for %{name}
Obsoletes: kdebase-runtime-devel < 4.7.97-10
Provides:  kdebase-runtime-devel = %{version}-%{release} 
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%if 0%{?drkonqi}
%package drkonqi
Summary: DrKonqi crash handler for KDE4
BuildRequires: kdepimlibs-devel
Requires: %{name} = %{version}-%{release}
%if 0%{?fedora} > 23
Requires: dnf-command(debuginfo-install)
%endif
Requires: kdialog
# drkonqi patch50 uses pkexec
Requires: polkit
%description drkonqi
%{summary}.
%endif

%package kuiserver
Summary: KDE Progress Info UI server
Provides: kuiserver = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
# split out at 15.08.2-1
%description kuiserver
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Obsoletes: kdebase-runtime-libs < 4.7.97-10
Provides:  kdebase-runtime-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%{?kdelibs4_requires}
%description libs
%{summary}.

%package flags
Summary: Geopolitical flags
Obsoletes: kdebase-runtime-flags < 4.7.97-10
Provides:  kdebase-runtime-flags = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description flags
%{summary}.

%if 0%{?smb}
%package kio-smb
Summary: Samba KIO slave
# upgrade path
Obsoletes: kde-runtime < 4.9.2-5
BuildRequires: pkgconfig(smbclient)
BuildRequires: make
Requires: %{name} = %{version}-%{release}
%description kio-smb
%{summary}.
%endif

%package -n kdesu
Summary: Runs a program with elevated privileges
# upgrade path, when kdesu was introduced
Obsoletes: kde-runtime < 14.12.3-2
# needed for non-conflicting libexec bits
Requires: %{name} = %{version}-%{release}
%description -n kdesu
%{summary}.

%package -n khelpcenter
Summary: KDE Help Center
# upgrade path
Obsoletes: kde-runtime < 4.13.3-3
Requires: %{name} = %{version}-%{release}
%description -n khelpcenter
%{summary}.

%package docs
Summary: User documentation and manuals
Epoch: 1
Obsoletes: %{name} < 4.13.3-3
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description docs
%{summary}.


%prep
%setup -q -n kde-runtime-%{version}

## upstream patches

%patch -P1 -p1 -b .searchproviders-shortcuts
%patch -P6 -p1 -b .home_onlyshowin_kde
%patch -P7 -p1 -b .htsearch
%patch -P8 -p1 -b .config
%patch -P9 -p1 -b .man-overrides
%if 0%{?fedora} < 19 && 0%{?rhel} < 7
%patch -P10 -p1 -b .kde310486
%endif
%patch -P11 -p1 -b .trash-readonly
%if 0%{?fedora} > 22
%patch -P53 -p1 -b .installdgbsymbols-dnf
%else
%patch -P50 -p1 -b .installdgbsymbols
%endif
%patch -P51 -p1 -b .install_gdb
%patch -P52 -p1 -b .fixbuild
%patch -P54 -p1 -b .libtirpc
%patch -P55 -p1 -b .optional_components

%if ! 0%{?webkit}
%patch -P300 -p1 -b .webkit
%global no_webkit -DKDERUNTIME_NO_WEBKIT:BOOL=ON -DPLASMA_NO_KDEWEBKIT:BOOL=ON
%endif


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DKDE4_ENABLE_FPIE:BOOL=ON \
  %{?no_webkit} \
%if 0%{?plasma5}
  -DBUILD_khelpcenter:BOOL=OFF \
  %{?!drkonqi:-DBUILD_drkonqi:BOOL=OFF} \
  %{?!kuiserver:-DBUILD_kuiserver:BOOL=OFF} \
  %{?!kwallet:-DBUILD_kwalletd:BOOL=OFF}
%endif

popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# fix documentation multilib conflict in index.cache
for f in kioslave/nepomuksearch kcontrol/spellchecking kcontrol/performance \
   kcontrol/kcmnotify kcontrol/kcmcss kcontrol/ebrowsing; do
   bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache.bz2
   sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
done

# kdesu symlink
ln -s %{_kde4_libexecdir}/kdesu %{buildroot}%{_kde4_bindir}/kdesu

# omit hicolor index.theme, use one from hicolor-icon-theme
rm -f %{buildroot}%{_kde4_iconsdir}/hicolor/index.theme

# remove country flags because some people/countries forbid some other
# people/countries' flags :-(
%{!?flags:rm -f %{buildroot}%{_kde4_datadir}/locale/l10n/*/flag.png}

%if 0%{?drkonqi}
# installdbgsymbols script
install -p -D -m755 drkonqi/doc/examples/installdbgsymbols_fedora.sh \
  %{buildroot}%{_kde4_libexecdir}/installdbgsymbols.sh
%endif

# rpaths
# use chrpath hammer for now, find better patching solutions later -- Rex
chrpath --list   %{buildroot}%{_libdir}/kde4/plugins/phonon_platform/kde.so ||:
chrpath --delete %{buildroot}%{_libdir}/kde4/plugins/phonon_platform/kde.so

## unpackaged files
# FIXME: -devel type files, omit for now
rm -vf  %{buildroot}%{_kde4_libdir}/lib{kwalletbackend,molletnetwork}.so
%if 0%{?rhel}
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/searchproviders/fedora.desktop
%endif

%if 0%{?plasma5}
rm -fv  %{buildroot}%{_kde4_bindir}/{kdesu,khelpcenter}
rm -fv  %{buildroot}%{_kde4_libexecdir}/khc_*
rm -fv  %{buildroot}%{_kde4_libdir}/libkdeinit4_{khelpcenter}.so
rm -frv %{buildroot}%{_kde4_docdir}/HTML/en/{kcontrol,kdesu,khelpcenter,knetattach,fundamentals,onlinehelp}
rm -frv %{buildroot}%{_kde4_appsdir}/khelpcenter/
rm -fv  %{buildroot}%{_kde4_datadir}/services/{khelpcenter}.desktop
rm -fv  %{buildroot}%{_kde4_datadir}/config.kcfg/khelpcenter.kcfg
rm -fv  %{buildroot}%{_mandir}/man1/kdesu.1*
# now provided by kde-cli-tools >= 5.23.90
# https://phabricator.kde.org/T14763
# https://invent.kde.org/plasma/kde-cli-tools/-/merge_requests/23
rm -fv  %{buildroot}%{_bindir}/{kde-open,keditfiletype,kioclient,kmimetypefinder,kstart,ksvgtopng}
%else
# install this service for KDE 3 applications too
mkdir %{buildroot}%{_datadir}/services
ln -s %{_kde4_datadir}/kde4/services/khelpcenter.desktop \
      %{buildroot}%{_datadir}/services/khelpcenter.desktop
%endif


%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


%files
%license COPYING COPYING.LIB
%if !0%{?plasma5}
# new conflicts with kde-cli-tools
%{_kde4_bindir}/kde-open
%{_kde4_bindir}/keditfiletype
%{_kde4_bindir}/kioclient
%{_kde4_bindir}/kmimetypefinder
%{_kde4_bindir}/kstart
%{_kde4_bindir}/ksvgtopng
%endif
%{_kde4_bindir}/kcmshell4
%{_kde4_bindir}/kde-cp
%{_kde4_bindir}/kde-mv
%{_kde4_bindir}/kde4
%{_kde4_bindir}/kde4-menu
%{_kde4_bindir}/kdebugdialog
%{_kde4_bindir}/kfile4
%{_kde4_bindir}/kglobalaccel
%{_kde4_bindir}/khotnewstuff-upload
%{_kde4_bindir}/khotnewstuff4
%{_kde4_bindir}/kiconfinder
%{_kde4_bindir}/knotify4
%{_kde4_bindir}/kquitapp
%{_kde4_bindir}/kreadconfig
%{_kde4_bindir}/ktraderclient
%{_kde4_bindir}/ktrash
%if 0%{?kwallet}
%{_kde4_bindir}/kwalletd
%{_kde4_libdir}/libkdeinit4_kwalletd.so
%{_kde4_appsdir}/kwalletd/
%endif
%{_kde4_bindir}/kwriteconfig
%{_kde4_bindir}/plasma-remote-helper
%{_kde4_bindir}/plasmapkg
%{_mandir}/man1/plasmapkg.1*
%{_kde4_bindir}/solid-hardware
%{_kde4_appsdir}/desktoptheme/
%{_kde4_appsdir}/hardwarenotifications/
%{_kde4_appsdir}/kcm_componentchooser/
%{_kde4_appsdir}/kcmlocale/
%{_kde4_appsdir}/kcm_phonon/
%{_kde4_appsdir}/kconf_update/*
%{_kde4_appsdir}/kde/
%{_kde4_appsdir}/kglobalaccel/
%{_kde4_appsdir}/kio_bookmarks/
%{_kde4_appsdir}/kio_desktop/
%{_kde4_appsdir}/kio_docfilter/
%{_kde4_appsdir}/kio_finger/
%{_kde4_appsdir}/kio_info/
%{_kde4_appsdir}/konqsidebartng/
%{_kde4_appsdir}/ksmserver/
%{_kde4_appsdir}/libphonon/
%{_kde4_appsdir}/phonon/
%dir %{_kde4_appsdir}/remoteview/
%{_kde4_appsdir}/remoteview/network.desktop
%{_kde4_configdir}/*.knsrc
%{_kde4_datadir}/config.kcfg/jpegcreatorsettings.kcfg
%{_datadir}/dbus-1/services/org.kde.knotify.service
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmremotewidgets.service
%{_kde4_datadir}/kde4/services/*.desktop
%{_kde4_datadir}/kde4/services/qimageioplugins/webp.desktop
%{_kde4_datadir}/kde4/services/*.protocol
%{_kde4_datadir}/kde4/services/kded/
%{_kde4_datadir}/kde4/services/searchproviders/
%{_kde4_datadir}/kde4/servicetypes/*
%{_kde4_datadir}/mime/packages/network.xml
%{_kde4_datadir}/mime/packages/webp.xml
%{_kde4_datadir}/sounds/*
%{_kde4_iconsdir}/default.kde4
%{_kde4_libdir}/kconf_update_bin/*
%{_kde4_libdir}/libkdeinit4_kcmshell4.so
%{_kde4_libdir}/libkdeinit4_kglobalaccel.so
%{_kde4_libdir}/kde4/platformimports/
%{_kde4_libdir}/kde4/kcm_*.so
%{_kde4_libdir}/kde4/kded_*.so
%{_kde4_libexecdir}/kcmremotewidgetshelper
%{_kde4_libexecdir}/kdeeject
%{_kde4_libexecdir}/kdesu
%attr(2755,root,nobody) %{_kde4_libexecdir}/kdesud
%{_kde4_libexecdir}/kdontchangethehostname
%{_kde4_libexecdir}/kioexec
%{_kde4_libexecdir}/knetattach
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_sysconfdir}/xdg/menus/kde-information.menu
%{_kde4_datadir}/applications/kde4/knetattach.desktop
%{_kde4_configdir}/kshorturifilterrc
%{_kde4_datadir}/desktop-directories/*.directory
%exclude %{_kde4_datadir}/desktop-directories/kde-information.directory
%{_kde4_datadir}/emoticons/kde4/
%{_kde4_datadir}/locale/l10n/
%{_kde4_datadir}/locale/currency/
%{?flags:%exclude %{_kde4_datadir}/locale/l10n/*/flag.png}
%{_polkit_qt_policydir}/*.policy
%{_sysconfdir}/dbus-1/system.d/*

%if 0%{?smb}
#files kio-smb
%dir %{_kde4_appsdir}/konqueror/dirtree/
%dir %{_kde4_appsdir}/konqueror/dirtree/remote/
%{_kde4_appsdir}/konqueror/dirtree/remote/smb-network.desktop
%{_kde4_appsdir}/remoteview/smb-network.desktop
%{_kde4_datadir}/kde4/services/smb.protocol
# dup'd in -libs glob
#{_kde4_libdir}/kde4/kio_smb.so
%endif

%files devel
%{_kde4_includedir}/*
%{_kde4_appsdir}/cmake/modules/*.cmake
%{_datadir}/dbus-1/interfaces/*.xml

%if 0%{?drkonqi}
%if 0%{?fedora} > 16 || 0%{?rhel} > 6
%post drkonqi
# make DrKonqi work by default by taming SELinux enough (suggested by dwalsh)
# if KDE_DEBUG is set, DrKonqi is disabled, so do nothing
# if it is unset (or empty), check if deny_ptrace is already disabled
# if not, disable it
if [ -z "$KDE_DEBUG" ] ; then
  if [ "`getsebool deny_ptrace 2>/dev/null`" == 'deny_ptrace --> on' ] ; then
    setsebool -P deny_ptrace off &> /dev/null || :
  fi
fi
%endif

%files drkonqi
%{_kde4_libexecdir}/drkonqi
%{_kde4_libexecdir}/installdbgsymbols.sh
%{_kde4_appsdir}/drkonqi/
%endif

%ldconfig_scriptlets libs

%files libs
# unversioned plugin:
%{_kde4_libdir}/attica_kde.so
%{_kde4_libdir}/libknotifyplugin.so
%if 0%{?kwallet}
%{_kde4_libdir}/libkwalletbackend.so.*
%endif
%{_kde4_libdir}/libmolletnetwork.so.*
%{_kde4_libdir}/kde4/*.so
%{_kde4_libdir}/kde4/imports/
# FIXME: Is this a good idea? Won't multilib apps need KCMs, too?
%exclude %{_kde4_libdir}/kde4/kcm_*.so
%exclude %{_kde4_libdir}/kde4/kded_*.so
%{_kde4_libdir}/kde4/plugins/phonon_platform/
%{_kde4_libdir}/kde4/plugins/imageformats/kimg_webp.so

%if 0%{?flags}
%files flags
%{_kde4_datadir}/locale/l10n/*/flag.png
%endif

%files docs
%{_kde4_docdir}/HTML/en/kdebugdialog/
%{_kde4_docdir}/HTML/en/kioslave/

%if 0%{?kuiserver}
%files kuiserver
%{_kde4_bindir}/kuiserver
%{_kde4_libdir}/libkdeinit4_kuiserver.so
%{_datadir}/dbus-1/services/org.kde.kuiserver.service
%{_kde4_datadir}/kde4/services/kuiserver.desktop
%endif

%if ! 0%{?plasma5}
%files -n khelpcenter
%{_kde4_bindir}/khelpcenter
%{_kde4_libexecdir}/khc_*
%{_kde4_libdir}/libkdeinit4_khelpcenter.so
%{_kde4_docdir}/HTML/en/khelpcenter/
%{_kde4_docdir}/HTML/en/fundamentals/
%{_kde4_docdir}/HTML/en/onlinehelp/
%{_kde4_appsdir}/khelpcenter/
%{_kde4_datadir}/kde4/services/khelpcenter.desktop
%{_kde4_datadir}/services/khelpcenter.desktop
%{_kde4_datadir}/config.kcfg/khelpcenter.kcfg
%{_kde4_datadir}/applications/kde4/Help.desktop
%{_kde4_datadir}/desktop-directories/kde-information.directory

%files -n kdesu
%{_kde4_bindir}/kdesu
%{_kde4_docdir}/HTML/en/kdesu/
%{_mandir}/man1/kdesu.1*
## include non-conflicting libexec bits here too ? -- rex
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 17.08.3-36
- Prepare for Oreon 11 (RP1)
