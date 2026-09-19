%global source0_hash none

%global _hardened_build 1

Summary: Frozen Bubble arcade game
Name: frozen-bubble
Version: 2.2.1
Release: 0.54.beta1%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://www.frozen-bubble.org/
Source0: http://www.frozen-bubble.org/data/frozen-bubble-%{version}-beta1.tar.bz2
Source1: frozen-bubble.desktop
Source2: fb-server.service
Patch0:  frozen-bubble-2.2.1-setuid.patch
Patch1:  0001-Fix-buffer-size-when-formatting-current-date.patch
Patch2:  frozen-bubble-2.2.1-Use-true-number-instead-of-quoted-version-number.patch
BuildRequires: /usr/bin/appstream-util
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(Alien::SDL) >= 1.413
BuildRequires: perl(autodie)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(IO::File)
BuildRequires: perl(IPC::System::Simple)
BuildRequires: perl(lib)
BuildRequires: perl(Locale::Maketext::Extract)
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(parent)
BuildRequires: perl(SDL) >= 2.511
BuildRequires: perl(Test::More)
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_Pango-devel
Requires:      perl(SDL) >= 2.511
Requires:      perl(Alien::SDL) >= 1.413
Requires:      hicolor-icon-theme

%{?perl_default_filter}

%description
Full-featured, colorful animated penguin eye-candy, 100 levels of 1p game, hours
and hours of 2p game, 3 professional quality 20-channels musics, 15 stereo
sound effects, 7 unique graphical transition effects and a level editor.
You need this game.

%package server
Summary: Frozen Bubble network game dedicated server
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

%description server
Frozen Bubble network game dedicated server. The server is already included
with the game in order to be launched automatically for LAN games, so you
only need to install this package if you want to run a fully dedicated
Frozen Bubble network game server.

%prep
%autosetup -p1 -n %{name}-%{version}-beta1
# Rename this README since the main server README has the same name
%{__mv} server/init/README server/README.init
# Change the example server configuration file to be a working one, which only
# launches a LAN server and doesn't try to register itself on the Internet
%{__sed} -ie "s#^a .*#z\nq\nL#" server/init/fb-server.conf

# Create a sysusers.d config file
cat >frozen-bubble.sysusers.conf <<EOF
u fbubble - - %{_datadir}/%{name} -
EOF

%build
export LDFLAGS="%{?__global_ldflags}"
export CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
sed -i "s|'-Wl,-rpath,/usr/.*',||" _build/build_params
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
#%%find_lang %%{name}

# Clean up unneeded files
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

# Desktop file
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}

# Icons
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-16x16.png \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-32x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-48x48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__install} -D -p -m 0644 share/icons/frozen-bubble-icon-64x64.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install server init script and default configuration
%{__install} -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_unitdir}/fb-server.service
%{__install} -D -p -m 0644 server/init/fb-server.conf \
    %{buildroot}%{_sysconfdir}/fb-server.conf

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: contact2@frozen-bubble.org
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">frozen-bubble.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>An addictive game about frozen bubbles</summary>
  <description>
    <p>
      Frozen Bubble is a free and open source game in which you throw colorful
      bubbles and build groups to destroy them.
    </p>
    <p>
      You can play this game locally or over the Internet.
      It also contains a level editor for you to create your own games.
    </p>
  </description>
  <url type="homepage">http://www.frozen-bubble.org/</url>
  <screenshots>
    <screenshot type="default">https://upload.wikimedia.org/wikipedia/commons/d/d6/Frozen-bubble.jpg</screenshot>
    <screenshot>http://www.frozen-bubble.org/data/fb2-5p.png</screenshot>
  </screenshots>
  <update_contact>contact2_at_frozen-bubble.org</update_contact>
</application>
EOF

install -m0644 -D frozen-bubble.sysusers.conf %{buildroot}%{_sysusersdir}/frozen-bubble.conf

%check
./Build test
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/frozen-bubble.appdata.xml

%post server
%systemd_post fb-server.service

%preun server
%systemd_preun fb-server.service

%postun server
%systemd_postun_with_restart fb-server.service

%files
%doc AUTHORS Changes HISTORY README
%license COPYING
%{_bindir}/%{name}*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Games/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man3/*.3pm*

%files server
%doc server/AUTHORS server/README*
%license COPYING
%config(noreplace) %{_sysconfdir}/fb-server.conf
%{_unitdir}/fb-server.service
%{_bindir}/fb-server
%{_sysusersdir}/frozen-bubble.conf

%changelog
%autochangelog
