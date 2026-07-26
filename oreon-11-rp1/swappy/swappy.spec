%global source0_hash 47886ad52d81980da3fd6cd401d985a8a6fb0a28bfa687d3b40d39d7f9349147

# -*-Mode: rpm-spec -*-

Name: swappy
Version: 1.5.1
Release: 8%{?dist}
Summary: Wayland native snapshot editing tool, inspired by Snappy on macOS
License: MIT
URL:     https://github.com/jtheoof/swappy
Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# gpg was downloaded by:
# gpg2 --recv-keys 0x6A6B35DBE9442683
# gpg2 --export --export-options export-minimal 0x6A6B35DBE9442683 > 6A6B35DBE9442683.gpg
Source2: 6A6B35DBE9442683.gpg

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: desktop-file-utils

# from the author re fontawesome: "Considering the icons that I
# currently use, swappy should work with FA 4. But if I need to add
# more tools (and so icons) in the future, I will pick from FA 5,
# which has a lot more than FA 4 so it might not work in the future.
# Therefore I would still recommend using FA >=5, but it's technically
# OK to have FA >= 4 at the moment."
Recommends: fontawesome-fonts
Recommends: wl-clipboard

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

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*

%license LICENSE

%doc README.md
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
