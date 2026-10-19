%global source0_hash ee73c292a4b457004b38c2df178eac025ab0b849fdd9e13253c1f8b5cf110710
%global foot_terminfo foot-extra
%global default_terminfo foot
%global fcft_minver 3.3.1
Name:           foot
Version:        1.28.0
Release:        1%{?dist}
Summary:        Fast, lightweight and minimalistic Wayland terminal emulator
License:        MIT AND CC-BY-SA-4.0
URL:            https://codeberg.org/dnkl/%{name}
Source0:        https://codeberg.org/dnkl/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-5BBD4992C116573F.asc
Source3:        org.codeberg.dnkl.foot.metainfo.xml
Requires:       fcft%{?_isa} >= %{fcft_minver}
Recommends:     ncurses-base
Requires:       (ncurses-base >= 6.4-5.20230520 if ncurses-base)
Requires:       (%{name}-terminfo = %{version}-%{release} if %{name}-terminfo)
Recommends:     /usr/bin/notify-send
Recommends:     /usr/bin/xdg-open
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  /usr/bin/tic
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libutempter
BuildRequires:  meson
BuildRequires:  pkgconfig(fcft)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tllist)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  tllist-static
# /oreon:deps
%description
Fast, lightweight and minimalistic Wayland terminal emulator.
Features:
 * Fast
 * Lightweight, in dependencies, on-disk and in-memory
 * Wayland native
 * DE agnostic
 * Server/daemon mode
 * User configurable font fallback
 * On-the-fly font resize
 * On-the-fly DPI font size adjustment
 * Scrollback search
 * Keyboard driven URL detection
 * Color emoji support
 * IME (via text-input-v3)
 * Multi-seat
 * Synchronized Updates support
 * Sixel image support

%package        terminfo
Summary:        Terminfo files for %{name} terminal
BuildRequires:  /usr/bin/tic
Requires:       ncurses-base
%description    terminfo
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson \
    -Dterminfo-base-name=%{foot_terminfo} \
    -Ddefault-terminfo=%{default_terminfo}
%meson_build
%install
%meson_install
install -D -pv -m0644 %{SOURCE3} \
    %{buildroot}%{_metainfodir}/org.codeberg.dnkl.foot.metainfo.xml
rm %{buildroot}%{_docdir}/%{name}/LICENSE
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}*.desktop
%post

%systemd_user_post %{name}-server.{service,socket}
%preun

%systemd_user_preun %{name}-server.{service,socket}
%files -f %{oreon_filedir}/main.list
%files -n foot-terminfo -f %{oreon_filedir}/foot-terminfo.list

%changelog

%autochangelog
