%global source0_hash ecca3aaf19ec82f86736f0f802a5a295f932a0d57db0c9558a24192c063be329

# TODO, maybe some day:
# - livebuffer patch, http://www.vdr-portal.de/board/thread.php?threadid=37309
# - channelfilter patch, http://www.u32.de/vdr.html#patches
# - pause patch (causes OSD placement issues at least with unrebuilt text2skin)
#   http://www.tolleri.net/vdr/vdr/vdr-1.6.0-2-pause-0.0.1.patch

# - The dvbhddevice plugin is no longer part of the VDR source archive.
#  You can get the latest version of this plugin from the author's repository at
#  https://bitbucket.org/powARman/dvbhddevice.
# - The dvbsddevice and rcu plugins are no longer part of the VDR source archive.
#  You can get the latest versions of these plugins from ftp://ftp.tvdr.de/vdr/Plugins.

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global _hardened_build 1
%bcond_without    docs

%global varbase   %{_var}/lib/vdr
%global videodir  %{varbase}/video
%global vardir    %{varbase}/data
%global plugindir %{_libdir}/vdr
%global configdir %{_sysconfdir}/vdr
%global cachedir  %{_var}/cache/vdr
%global rundir    /run/vdr
%global vdr_user  vdr
%global vdr_group video
# From APIVERSION in config.h
%global apiver    12

Name:           vdr
Version:        2.8.1
Release:        1%{?dist}
Summary:        Video Disk Recorder

License:        GPL-2.0-or-later
URL:            http://www.tvdr.de/
# Get vdr source from http://git.tvdr.de/?p=vdr.git;a=snapshot;h=refs/tags/2.8.1;sf=tbz2
# wget --content-disposition "http://git.tvdr.de/?p=vdr.git;a=snapshot;h=refs/tags/2.8.1;sf=tbz2"
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.sudoers
Source5:        %{name}-reccmds.conf
Source6:        %{name}-commands.conf
Source7:        %{name}-runvdr.sh
Source8:        %{name}-dvbsddevice.conf
Source9:        %{name}-config.sh
Source10:       %{name}-README.package
Source11:       %{name}-skincurses.conf
Source12:       %{name}-dvbhddevice.conf
Source13:       %{name}-timercmds.conf
Source14:       %{name}-shutdown.sh
Source15:       %{name}-moveto.sh
Source16:       %{name}-CHANGES.package.old
Source17:       %{name}.macros
Source18:       http://cdn.debian.net/debian/pool/main/v/vdr/vdr_2.2.0-5.debian.tar.bz2
Source19:       %{name}-check-setup.sh
Source20:       %{name}-rcu.conf
Source21:       %{name}-set-wakeup.sh
Source30:       https://bitbucket.org/powARman/dvbhddevice/get/3473a7b939d7.zip
Source31:       ftp://ftp.tvdr.de/vdr/Plugins/vdr-dvbsddevice-2.2.0.tgz
Source32:       ftp://ftp.tvdr.de/vdr/Plugins/vdr-rcu-2.2.0.tgz

Patch0:         define_AUDIO_GET_PTS.patch
Patch1:         http://zap.tartarus.org/~ds/debian/dists/stable/main/source/vdr_1.4.5-2.ds.diff.gz
# Extracted from http://copperhead.htpc-forum.de/downloads/extensionpatch/extpngvdr1.7.21v1.diff.gz
Patch3:         %{name}-1.7.21-plugin-missing.patch
Patch4:         %{name}-2.4.0-paths.patch
# http://vdrportal.de/board/thread.php?postid=343665#post343665
Patch5:         12_osdbase-maxitems.patch
Patch6:         %{name}-2.7.4-fedora-pkgconfig.patch
# https://www.vdr-portal.de/file-download/40760/
Patch11:	%{name}-%{version}-MainMenuHooks-v1_0_5.diff
# https://www.vdr-portal.de/index.php?attachment/44831-vdr-2-4-6-clearobsoletechannels-diff
Patch99:        %{name}-2.4.6-ClearObsoleteChannels2.diff

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig
BuildRequires:  perl(File::Spec)
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gettext
# systemd >= 186 for scriptlet macros
BuildRequires:  systemd >= 186
BuildRequires:  systemd-devel
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
# udev >= 136-1 for the audio, cdrom, dialout, and video groups
Requires:       udev >= 136-1
# sudo for the shutdown script, >= 1.7.2p2-3 for sudoers.d functionality
Requires:       sudo >= 1.7.2p2-3
# util-linux >= 2.15 for "rtcwake -m no" timer driven wakeups
Requires:       util-linux >= 2.15
Requires:       vdrsymbol-fonts
# systemd >= 189 for RestartPreventExitStatus=
Requires(post,preun,postun): systemd >= 189
Provides:       vdr(abi)%{?_isa} = %{apiver}
Obsoletes:      vdr-subtitles <= 0.5.0
Obsoletes:      vdr-sky < 1.7.11

%description
VDR implements a complete digital set-top-box and video recorder.
It can work with signals received from satellites (DVB-S) as well as
cable (DVB-C) and terrestrial (DVB-T) signals.  At least one DVB card
is required to run VDR.

%package        devel
Summary:        Development files for VDR
Requires:       gettext-runtime
Provides:       vdr-devel(api) = %{apiver}

%description    devel
%{summary}.

%package        docs
Summary:        Developer documentation for VDR
BuildArch:      noarch

%description    docs
%{summary}.

%package        dvbhddevice
Summary:        VDR output device plugin for TechnoTrend S2-6400 DVB cards
Requires:       vdr(abi)%{?_isa} = %{apiver}

%description    dvbhddevice
The dvbhddevice plugin implements a VDR output device for the "Full
Featured TechnoTrend S2-6400" DVB cards.

%package        dvbsddevice
Summary:        VDR output device plugin for full featured SD DVB cards
Requires:       vdr(abi)%{?_isa} = %{apiver}
# To get this subpackage pulled in on upgrades
Obsoletes:      vdr < 1.7.11

%description    dvbsddevice
The dvbsddevice plugin implements the output device for the "Full
Featured" DVB cards based on the TechnoTrend/Fujitsu-Siemens design.

%package        rcu
Summary:        VDR remote control unit plugin
Requires:       vdr(abi)%{?_isa} = %{apiver}
# To get this subpackage pulled in on upgrades
Obsoletes:      vdr < 1.7.25

%description    rcu
The rcu plugin implements a remote control unit for VDR.

%package        skincurses
Summary:        Shell window skin plugin for VDR
BuildRequires:  ncurses-devel
Requires:       vdr(abi)%{?_isa} = %{apiver}

%description    skincurses
The skincurses plugin implements a VDR skin that works in a shell
window, using only plain text output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 18
# dvbhddevice
unzip -o %{SOURCE30} -d $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src
mv $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/powARman-dvbhddevice-3473a7b939d7 $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/dvbhddevice
cd PLUGINS/src
%patch 0 -p3
cd ../..
# dvbsddevice
tar -xzf %{SOURCE31} -C $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src
mv $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/dvbsddevice-2.2.0 $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/dvbsddevice
# rcu
tar -xzf %{SOURCE32} -C $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src
mv $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/rcu-2.2.0 $RPM_BUILD_DIR/vdr-%{version}/PLUGINS/src/rcu

%patch 1 -p1
# sort_options would be nice, but it conflicts with channel+epg which is nicer
#patch -F 0 -i debian/patches/02_sort_options.dpatch
# TODO: does not apply since 1.7.24
#patch -F 0 -i debian/patches/06_recording_scan_speedup.dpatch
patch -F 2 -i debian/patches/07_blockify_define.dpatch
%patch 3 -p1
sed \
    -e 's|__CACHEDIR__|%{cachedir}|'   \
    -e 's|__CONFIGDIR__|%{configdir}|' \
    -e 's|__PLUGINDIR__|%{plugindir}|' \
    -e 's|__VARDIR__|%{vardir}|'       \
    -e 's|__VIDEODIR__|%{videodir}|'   \
    %{PATCH4} | %{__patch} -p1
%patch 5 -p1
%patch 6 -p1
%patch 11 -p1
%patch 99 -p1

# Patch APIVERSION TO 2.4.8 to match VDRVERSION
# sed -i 's/2\.4\.3/2.4.8/' config.h
# sed -i 's/20406/20407/' config.h

for f in CONTRIBUTORS HISTORY UPDATE-1.4.0 \
    PLUGINS/src/dvbhddevice/HISTORY; do
    iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f && mv $f.utf8 $f
done

cp -p %{SOURCE5} reccmds.conf
cp -p %{SOURCE13} timercmds.conf
cp -p %{SOURCE6} commands.conf
# Unfortunately these can't have comments in them, so ship 'em empty.
cat /dev/null > channels.conf
cat /dev/null > remote.conf
cat /dev/null > setup.conf
cat /dev/null > timers.conf

install -pm 644 %{SOURCE10} README.package
install -pm 644 %{SOURCE16} CHANGES.package.old

# Would like to do "files {channels,setup,timers}.conf" from config dir
# only, but rename() in cSafeFile barks "device or resource busy", cf.
# http://lists.suse.com/archive/suse-programming-e/2003-Mar/0051.html
cat << EOF > %{name}.rwtab
dirs    %{cachedir}
files   %{configdir}
files   %{vardir}
EOF

# Disable some graphs that end up too big to be useful.
for g in COLLABORATION INCLUDE INCLUDED_BY ; do
    sed -i -e 's/^\(\s*'$g'_GRAPH\s*=\s*\).*/\1NO/' Doxyfile
done

# Create a sysusers.d config file
cat >vdr.sysusers.conf <<EOF
u vdr -:%{vdr_group} 'Video Disk Recorder' %{vardir} -
m vdr audio
m vdr cdrom
m vdr dialout
EOF

%build
cat << EOF > Make.config
CC           = %{__cc}
CXX          = %{__cxx}

CFLAGS       = \$(shell pkg-config vdr --variable=cflags)
CXXFLAGS     = \$(shell pkg-config vdr --variable=cxxflags)
LDFLAGS      = $RPM_LD_FLAGS

PREFIX       = %{_prefix}
MANDIR       = \$(shell pkg-config vdr --variable=mandir)
BINDIR       = \$(shell pkg-config vdr --variable=bindir)

LOCDIR       = \$(shell pkg-config vdr --variable=locdir)
PLUGINLIBDIR = \$(shell pkg-config vdr --variable=libdir)
VIDEODIR     = \$(shell pkg-config vdr --variable=videodir)
CONFDIR      = \$(shell pkg-config vdr --variable=configdir)
CACHEDIR     = \$(shell pkg-config vdr --variable=cachedir)
RESDIR       = \$(shell pkg-config vdr --variable=resdir)
INCDIR       = %{_includedir}
LIBDIR       = \$(PLUGINLIBDIR)

PLGCFG       = \$(LIBDIR)/plugins.mk
LIRC_DEVICE  = %{_localstatedir}/run/lirc/lircd
# New Bug 1873027 LIRC_DEVICE  = /run/lirc/lircd
VDR_USER     = \$(shell pkg-config vdr --variable=user)
SDNOTIFY     = 1
EOF

cat << EOF > plugins.mk
LDFLAGS = $RPM_LD_FLAGS
EOF

cp plugins.mk bundled-plugins.mk
cat << EOF >> bundled-plugins.mk
CFLAGS += -I$PWD/include
CXXFLAGS += -I$PWD/include
EOF

cflags="${RPM_OPT_FLAGS/-O2/-O3} -fPIC" # see HISTORY for 1.7.17 for -O3

make vdr.pc BINDIR=%{_bindir} MANDIR=%{_mandir} CONFDIR=%{configdir} \
    VIDEODIR=%{videodir} CACHEDIR=%{cachedir} RESDIR=%{_datadir}/vdr \
    LIBDIR=%{plugindir} LOCDIR=%{_datadir}/locale RUNDIR=%{rundir} \
    VARDIR=%{vardir} VDR_USER=%{vdr_user} VDR_GROUP=%{vdr_group} \
    LDFLAGS="$RPM_LD_FLAGS" CFLAGS="$cflags" \
    CXXFLAGS="$cflags -Werror=overloaded-virtual -Wno-parentheses"

PKG_CONFIG_PATH="$PWD:$PKG_CONFIG_PATH" \
%make_build vdr include-dir i18n

for plugin in dvbhddevice dvbsddevice rcu skincurses ; do
    %make_build -C PLUGINS/src/$plugin VDRDIR=$PWD \
        PLGCFG=$PWD/bundled-plugins.mk all
done

%if %{with docs}
%make_build srcdoc
%endif

%install
# Not using the install-pc target to preserve our already good vdr.pc
install -Dpm 644 vdr.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/vdr.pc

PKG_CONFIG_PATH="$RPM_BUILD_ROOT%{_libdir}/pkgconfig:$PKG_CONFIG_PATH" \
make install-bin install-dirs install-conf install-doc install-i18n \
    install-includes DESTDIR=$RPM_BUILD_ROOT

install -pm 755 epg2html $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_sbindir}
#mv $RPM_BUILD_ROOT%{_bindir}/vdr $RPM_BUILD_ROOT%{_sbindir}

# Avoid mv error by checking if source and destination are the same
if [ "$RPM_BUILD_ROOT%{_bindir}/vdr" != "$RPM_BUILD_ROOT%{_sbindir}/vdr" ]; then
    mv $RPM_BUILD_ROOT%{_bindir}/vdr $RPM_BUILD_ROOT%{_sbindir}
fi

install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d

install -dm 755 $RPM_BUILD_ROOT%{vardir}/themes
touch $RPM_BUILD_ROOT%{vardir}/themes/{classic,sttng}-default.theme

install -pm 755 %{SOURCE7} $RPM_BUILD_ROOT%{_sbindir}/runvdr
sed -i \
    -e 's|/usr/sbin/|%{_sbindir}/|'                    \
    -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|g' \
    -e 's|/usr/lib/vdr\b|%{plugindir}|'                \
    -e 's|VDR_PLUGIN_VERSION|%{apiver}|'               \
    $RPM_BUILD_ROOT%{_sbindir}/runvdr

install -Dm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|' \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr

touch $RPM_BUILD_ROOT%{videodir}/.update

install -dm 755 $RPM_BUILD_ROOT%{plugindir}/bin

install -m 755 %{SOURCE14} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-shutdown.sh
sed -i \
    -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|' \
    -e 's|/var/run/vdr/|%{rundir}/|'                  \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-shutdown.sh

install -m 755 %{SOURCE15} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-moveto.sh
sed -i \
    -e 's|/var/lib/vdr/video|%{videodir}|' \
    -e 's|/etc/vdr/|%{configdir}/|'        \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-moveto.sh

install -m 755 %{SOURCE19} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-check-setup
sed -i \
    -e 's|/etc/vdr/|%{configdir}/|' \
    -e 's|VDR_USER|%{vdr_user}|'    \
    -e 's|VDR_GROUP|%{vdr_group}|'  \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-check-setup

install -m 755 %{SOURCE21} $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-set-wakeup
sed -i \
    -e 's|/usr/sbin/|%{_sbindir}/|'  \
    -e 's|/var/run/vdr/|%{rundir}/|' \
    $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-set-wakeup

install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
sed -i \
    -e 's|/usr/lib/vdr/|%{plugindir}/|'        \
    -e 's|/usr/sbin/|%{_sbindir}/|'            \
    -e 's|/usr/share/doc/vdr/|%{_pkgdocdir}/|' \
    $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

install -Dpm 440 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sudoers.d/vdr

touch $RPM_BUILD_ROOT%{cachedir}/epg.data
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/vdr/{logos,plugins}
install -dm 755 $RPM_BUILD_ROOT%{rundir}
touch $RPM_BUILD_ROOT%{rundir}/next-timer
install -dm 755 $RPM_BUILD_ROOT%{vardir}

install -Dpm 644 %{name}.rwtab $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/%{name}

install -dm 755 $RPM_BUILD_ROOT%{_pkgdocdir}
install -pm 644 CHANGES.package.old CONTRIBUTORS \
    HISTORY* INSTALL MANUAL PLUGINS.html README* UPDATE-?.?.0 \
    $RPM_BUILD_ROOT%{_pkgdocdir}
%if %{with docs}
cp -pR srcdoc/html $RPM_BUILD_ROOT%{_pkgdocdir}
%endif

# devel

abs2rel() { perl -MFile::Spec -e 'print File::Spec->abs2rel(@ARGV)' "$@" ; }

install -pm 755 %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/vdr-config
install -pm 755 newplugin $RPM_BUILD_ROOT%{_bindir}/vdr-newplugin
install -pm 644 Make.{config,global} plugins.mk $RPM_BUILD_ROOT%{_libdir}/vdr
ln -s $(abs2rel %{_includedir}/vdr/config.h %{_libdir}/vdr) \
    $RPM_BUILD_ROOT%{_libdir}/vdr
macrodir=%{_sysconfdir}/rpm
[ -d %{_rpmconfigdir}/macros.d ] && macrodir=%{_rpmconfigdir}/macros.d
install -Dpm 644 %{SOURCE17} $RPM_BUILD_ROOT$macrodir/macros.vdr
echo $macrodir/macros.vdr > %{name}-devel.files

# i18n

%find_lang %{name}
sed -i -e '1i%%defattr(-,root,root,-)' %{name}.lang

install -dm 755 $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
echo "d %{rundir} 0755 %{vdr_user} root -" \
    > $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/%{name}.conf
echo "%{_prefix}/lib/tmpfiles.d/%{name}.conf" \
    >> %{name}.lang

# plugins

%make_install -C PLUGINS/src/dvbhddevice
install -pm 644 %{SOURCE12} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/dvbhddevice.conf
%find_lang %{name}-dvbhddevice

%make_install -C PLUGINS/src/dvbsddevice
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/dvbsddevice.conf

%make_install -C PLUGINS/src/rcu
install -pm 644 %{SOURCE20} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/rcu.conf

%make_install -C PLUGINS/src/skincurses
install -pm 644 %{SOURCE11} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
%find_lang %{name}-skincurses

install -m0644 -D vdr.sysusers.conf %{buildroot}%{_sysusersdir}/vdr.conf

%check
export PKG_CONFIG_PATH=$RPM_BUILD_ROOT%{_libdir}/pkgconfig
if [ "$(pkg-config vdr --variable=apiversion)" != "%{apiver}" ] ; then
    echo "ERROR: API version mismatch in vdr.pc / package / config.h" ; exit 1
fi

%post
%systemd_post %{name}.service
systemctl daemon-reload

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{name}.lang
%{_pkgdocdir}
%exclude %{_pkgdocdir}/PLUGINS.html
%if %{with docs}
%exclude %{_pkgdocdir}/html/
%endif
%config(noreplace) %{_sysconfdir}/sudoers.d/vdr
%config(noreplace) %{_sysconfdir}/sysconfig/vdr
%config(noreplace) %{_sysconfdir}/rwtab.d/%{name}
%config %dir %{_sysconfdir}/sysconfig/vdr-plugins.d/
%{_bindir}/epg2html
%{_bindir}/svdrpsend
%{_sbindir}/runvdr
%{_sbindir}/vdr
%{_unitdir}/%{name}.service
%dir %{plugindir}/
%dir %{plugindir}/bin/
%{plugindir}/bin/%{name}-check-setup
%{plugindir}/bin/%{name}-moveto.sh
%{plugindir}/bin/%{name}-set-wakeup
%{plugindir}/bin/%{name}-shutdown.sh
%{_datadir}/vdr/
%{_mandir}/man1/svdrpsend.1*
%{_mandir}/man1/vdr.1*
%{_mandir}/man5/vdr.5*
%dir %{varbase}/
%defattr(-,%{vdr_user},%{vdr_group},-)
# TODO: tighten ownerships to root:root for some files in %%{configdir}
%config(noreplace) %{configdir}/*.conf
%dir %{videodir}/
%ghost %{videodir}/.update
%ghost %{vardir}/themes/*.theme
%ghost %{cachedir}/epg.data
%defattr(-,%{vdr_user},root,-)
%dir %{configdir}/
%dir %{configdir}/plugins/
%dir %{rundir}/
%ghost %{rundir}/next-timer
%dir %{vardir}/
%dir %{vardir}/themes/
%dir %{cachedir}/
%{_sysusersdir}/vdr.conf

%files devel -f %{name}-devel.files
%{!?_with_docs:%dir %{_pkgdocdir}}
%license COPYING
%if ! %{with docs}
%{_pkgdocdir}/PLUGINS.html
%endif
%{_bindir}/vdr-config
%{_bindir}/vdr-newplugin
%{_includedir}/libsi/
%{_includedir}/vdr/
%{_libdir}/pkgconfig/vdr.pc
%dir %{_libdir}/vdr/
%{_libdir}/vdr/Make.config
%{_libdir}/vdr/Make.global
%{_libdir}/vdr/config.h
%{_libdir}/vdr/plugins.mk

%if %{with docs}
%files docs
%dir %{_pkgdocdir}
%license COPYING
%{_pkgdocdir}/PLUGINS.html
%{_pkgdocdir}/html/
%endif

%files dvbhddevice -f %{name}-dvbhddevice.lang
%license PLUGINS/src/dvbhddevice/COPYING
%doc PLUGINS/src/dvbhddevice/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/dvbhddevice.conf
%{plugindir}/libvdr-dvbhddevice.so.%{apiver}

%files dvbsddevice
%license PLUGINS/src/dvbsddevice/COPYING
%doc PLUGINS/src/dvbsddevice/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/dvbsddevice.conf
%{plugindir}/libvdr-dvbsddevice.so.%{apiver}

%files rcu
%license PLUGINS/src/rcu/COPYING
%doc PLUGINS/src/rcu/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/rcu.conf
%{plugindir}/libvdr-rcu.so.%{apiver}

%files skincurses -f %{name}-skincurses.lang
%license PLUGINS/src/skincurses/COPYING
%doc PLUGINS/src/skincurses/{HISTORY,README}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
%{plugindir}/libvdr-skincurses.so.%{apiver}

%changelog
%autochangelog
