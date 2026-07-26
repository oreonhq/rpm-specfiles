%global source0_hash none

Name:           nethack-vultures
Version:        2.1.2
Release:        45%{?dist}
Summary:        NetHack - Vulture's Eye and Vulture's Claw

License:        NGPL
URL:            http://www.darkarts.co.za/vulture-for-nethack
# This location is no longer valid
Source0:        http://downloads.usrsrc.org/vultures/%{version}/vultures-%{version}-full.tar.bz2
Source1:        %{name}.logrotate
Patch0:         %{name}-1.11.0-optflags.patch
Patch1:         %{name}-2.1.2-config.patch
Patch2:         %{name}-1.10.1-clawguide.patch
Patch3:         %{name}-2.1.2-tabfullscreen.patch
Patch4:         %{name}-2.1.2-logging.patch
Patch5:         %{name}-libpng.patch
Patch6:         format-fix.patch
Patch7:         parser-fix.patch
Patch8:         make-bison.patch
Patch9:         nethack-vultures-c99.patch
Patch10:	objtype.patch
Patch11:	doorfix.patch
Patch12:	system.patch
# Prototype mismatch for what looks like an unused function/feature
Patch13:	botl-unused.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel >= 1.2.6
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL-static
BuildRequires:  libpng-devel
BuildRequires:  ncurses-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  desktop-file-utils
BuildRequires:  groff
BuildRequires:  util-linux

# Automate finding font paths
%global fonts font(bitstreamveraserif)
BuildRequires:  fontconfig %{fonts}
Requires:       %{fonts}

Requires:       /usr/bin/bzip2
Requires:       logrotate
%if 0%{?fedora} < 43
Requires(pre):  shadow-utils
%endif
Requires(pre):  coreutils
Obsoletes:      nethack-falconseye <= 1.9.4-6.a

%description
Vulture's Eye is a mouse-driven interface for NetHack that enhances
the visuals, audio and accessibility of the game, yet retains all the
original gameplay and game features.  Vulture's Eye is based on
Falcon's Eye, but is greatly extended.  Also included is Vulture's
Claw, which is based on the Slash'Em core.

%prep
%setup -q -n vultures-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -F1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p0 -b .libpng
%patch -P6 -p0 -b .format-fix
%patch -P7 -p0 -b .parser-fix
%patch -P8 -p0 -b .make-bison
%patch -P9 -p1
%patch -P10 -p0
%patch -P11 -p0
%patch -P12 -p0
%patch -P13 -p0
sed -i -e 's|/usr/games/lib/nethackdir|%{_prefix}/games/vultureseye|g' \
    nethack/doc/{nethack,recover}.6 nethack/include/config.h
sed -i -e 's|/var/lib/games/nethack|%{_var}/games/vultureseye|g' \
    nethack/include/unixconf.h
sed -i -e 's|/usr/games/lib/nethackdir|%{_prefix}/games/vulturesclaw|g' \
    slashem/doc/{nethack,recover}.6 slashem/include/config.h
sed -i -e 's|/var/lib/games/nethack|%{_var}/games/vulturesclaw|' \
    slashem/include/unixconf.h

%build
# Note: no %{?_smp_mflags} in any of these: various parallel build issues.
for i in nethack slashem ; do
    make $i/Makefile
    make -C $i
    make -C $i/util recover dlb dgn_comp lev_comp YACC="bison -y"
    make -C $i/dat spec_levs quest_levs
done

%install
rm -rf $RPM_BUILD_ROOT

make -C nethack install CHGRP=: CHOWN=: \
    GAMEDIR=$RPM_BUILD_ROOT%{_prefix}/games/vultureseye \
    VARDIR=$RPM_BUILD_ROOT%{_var}/games/vultureseye \
    SHELLDIR=$RPM_BUILD_ROOT%{_bindir}
make -C slashem install CHGRP=: CHOWN=: \
    GAMEDIR=$RPM_BUILD_ROOT%{_prefix}/games/vulturesclaw \
    VARDIR=$RPM_BUILD_ROOT%{_var}/games/vulturesclaw \
    SHELLDIR=$RPM_BUILD_ROOT%{_bindir}

install -dm 755 $RPM_BUILD_ROOT%{_mandir}/man6
install -pm 644 nethack/doc/nethack.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vultureseye.6
install -pm 644 nethack/doc/recover.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vultureseye-recover.6
install -pm 644 slashem/doc/nethack.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vulturesclaw.6
install -pm 644 slashem/doc/recover.6 \
    $RPM_BUILD_ROOT%{_mandir}/man6/vulturesclaw-recover.6

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
for i in vultureseye vulturesclaw ; do
    desktop-file-install \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        --mode=644 \
        --add-category=RolePlaying \
        --remove-category=Application \
        --remove-category=3DGame \
        --remove-category=PuzzleGame \
        dist/unix/desktop/$i.desktop
    mv $RPM_BUILD_ROOT%{_prefix}/games/$i/*.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/$i.png
    mv $RPM_BUILD_ROOT%{_prefix}/games/$i/recover \
        $RPM_BUILD_ROOT%{_bindir}/$i-recover
done

ln -sf $(fc-match -f "%{file}" "bitstream:vera:serif") \
    $RPM_BUILD_ROOT%{_prefix}/games/vulturesclaw/fonts
ln -sf $(fc-match -f "%{file}" "bitstream:vera:serif") \
    $RPM_BUILD_ROOT%{_prefix}/games/vultureseye/fonts

rm -r $RPM_BUILD_ROOT%{_prefix}/games/vultures*/manual

# Save quite a bit of space
/usr/bin/hardlink -cv $RPM_BUILD_ROOT%{_prefix}/games/vultures*

chmod -s $RPM_BUILD_ROOT%{_prefix}/games/vultures*/vultures* # for stripping

# Clean up
sed -i -e "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT%{_bindir}/vultures{eye,claw}
rm $RPM_BUILD_ROOT%{_prefix}/games/vultures*/*.ico

install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -dm 775 $RPM_BUILD_ROOT%{_var}/log/vultures/

%if 0%{?fedora} >= 43
mkdir -p $RPM_BUILD_ROOT%{_sysusersdir}
cat > $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf <<EOF
g vultures -
EOF
%endif

%pre
%if 0%{?fedora} < 43
/usr/sbin/groupadd vultures 2> /dev/null || :
%endif
# Get dir symlinks that were there once out of the way
for dir in graphics sound music ; do
    [ -L %{_prefix}/games/vulturesclaw/$dir ] && \
        rm -f %{_prefix}/games/vulturesclaw/$dir || :
done

%files
%doc nethack/README nethack/dat/license nethack/dat/history nethack/dat/*help
%doc slashem/readme.txt slashem/history.txt slashem/slamfaq.txt
%doc vultures/gamedata/manual/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/vultures*
%dir %{_prefix}/games/vultureseye/
%{_prefix}/games/vultureseye/config/
%{_prefix}/games/vultureseye/defaults.nh
%{_prefix}/games/vultureseye/graphics/
%{_prefix}/games/vultureseye/license
%{_prefix}/games/vultureseye/music/
%{_prefix}/games/vultureseye/nhdat
%{_prefix}/games/vultureseye/sound/
%{_prefix}/games/vultureseye/fonts/
%{_prefix}/games/vultureseye/tiles/
%attr(2755,root,vultures) %{_prefix}/games/vultureseye/vultureseye
%dir %{_prefix}/games/vulturesclaw/
%{_prefix}/games/vulturesclaw/config/
%{_prefix}/games/vulturesclaw/defaults.nh
%{_prefix}/games/vulturesclaw/graphics/
%{_prefix}/games/vulturesclaw/Guidebook.txt
%{_prefix}/games/vulturesclaw/license
%{_prefix}/games/vulturesclaw/music/
%{_prefix}/games/vulturesclaw/nh*share
%{_prefix}/games/vulturesclaw/sound/
%{_prefix}/games/vulturesclaw/fonts/
%{_prefix}/games/vulturesclaw/tiles/
%attr(2755,root,vultures) %{_prefix}/games/vulturesclaw/vulturesclaw
%{_datadir}/applications/*vultures*.desktop
%{_datadir}/icons/hicolor/48x48/apps/vultures*.png
%{_mandir}/man6/vultures*.6*
%defattr(664,root,vultures,775)
%dir %{_var}/games/vultureseye/
%config(noreplace) %{_var}/games/vultureseye/record
%config(noreplace) %{_var}/games/vultureseye/perm
%config(noreplace) %{_var}/games/vultureseye/logfile
%dir %{_var}/games/vultureseye/save/
%dir %{_var}/games/vulturesclaw/
%config(noreplace) %{_var}/games/vulturesclaw/record
%config(noreplace) %{_var}/games/vulturesclaw/perm
%config(noreplace) %{_var}/games/vulturesclaw/logfile
%dir %{_var}/games/vulturesclaw/save/
%dir %{_var}/log/vultures/
%if 0%{?fedora} >= 43
%{_sysusersdir}/%{name}.conf
%endif

%changelog
%autochangelog
