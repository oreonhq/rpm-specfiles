%global source0_hash 2e88340a8da274b87373ec0740746da78120cc6fbfdd201a4dd6999cac790e4a
%global app_id io.github.Hexchat
Summary:        A popular and easy to use graphical IRC (chat) client
Name:      hexchat
Version:   2.16.2
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://hexchat.github.io
Source0:        https://github.com/hexchat/hexchat/releases/download/v%{version}/hexchat-%{version}.tar.xz
Patch0:    https://github.com/hexchat/hexchat/commit/70069cd50eb07e8a40ac9b0efbb83fcb91a78b99.patch
Patch1:    https://github.com/hexchat/hexchat/commit/cc60ad275a56126904df0b5e37cfd20db22cb359.patch
Requires:      python3-cffi
Requires:      (enchant or enchant2)
Recommends:    sound-theme-freedesktop
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  perl-ExtUtils-Embed
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-cffi
# /oreon:deps
%description
HexChat is an easy to use graphical IRC chat client for the X Window System.
It allows you to join multiple IRC channels (chat rooms) at the same time, 
talk publicly, private one-on-one conversations etc. Even file transfers
are possible.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dwith-lua=lua %{?flatpak:-Ddbus-service-use-appid=true}
%meson_build
%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hexchat-devel -f %{oreon_filedir}/hexchat-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.16.2-1
- Prepare for Oreon 11 (RP1)
