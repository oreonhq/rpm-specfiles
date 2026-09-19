%global source0_hash 28838bfa974a0b769b04a8820ad7953a7ad0835eb5d1764db173deac75984b6f

%define pkgverdir %(echo %version|sed s/\\\\\./_/)

Name:           openmsx
Version:        21.0
Release:        2%{?dist}
Summary:        An emulator for the MSX home computer system
License:        GPL-2.0-only
URL:            https://openmsx.org/
Source0:        https://github.com/openMSX/openMSX/releases/download/RELEASE_%{pkgverdir}/%{name}-%{version}.tar.gz
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  docbook-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel >= 2.1.0
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_ttf-devel
# OpenMSX does not build with Tcl 9.0
BuildRequires:  tcl-devel < 1:9
BuildRequires:  zlib-devel
Requires:       cbios-%{name}
Requires:       hicolor-icon-theme

# Catapult is no longer maintained
Obsoletes:      %{name}-catapult <= 19.1

%description
openMSX is an emulator for the MSX home computer system. Its goal is to emulate
all aspects of the MSX with high accuracy. In addition to emulating MSX, MSX2,
MSX2+, MSX Turbo R and many of it's peripherals, it also support emulating the
ColecoVision game console and the SpectraVideo SVI-318 and SVI-328 home
computer systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Make the custom flavour module, so we can use RPM OPT FLAGS here
cat > build/flavour-rpm.mk << EOF
# Opt flags.
CXXFLAGS+=%{optflags} -DNDEBUG
LINK_FLAGS+=%{__global_ldflags}

# Dont strip exe, let rpm do it and save debug info
OPENMSX_STRIP:=false
EOF

cat > build/custom.mk << EOF
PYTHON:=python3
INSTALL_BASE:=%{_prefix}
VERSION_EXEC:=false
SYMLINK_FOR_BINARY:=false
INSTALL_CONTRIB:=false
INSTALL_SHARE_DIR=%{_datadir}/%{name}
INSTALL_DOC_DIR=%{_docdir}/%{name}
EOF

%configure
%make_build OPENMSX_FLAVOUR=rpm

# Build desktop icon
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=openMSX
GenericName=MSX Emulator
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
Keywords=emulator;msx;openmsx;
EOF

# Build the man page
docbook2man doc/openmsx.sgml -o ./

%install
%make_install OPENMSX_FLAVOUR=rpm V=1

rm $RPM_BUILD_ROOT%{_docdir}/%{name}/GPL.txt

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/machines/*.txt \
   $RPM_BUILD_ROOT%{_docdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/settings.xml \
   $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
ln -s --target-directory=$RPM_BUILD_ROOT%{_datadir}/%{name} \
   ../../../etc/openmsx/settings.xml

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 0644 OPENMSX.1 $RPM_BUILD_ROOT%{_mandir}/man1/openmsx.1

# Install icon set and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
for i in 16 32 48 64 128; do
install -pm 0644 share/icons/openMSX-logo-"$i".png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$i"x"$i"/apps/%{name}.png
done

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
                     %{name}.desktop

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: BUGTRACKER DEAD
SentUpstream: 2014-09-25
-->
<component type="desktop">
  <id>openmsx.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0</project_license>
  <name>openMSX</name>
  <summary>Emulate all aspects of the MSX with high accuracy</summary>
  <description>
    <p>
      OpenMSX is an emulator for the MSX home computer system. MSX is an old
      Z80-based family of home computers as an attempt to establish
      a single standard in home computing similar to VHS in video.
    </p>
    <p>
      The MSX standard has been designed by a company called ASCII in Cooperation
      with Microsoft which has provided a firmware version of its extended BASIC
      (called "MicroSoft eXtended BASIC") for the machine, which explains the
      MSX name.
    </p>
    <p>
     In addition to emulating MSX, MSX2, MSX2+, MSX Turbo R and many of it's
     peripherals, openMSX also support emulating the ColecoVision game console
     and the SpectraVideo SVI-318 and SVI-328 home computer systems.
    </p>
  </description>
  <url type="homepage">http://openmsx.org/</url>
  <url type="help">http://openmsx.org/manual/user.html</url>
  <screenshots>
    <screenshot type="default">http://openmsx.org/images/screenshots/mlimit3.png</screenshot>
    <screenshot>http://openmsx.org/images/screenshots/ide.png</screenshot>
    <screenshot>http://openmsx.org/images/screenshots/tb-underwater.png</screenshot>
  </screenshots>
  <updatecontact>jwrdegoede_at_fedoraproject.org</updatecontact>
</component>
EOF
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc %{_docdir}/%{name}
%license doc/GPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/settings.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
