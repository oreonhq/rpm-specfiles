%global source0_hash e379dc118a38cd1866219cbba8dddf1d50cacd041135f10d8aee5843234643ee

Name:           fbzx
Version:        4.8.0
Release:        14%{?dist}
Summary:        A ZX Spectrum emulator for FrameBuffer

License:        GPL-3.0-or-later
URL:            https://www.rastersoft.com/programas/fbzx.html
Source0:        %{name}-%{version}-noroms.tar.gz
# The above file is derived from:
# https://gitlab.com/rastersoft/fbzx/-/archive/4.8.0/fbzx-4.8.0.tar.gz
# This file contains Spectrum ROMs and cannot be shipped in Fedora. 
# Therefore we use this script to remove them before shipping it. 
# Download the upstream tarball and invoke this script while in 
# the tarball's directory:
# ./fbzx-generate-tarball.sh 4.8.0
Source1:        %{name}-generate-tarball.sh
Source2:        README_%{name}.Fedora
# Debian man page
Source3:        %{name}.1
# Fix building with gcc 15
Patch0:         %{name}-4.8.0-gcc15.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
FBZX is a Sinclair Spectrum emulator, designed to work at full screen using 
the FrameBuffer or under X-Windows. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix Makefile
sed -i 's/$(CXX) -o/$(CXX) $(CXXFLAGS) -o/' src/Makefile

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix} NOROMS=1

# remove obsolete pixmap
rm -rf %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# fix desktop file
desktop-file-install \
  --delete-original \
  --add-category Emulator \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# verify AppData file
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/*.appdata.xml

# install man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1/

# install Fedora README
install -p -m 644 %{SOURCE2} %{buildroot}%{_pkgdocdir}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING
%license COPYING

%changelog
%autochangelog
