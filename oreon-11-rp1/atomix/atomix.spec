%global source0_hash c8849317688d87da734c9063035631052007f2a8799b6c6cc915265880b55fb4

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           atomix
Version:        44.0
Release:        9%{?dist}
Summary:        Puzzle game: Build molecules out of isolated atoms

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Atomix
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  meson

%description
Atomix is yet another little mind game. You have to build molecules out of
single atoms laying around. Of course there is a time limit and the handling is
not as easy as you might expect ;-). This game is inspired by the original
Amiga game Atomix and uses the GNOME libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/atomix.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/atomix
%{_datadir}/atomix
%{_datadir}/applications/atomix.desktop
%{_datadir}/icons/hicolor/*/apps/atomix.png
%{_datadir}/icons/hicolor/symbolic/apps/atomix-symbolic.svg
%{_metainfodir}/atomix.appdata.xml

%changelog
%autochangelog
