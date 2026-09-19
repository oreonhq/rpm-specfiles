%global source0_hash 24f2f7db9cf7faf53b95f9e2580e6f596205a98ed0c335cfe834c64785ad4f5a

Name:           uqm
Version:        0.8.0
Release:        8%{?dist}
Summary:        The Ur-Quan Masters, a port of the classic game Star Control II

# Upstream claims everything to be under GPL-2.0-or-later.
# In reality, the source contains many files copied from other projects,
# with a variety of open source licenses.
License:        GPL-2.0-or-later AND GPL-2.0-only AND LGPL-2.1-or-later AND Zlib
URL:            http://sc2.sourceforge.net/
Source0:        http://download.sf.net/sc2/%{name}-%{version}-src.tgz
Source1:        %{name}.conf
Source2:        %{name}.sh
Source3:        %{name}.desktop
Source4:        %{name}-functions.sh
Source5:        %{name}.autodlrc
Patch0:         %{name}-optflags.patch

BuildRequires:  SDL-devel >= 1.2.8
BuildRequires:  SDL_image-devel >= 1.2.4
BuildRequires:  ImageMagick
BuildRequires:  libvorbis-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libGLU-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libpng-devel
BuildRequires:  gcc
Requires:       autodownloader
Provides:       uqm-content = %{version}-%{release}
Provides:       uqm-content-3domusic = %{version}-%{release}
Provides:       uqm-content-voice = %{version}-%{release}
Obsoletes:      uqm-content <= 0.6.0-2
Obsoletes:      uqm-content-3domusic <= 0.6.0-2
Obsoletes:      uqm-content-voice <= 0.6.0-2

%description
The Ur-Quan Masters is a port of the classic game Star Control II to
modern systems.  The program code that comprises The Ur-Quan Masters
was derived from code written by Toys for Bob, Inc. for the 3DO
version of Star Control II, with their permission and encouragement.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn uqm-0.8.0
find -type d -name CVS -exec rm -rf {} ';'
%patch -P0 -p0

%build
echo INPUT_install_sharedir_VALUE=%{_datadir} > config.state
sed -i 's|@CONTENTDIR@|~/.uqm|g' src/config_unix.h.in
sh ./build.sh uqm < /dev/null
convert src/res/ur-quan-icon-std.ico uqm.png

%install

install -dm 755 $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}
sed -e 's|/etc/|%{_sysconfdir}/|' %{SOURCE1} > \
  $RPM_BUILD_ROOT%{_sysconfdir}/uqm.conf
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/uqm.conf
sed -e 's|/usr/games/|%{_prefix}/games/|' %{SOURCE2} \
  > $RPM_BUILD_ROOT%{_bindir}/uqm
chmod 755 $RPM_BUILD_ROOT%{_bindir}/uqm

install -Dpm 755 uqm $RPM_BUILD_ROOT%{_prefix}/games/uqm

install -dm 755 \
  $RPM_BUILD_ROOT%{_datadir}/uqm/content/packages/addons
echo %{version} > $RPM_BUILD_ROOT%{_datadir}/uqm/content/version

desktop-file-install \
  --mode 644 \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
 %{SOURCE3}
install -Dpm 644 uqm-5.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/uqm.png

# needed "data" files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}

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
<!-- Copyright 2014 Luya Tshimbalanga <luya@fedoraproject.org> -->
<!--
BugReportURL: https://bugs.uqm.stack.nl/show_bug.cgi?id=1199
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">uqm.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Classic space adventure game</summary>
  <description>
    <p>
    A port of classic game Star Control II that includes adventure and melee
    mode with enhancement for modern system.
    </p>
  </description>
  <url type="homepage">http://sc2.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://sc2.sourceforge.net/screenshots/meleestep.png</screenshot>
    <screenshot>http://sc2.sourceforge.net/screenshots/scale_triscan.png</screenshot>
    <screenshot>http://sc2.sourceforge.net/screenshots/slaveshield.png</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc AUTHORS ChangeLog Contributing README
%doc WhatsNew doc/users/manual.txt
%config(noreplace) %{_sysconfdir}/uqm.conf
%{_bindir}/uqm
%{_prefix}/games/uqm
%{_datadir}/uqm/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/uqm.png

%changelog
%autochangelog
