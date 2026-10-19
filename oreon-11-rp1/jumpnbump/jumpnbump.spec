%global source0_hash a89384df54bc69227424ea03a8e3a948b58a7e948f68f9926e287cd0ff4a7bfa
%global rdnsname io.gitlab.LibreGames.jumpnbump
Name:           jumpnbump
Version:        1.70
Release:        1%{?dist}
Summary:        Cute multiplayer platform game with bunnies
License:        GPL-2.0-or-later
URL:            https://gitlab.com/LibreGames/jumpnbump
Source0:        https://gitlab.com/LibreGames/jumpnbump/-/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Requires:       libmodplug
Requires:       libxmp
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
# /oreon:deps
%description
Jump 'n Bump is a cute multiplayer platform game in which you, as a bunny,
have to jump on your opponents to make them explode. It is a true multiplayer
game with network support and shouldn't be played alone, although computer
bunnies with limited AI are available. The game is a UNIX port of the old DOS
game by Brainchild Design.

%package menu
Summary:        Level selection and config menu for the Jump 'n Bump game
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  make
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pillow
Requires:       python3-gobject
%description menu
Python 3/GTK+3 based level selection and configuration interface for the Jump 'n
Bump game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{?build_cflags}"
export LDFLAGS="%{?build_ldflags}"
%make_build PREFIX=%{_prefix} SYSINSTALL=1
%make_build PREFIX=%{_prefix} -C menu
%install
%make_install PREFIX=%{_prefix} SYSINSTALL=1
%make_install PREFIX=%{_prefix} -C menu
%find_lang %{name}-menu
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}{,-menu}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n jumpnbump-menu -f %{oreon_filedir}/jumpnbump-menu.list

%changelog

%autochangelog
