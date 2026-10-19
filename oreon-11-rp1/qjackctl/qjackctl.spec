%global source0_hash dfffef1ddc65df666a1f0eba89a1d6d85fab47c765a91de36a5ef6360472899a
Summary:        Qt based JACK control application
Name:          qjackctl
Version:       1.0.6
Release:        1%{?dist}
URL:           http://qjackctl.sourceforge.net
Source0:        http://downloads.sourceforge.net/qjackctl/files/%{name}-%{version}.tar.gz
License:       GPL-2.0-or-later
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  portaudio-devel
# /oreon:deps
%description
Qjackctl is a simple application to control the JACK sound server daemon,
specific for the Linux Audio Desktop infrastructure. It provides a simple GUI
dialog for setting several JACK daemon parameters, which are properly saved
between sessions, and a way to control the status of the audio server daemon.
With time, this primordial interface has become richer by including a enhanced
patch bay and connection control features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake} \
  %{?flatpak:-DCONFIG_WAYLAND=1} \
  -DCONFIG_JACK_VERSION=1
%{cmake_build}
%install
%{cmake_install}
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.rncbc.qjackctl.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.rncbc.qjackctl.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
