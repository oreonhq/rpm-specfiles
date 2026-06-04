%global source0_hash none
%global source1_hash fd80466d8da6f402b992efe1adf99f8cc7dab66b01167dcf788b598a1c465df3

%if 0%{?fedora} > 17 || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global systemd_login1 1
%endif

# if 0%%{?fedora} < 24
%global kdm 1
# endif

%if 0%{?fedora} > 23 && 0%{?oreon} < 11
%global kdm_settings 1
%endif

%if 0%{?fedora} < 25 || (0%{?oreon} >= 11)
%define strigi 1
%endif

Summary: KDE Workspace
Name:    kde-workspace
Epoch:   1
Version: 4.11.22
Release: 47%{?dist}

License: GPL-2.0-only
URL:     https://github.com/KDE/%{name}
Source0:        https://github.com/KDE/kde-workspace/archive/refs/tags/v%{version}.tar.gz#/kde-workspace-%{version}.tar.xz
%if 0%{?kdm_settings}
Source1:        kdm-settings-2.tar.gz
%endif

# add konsole menuitem
# FIXME?  only show menu when/if konsole is installed? then we can drop the hard-dep
Patch2: kde-workspace-4.9.90-plasma_konsole.patch

# make strigi optional
Patch3: kde-workspace-strigi.patch

# RH/Fedora-specific: Force kdm and kdm_greet to be hardened
Patch4: kde-workspace-4.10.4-kdm-harden.patch

# kubuntu kudos! bulletproof-X bits ripped out
# SUSE kudos! plymouth fixed by Laercio de Sousa and Stefan Brüns
Patch19: kde-workspace-4.11.1-kdm_plymouth081.patch
Patch20: kdebase-workspace-4.4.92-xsession_errors_O_APPEND.patch

# add support for automatic multi-seat provided by systemd using existing reserve seats in KDM
Patch27: kde-workspace-4.11.1-kdm-logind-multiseat.patch

# avoid conflict between kcm_colors 4 and plasma-desktop 5
Patch28: kde-workspace-4.11.16-colorschemes-kde4.patch

# use /etc/login.defs to define a 'system' account instead of hard-coding 500
Patch52: kde-workspace-4.8.2-bz#732830-login.patch

# kdm overwrites ~/.Xauthority with wrong SELinux context on logout
# http://bugzilla.redhat.com/567914
# http://bugs.kde.org/242065
Patch53: kde-workspace-4.7.95-kdm_xauth.patch

# kdm (local) ipv6
# https://bugzilla.redhat.com/show_bug.cgi?id=1187957
Patch56: kde-workspace-kdm_local_ipv6.patch

# pam/systemd bogosity: kdm restart/shutdown does not work
# http://bugzilla.redhat.com/796969
Patch57: kde-workspace-4.8.0-bug796969.patch

Patch58: kde-workspace-4.9.11-new_rundir.patch
Patch59: kdm-settings-new_rundir.patch
## upstream patches

## plasma active patches

## Fedora specific patches

# rhel patches

## trunk (Plasma 5) patches

# kdmtheme's functionality is provided here

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= 4.14.4
BuildRequires: kactivities-devel
BuildRequires: libjpeg-devel
BuildRequires: pam-devel

# TODO: Can we strip this even more?
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(libpng)
%if 0%{?strigi}
BuildRequires: pkgconfig(libstreamanalyzer)
%endif
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xres)

# For AutoReq cmake-filesystem
BuildRequires: cmake

%description
The KDE Workspace consists of what is the desktop of the
KDE Desktop Environment.

%package devel
Summary:  Development files for %{name}
Obsoletes: kdebase-workspace-devel < 4.7.97-10
Provides:  kdebase-workspace-devel = %{version}-%{release}
Provides: solid-bluetooth-devel = %{version}-%{release}
#Requires: ksysguard-libs%%{?_isa} = %%{epoch}:%%{version}-%%{release}
Requires: libkworkspace%{?_isa} = %{epoch}:%{version}-%{release}
Requires: kdelibs4-devel
%description devel
%{summary}.

%package -n kcm_colors
Summary: Colors KDE Control Module
Conflicts: kde-workspace < 4.8.0-2
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%{?kde_runtime_requires}
%description -n kcm_colors
The Color Selection module is comprised of several sections:
* The Scheme tab, used to manage schemes
* The Options tab, used to change the options of the current scheme
* The Colors tab, used to change the colors of the current scheme
* The state effects tabs (Inactive, Disabled)

%package -n kde-platform-plugin
Summary: KDE4 Platform plugin
Requires: %{name}-common = %{epoch}:%{version}-%{release}
# if 0%%{?fedora} > 22
## skip Supplements until dnf handling is better/fixed:
## https://bugzilla.redhat.com/show_bug.cgi?id=1325471
%if 0
Supplements: (kde-runtime and plasma-workspace)
%endif
%description -n kde-platform-plugin
%{summary}.

%package -n kdm
Summary: The KDE login manager
Provides: kdebase-kdm = %{version}-%{release}
Provides: service(graphical-login) = kdm
%if 0%{?kdm_settings}
Requires: kdm-settings = %{epoch}:%{version}-%{release}
%else
Requires: kde-settings-kdm
%endif
Requires: kgreeter-plugins = %{epoch}:%{version}-%{release}
Requires: libkworkspace%{?_isa} =  %{epoch}:%{version}-%{release}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description -n kdm
KDM provides the graphical login screen, shown shortly after boot up,
log out, and when user switching.

%if 0%{?kdm_settings}
%package -n kdm-settings
Summary: Configuration files for kdm
Obsoletes: kde-settings-kdm < 1:4.11
Provides:  kde-settings-kdm = %{epoch}:%{version}-%{release}
BuildRequires: systemd
BuildRequires: make
Requires: kdm = %{epoch}:%{version}-%{release}
Requires: desktop-backgrounds-compat
Requires: system-logos
Requires: xorg-x11-xinit
Requires(pre): coreutils
Requires(post): coreutils grep sed
Requires(post): kde4-macros(api) = %{_kde4_macros_api}
%{?systemd_requires}
BuildArch: noarch
%description -n kdm-settings
%{summary}.
%endif

%package -n kdm-themes
Summary: Extra KDM Themes
Obsoletes: kdm < 4.7.3-9
Requires: kdm = %{epoch}:%{version}-%{release}
# http://bugzilla.redhat.com/753409
# http://bugzilla.redhat.com/784389
Requires: kde-wallpapers
# kdm already pulls in -common
#Requires: %%{name}-common = %%{epoch}:%%{version}-%%{release}
BuildArch: noarch
%description -n kdm-themes
A collection of extra kdm themes, including: circles, horos, oxygen, oxygen-air,
as well as stripes wallpaper.

%package -n kgreeter-plugins
Summary: KDE Greeter Plugin Components
# kgreet_* plugins moved
Conflicts: kdm < 4.6.90-4
Conflicts: kde-workspace < 4.7.80-3
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description -n kgreeter-plugins
%{summary} that are needed by KDM and Screensaver unlocking.

%package -n ksysguard-libs
Summary: Runtime libraries for KDE 4 version of ksysguard
# when spilt occurred
Conflicts: kdebase-workspace-libs < 4.7.2-2
Requires: libksysguard-common >= 5
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%{?kdelibs4_requires}
%description -n ksysguard-libs
%{summary}.

%package -n ksystraycmd
Summary:  Allows any application to be kept in the system tray
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description -n ksystraycmd
%{summary}.

%package -n libkworkspace
Summary: Runtime libkworkspace library
# when spilt occurred
Conflicts: kdebase-workspace-libs < 4.7.2-2
Obsoletes: kdebase-workspace-libs-kworkspace < 4.7.2-3
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%{?kdelibs4_requires}
%description -n libkworkspace
%{summary}.

%package common
Summary: KDE Workspace 4 legacy package
BuildArch: noarch
Obsoletes: kdebase-workspace < 4.7.97-10
Obsoletes: kdebase-workspace-akonadi < 4.7.97-10
Obsoletes: kdebase-workspace-googlegadgets < 4.5.80-7
Obsoletes: kdebase-workspace-ksplash-themes < 4.7.97-10
Obsoletes: kdebase-workspace-libs < 4.7.97-10
Obsoletes: kded_randrmonitor < 4.9.98-5
Obsoletes: kde-base-artwork < 1:14.12.3
## Let plasma-desktop be the only pkg that Obsoletes: kde-workspace,
## at least until dnf is fixed to match yum's behavior
#Obsoletes: kde-workspace < 1:4.11.16-2
Obsoletes: kde-workspace-akonadi < 1:4.11.16-2
Obsoletes: kde-workspace-libs < 1:4.11.16-2
Obsoletes: kde-workspace-python-applet < 4.5.80-7
%if ! 0%{?kdm}
Obsoletes: kdm < %{epoch}:%{version}-%{release}
Obsoletes: kdm-themes < %{epoch}:%{version}-%{release}
Obsoletes: kgreeter-plugins < %{epoch}:%{version}-%{release}
%endif
Obsoletes: kdmtheme < 1.3
Obsoletes: ksplash-themes < 1:4.11.16-2
Obsoletes: ksysguard-libs < 1:4.11.22-30
Obsoletes: plasma-scriptengine-googlegadgets < 4.7.1
Obsoletes: plasma-scriptengine-python < 1:4.11.16-2
Obsoletes: plasma-scriptengine-ruby < 1:4.11.16-2
Obsoletes: ktux < 1:14.12.3
## other kde4-only plasmoids
Obsoletes: kde-plasma-daisy < 0.1
Obsoletes: kde-plasma-quickaccess < 0.8.1-20
Obsoletes: kde-plasma-runcommand < 2.4-20
Obsoletes: kde-plasma-smooth-tasks < 0.1
Obsoletes: kde-plasma-translatoid < 1.30-20
%description common
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n kde-workspace-%{version} %{?kdm_settings:-a1}

# Well, I looked at doing this using the context menu plugin system and it
# looked like a lot more work than this simple patch to me. -- Kevin
# FIXME/REBASE -- rex
%patch 2 -p1 -b .plasma-konsole
%patch 3 -p1 -b .strigi
%patch 4 -p1 -b .harden
# no backup file, since the whole dir gets installed
%patch 19 -p1 -b .kdm_plymouth
%patch 20 -p1 -b .xsession_errors_O_APPEND
%patch 27 -p1 -b .kdm_logind
%patch 28 -p1 -b .colorschemes-kde4

# upstreamable patches
%patch 52 -p1 -b .bz#732830-login
%patch 53 -p1 -b .kdm_xauth
%patch 56 -p0 -b .kdm_local_ipv6
%patch 57 -p1 -b .bug796969
%patch 58 -p1 -b .new_rundir
%if 0%{?kdm_settings}
pushd kdm-settings
#this patch can't have backups
%patch 59 -p1
popd
%endif

# upstream patches

# Fedora patches

# rhel patches

# trunk (Plasma 5) patches


# Disable some libs (only keep kworkspace, kdm)
for lib in kephal ksysguard oxygen plasmaclock plasmagenericshell taskmanager; do
    sed -i "/add_subdirectory($lib)/s/^/#/" libs/CMakeLists.txt
done

# make libs/kdm optional
sed -i -e 's/add_subdirectory(kdm)/macro_optional_add_subdirectory(kdm)/' \
  kdm/CMakeLists.txt \
  libs/CMakeLists.txt \
  doc/CMakeLists.txt

# Disable all docs except for KDM and kcontrol
for doc in klipper kfontview kmenuedit ksysguard plasma-desktop systemsettings kinfocenter PolicyKit-kde; do
    sed -i "/add_subdirectory($doc)/s/^/#/" doc/CMakeLists.txt
done

# Disable all kcontrol docs except for colors
for doc in clock desktopthemedetails joystick kcmaccess kcmstyle solid-actions splashscreen powerdevil kwincompositing kwinscreenedges \
           autostart bell cursortheme fonts fontinst keys keyboard kwindecoration desktop mouse paths screensaver windowspecific \
           windowbehaviour kwintabbox kcmsmserver workspaceoptions khotkeys; do
    sed -i "/add_subdirectory($doc)/s/^/#/" doc/kcontrol/CMakeLists.txt
done

# Disable all KCMs except for colors
for kcm in randr keyboard bell input access screensaver dateandtime autostart launch krdb style desktoptheme standard_actions keys \
           workspaceoptions hardware desktoppaths fonts kfontinst; do
    sed -i "/add_subdirectory( $kcm )/s/^/#/" kcontrol/CMakeLists.txt
done


%build
# TODO: Please submit an issue to upstream (rhbz#2380675)
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# workaround bug #1316964
export CFLAGS="%{optflags} -Dinline=__inline__"

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DKDE4_ENABLE_FPIE:BOOL=ON \
  -DKDE4_KDM_PAM_SERVICE=kdm \
  -DKDE4_KCHECKPASS_PAM_SERVICE=kcheckpass \
  -DKDE4_KSCREENSAVER_PAM_SERVICE=kscreensaver \
  -DBUILD_kdm:BOOL=%{?kdm:ON}%{!?kdm:OFF} \
  -DBUILD_systemsettings:BOOL=OFF \
  -DBUILD_kcheckpass:BOOL=OFF \
  -DBUILD_kwin:BOOL=OFF \
  -DBUILD_ksmserver:BOOL=OFF \
  -DBUILD_ksplash:BOOL=OFF \
  -DBUILD_powerdevil:BOOL=OFF \
  -DBUILD_qguiplatformplugin_kde:BOOL=ON \
  -DBUILD_ksysguard:BOOL=OFF \
  -DBUILD_klipper:BOOL=OFF \
  -DBUILD_kmenuedit:BOOL=OFF \
  -DBUILD_krunner:BOOL=OFF \
  -DBUILD_solid-actions-kcm:BOOL=OFF \
  -DBUILD_kstartupconfig:BOOL=OFF \
  -DBUILD_freespacenotifier:BOOL=OFF \
  -DBUILD_kscreensaver:BOOL=OFF \
  -DBUILD_kinfocenter:BOOL=OFF \
  -DBUILD_ktouchpadenabler:BOOL=OFF \
  -DBUILD_kcminit:BOOL=OFF \
  -DBUILD_khotkeys:BOOL=OFF \
  -DBUILD_kwrited:BOOL=OFF \
  -DBUILD_appmenu:BOOL=OFF \
  -DBUILD_cursors:BOOL=OFF \
  -DBUILD_plasma:BOOL=OFF \
  -DBUILD_statusnotifierwatcher:BOOL=OFF \
  -DBUILD_kstyles:BOOL=OFF
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# move devel symlinks
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/devel
pushd %{buildroot}%{_kde4_libdir}
for i in lib*.so
do
  case "$i" in
    libksgrd.so|libksignalplotter.so|liblsofui.so|libprocesscore.so|libprocessui.so)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
    *)
      ;;
  esac
done
popd

## unpackaged files
%if 0%{?kdm}
# remove extraneous files
rm -rfv %{buildroot}%{_kde4_appsdir}/kdm/sessions/
rm -rfv %{buildroot}%{_datadir}/config/kdm

# own %%{_kde4_appsdir}/kdm/faces and set default user image
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/faces
pushd %{buildroot}%{_kde4_appsdir}/kdm/faces
ln -sf ../pics/users/default1.png .default.face.icon
popd

%if 0%{?kdm_settings}
# kdm-settings
pushd kdm-settings/
tar cpf - . | tar --directory %{buildroot} -xvpf -
popd

# config dir kdm symlink
ln -sf ../../../etc/kde/kdm %{buildroot}%{_datadir}/config/kdm

# own these
mkdir -p %{buildroot}%{_localstatedir}/lib/kdm
mkdir -p %{buildroot}%{_rundir}/{kdm,xdmctl}
%endif

%endif

# Keep dreaming...
rm -rfv %{buildroot}/%{_kde4_bindir}/startkde

# Remove ksysguard processlisthelper (provided by libksysguard-common)
rm -rfv %{buildroot}/%{_sysconfdir}/dbus-1
rm -rfv %{buildroot}/%{_kde4_libexecdir}/ksysguardprocesslist_helper
rm -rfv %{buildroot}/%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
rm -rfv %{buildroot}/%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

# colors doc conflicts with plasma-desktop-doc
rm -rfv %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/colors/


%files common
%doc COPYING README

%files devel
%{_kde4_includedir}/*
%{_kde4_appsdir}/cmake/modules/*.cmake
%{_kde4_libdir}/cmake/KDE4Workspace/
%{_kde4_libdir}/libkworkspace.so
# ksysguard-libs
%if 0
%{_kde4_libdir}/kde4/devel/libksgrd.so
%{_kde4_libdir}/kde4/devel/libksignalplotter.so
%{_kde4_libdir}/kde4/devel/liblsofui.so
%{_kde4_libdir}/kde4/devel/libprocesscore.so
%{_kde4_libdir}/kde4/devel/libprocessui.so
%endif

%files -n kde-platform-plugin
%{_kde4_libdir}/kde4/plugins/gui_platform/libkde.so

%files -n kcm_colors
%{_kde4_datadir}/kde4/services/colors.desktop
%{_kde4_libdir}/kde4/kcm_colors.so
%{_kde4_configdir}/colorschemes-kde4.knsrc
%{_kde4_appsdir}/color-schemes/Honeycomb.colors
%{_kde4_appsdir}/color-schemes/Norway.colors
%{_kde4_appsdir}/color-schemes/ObsidianCoast.colors
%{_kde4_appsdir}/color-schemes/Oxygen.colors
%{_kde4_appsdir}/color-schemes/OxygenCold.colors
%{_kde4_appsdir}/color-schemes/Steel.colors
%{_kde4_appsdir}/color-schemes/WontonSoup.colors
%{_kde4_appsdir}/color-schemes/Zion.colors
%{_kde4_appsdir}/color-schemes/ZionReversed.colors

%if 0%{?kdm}
%files -n kdm
%{_kde4_bindir}/genkdmconf
%{_kde4_bindir}/kdm
%{_kde4_bindir}/kdmctl
%{_kde4_libexecdir}/kdm_config
%{_kde4_libexecdir}/kdm_greet
%{_kde4_libexecdir}/krootimage
%{_kde4_docdir}/HTML/en/kdm/
%dir %{_kde4_appsdir}/doc
%{_kde4_appsdir}/doc/kdm/
%dir %{_kde4_appsdir}/kdm/
%{_kde4_appsdir}/kdm/faces/
%{_kde4_appsdir}/kdm/patterns/
%{_kde4_appsdir}/kdm/pics/
%{_kde4_appsdir}/kdm/programs/
%dir %{_kde4_appsdir}/kdm/themes/
# kcm
%{_kde4_appsdir}/kcontrol/
%{_kde4_libdir}/kde4/kcm_kdm.so
%{_kde4_libexecdir}/kcmkdmhelper
%{_kde4_datadir}/config/background.knsrc
%{_kde4_datadir}/config/kdm.knsrc
%{_kde4_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkdm.service
%{_kde4_datadir}/kde4/services/kdm.desktop
%{_kde4_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkdm.policy

%if 0%{?kdm_settings}
%post -n kdm-settings
%{?systemd_post:%systemd_post kdm.service}
(grep '^UserAuthDir=/run/kdm$' %{_sysconfdir}/kde/kdm/kdmrc > /dev/null && \
 sed -i.rpmsave -e 's|^UserAuthDir=/run/kdm$|#UserAuthDir=/tmp|' \
 %{_sysconfdir}/kde/kdm/kdmrc
) ||:

%preun -n kdm-settings
%{?systemd_preun:%systemd_preun kdm.service}

%postun -n kdm-settings
%{?systemd_postun}

%files -n kdm-settings
%config(noreplace) /etc/pam.d/kdm*
# compat symlink
%{_datadir}/config/kdm
%dir %{_sysconfdir}/kde/kdm
%config(noreplace) %{_sysconfdir}/kde/kdm/kdmrc
%dir %{_localstatedir}/lib/kdm
%config(noreplace) %{_localstatedir}/lib/kdm/backgroundrc
%ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/kde/kdm/README*
%config(noreplace) %{_sysconfdir}/kde/kdm/Xaccess
%config(noreplace) %{_sysconfdir}/kde/kdm/Xresources
%config(noreplace) %{_sysconfdir}/kde/kdm/Xsession
%config(noreplace) %{_sysconfdir}/kde/kdm/Xsetup
%config(noreplace) %{_sysconfdir}/kde/kdm/Xwilling
# own logrotate.d/ avoiding hard dep on logrotate
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/kdm
%{_tmpfilesdir}/kdm.conf
%attr(0711,root,root) %dir %{_rundir}/kdm
%attr(0711,root,root) %dir %{_rundir}/xdmctl
%{_unitdir}/kdm.service
# default/generic fedora theme
%{_kde4_appsdir}/kdm/themes/fedora/
%endif

%files -n kdm-themes
%{_kde4_appsdir}/kdm/themes/ariya/
%{_kde4_appsdir}/kdm/themes/circles/
%{_kde4_appsdir}/kdm/themes/elarun/
%{_kde4_appsdir}/kdm/themes/horos/
%{_kde4_appsdir}/kdm/themes/oxygen/
%{_kde4_appsdir}/kdm/themes/oxygen-air/
# not sure why this is included in kdm sources... ? -- rex
%{_kde4_datadir}/wallpapers/stripes.png*

%files -n kgreeter-plugins
%{_kde4_libdir}/kde4/kgreet_classic.so
%{_kde4_libdir}/kde4/kgreet_generic.so
%{_kde4_libdir}/kde4/kgreet_winbind.so
%endif

%if 0
%ldconfig_scriptlets -n ksysguard-libs

%files -n ksysguard-libs
%{_kde4_libdir}/kde4/plugins/designer/ksignalplotterwidgets.so
%{_kde4_libdir}/libksignalplotter.so.4*
%{_kde4_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%{_kde4_libdir}/kde4/plugins/designer/ksysguardlsofwidgets.so
%{_kde4_libdir}/libksgrd.so.4*
%{_kde4_libdir}/liblsofui.so.4*
%{_kde4_libdir}/libprocesscore.so.4*
%{_kde4_libdir}/libprocessui.so.4*
%{_kde4_appsdir}/ksysguard
%endif

%files -n ksystraycmd
%{_kde4_bindir}/ksystraycmd

%ldconfig_scriptlets -n libkworkspace

%files -n libkworkspace
%{_kde4_libdir}/libkworkspace.so.4*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:4.11.22-47
- Import
