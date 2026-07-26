%global source0_hash f287093c757a71232000f210ee4a4edeccc9e8af0817d5be43084e84aebd4709

%global logwatch_root %{_datadir}/logwatch
%global logwatch_conf %{logwatch_root}/dist.conf
%global logwatch_scripts %{logwatch_root}/scripts

Name:           xpilot-ng
Version:        4.7.3
Release:        38%{?dist}
Summary:        Space arcade game for multiple players

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://xpilot.sourceforge.net
Source0:        http://downloads.sourceforge.net/sourceforge/xpilot/xpilot-ng-%{version}.tar.gz
Source1:        xpilot-ng.png
Source2:        xpilot-ng-sdl.desktop
Source3:        xpilot-ng-sdl.appdata.xml
Source4:        xpilot-ng-server.service
Source5:        xpilot-ng.sysconfig
Source6:        xpilot-ng.logrotate
Source7:        xpilot-ng-server.conf
Source10:       logwatch.logconf.xpilot
Source11:       logwatch.script.xpilot
Source12:       logwatch.serviceconf.xpilot
Source13:       logwatch.shared.applyxpilotdate
Source14:       xpilot-ng-server.metainfo.xml
Patch0:         xpilot-ng-4.7.2-scoreassert.patch
Patch1:         xpilot-ng-4.7.2-rhbz830640.patch
Patch2:         xpilot-ng-4.7.3-fix-alut-detect.patch
Patch3:         xpilot-ng-c99.patch
Patch4:         xpilot-ng-SDL_window.patch
Patch5:         xpilot-ng-c99-return-mismatch.patch
Patch6:         xpilot-ng-c99-incompatible-pointer-types.patch
Patch7:         xpilot-ng-c23.patch

BuildRequires:  gcc make
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  expat-devel SDL_ttf-devel SDL_image-devel zlib-devel
BuildRequires:  libXt-devel libGLU-devel
BuildRequires:  openal-soft-devel freealut-devel automake
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-data = %{version}-%{release} hicolor-icon-theme
Provides:       %{name}-engine = %{version}-%{release}

%description
A highly addictive, infinitely configurable multi-player space
arcade game.  You pilot a spaceship around space, dodging
obstacles, shooting players and bots, collecting power-ups, and
causing general mayhem.

%package x11
Summary:        Xpilot-ng X11 version
Requires:       %{name}-data = %{version}-%{release}
Provides:       %{name}-engine = %{version}-%{release}

%description x11
Version of %{name} which uses libX11 rather then SDL.

%package data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release} dejavu-sans-fonts

%description data
Data files for %{name}.

%package server
Summary:        Server for hosting xpilot games
Requires:       %{name}-data = %{version}-%{release}
Requires:       logrotate
%{?sysusers_requires_compat}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  systemd
Provides:       %{name}-engine = %{version}-%{release}
# Make sure the old no longer supported selinux policy from 4.7.2 gets removed
Obsoletes:      %{name}-selinux < %{version}-%{release}
Provides:       %{name}-selinux = %{version}-%{release}

%description server
The xpilot server.  This allows you to host xpilot games on your
computer and develop new xpilot maps.  This is required if you
are playing alone, but not required if you are joining one of the
public xpilot games hosted on the internet.

%package logwatch
Summary:        Logwatch scripts for the xpilot game server
Requires:       %{name}-server = %{version}-%{release} logwatch

%description logwatch
logwatch scripts for the Xpilot game server

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# regenerate autofoo files for patch2
autoreconf -ivf
# fixup textfile encodings
pushd doc/man
iconv --from=ISO-8859-1 --to=UTF-8 xpilot-ng-server.man > xpilot-ng-server.man.new
touch -r xpilot-ng-server.man xpilot-ng-server.man.new
mv xpilot-ng-server.man.new xpilot-ng-server.man

iconv --from=ISO-8859-1 --to=UTF-8 xpilot-ng-x11.man > xpilot-ng-x11.man.new
touch -r xpilot-ng-x11.man xpilot-ng-x11.man.new
mv xpilot-ng-x11.man.new xpilot-ng-x11.man
popd

iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new
touch -r AUTHORS AUTHORS.new
mv AUTHORS.new AUTHORS

%build
%configure --enable-sound
iconv --from=ISO-8859-1 --to=UTF-8 README -o README
touch -r README.in README
make %{?_smp_mflags}

%install
%make_install INSTALL="install -p"

# Drop old Python 2 only map conversion script
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/mapconvert.py

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.xml

install -p -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/lib/systemd/system/%{name}-server.service

# Copy certain configuration files to /etc so that they can be properly managed
# as config files.
install -p -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}-server-cmdline-opts
install -p -D -m 644 lib/defaults.txt $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/defaults.txt
install -p -D -m 600 lib/password.txt $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/password.txt

install -p -D -m 644 %{SOURCE6} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}-server

# Install sysusers file
install -p -D -m 0644 %{SOURCE7} %{buildroot}%{_sysusersdir}/xpilot-ng-server.conf

# Replace bundled fonts with system fonts

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/FreeSansBoldOblique.ttf
ln -s %{_datadir}/fonts/dejavu/DejaVuSans-BoldOblique.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/FreeSansBoldOblique.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/VeraMoBd.ttf
ln -s %{_datadir}/fonts/dejavu/DejaVuSansMono-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/VeraMoBd.ttf

# Install logwatch files
install -pD -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{logwatch_conf}/logfiles/%{name}.conf
install -pD -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{logwatch_scripts}/services/%{name}
install -pD -m 0644 %{SOURCE12} $RPM_BUILD_ROOT%{logwatch_conf}/services/%{name}.conf
install -pD -m 0644 %{SOURCE13} $RPM_BUILD_ROOT%{logwatch_scripts}/shared/applyxpilotdate

%pre server
%sysusers_create_compat %{SOURCE7}

%post server
%systemd_post xpilot-ng-server.service

%preun server
%systemd_preun xpilot-ng-server.service

%postun server
%systemd_postun_with_restart xpilot-ng-server.service 

%files
%{_bindir}/xpilot-ng-replay
%{_bindir}/xpilot-ng-sdl
%{_datadir}/appdata/xpilot-ng-sdl.appdata.xml
%{_datadir}/applications/xpilot-ng-sdl.desktop
%{_datadir}/icons/hicolor/48x48/apps/xpilot-ng.png
%{_mandir}/man6/xpilot-ng-replay.6.gz
%{_mandir}/man6/xpilot-ng-sdl.6.gz

%files data
%doc AUTHORS BUGS ChangeLog FEATURES README TODO
%license COPYING
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/textures
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/sound

%files x11
%{_bindir}/xpilot-ng-x11
%{_mandir}/man6/xpilot-ng-x11.6.gz

%files server
%{_sysusersdir}/xpilot-ng-server.conf
%{_bindir}/xpilot-ng-xp-mapedit
%{_bindir}/xpilot-ng-server
/lib/systemd/system/xpilot-ng-server.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/textures
%exclude %{_datadir}/%{name}/fonts
%exclude %{_datadir}/%{name}/sound
%{_datadir}/appdata/xpilot-ng-server.metainfo.xml
%dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(0600,xpilot,root) %{_sysconfdir}/%{name}/password.txt
%config(noreplace) %{_sysconfdir}/%{name}/defaults.txt
%config(noreplace) %{_sysconfdir}/%{name}/xpilot-ng-server-cmdline-opts
%{_mandir}/man6/xpilot-ng-server.6.gz
%{_mandir}/man6/xpilot-ng-xp-mapedit.6.gz

%files logwatch
%{logwatch_conf}/logfiles/%{name}.conf
%{logwatch_conf}/services/%{name}.conf
%{logwatch_scripts}/services/%{name}
%{logwatch_scripts}/shared/applyxpilotdate

%changelog
%autochangelog
