%global source0_hash 1001b215d68c7e450b74bcf11510adb3ac60074ed46d5a160eb851bafcc14c3c
%define debug_package %{nil}
Name:           lutris
Version:        0.5.22
Release:        1%{?dist}
Summary:        Install and play any video game easily
License:        GPL-3.0-only
URL:            http://%{name}.net
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
Requires:       cabextract
Requires:       gtk3, psmisc
Requires:       hicolor-icon-theme
Requires:       gnome-desktop3
Requires:       python3-distro
Requires:       python3-cairo
Requires:       libXScrnSaver
Requires:       mesa-vulkan-drivers
Requires:       mesa-dri-drivers
Requires:       vulkan-loader
Requires:       mesa-libGL
Requires:       glx-utils
Requires:       gvfs
Requires:       webkit2gtk4.1
Requires:       protobuf
Recommends: 	p7zip, curl
Recommends:	fluid-soundfont-gs
Recommends:     wine-core
Recommends:	p7zip-plugins
Recommends:	gamemode
Recommends:     libFAudio
Recommends:     gamescope
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-lutris = %{version}-%{release}
# /oreon:deps
%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%meson
%meson_build
%install
%pyproject_install
%meson_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/net.%{name}.Lutris.metainfo.xml
%fdupes %{buildroot}%{python3_sitelib}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications share/applications/net.%{name}.Lutris.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications share/applications/net.%{name}.Lutris1.desktop
%find_lang %{name} --with-man
%oreon_autofiles main

%check

%files

%changelog

%autochangelog
