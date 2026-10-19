%global source0_hash f615cc4c61e033cddc60093003ef03646d246a0ac14becb9cdac9b5fabf37bbe
Name: swappy
Version: 1.8.0
Release:        1%{?dist}
Summary:        Wayland native snapshot editing tool, inspired by Snappy on macOS
License: MIT
URL:     https://github.com/jtheoof/swappy
Source0:        https://github.com/jtheoof/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2: 6A6B35DBE9442683.gpg
Recommends: fontawesome-fonts
Recommends: wl-clipboard
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(pango)
BuildRequires:  scdoc
# /oreon:deps
%description
A Wayland native snapshot and editor tool, inspired by Snappy on
macOS. Works great with grim, slurp and sway. But can easily work with
other screen copy tools that can output a final PNG image to stdout.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%gpgverify -k 2 -s 1 -d 0
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps res/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
sed -i 's/^Exec=.*$/Exec=sh -c "if [ -n \\"\\\\$*\\" ]; then exec swappy -f \\"\\\\$@\\"; else grim -g \\"\\\\$(slurp)\\" - | swappy -f -; fi" placeholder %F/' %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
