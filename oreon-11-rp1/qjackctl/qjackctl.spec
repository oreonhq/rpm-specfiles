%global source0_hash ce6056dd17fd5c1e8cca928754357f3cc6a6ff8464c9e05b07f8011b2597ec61

Summary:       Qt based JACK control application
Name:          qjackctl
Version:       1.0.5
Release:       1%{?dist}
URL:           http://qjackctl.sourceforge.net
Source0:       http://downloads.sourceforge.net/qjackctl/files/%{name}-%{version}.tar.gz
License:       GPL-2.0-or-later
Requires:      hicolor-icon-theme

BuildRequires: cmake
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: libappstream-glib

%description
Qjackctl is a simple application to control the JACK sound server daemon,
specific for the Linux Audio Desktop infrastructure. It provides a simple GUI
dialog for setting several JACK daemon parameters, which are properly saved
between sessions, and a way to control the status of the audio server daemon.
With time, this primordial interface has become richer by including a enhanced
patch bay and connection control features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{cmake} \
  %{?flatpak:-DCONFIG_WAYLAND=1} \
  -DCONFIG_JACK_VERSION=1
%{cmake_build}

%install
%{cmake_install}

# Handle locales
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.rncbc.qjackctl.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.rncbc.qjackctl.metainfo.xml

%files -f qjackctl.lang
%doc ChangeLog README
%license LICENSE
%{_bindir}/qjackctl
%dir %{_datadir}/qjackctl/
%dir %{_datadir}/qjackctl/palette/
%dir %{_datadir}/qjackctl/translations/
%{_datadir}/qjackctl/palette/*
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.qjackctl.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.qjackctl.svg
%{_datadir}/applications/org.rncbc.qjackctl.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
%{_datadir}/metainfo/org.rncbc.qjackctl.metainfo.xml

%changelog
%autochangelog
