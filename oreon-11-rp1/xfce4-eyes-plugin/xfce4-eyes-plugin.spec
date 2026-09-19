%global source0_hash 87f9b978ca75abb3aa5edb1315eb65ef98654a662c14621847ddffe8aa6574ad

%global _hardened_build 1
%global minor_version 4.7
%global xfceversion 4.16

Name:           xfce4-eyes-plugin
Version:        4.7.0
Release:        %autorelease
Summary:        Eyes for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  meson

Requires:       xfce4-panel >= %{xfceversion}

%description
A xfce4 panel plugin that adds eyes which watch your every step. Scary!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS
%license COPYING
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_datadir}/icons/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes

%changelog
%autochangelog
