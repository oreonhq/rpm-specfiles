%global source0_hash b35cf78232992a6b0f605ac1e931478a331478bf71a2f4ae750d71a6124adcd8

Summary:       Qt based Fluidsynth GUI front end
Name:          qsynth
Version:       1.0.5
Release:       2%{?dist}
URL:           http://qsynth.sourceforge.net
Source0:       http://downloads.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
License:       GPL-2.0-or-later
Requires:      hicolor-icon-theme
Requires:      soundfont2-default

# Set correct paths for sound fonts
# Increase default buffer size
Patch:         qsynth-fedora-defaults.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth-devel
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: libappstream-glib

%description
QSynth is a fluidsynth GUI front-end application written in C++ around the Qt4
toolkit using Qt Designer. Eventually it may evolve into a softsynth management
application allowing the user to control and manage a variety of command line
softsynth but for the moment it wraps the excellent FluidSynth. FluidSynth is a
command line software synthesizer based on the Soundfont specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# fedora-defaults.patch
sed -i -e 's|@DATADIR@|%{_datadir}|g' src/qsynthOptions.cpp

%build
# pipewire-jack is not in the default search path
export LDFLAGS="$LDFLAGS $(pkg-config --libs jack)"
%{cmake} %{?flatpak:-DCONFIG_WAYLAND=ON}
%{cmake_build}

%install
%{cmake_install}

# desktop file
desktop-file-edit \
  --add-category="X-Synthesis" \
  %{buildroot}%{_datadir}/applications/org.rncbc.qsynth.desktop

# Handle locales
%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.rncbc.qsynth.metainfo.xml

%files -f qsynth.lang
%doc ChangeLog README
%license LICENSE
%{_bindir}/qsynth
%dir %{_datadir}/qsynth/
%dir %{_datadir}/qsynth/palette/
%dir %{_datadir}/qsynth/translations/
%{_datadir}/qsynth/palette/*
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.qsynth.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.qsynth.svg
%{_datadir}/applications/org.rncbc.qsynth.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
%{_metainfodir}/org.rncbc.qsynth.metainfo.xml

%changelog
%autochangelog
