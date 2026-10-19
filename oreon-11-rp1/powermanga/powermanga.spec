%global source0_hash da753fce83905a6db3fd8ea65c70c57d662362c86c429d6c6954417144f943e8
Summary:        Arcade 2D shoot-them-up game
Name:           powermanga
Version:        0.93.1
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            http://linux.tlk.fr/games/Powermanga/
Source0:        http://linux.tlk.fr/games/Powermanga/download/powermanga-%{version}.tgz
Source1: powermanga.png
Source2: powermanga.desktop
Patch0:         powermanga-0.93.1-install.patch
Requires:       libmikmod
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libXt-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libmikmod-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Powermanga is a vertical scrolling arcade style 2D shoot-them-up game with
41 levels and more than 200 sprites.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
autoreconf -v -i

%build

%configure
%make_build
%install
%make_install
%{__chmod} g-s %{buildroot}%{_bindir}/powermanga
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/powermanga.png
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}
echo "Lang=en" > \
    %{buildroot}%{_datadir}/powermanga/texts/config.ini
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
