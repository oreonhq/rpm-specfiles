%global source0_hash 4beb43f2d80719f53eb427f2185d43fe65bb82a763e25b3b1fe088d8947c2d73

%global foot_terminfo foot-extra
%global default_terminfo foot
%global fcft_minver 3.3.1

Name:           foot
Version:        1.26.1
Release:        1%{?dist}
Summary:        Fast, lightweight and minimalistic Wayland terminal emulator

# Main package license: MIT
# icons/hicolor/scalable/apps/foot.svg: CC-BY-SA-4.0
License:        MIT AND CC-BY-SA-4.0
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# Daniel Eklöf (Git signing) <daniel@ekloef.se>
Source2:        gpgkey-5BBD4992C116573F.asc
Source3:        org.codeberg.dnkl.foot.metainfo.xml

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros

BuildRequires:  libutempter
BuildRequires:  pkgconfig(fcft) >= %{fcft_minver}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tllist) >= 1.1.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-scanner) 
BuildRequires:  pkgconfig(xkbcommon)
# require *-static for header-only library
BuildRequires:  tllist-static

Requires:       fcft%{?_isa} >= %{fcft_minver}

Recommends:     ncurses-base
Requires:       (ncurses-base >= 6.4-5.20230520 if ncurses-base)
# require matching version of foot-terminfo if installed
Requires:       (%{name}-terminfo = %{version}-%{release} if %{name}-terminfo)

# Optional dependency for bell = notify option
Recommends:     /usr/bin/notify-send
# Optional dependency for opening URLs
Recommends:     /usr/bin/xdg-open
Requires:       hicolor-icon-theme

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
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}*.desktop

%post
%systemd_user_post %{name}-server.{service,socket}

%preun
%systemd_user_preun %{name}-server.{service,socket}

%files
%license LICENSE
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/%{name}.ini
%{_bindir}/%{name}
%{_bindir}/%{name}client
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/org.codeberg.dnkl.foot.metainfo.xml
%{bash_completions_dir}/foot*
%{fish_completions_dir}/foot*
%{zsh_completions_dir}/_foot*
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/CHANGELOG.md
%doc %{_docdir}/%{name}/README.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}client.1*
%{_mandir}/man5/%{name}.ini.5*
%{_mandir}/man7/%{name}-ctlseqs.7*
%{_userunitdir}/%{name}-server.service
%{_userunitdir}/%{name}-server.socket

%files terminfo
%license LICENSE
%dir %{_datadir}/terminfo/f
%{_datadir}/terminfo/f/%{foot_terminfo}
%{_datadir}/terminfo/f/%{foot_terminfo}-direct

%changelog
%autochangelog
