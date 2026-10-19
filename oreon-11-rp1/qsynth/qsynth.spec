%global source0_hash 7bba1591aec2aeb57171aa37697d33f038de7ee22b3f8cf50aaada772ca89ac1
Summary:        Qt based Fluidsynth GUI front end
Name:          qsynth
Version:       1.0.6
Release:        1%{?dist}
URL:           http://qsynth.sourceforge.net
Source0:        http://downloads.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
License:       GPL-2.0-or-later
Requires:      hicolor-icon-theme
Requires:      soundfont2-default
Patch:         qsynth-fedora-defaults.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
# /oreon:deps
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

export LDFLAGS="$LDFLAGS $(pkg-config --libs jack)"
%{cmake} %{?flatpak:-DCONFIG_WAYLAND=ON}
%{cmake_build}
%install
%{cmake_install}
desktop-file-edit \
  --add-category="X-Synthesis" \
  %{buildroot}%{_datadir}/applications/org.rncbc.qsynth.desktop
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.rncbc.qsynth.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
