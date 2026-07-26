%global source0_hash none

# Don't build internal static libs as shared
%global _cmake_shared_libs %{nil}

Name:           warzone2100
Version:        4.6.3
Release:        1%{?dist}
Summary:        Innovative 3D real-time strategy

# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://wz2100.net/
Source0:        https://github.com/Warzone2100/warzone2100/releases/download/%{version}/warzone2100_src.tar.xz
Source1:        https://github.com/Warzone2100/wz-sequences/releases/download/v3/high-quality-en-sequences.wz

Patch1:         cmake4.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# https://github.com/Warzone2100/warzone2100/issues/4577
ExcludeArch:    s390x

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildREquires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glslc
BuildRequires:  harfbuzz-devel
BuildRequires:  libcurl-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libzip-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  p7zip
BuildRequires:  physfs-devel
BuildRequires:  protobuf-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  SDL3-devel
BuildRequires:  sqlite-devel
BuildRequires:  vulkan-devel

Requires: hicolor-icon-theme
Recommends: %{name}-sequences

%description
Warzone 2100 was an innovative 3D real-time strategy game back in 1999, and
most will agree it didn't enjoy the commercial success it should have had. The
game's source code was liberated on December 6th, 2004, under a GPL license
(see COPYING in this directory for details). Soon after that, the Warzone 2100
ReDev project was formed to take care of its future.

%package sequences
Summary:        Video file for %{name}
Requires:       %{name}
BuildArch:      noarch

%description sequences
Video file for %{name}.

%prep
%autosetup -n warzone2100 -p1

# Don't use -Werror for distro builds
sed -i -e '/^CONFIGURE_WZ_COMPILER_WARNINGS()$/d' CMakeLists.txt

%build
%cmake -DWZ_DISTRIBUTOR=Fedora
%cmake_build

%install
%cmake_install
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}
%find_lang %{name} --all-name
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/warzone2100/sequences.wz

# Fix icon install path
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mv $RPM_BUILD_ROOT%{_datadir}/icons/net.wz2100.warzone2100.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/net.wz2100.warzone2100.png

%files -f %{name}.lang
%license COPYING COPYING.NONGPL COPYING.README
%doc AUTHORS ChangeLog
%{_bindir}/warzone2100
%{_datadir}/applications/net.wz2100.warzone2100.desktop
%{_datadir}/icons/hicolor/128x128/apps/net.wz2100.warzone2100.png
%{_datadir}/metainfo/net.wz2100.warzone2100.metainfo.xml
%{_datadir}/warzone2100/
%exclude %{_datadir}/warzone2100/sequences.wz
%{_mandir}/man6/warzone2100.6*

%files sequences
%{_datadir}/warzone2100/sequences.wz

%changelog
%autochangelog
