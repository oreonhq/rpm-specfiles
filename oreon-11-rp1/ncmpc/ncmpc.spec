%global source1_hash e936cf3ea0b3ff15314db118a67c6d0a9189d439e1e92212d33ecb502881c852
%global source0_hash f678e6c600200af4c5d36174de4e1e82e423962c41b6f52844a25d6d1ec4cb11
Name:           ncmpc
Version:        0.54
Release:        1%{?dist}
Summary:        A curses client for the Music Player Daemon (MPD)
License:        GPL-2.0-or-later
URL:            https://www.musicpd.org/
Source0:        https://www.musicpd.org/download/ncmpc/0/ncmpc-%{version}.tar.xz
Source1:        https://www.musicpd.org/download/ncmpc/0/ncmpc-%{version}.tar.xz.sig
Source2:        gpgkey-236E8A58C6DB4512.gpg
# oreon:deps
BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(lirc)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  python3dist(sphinx)
# /oreon:deps
%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc connects to
a MPD running on a machine on the local network, and controls this with an
interface inspired by cplay.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson \
    -Dchat_screen=true \
    -Dlyrics_screen=true \
    -Dlyrics_plugin_dir=%{_datadir}/ncmpc/lyrics
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc
install -p -m644 doc/config.sample \
    $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc/config
install -p -m644 doc/keys.sample $RPM_BUILD_ROOT%{_sysconfdir}/ncmpc/keys
%find_lang ncmpc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
