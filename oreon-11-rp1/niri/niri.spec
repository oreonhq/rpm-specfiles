%global source0_hash 134c602d8e0d53413a52d6cd58f9ce7e79a07d03288ee0a51ba1abd5db1b1ad9
%bcond check 1
Name:           niri
Version:        26.04
Release:        1%{?dist}
Summary:        Scrollable-tiling Wayland compositor
SourceLicense:  GPL-3.0-or-later
License:        %{shrink:
    GPL-3.0-or-later AND
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    ISC AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 OR MIT OR Unlicense) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR MIT OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
URL:            https://github.com/YaLTeR/niri
Source0:        https://github.com/YaLTeR/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        niri-%{version}-vendor.tar.xz
Source2:        vendor.toml
ExcludeArch:    %{ix86}
Requires:       xwayland-satellite >= 0.7
Requires:       libwayland-server
Recommends:     gnome-keyring
Recommends:     xdg-desktop-portal-gnome
Recommends:     xdg-desktop-portal-gtk
Recommends:     alacritty
Recommends:     fuzzel
Recommends:     swaylock
Recommends:     wireplumber
Recommends:     waybar
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A scrollable-tiling Wayland compositor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n niri-%{version} -a1 -p1
cat %{SOURCE2} >> .cargo/config.toml
%oreon_vendor_cargo
%build

export NIRI_BUILD_VERSION_STRING="%{version}"
%cargo_build
target/rpm/niri completions bash > niri.bash
target/rpm/niri completions fish > niri.fish
target/rpm/niri completions zsh > _niri
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt
%install
install -Dpm0755 target/rpm/niri -t %{buildroot}%{_bindir}
install -Dpm0755 resources/niri-session -t %{buildroot}%{_bindir}
install -Dpm0644 resources/niri.desktop -t %{buildroot}%{_datadir}/wayland-sessions
install -Dpm0644 resources/niri-portals.conf -t %{buildroot}%{_datadir}/xdg-desktop-portal
install -Dpm0644 resources/niri.service -t %{buildroot}%{_userunitdir}
install -Dpm0644 resources/niri-shutdown.target -t %{buildroot}%{_userunitdir}
install -Dpm0644 niri.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm0644 niri.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm0644 _niri -t %{buildroot}%{zsh_completions_dir}
%oreon_autofiles main
%if %{with check}
%check

export RAYON_NUM_THREADS=2
%cargo_test -- --workspace --exclude niri-visual-tests -- --test-threads 2
%endif
%post

%systemd_user_post niri.service
%preun

%systemd_user_preun niri.service
%postun

%systemd_user_postun_with_reload niri.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
